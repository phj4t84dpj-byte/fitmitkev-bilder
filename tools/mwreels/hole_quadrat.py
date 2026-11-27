# /// script
# dependencies = ["huggingface_hub>=0.30", "requests", "pillow"]
# ///
# Quadratische Higgsfield-Bilder holen (ohne Token an cloudfront), je 768x768 in den Datensatz und als ein Mosaik (5 Spalten).
# env JOBS = JSON [[url, "ordner/<Key>.jpg"], ...]
import os, io, json, requests
from huggingface_hub import HfApi
from PIL import Image
api = HfApi(token=os.environ["HF_TOKEN"]); REPO = "kevrsztorm/fitmitkev-bilder"
J = json.loads(os.environ["JOBS"]); ims = []
for url, ziel in J:
    im = Image.open(io.BytesIO(requests.get(url, timeout=120).content)).convert("RGB")
    w, h = im.size; s = min(w, h); im = im.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s)).resize((768, 768), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "JPEG", quality=92)
    api.upload_file(path_or_fileobj=b.getvalue(), path_in_repo=ziel, repo_id=REPO, repo_type="dataset"); ims.append(im); print("OK", ziel, flush=True)
cols = 5; rows = (len(ims) + cols - 1) // cols
m = Image.new("RGB", (cols * 768, rows * 768), "white")
for i, im in enumerate(ims): m.paste(im, ((i % cols) * 768, (i // cols) * 768))
b = io.BytesIO(); m.save(b, "JPEG", quality=90)
api.upload_file(path_or_fileobj=b.getvalue(), path_in_repo=J[0][1].split("/")[0] + "/_mosaik.jpg", repo_id=REPO, repo_type="dataset"); print("Mosaik")
