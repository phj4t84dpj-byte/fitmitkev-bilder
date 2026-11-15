# -*- coding: utf-8 -*-
"""Facebook-Beitragsbild zum YouTube-Video „Langos wie vom Weihnachtsmarkt“ (Kev 15.11.2026, 19:14).
Aufbau wie yt/Facebook_Kuchen_Bowl.jpg: oben das Thumbnail, unten dunkles Feld mit Zutaten (Teig aus Kevs Rezeptkarte),
drei Beläge (Ausschnitte aus dem Thumbnail), kcal-Karte und rote Leiste „Ganzes Video – Link im 1. Kommentar“.
Aufruf: python3 langos.py <thumbnail.png> <ausgabe.jpg>"""
import sys, os, base64, io
from PIL import Image
from playwright.sync_api import sync_playwright
S='/tmp/claude-0/-home-claude/62a14d94-6bfc-5e5c-b2da-15988fbe030e/scratchpad'
F=f"{S}/fonts/gf/ofl"; T=f"{S}/tilex/tiles_orig"
thumb, out = sys.argv[1], sys.argv[2]
def b64(im, fmt='JPEG'):
    b=io.BytesIO(); im.save(b, fmt, quality=92); return base64.b64encode(b.getvalue()).decode()
im=Image.open(thumb).convert('RGB')
top=b64(im)
# Ausschnitte der drei Langos aus dem Thumbnail (Mittelpunkt, Radius in Thumbnail-Pixeln)
crops=[(525,690,175),(912,680,190),(1295,690,185)]
cimg=[]
for cx,cy,r in crops:
    c=im.crop((cx-r,cy-r,cx+r,cy+r)).resize((240,240)); cimg.append(b64(c))
def tile(n): return b64(Image.open(f"{T}/{n}.png").convert('RGBA'),'PNG')
Z=[('210 g','Dinkelmehl','dinkelmehl'),('210 g','Skyr Natur','skyr'),('1½ TL','Backpulver','backpulver'),('4 g pro Langos','Olivenöl + 1 Prise Salz','olivenoel')]
zt=''.join(f'<div class="z"><div class="zi"><img src="data:image/png;base64,{tile(t)}"></div><div><div class="zm">{m}</div><div class="zn">{n}</div></div></div>' for m,n,t in Z)
B=[('1','Klassisch','Skyr-Creme, Käse, Frühlingszwiebeln'),('2','Süß','Skyr-Creme + rote Marmelade'),('3','Pesto &amp; Feta','grünes Pesto, Feta')]
bt=''.join(f'<div class="v"><img src="data:image/jpeg;base64,{cimg[i]}"><div class="vn">{n}</div><div><div class="vt">{t}</div><div class="vs">{s}</div></div></div>' for i,(n,t,s) in enumerate(B))
HTML=f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-SemiBold.ttf');font-weight:600}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-Bold.ttf');font-weight:700}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-Medium.ttf');font-weight:500}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-ExtraBold.ttf');font-weight:800}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#1f1d1b;font-family:P;color:#fff;position:relative;overflow:hidden}}
.top{{position:absolute;left:0;top:0;width:1080px;height:608px;background:url(data:image/jpeg;base64,{top}) center/cover}}
.top:after{{content:'';position:absolute;left:0;right:0;bottom:0;height:60px;background:linear-gradient(to bottom,rgba(31,29,27,0),#1f1d1b)}}
.nb{{position:absolute;width:46px;height:46px;border-radius:10px;background:#ffd400;color:#111;font-weight:800;font-size:30px;display:flex;align-items:center;justify-content:center;box-shadow:0 3px 8px rgba(0,0,0,.4)}}
.left{{position:absolute;left:48px;top:628px;width:548px}}
h2{{font-weight:800;font-size:58px;color:#ffd400;letter-spacing:1px;line-height:1}}
.sub{{font-weight:500;font-size:21px;color:#cfc8bf;margin:6px 0 12px}}
.z{{display:flex;align-items:center;gap:20px;padding:9px 0;border-bottom:2px solid #34312d}}
.zi{{width:78px;height:78px;border-radius:14px;background:#fff;display:flex;align-items:center;justify-content:center;flex:none}}
.zi img{{max-width:70px;max-height:70px}}
.zm{{font-weight:700;font-size:25px;color:#ffd400;line-height:1.1}}
.zn{{font-weight:600;font-size:28px;line-height:1.15}}
.bl{{font-weight:500;font-size:22px;color:#cfc8bf;margin:16px 0 10px}}
.bs3{{display:flex;gap:12px}}
.b{{position:relative;flex:1;background:#2b2825;border-radius:16px;padding:12px 8px 12px;text-align:center}}
.b img{{width:108px;height:108px;border-radius:50%;object-fit:cover;border:3px solid #fff}}
.b .bn{{position:absolute;left:10px;top:10px;width:32px;height:32px;border-radius:7px;background:#ffd400;color:#111;font-weight:800;font-size:21px;display:flex;align-items:center;justify-content:center}}
.bt{{font-weight:700;font-size:21px;margin-top:6px}}
.bs{{font-weight:500;font-size:16px;color:#d8d2ca;line-height:1.25;margin-top:2px}}
.right{{position:absolute;left:628px;top:628px;width:404px}}
.v{{position:relative;display:flex;align-items:center;gap:16px;background:#2b2825;border-radius:18px;padding:10px 14px;margin-bottom:10px}}
.v img{{width:78px;height:78px;border-radius:50%;object-fit:cover;border:3px solid #fff;flex:none}}
.vn{{position:absolute;left:8px;top:8px;width:32px;height:32px;border-radius:7px;background:#ffd400;color:#111;font-weight:800;font-size:21px;display:flex;align-items:center;justify-content:center}}
.vt{{font-weight:700;font-size:24px;line-height:1.15}}
.vs{{font-weight:500;font-size:17px;color:#d8d2ca;line-height:1.3;margin-top:2px}}
.note{{background:#2b2825;border-radius:18px;padding:16px 20px;margin-top:18px}}
.card{{background:#2b2825;border-radius:20px;padding:22px 24px;margin-bottom:16px}}
.k1{{font-weight:600;font-size:19px;letter-spacing:3px;color:#b9b2a8}}
.k2{{font-weight:800;font-size:44px;line-height:1.15}} .k2 span{{color:#ffd400;font-size:32px}}
.k3{{font-weight:500;font-size:24px;color:#e8e2da}}
.pt{{font-weight:700;font-size:24px;line-height:1.25}} .pt b{{color:#ffd400}}
.ps{{font-weight:500;font-size:20px;color:#d8d2ca;line-height:1.35;margin-top:6px}}
.cta{{position:absolute;left:628px;top:1160px;width:404px;height:158px;border-radius:20px;background:#e3261f;padding:18px 24px;box-shadow:0 8px 20px rgba(0,0,0,.35)}}
.c1{{font-weight:700;font-size:18px;letter-spacing:3px;color:#ffe9a8}}
.c2{{font-weight:800;font-size:38px;line-height:1.12;margin-top:6px}}
</style></head><body>
<div class="top"></div>
<div class="nb" style="left:268px;top:262px">1</div><div class="nb" style="left:490px;top:252px">2</div><div class="nb" style="left:706px;top:258px">3</div>
<div class="left"><h2>LANGOS</h2><div class="sub">Zutaten · Teig für 3 Stück</div>{zt}
<div class="note"><div class="pt"><b>Ohne Fritteuse:</b> nur 4 g Öl pro Langos statt im Fett ausgebacken</div><div class="ps">Langos vom Weihnachtsmarkt: oft über 600 kcal</div></div></div>
<div class="right">
<div class="card" style="padding:14px 24px;margin-bottom:8px"><div class="k1">PRO LANGOS</div><div class="k2">unter 400 <span>kcal</span></div><div class="k3">Teig aus Skyr, ohne Hefe</div></div>
<div class="k1" style="margin:4px 0 8px 4px">3 BELÄGE</div>{bt}
</div>
<div class="cta"><div class="c1">▸ GANZES VIDEO</div><div class="c2">Link im<br>1. Kommentar 👇</div></div>
</body></html>"""
open('/tmp/claude-0/-home-claude/62a14d94-6bfc-5e5c-b2da-15988fbe030e/scratchpad/_langos.html','w').write(HTML)
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
    pg.goto('file:///tmp/claude-0/-home-claude/62a14d94-6bfc-5e5c-b2da-15988fbe030e/scratchpad/_langos.html'); pg.wait_for_timeout(500)
    print(pg.evaluate("()=>{const l=document.querySelector('.left').getBoundingClientRect(),r=document.querySelector('.right').getBoundingClientRect();return [l.bottom,r.bottom,document.querySelector('.c2').scrollWidth]}"))
    pg.screenshot(path=out.replace('.jpg','.png')); b.close()
Image.open(out.replace('.jpg','.png')).convert('RGB').save(out,quality=92); os.remove(out.replace('.jpg','.png'))
print('ok',out)
