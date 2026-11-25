# /// script
# dependencies = ["huggingface_hub>=0.30", "requests", "pillow", "imageio-ffmpeg"]
# ///
# Rezeptvideo-Test: Clips holen, auf 4:5 (720x900) bringen, Schrift als Bild darüberlegen, zusammenschneiden.
# env SPEC = JSON {"name": "...", "clips": [[quelle, dauer, text], ...], "ende": [bildquelle, dauer, [zeile1, zeile2, ...]]}
#   quelle: "hf:pfad/im/datensatz" oder https-Adresse. Ergebnis: video1/<name>.mp4 und video1/<name>_sheet.jpg im Datensatz.
import os, json, subprocess, requests, io
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from huggingface_hub import HfApi, hf_hub_download
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
TOK = os.environ["HF_TOKEN"]; api = HfApi(token=TOK); REPO = "kevrsztorm/fitmitkev-bilder"
SPEC = json.loads(os.environ["SPEC"]); W, H = 720, 900
FONT = "https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/tools/fonts/Poppins-Bold.ttf"
open("font.ttf", "wb").write(requests.get(FONT, timeout=60).content)

def hole(q, ziel):
    if q.startswith("hf:"):
        p = hf_hub_download(REPO, q[3:], repo_type="dataset", token=TOK); os.system(f"cp '{p}' '{ziel}'")
    else:
        r = requests.get(q, headers={"Authorization": f"Bearer {TOK}"}, timeout=180); r.raise_for_status(); open(ziel, "wb").write(r.content)

def schrift(zeilen, datei, gross=54, oben=False):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    f = ImageFont.truetype("font.ttf", gross); y = 70 if oben else None
    boxen = []
    for z in zeilen:
        while d.textlength(z, font=f) > W - 90 and f.size > 28: f = ImageFont.truetype("font.ttf", f.size - 2)
    hz = f.size + 26; gesamt = hz * len(zeilen) + 10 * (len(zeilen) - 1)
    if y is None: y = H - gesamt - 90
    for z in zeilen:
        tw = d.textlength(z, font=f); x = (W - tw) / 2
        d.rounded_rectangle([x - 22, y, x + tw + 22, y + hz], radius=18, fill=(255, 248, 238, 235))
        d.text((x, y + 9), z, font=f, fill=(92, 52, 30, 255)); y += hz + 10
    img.save(datei)

def lauf(*a):
    r = subprocess.run([FF, "-y", "-loglevel", "error", *a], capture_output=True, text=True)
    if r.returncode: print(r.stderr); raise SystemExit(1)

VF = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}:(iw-{W})/2:(ih-{H})*0.85,fps=24,setsar=1"
segs = []; DAUER = {}
for i, (q, dauer, text) in enumerate(SPEC["clips"], 1):
    hole(q, f"c{i}.mp4"); schrift(text, f"t{i}.png", oben=SPEC.get("oben", False))
    lauf("-i", f"c{i}.mp4", "-loop", "1", "-i", f"t{i}.png", "-filter_complex", f"[0:v]{VF}[v];[v][1:v]overlay=0:0:shortest=1,format=yuv420p",
         "-t", str(dauer), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", f"s{i}.mp4")
    segs.append(f"s{i}.mp4"); DAUER[f"s{i}.mp4"] = dauer; print("Clip", i, "fertig")
q, dauer, zeilen = SPEC["ende"]; hole(q, "ende_src.jpg")
bg = Image.open("ende_src.jpg").convert("RGB"); s = max(W / bg.width, H / bg.height)
bg = bg.resize((int(bg.width * s) + 1, int(bg.height * s) + 1)); bg = bg.crop(((bg.width - W) // 2, (bg.height - H) // 2, (bg.width - W) // 2 + W, (bg.height - H) // 2 + H))
bg.save("ende.jpg", quality=95); schrift(zeilen, "te.png", gross=58)
n = int(dauer * 24)
lauf("-loop", "1", "-i", "ende.jpg", "-loop", "1", "-i", "te.png", "-filter_complex",
     f"[0:v]scale=1440:1800,zoompan=z='1+0.0008*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps=24,setsar=1[v];[v][1:v]overlay=0:0,format=yuv420p",
     "-frames:v", str(n), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "sE.mp4")
segs.append("sE.mp4"); DAUER["sE.mp4"] = dauer
open("liste.txt", "w").write("".join(f"file '{x}'\n" for x in segs))
name = SPEC["name"]
lauf("-f", "concat", "-safe", "0", "-i", "liste.txt", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest",
     "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-movflags", "+faststart", f"{name}.mp4")
# Kontaktbogen: je Abschnitt 3 Bilder
bilder = []
for x in segs:
    for t in (0.3, 0.5, 0.85):
        lauf("-ss", f"{t * DAUER[x] * 0.95:.2f}", "-i", x, "-frames:v", "1", "f.jpg")
        bilder.append(Image.open("f.jpg").convert("RGB").resize((240, 300)))
sp = 6; zeilen_n = (len(bilder) + sp - 1) // sp
sheet = Image.new("RGB", (240 * sp, 300 * zeilen_n), "white")
for k, b in enumerate(bilder): sheet.paste(b, ((k % sp) * 240, (k // sp) * 300))
sheet.save("sheet.jpg", quality=88)
api.upload_file(path_or_fileobj=f"{name}.mp4", path_in_repo=f"video1/{name}.mp4", repo_id=REPO, repo_type="dataset")
api.upload_file(path_or_fileobj="sheet.jpg", path_in_repo=f"video1/{name}_sheet.jpg", repo_id=REPO, repo_type="dataset")
print("FERTIG", os.path.getsize(f"{name}.mp4"))
