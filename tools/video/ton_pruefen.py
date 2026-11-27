# /// script
# dependencies = ["requests", "imageio-ffmpeg"]
# ///
# Prüft Lautstärke von Audio-/Videodateien (ohne Token): env URLS = JSON-Liste.
import os, json, subprocess, requests, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
for i, u in enumerate(json.loads(os.environ["URLS"])):
    p = f"d{i}"; open(p, "wb").write(requests.get(u, timeout=300).content)
    info = subprocess.run([FF, "-i", p], capture_output=True, text=True).stderr
    print("====", u.rsplit("/", 1)[-1], os.path.getsize(p), "Bytes")
    for l in info.splitlines():
        if "Duration" in l or "Stream" in l: print("  ", l.strip())
    for start, dur in [(0, 99), (0, 2), (2, 4), (6, 4), (10, 5)]:
        r = subprocess.run([FF, "-ss", str(start), "-t", str(dur), "-i", p, "-vn", "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
        mv = [l.split("] ")[-1] for l in r.splitlines() if "mean_volume" in l or "max_volume" in l]
        print(f"   {start}-{start+dur}s", mv, flush=True)
