# /// script
# dependencies = ["huggingface_hub>=0.30", "requests"]
# ///
# Holt Dateien von hf.space-Adressen (aus der Shell gesperrt) und legt sie im Datensatz kevrsztorm/fitmitkev-bilder ab.
# env JOBS = JSON-Liste [[url, ziel], ...]
import os, json, requests
from huggingface_hub import HfApi
TOK = os.environ["HF_TOKEN"]; api = HfApi(token=TOK); REPO = "kevrsztorm/fitmitkev-bilder"
for url, ziel in json.loads(os.environ["JOBS"]):
    try:
        r = requests.get(url, headers={"Authorization": f"Bearer {TOK}"}, timeout=120); r.raise_for_status()
        api.upload_file(path_or_fileobj=r.content, path_in_repo=ziel, repo_id=REPO, repo_type="dataset")
        print("OK", ziel, len(r.content))
    except Exception as e:
        print("FEHLER", ziel, e)
