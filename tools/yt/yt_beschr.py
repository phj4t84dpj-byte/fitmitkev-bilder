# /// script
# dependencies = ["huggingface_hub>=0.30", "requests"]
# ///
# Holt Video-Beschreibungen über die öffentliche YouTube-Player-Schnittstelle (ohne Token an YouTube)
# und legt sie als yt/<ORDNER>/beschreibungen.json im Datensatz ab. env IDS, ORDNER
import os, json, re, requests
from huggingface_hub import HfApi
api = HfApi(token=os.environ["HF_TOKEN"]); REPO = "kevrsztorm/fitmitkev-bilder"
ids = os.environ["IDS"].split(","); ordner = os.environ.get("ORDNER", "ytwoche")
CL = [("WEB", "2.20241120.01.00", {}), ("ANDROID", "19.44.38", {"androidSdkVersion": 30}),
      ("TVHTML5_SIMPLY_EMBEDDED_PLAYER", "2.0", {}), ("IOS", "19.45.4", {"deviceModel": "iPhone16,2"})]
out = {}
for v in ids:
    d = {}
    for name, ver, extra in CL:
        try:
            body = {"videoId": v, "context": {"client": {"clientName": name, "clientVersion": ver, "hl": "de", "gl": "DE", **extra}}}
            r = requests.post("https://www.youtube.com/youtubei/v1/player?prettyPrint=false", json=body,
                              headers={"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}, timeout=30)
            vd = r.json().get("videoDetails", {})
            if vd.get("shortDescription"):
                d = {"client": name, "titel": vd.get("title"), "beschreibung": vd["shortDescription"], "sekunden": vd.get("lengthSeconds")}
                break
            d.setdefault("versuche", []).append(f"{name}:{r.status_code}:{list(r.json().keys())[:5]}")
        except Exception as e:
            d.setdefault("versuche", []).append(f"{name}:{e}")
    if not d.get("beschreibung"):
        try:
            h = requests.get(f"https://www.youtube.com/watch?v={v}&hl=de&bpctr=9999999999", headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)", "Accept-Language": "de-DE"},
                             cookies={"SOCS": "CAI", "CONSENT": "YES+cb"}, timeout=30).text
            m = re.search(r'"shortDescription":"((?:[^"\\]|\\.)*)"', h)
            if m: d["beschreibung"] = json.loads('"' + m.group(1) + '"'); d["client"] = "html"
            else: d.setdefault("versuche", []).append("html:" + h[:200].replace("\n", " "))
        except Exception as e: d.setdefault("versuche", []).append(f"html:{e}")
    out[v] = d; print(v, d.get("client"), len(d.get("beschreibung", "")), d.get("versuche"))
api.upload_file(path_or_fileobj=json.dumps(out, ensure_ascii=False, indent=1).encode(), path_in_repo=f"yt/{ordner}/beschreibungen.json", repo_id=REPO, repo_type="dataset")
print("FERTIG")
