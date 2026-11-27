# /// script
# dependencies = ["huggingface_hub>=0.30", "requests", "imageio-ffmpeg"]
# ///
# Mehrwert-Reel vertonen: stummes Video + Stimme (ab VOR s, Originaltempo) + leise Musik. Ohne Token an fremde Adressen.
# env JOBS = JSON [{"name":..., "video":url, "voice":url, "musik":url, "ziel":"ordner"}], env VOR (Standard 0.5)
import os, re, json, subprocess, requests
from huggingface_hub import HfApi
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe(); api = HfApi(token=os.environ["HF_TOKEN"]); REPO = "kevrsztorm/fitmitkev-bilder"
VOR = float(os.environ.get("VOR", "0.5"))
def lade(u, p): open(p, "wb").write(requests.get(u, timeout=300).content)
def dauer(p):
    e = subprocess.run([FF, "-i", p], capture_output=True, text=True).stderr
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", e).groups(); return int(h)*3600 + int(m)*60 + float(s)
def ff(*a):
    r = subprocess.run([FF, "-y", "-loglevel", "error", *a], capture_output=True, text=True)
    if r.returncode: print(r.stderr); raise SystemExit(1)
AF = "aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo"
for j in json.loads(os.environ["JOBS"]):
    n = j["name"]; lade(j["video"], "v.mp4"); lade(j["voice"], "s.audio"); lade(j["musik"], "m.audio")
    dv = dauer("v.mp4"); ms = int(VOR * 1000)
    ff("-i", "s.audio", "-af", f"{AF},adelay={ms}:all=1,volume=1.5,apad,atrim=0:{dv:.2f},asetpts=N/SR/TB", "stimme.wav")
    ff("-stream_loop", "-1", "-i", "m.audio", "-af", f"{AF},atrim=0:{dv:.2f},asetpts=N/SR/TB,volume=0.2,afade=t=in:d=0.6,afade=t=out:st={dv-1.5:.2f}:d=1.5", "musik.wav")
    ff("-i", "stimme.wav", "-i", "musik.wav", "-filter_complex", "[0:a][1:a]amix=inputs=2:duration=first:normalize=0[a]", "-map", "[a]", "mix.wav")
    ff("-i", "v.mp4", "-i", "mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", f"{dv:.2f}", "-movflags", "+faststart", "out.mp4")
    for a, b in [(0.6, 4), (4, 8), (8, 12), (12, dv - 2)]:
        r = subprocess.run([FF, "-ss", str(a), "-t", str(b - a), "-i", "out.mp4", "-vn", "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
        mv = [l.split("] ")[-1] for l in r.splitlines() if "mean_volume" in l]; print(n, f"{a}-{b:.1f}s", mv, flush=True)
        if not mv or float(mv[0].split()[1]) < -40: print("FEHLER: kein Ton", n); raise SystemExit(1)
    api.upload_file(path_or_fileobj="out.mp4", path_in_repo=f"{j['ziel']}/{n}.mp4", repo_id=REPO, repo_type="dataset"); print("OK", n, flush=True)
