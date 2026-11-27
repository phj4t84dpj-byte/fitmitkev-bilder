# /// script
# dependencies = ["huggingface_hub>=0.30", "requests", "imageio-ffmpeg", "numpy", "num2words",
#                 "torch==2.5.1", "torchaudio==2.5.1"]
# [[tool.uv.index]]
# name = "pytorch-cpu"
# url = "https://download.pytorch.org/whl/cpu"
# explicit = true
# [tool.uv.sources]
# torch = { index = "pytorch-cpu" }
# torchaudio = { index = "pytorch-cpu" }
# ///
# Wort-Zeiten einer Sprachaufnahme bestimmen (erzwungene Ausrichtung, torchaudio MMS_FA).
# env JOBS = JSON [{"name":..., "voice":url, "text":"Sprechertext mit Ziffern", "ziel":"ordner"}]
# Ergebnis: <ziel>/<name>_zeiten.json = {"dauer": s, "woerter": [{"w","s","e"}, ...]}
import os, re, json, subprocess, requests
import numpy as np, torch, torchaudio
import imageio_ffmpeg
from num2words import num2words
from huggingface_hub import HfApi

FF = imageio_ffmpeg.get_ffmpeg_exe()


def norm(w):
    return re.sub(r"[^0-9a-zäöüß]", "", w.lower())


def gesprochen(t):
    t = re.sub(r"\d+", lambda m: num2words(int(m.group()), lang="de"), t.lower())
    for a, b in (("ä", "a"), ("ö", "o"), ("ü", "u"), ("ß", "ss")):
        t = t.replace(a, b)
    return re.sub(r"[^a-z]", "", t)


api = HfApi(token=os.environ["HF_TOKEN"]); REPO = "kevrsztorm/fitmitkev-bilder"
b = torchaudio.pipelines.MMS_FA
model = b.get_model(with_star=False); tok = b.get_tokenizer(); aligner = b.get_aligner()
for j in json.loads(os.environ["JOBS"]):
    open("s.audio", "wb").write(requests.get(j["voice"], timeout=300).content)
    roh = subprocess.run([FF, "-loglevel", "error", "-i", "s.audio", "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                         capture_output=True).stdout
    wav = torch.from_numpy(np.frombuffer(roh, dtype=np.float32).copy())[None]
    toks = [t for t in j["text"].split() if norm(t)]
    with torch.inference_mode():
        em, _ = model(wav)
    spans = aligner(em[0], tok([gesprochen(t) for t in toks]))
    r = wav.size(1) / em.size(1) / 16000
    out = {"dauer": wav.size(1) / 16000,
           "woerter": [{"w": t, "s": round(sp[0].start * r, 3), "e": round(sp[-1].end * r, 3)} for t, sp in zip(toks, spans)]}
    json.dump(out, open("z.json", "w"), ensure_ascii=False)
    api.upload_file(path_or_fileobj="z.json", path_in_repo=f"{j['ziel']}/{j['name']}_zeiten.json", repo_id=REPO, repo_type="dataset")
    print("OK", j["name"], round(out["dauer"], 2), flush=True)
