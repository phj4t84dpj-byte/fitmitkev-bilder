# /// script
# dependencies = ["huggingface_hub>=0.30", "requests", "imageio-ffmpeg"]
# ///
# Reel vertonen: Video + deutsches Voiceover + Hintergrundmusik mischen (ohne Token an fremde Adressen).
# env JOBS = JSON [{"name":..., "video":url, "voice":url|null, "musik":url, "ziel":"ordner"}]
# "nur_voice": true lädt nur die Voiceover-Fassung hoch.
# Ergebnis je Video: <ziel>/<name>_voiceover.mp4 (Stimme + leise Musik) und <ziel>/<name>_musik.mp4 (nur Musik).
import os, json, re, subprocess, requests
from huggingface_hub import HfApi
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe(); api = HfApi(token=os.environ["HF_TOKEN"]); REPO = "kevrsztorm/fitmitkev-bilder"
def lade(u, p): open(p, "wb").write(requests.get(u, timeout=300).content)
def dauer(p):
    e = subprocess.run([FF, "-i", p], capture_output=True, text=True).stderr
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", e).groups(); return int(h)*3600 + int(m)*60 + float(s)
def ff(*a):
    r = subprocess.run([FF, "-y", "-loglevel", "error", *a], capture_output=True, text=True)
    if r.returncode: print(r.stderr); raise SystemExit(1)
for j in json.loads(os.environ["JOBS"]):
    n = j["name"]; lade(j["video"], "v.mp4"); lade(j["musik"], "m.audio")
    dv = dauer("v.mp4"); print(n, "Video", dv, flush=True)
    fade = f"afade=t=in:d=0.5,afade=t=out:st={dv-1.2:.2f}:d=1.2"
    ff("-i", "v.mp4", "-i", "m.audio", "-filter_complex", f"[1:a]atrim=0:{dv:.2f},volume=0.9,{fade}[a]", "-map", "0:v", "-map", "[a]",
       "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", f"{dv:.2f}", "-movflags", "+faststart", "musik.mp4")
    if not j.get("nur_voice"):
        api.upload_file(path_or_fileobj="musik.mp4", path_in_repo=f"{j['ziel']}/{n}_musik.mp4", repo_id=REPO, repo_type="dataset")
    if j.get("voice"):
        lade(j["voice"], "s.audio"); ds = dauer("s.audio"); ziel = dv - 0.8
        tempo = max(1.0, ds / ziel) if ds > ziel else 1.0; print(n, "Stimme", ds, "Tempo", round(tempo, 3), flush=True)
        AF = "aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo"
        # Stufe 1: Stimme und Musik einzeln auf volle Videolänge als WAV
        ff("-i", "s.audio", "-af", f"{AF},atempo={tempo:.3f},adelay=300:all=1,volume=1.6,apad,atrim=0:{dv:.2f},asetpts=N/SR/TB", "-ar", "44100", "-ac", "2", "stimme.wav")
        ff("-i", "m.audio", "-vn", "-af", f"{AF},atrim=0:{dv:.2f},asetpts=N/SR/TB,volume=0.22,{fade},apad,atrim=0:{dv:.2f}", "-ar", "44100", "-ac", "2", "musik.wav")
        # Stufe 2: mischen und an das Video hängen
        ff("-i", "stimme.wav", "-i", "musik.wav", "-filter_complex", "[0:a][1:a]amix=inputs=2:duration=first:normalize=0[a]", "-map", "[a]", "-ar", "44100", "-ac", "2", "mix.wav")
        ff("-i", "v.mp4", "-i", "mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", f"{dv:.2f}", "-movflags", "+faststart", "voice.mp4")
        # Prüfen: in jedem Abschnitt muss Ton sein
        for a, b in [(0.5, 3), (3, 7), (7, 11), (11, dv - 1)]:
            r = subprocess.run([FF, "-ss", str(a), "-t", str(b - a), "-i", "voice.mp4", "-vn", "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
            mv = [l.split("] ")[-1] for l in r.splitlines() if "mean_volume" in l]
            print(n, f"{a}-{b:.1f}s", mv, flush=True)
            if not mv or float(mv[0].split()[1]) < -40: print("FEHLER: kein Ton", n); raise SystemExit(1)
        api.upload_file(path_or_fileobj="voice.mp4", path_in_repo=f"{j['ziel']}/{n}_voiceover.mp4", repo_id=REPO, repo_type="dataset")
    print("OK", n, flush=True)
