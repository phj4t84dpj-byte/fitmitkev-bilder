# /// script
# dependencies = ["huggingface_hub>=0.30", "requests", "imageio-ffmpeg", "pillow", "faster-whisper", "numpy"]
# ///
# Untertitel fest ins Reel schreiben (groß, mittig, 2–3 Wörter auf einmal).
# Wortlaut kommt aus dem Sprechertext, die Zeiten aus Whisper (Wort-Zeitstempel).
# env JOBS = JSON [{"name":..., "video":url, "text":"Sprechertext mit Ziffern", "ziel":"ordner"}]
# env FONT = URL einer TTF-Schrift. Ergebnis: <ziel>/<name>_untertitel.mp4
import os, re, json, subprocess, difflib, requests
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
GELB, WEISS = (255, 212, 0), (255, 255, 255)


def lade(u, p):
    open(p, "wb").write(requests.get(u, timeout=300).content)


def ff(*a):
    r = subprocess.run([FF, "-y", "-loglevel", "error", *a], capture_output=True, text=True)
    if r.returncode:
        print(r.stderr); raise SystemExit(1)


def norm(w):
    return re.sub(r"[^0-9a-zäöüß]", "", w.lower())


def stuecke(text):
    """Text in Anzeige-Stücke teilen: höchstens 3 Wörter / ca. 18 Zeichen, Schnitt nach Satzzeichen."""
    roh = text.split(); toks, strich = [], set()
    for t in roh:
        if norm(t):
            toks.append(t)
        elif toks:
            strich.add(len(toks) - 1)  # Gedankenstrich: nach dem Wort davor schneiden
    out, cur = [], []
    for i, t in enumerate(toks):
        cur.append(i)
        laenge = len(" ".join(toks[j] for j in cur))
        ende = re.search(r"[.,!?:]$", t) or i in strich
        nxt = len(toks[i + 1]) if i + 1 < len(toks) else 0
        # kurzes Satzende noch mitnehmen („ab in den Ofen.“ statt „ab in den | Ofen.“)
        satzende_naechstes = i + 1 < len(toks) and (re.search(r"[.,!?:]$", toks[i + 1]) or (i + 1) in strich)
        if not ende and satzende_naechstes and len(cur) < 4 and laenge + 1 + nxt <= 21:
            continue
        if ende or len(cur) >= 3 or laenge + 1 + nxt > 18:
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return toks, out


def zeiten(toks, words, dauer):
    """Jedem Sprechertext-Wort eine Startzeit geben (Abgleich mit Whisper, Lücken interpolieren)."""
    a = [norm(t) for t in toks]; b = [norm(w["w"]) for w in words]
    st = [None] * len(toks)
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            st[blk.a + k] = words[blk.b + k]["s"]
    if not words:
        words = [{"s": 0.3, "e": dauer - 0.8}]
    known = [(i, s) for i, s in enumerate(st) if s is not None]
    if not known:
        t0, t1 = words[0]["s"], words[-1]["e"]
        return [t0 + (t1 - t0) * i / len(toks) for i in range(len(toks))], t1
    for i in range(len(toks)):
        if st[i] is None:
            prev = max([k for k in known if k[0] < i], default=None)
            nxt = min([k for k in known if k[0] > i], default=None)
            if prev and nxt:
                st[i] = prev[1] + (nxt[1] - prev[1]) * (i - prev[0]) / (nxt[0] - prev[0])
            elif prev:
                st[i] = prev[1] + 0.35 * (i - prev[0])
            else:
                st[i] = max(0.0, nxt[1] - 0.35 * (nxt[0] - i))
    return st, words[-1]["e"]


def bild(woerter, pfad, W, font):
    """Ein Stück als transparentes PNG (weiß mit schwarzem Rand, Zahlen gelb), bei Bedarf zweizeilig."""
    zeilen, cur = [], []
    for w in woerter:
        test = " ".join(cur + [w])
        if cur and font.getlength(test) * 1.04 > W * 0.9:
            zeilen.append(cur); cur = [w]
        else:
            cur.append(w)
    zeilen.append(cur)
    lh = int(font.size * 1.18)
    img = Image.new("RGBA", (W, lh * len(zeilen) + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    for zi, z in enumerate(zeilen):
        breite = sum(font.getlength(w) for w in z) + font.getlength(" ") * 1.6 * (len(z) - 1); x = (W - breite) / 2; y = 20 + zi * lh
        for w in z:
            farbe = GELB if re.search(r"\d", w) else WEISS
            d.text((x, y), w, font=font, fill=farbe, stroke_width=max(4, font.size // 9), stroke_fill=(0, 0, 0))
            x += font.getlength(w) + font.getlength(" ") * 1.6
    img.save(pfad)
    return img.size[1]


def untertitel(video, text, aus, words=None, fontpfad="font.ttf"):
    info = subprocess.run([FF, "-i", video], capture_output=True, text=True).stderr
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", info).groups(); dauer = int(h) * 3600 + int(m) * 60 + float(s)
    W, H = map(int, re.search(r", (\d{3,4})x(\d{3,4})", info).groups())
    if words is None:
        from faster_whisper import WhisperModel
        import numpy as np
        roh = subprocess.run([FF, "-loglevel", "error", "-i", video, "-vn", "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                             capture_output=True).stdout
        audio = np.frombuffer(roh, dtype=np.float32)
        # ohne initial_prompt: mit Prompt schreibt Whisper den Text ab und die Zeiten werden ungenau
        seg, _ = WhisperModel(os.environ.get("WMODEL", "medium"), device="cpu", compute_type="int8").transcribe(
            audio, language="de", word_timestamps=True, vad_filter=False, condition_on_previous_text=False)
        words = [{"w": w.word.strip(), "s": w.start, "e": w.end} for sg in seg for w in sg.words]
    print("Whisper:", " ".join(f"{w['w']}@{w['s']:.2f}" for w in words), flush=True)
    toks, teile = stuecke(text)
    st, letzt = zeiten(toks, words, dauer)
    font = ImageFont.truetype(fontpfad, int(W * 0.088))
    eingaben, filt, vor = [], [], "[0:v]"
    for k, idx in enumerate(teile):
        a = st[idx[0]]
        b = st[teile[k + 1][0]] if k + 1 < len(teile) else min(dauer - 0.05, letzt + 0.6)
        b = max(b, a + 0.35)
        hoehe = bild([toks[i] for i in idx], f"u{k}.png", W, font)
        y = int(H * 0.60 - hoehe / 2)
        print(f"  {a:5.2f}–{b:5.2f}  {' '.join(toks[i] for i in idx)}", flush=True)
        eingaben += ["-i", f"u{k}.png"]
        nach = f"[v{k}]"
        filt.append(f"{vor}[{k + 1}:v]overlay=0:{y}:enable='between(t,{a:.2f},{b - 0.01:.2f})'{nach}")
        vor = nach
    ff("-i", video, *eingaben, "-filter_complex", ";".join(filt), "-map", vor, "-map", "0:a",
       "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "copy",
       "-movflags", "+faststart", aus)


if __name__ == "__main__":
    from huggingface_hub import HfApi
    api = HfApi(token=os.environ["HF_TOKEN"]); REPO = "kevrsztorm/fitmitkev-bilder"
    lade(os.environ["FONT"], "font.ttf")
    for j in json.loads(os.environ["JOBS"]):
        n = j["name"]; lade(j["video"], "v.mp4"); print("==", n, flush=True)
        untertitel("v.mp4", j["text"], "out.mp4")
        if os.environ.get("DRY"):
            continue
        api.upload_file(path_or_fileobj="out.mp4", path_in_repo=f"{j['ziel']}/{n}_untertitel.mp4", repo_id=REPO, repo_type="dataset")
        print("OK", n, flush=True)
