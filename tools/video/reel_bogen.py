# /// script
# dependencies = ["huggingface_hub>=0.30", "requests", "pillow", "imageio-ffmpeg"]
# ///
# Higgsfield-Videos (cloudfront, ohne Token) holen, als MP4 in den Datensatz legen und je Video einen Bogen mit 8 Standbildern bauen.
# env JOBS = JSON [[url, "ordner/<Name>.mp4"], ...]
import os, json, subprocess, requests, glob
from PIL import Image, ImageDraw
from huggingface_hub import HfApi
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe(); api = HfApi(token=os.environ["HF_TOKEN"]); REPO = "kevrsztorm/fitmitkev-bilder"
for url, ziel in json.loads(os.environ["JOBS"]):
    open("v.mp4", "wb").write(requests.get(url, timeout=300).content)
    api.upload_file(path_or_fileobj="v.mp4", path_in_repo=ziel, repo_id=REPO, repo_type="dataset")
    for f in glob.glob("f*.jpg"): os.remove(f)
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", "v.mp4", "-vf", "fps=8/15,scale=270:-2", "f%02d.jpg"], check=True)
    fr = sorted(glob.glob("f*.jpg"))[:8]; ims = [Image.open(f) for f in fr]
    w, h = ims[0].size; sh = Image.new("RGB", (w * 4, h * 2), "white")
    for i, im in enumerate(ims): sh.paste(im, ((i % 4) * w, (i // 4) * h))
    sh.save("sheet.jpg", quality=88)
    api.upload_file(path_or_fileobj="sheet.jpg", path_in_repo=ziel.replace(".mp4", "_bogen.jpg"), repo_id=REPO, repo_type="dataset")
    print("OK", ziel, len(fr), flush=True)
