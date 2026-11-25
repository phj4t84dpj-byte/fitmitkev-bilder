# /// script
# dependencies = ["huggingface_hub>=0.30", "requests", "pillow"]
# ///
# Higgsfield-Ergebnisse (cloudfront) holen, als JPG 1024x1280 in den Datensatz legen und je Ordner einen Auswahlbogen bauen.
# env JOBS = JSON [[url, "ordner/<Key>_s<n>.jpg"], ...]
import os, io, json, requests
from huggingface_hub import HfApi
from PIL import Image, ImageDraw
TOK = os.environ["HF_TOKEN"]; api = HfApi(token=TOK); REPO = "kevrsztorm/fitmitkev-bilder"
J = json.loads(os.environ["JOBS"]); thumbs = []
for url, ziel in J:
    im = Image.open(io.BytesIO(requests.get(url, timeout=120).content)).convert("RGB")
    w, h = im.size; t = 4 / 5
    if w / h > t: nw = round(h * t); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    elif w / h < t: nh = round(w / t); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    im = im.resize((1024, 1280), Image.LANCZOS); b = io.BytesIO(); im.save(b, "JPEG", quality=93)
    api.upload_file(path_or_fileobj=b.getvalue(), path_in_repo=ziel, repo_id=REPO, repo_type="dataset"); print("OK", ziel, (w, h), flush=True)
    thumbs.append((ziel, im.resize((320, 400), Image.LANCZOS)))
cols = 6; rows = (len(thumbs) + cols - 1) // cols
sh = Image.new("RGB", (cols * 320, rows * 400), "white"); d = ImageDraw.Draw(sh)
for i, (z, t) in enumerate(thumbs):
    x, y = (i % cols) * 320, (i // cols) * 400; sh.paste(t, (x, y))
    d.rectangle((x, y, x + 320, y + 30), fill=(0, 0, 0)); d.text((x + 6, y + 4), z.split("/")[-1][:-4], fill=(255, 255, 0), font_size=20)
b = io.BytesIO(); sh.save(b, "JPEG", quality=88)
ordner = J[0][1].split("/")[0]
api.upload_file(path_or_fileobj=b.getvalue(), path_in_repo=f"{ordner}/_auswahl.jpg", repo_id=REPO, repo_type="dataset"); print("Bogen", ordner)
