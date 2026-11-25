# /// script
# dependencies = ["huggingface_hub>=0.30", "requests", "pillow"]
# ///
# Ausgewählte Bilder (1024x1280) nebeneinander zu einem Mosaik in voller Größe – ein Anhang statt vieler; lokal wieder zerschneiden.
# env FILES = "pfad1,pfad2,...", OUT = Zielpfad im Datensatz
import os, io, requests
from huggingface_hub import HfApi
from PIL import Image
TOK = os.environ["HF_TOKEN"]; api = HfApi(token=TOK); REPO = "kevrsztorm/fitmitkev-bilder"
F = os.environ["FILES"].split(","); M = Image.new("RGB", (1024 * len(F), 1280), "white")
for i, f in enumerate(F):
    r = requests.get(f"https://huggingface.co/datasets/{REPO}/resolve/main/{f}", headers={"Authorization": f"Bearer {TOK}"}, timeout=90); r.raise_for_status()
    M.paste(Image.open(io.BytesIO(r.content)).convert("RGB").resize((1024, 1280)), (1024 * i, 0)); print("ok", f, flush=True)
b = io.BytesIO(); M.save(b, "JPEG", quality=94)
api.upload_file(path_or_fileobj=b.getvalue(), path_in_repo=os.environ["OUT"], repo_id=REPO, repo_type="dataset"); print("FERTIG", os.environ["OUT"])
