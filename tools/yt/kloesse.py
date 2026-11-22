# -*- coding: utf-8 -*-
"""Facebook-Beitragsbild zum YouTube-Video „Klöße mit Hack und Käse überbacken“ (Kev 22.11.2026, 21:41).
Aufbau wie yt/Facebook_Langos.jpg und yt/Facebook_Kuchen_Bowl.jpg: oben das Thumbnail, unten dunkles Feld mit den Zutaten
(Kevs Liste aus der Videobeschreibung), rechts kcal-Karte, drei Stichpunkte und rote Leiste „Ganzes Video – Link im 1. Kommentar“.
Auf dem Bild steht kein Markenname (Kochsahne light statt Cremefine) und in der Facebook-Fassung des Thumbnails kein „Abnehm-“
(Regel: das Wort „abnehmen“ nicht auf Facebook-Bildern) – dafür „Überbackene Klöße“, siehe thumb_fb().
Nährwerte von Kev: 3 Portionen je 395 kcal / 33 g Eiweiß; ganze Form 1.190 kcal / 99 g Eiweiß → halbe Form 595 kcal / 50 g Eiweiß
(daher „50g PROTEIN“ auf dem Thumbnail).
Aufruf: python3 kloesse.py <thumbnail.png> <ausgabe.jpg>            (Thumbnail unverändert)
        python3 kloesse.py <thumbnail.png> <ausgabe.jpg> fb         (Thumbnail mit neuem Titel ohne „Abnehm-“)"""
import sys, os, base64, io
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright
S='/tmp/claude-0/-home-claude/62a14d94-6bfc-5e5c-b2da-15988fbe030e/scratchpad'
F=f"{S}/fonts/gf/ofl"; T=f"{S}/tilex/tiles_orig"
thumb, out = sys.argv[1], sys.argv[2]
FB = len(sys.argv)>3 and sys.argv[3]=='fb'

def thumb_fb(path):
    """Gelben Titel „Abnehm-/Klöße“ (1365x768-Thumbnail) herausrechnen und „Überbackene/Klöße“ in gleicher Farbe neu setzen.
    Zeile 1: jede Spalte läuft gerade von Bildzeile 1 nach 133 (gleichmäßig dunkle Wand). Zeile 2: jede Zeile läuft gerade von
    Spalte 872 nach 1284 (die waagerechte Lichterleiste bleibt erhalten). Danach weiche Kante und etwas Körnung."""
    import cv2
    im=cv2.imread(path).astype(np.float32); H,W=im.shape[:2]; o=im.copy()
    x0,x1,ya,yb=782,W,1,133
    t=((np.arange(ya,yb+1)-ya)/(yb-ya))[:,None,None]
    o[ya:yb+1,x0:x1]=im[ya:ya+1,x0:x1]*(1-t)+im[yb:yb+1,x0:x1]*t
    xa,xb,y0,y1=872,1284,134,264
    s=((np.arange(xa,xb+1)-xa)/(xb-xa))[None,:,None]
    o[y0:y1+1,xa:xb+1]=im[y0:y1+1,xa:xa+1]*(1-s)+im[y0:y1+1,xb:xb+1]*s
    m=np.zeros((H,W),np.float32); m[ya:yb+1,x0:x1]=1; m[y0:y1+1,xa:xb+1]=1
    mb=cv2.GaussianBlur(m,(0,0),3)[:,:,None]
    o=o*(1-mb)+cv2.GaussianBlur(o,(0,0),5)*mb
    o+=np.random.default_rng(3).normal(0,1.6,o.shape).astype(np.float32)*mb
    pil=Image.fromarray(np.clip(o,0,255).astype(np.uint8)[:,:,::-1]); d=ImageDraw.Draw(pil)
    def setze(txt,size,cx,base,sw):
        f=ImageFont.truetype(f"{F}/poppins/Poppins-ExtraBold.ttf",size); bb=d.textbbox((0,0),txt,font=f,anchor='ls',stroke_width=sw)
        d.text((cx-(bb[2]-bb[0])/2-bb[0],base),txt,font=f,fill=(243,207,3),anchor='ls',stroke_width=sw,stroke_fill=(20,18,14))
    setze('Überbackene',80,1072,100,4); setze('Klöße',152,1072,252,5)
    return pil

def b64(im, fmt='JPEG'):
    b=io.BytesIO(); im.save(b, fmt, quality=93); return base64.b64encode(b.getvalue()).decode()
im = thumb_fb(thumb) if FB else Image.open(thumb).convert('RGB')
top=b64(im)
def tile(n): return b64(Image.open(f"{T}/{n}.png").convert('RGBA'),'PNG')
Z=[('300 g','Kloßteig (küchenfertig)','kartoffelkloesse'),('300 g','Mageres Rinderhack (max. 5 % Fett)','rinderhack'),
   ('100 g','Reibekäse (fettarm)','reibekaese_light'),('100 g','Kochsahne light','kochsahne'),
   ('1 Stück','Rote Paprika','rote_paprika'),('1 Stück','Möhre','karotten'),('1 Stück','Rote Zwiebel','rote_zwiebel'),('20 g','Tomatenmark','tomatenmark')]
zt=''.join(f'<div class="z"><div class="zi"><img src="data:image/png;base64,{tile(t)}"></div><div><div class="zm">{m}</div><div class="zn">{n}</div></div></div>' for m,n,t in Z)
B=[('1','Fertiger Kloßteig','aus dem Kühlregal, kein Reiben'),('2','Hack-Gemüse-Soße','mit Paprika, Möhre und Zwiebel'),('3','Mit Käse überbacken','alles zusammen in einer Form')]
bt=''.join(f'<div class="v"><div class="vn">{n}</div><div><div class="vt">{t}</div><div class="vs">{s}</div></div></div>' for n,t,s in B)
HTML=f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-SemiBold.ttf');font-weight:600}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-Bold.ttf');font-weight:700}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-Medium.ttf');font-weight:500}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-ExtraBold.ttf');font-weight:800}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#1f1d1b;font-family:P;color:#fff;position:relative;overflow:hidden}}
.top{{position:absolute;left:0;top:0;width:1080px;height:608px;background:url(data:image/jpeg;base64,{top}) center/cover}}
.top:after{{content:'';position:absolute;left:0;right:0;bottom:0;height:60px;background:linear-gradient(to bottom,rgba(31,29,27,0),#1f1d1b)}}
.left{{position:absolute;left:48px;top:628px;width:548px}}
h2{{font-weight:800;font-size:58px;color:#ffd400;letter-spacing:1px;line-height:1}}
.sub{{font-weight:500;font-size:21px;color:#cfc8bf;margin:6px 0 6px}}
.z{{display:flex;align-items:center;gap:18px;padding:4px 0;border-bottom:2px solid #34312d}}
.zi{{width:54px;height:54px;border-radius:11px;background:#fff;display:flex;align-items:center;justify-content:center;flex:none}}
.zi img{{max-width:48px;max-height:48px}}
.zm{{font-weight:700;font-size:20px;color:#ffd400;line-height:1.1}}
.zn{{font-weight:600;font-size:23px;line-height:1.15}}
.dazu{{background:#2b2825;border-radius:14px;padding:8px 16px;margin-top:9px;font-weight:500;font-size:18.5px;color:#e8e2da;line-height:1.3}}
.dazu b{{color:#ffd400;font-weight:700}}
.right{{position:absolute;left:628px;top:628px;width:404px}}
.card{{background:#2b2825;border-radius:20px;padding:14px 24px 16px;margin-bottom:10px}}
.k1{{font-weight:600;font-size:19px;letter-spacing:3px;color:#b9b2a8}}
.k2{{font-weight:800;font-size:46px;line-height:1.12}} .k2 span{{color:#ffd400;font-size:32px}}
.k3{{font-weight:600;font-size:25px;color:#fff}}
.k4{{font-weight:500;font-size:19px;color:#d8d2ca;border-top:2px solid #3a3632;margin-top:10px;padding-top:9px;line-height:1.3}} .k4 b{{color:#ffd400;font-weight:700}}
.v{{position:relative;display:flex;align-items:center;gap:16px;background:#2b2825;border-radius:18px;padding:10px 16px;margin-bottom:8px;min-height:76px}}
.vn{{width:40px;height:40px;border-radius:9px;background:#ffd400;color:#111;font-weight:800;font-size:25px;display:flex;align-items:center;justify-content:center;flex:none}}
.vt{{font-weight:700;font-size:24px;line-height:1.15}}
.vs{{font-weight:500;font-size:17.5px;color:#d8d2ca;line-height:1.3;margin-top:2px}}
.cta{{position:absolute;left:628px;top:1160px;width:404px;height:158px;border-radius:20px;background:#e3261f;padding:18px 24px;box-shadow:0 8px 20px rgba(0,0,0,.35)}}
.c1{{font-weight:700;font-size:18px;letter-spacing:3px;color:#ffe9a8}}
.c2{{font-weight:800;font-size:38px;line-height:1.12;margin-top:6px}}
</style></head><body>
<div class="top"></div>
<div class="left"><h2>ZUTATEN</h2><div class="sub">für 2–3 Portionen · eine Auflaufform</div>{zt}
<div class="dazu"><b>Dazu:</b> 5 g Gemüsebrühe (Pulver) und eine Messerspitze Butter zum Anbraten</div></div>
<div class="right">
<div class="card"><div class="k1">PRO PORTION</div><div class="k2">395 <span>kcal</span></div><div class="k3">33 g Eiweiß</div>
<div class="k4">bei 3 Portionen · die halbe Form hat<br><b>595 kcal und 50 g Eiweiß</b></div></div>
<div class="k1" style="margin:12px 0 8px 4px">SO EINFACH</div>{bt}
</div>
<div class="cta"><div class="c1">▸ GANZES VIDEO</div><div class="c2">Link im<br>1. Kommentar 👇</div></div>
</body></html>"""
hp=f'{S}/yt3/_kloesse.html'; os.makedirs(os.path.dirname(hp),exist_ok=True); open(hp,'w').write(HTML)
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
    pg.goto('file://'+hp); pg.wait_for_timeout(500)
    print(pg.evaluate("()=>{const l=document.querySelector('.left').getBoundingClientRect(),r=document.querySelector('.right').getBoundingClientRect();return {links_unten:l.bottom,rechts_unten:r.bottom,cta_oben:1160,rand_unten:1318,breit:[...document.querySelectorAll('.zn,.vt,.vs')].filter(e=>e.scrollWidth>e.clientWidth+1).map(e=>e.textContent)}}"))
    pg.screenshot(path=out.replace('.jpg','.png')); b.close()
Image.open(out.replace('.jpg','.png')).convert('RGB').save(out,quality=93); os.remove(out.replace('.jpg','.png'))
print('ok',out)
