# /// script
# dependencies = ["huggingface_hub>=0.30", "requests"]
# ///
# Holt zu YouTube-Videos Titel, Beschreibung und Thumbnail (ohne Token an YouTube) und legt alles
# in einem Commit im Datensatz kevrsztorm/fitmitkev-bilder unter yt/<ORDNER>/ ab.
# env IDS = Komma-Liste der Video-Ids, ORDNER = Zielordner
import os, json, re, requests, tempfile
from huggingface_hub import HfApi
api = HfApi(token=os.environ["HF_TOKEN"]); REPO = "kevrsztorm/fitmitkev-bilder"
ids = os.environ["IDS"].split(","); ordner = os.environ.get("ORDNER", "ytwoche")
H = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
     "Accept-Language": "de-DE,de;q=0.9"}
tmp = tempfile.mkdtemp(); info = {}
for v in ids:
    d = {"id": v}
    try:
        o = requests.get("https://www.youtube.com/oembed", params={"url": f"https://www.youtube.com/watch?v={v}", "format": "json"}, headers=H, timeout=30).json()
        d["titel"] = o.get("title")
    except Exception as e: d["oembed_fehler"] = str(e)
    try:
        html = requests.get(f"https://www.youtube.com/watch?v={v}&hl=de", headers=H, cookies={"CONSENT": "YES+1"}, timeout=30).text
        m = re.search(r'"shortDescription":"((?:[^"\\]|\\.)*)"', html)
        if m: d["beschreibung"] = json.loads('"' + m.group(1) + '"')
        m = re.search(r'"lengthSeconds":"(\d+)"', html)
        if m: d["sekunden"] = int(m.group(1))
        m = re.search(r'"publishDate":"([^"]+)"', html)
        if m: d["datum"] = m.group(1)
    except Exception as e: d["seite_fehler"] = str(e)
    for q in ("maxresdefault", "sddefault", "hqdefault"):
        r = requests.get(f"https://i.ytimg.com/vi/{v}/{q}.jpg", headers=H, timeout=30)
        if r.ok and len(r.content) > 5000:
            open(f"{tmp}/{v}.jpg", "wb").write(r.content); d["thumb"] = q; break
    info[v] = d; print(v, d.get("titel"), d.get("thumb"), len(d.get("beschreibung", "")))
json.dump(info, open(f"{tmp}/info.json", "w"), ensure_ascii=False, indent=1)
api.upload_folder(folder_path=tmp, path_in_repo=f"yt/{ordner}", repo_id=REPO, repo_type="dataset")
print("FERTIG")
