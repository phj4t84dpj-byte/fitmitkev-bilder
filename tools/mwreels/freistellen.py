# /// script
# dependencies = ["huggingface_hub>=0.30", "requests", "pillow", "rembg[cpu]", "numpy"]
# ///
# Fotos aus dem Datensatz freistellen (rembg, Modell isnet-general-use), als PNG mit Transparenz hochladen
# und alle zusammen als ein PNG-Mosaik (je Feld 640x640, 5 Spalten) zum Ansehen.
# env KEYS = "a,b,c", env ORDNER = Datensatz-Ordner mit <key>.jpg
import os, io, requests
from huggingface_hub import HfApi
from PIL import Image
from rembg import remove, new_session
TOK = os.environ["HF_TOKEN"]; api = HfApi(token=TOK); REPO = "kevrsztorm/fitmitkev-bilder"
O = os.environ["ORDNER"]; KEYS = os.environ["KEYS"].split(",")
ses = new_session("isnet-general-use"); out = []
for k in KEYS:
    r = requests.get(f"https://huggingface.co/datasets/{REPO}/resolve/main/{O}/{k}.jpg", headers={"Authorization": f"Bearer {TOK}"}, timeout=120)
    im = Image.open(io.BytesIO(r.content)).convert("RGB")
    cut = remove(im, session=ses, post_process_mask=True)
    bb = cut.getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox(); cut = cut.crop(bb)
    s = max(cut.size); pad = Image.new("RGBA", (s, s), (0, 0, 0, 0)); pad.paste(cut, ((s - cut.width) // 2, (s - cut.height) // 2))
    pad = pad.resize((640, 640), Image.LANCZOS); b = io.BytesIO(); pad.save(b, "PNG")
    api.upload_file(path_or_fileobj=b.getvalue(), path_in_repo=f"{O}/cut_{k}.png", repo_id=REPO, repo_type="dataset"); out.append(pad); print("OK", k, flush=True)
m = Image.new("RGBA", (5 * 640, ((len(out) + 4) // 5) * 640), (0, 0, 0, 0))
for i, p in enumerate(out): m.paste(p, ((i % 5) * 640, (i // 5) * 640))
b = io.BytesIO(); m.save(b, "PNG"); api.upload_file(path_or_fileobj=b.getvalue(), path_in_repo=f"{O}/_cut_mosaik.png", repo_id=REPO, repo_type="dataset")
g = Image.new("RGB", m.size, (0, 255, 0)); g.paste(m, (0, 0), m); b = io.BytesIO(); g.save(b, "JPEG", quality=92)
api.upload_file(path_or_fileobj=b.getvalue(), path_in_repo=f"{O}/_cut_mosaik_gruen.jpg", repo_id=REPO, repo_type="dataset"); print("Mosaik")
