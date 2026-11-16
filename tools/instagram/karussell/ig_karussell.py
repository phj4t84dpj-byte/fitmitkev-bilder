# -*- coding: utf-8 -*-
"""Instagram-Rezept-Karussell „Schritt für Schritt“ (3:4, 1080x1440): Foto vollflächig, Text oben mittig
(Poppins Bold, weiß, schwarze Kontur 7 px + weicher Schatten); letzte Slide = Einkaufsliste im Notiz-Look mit Folgen-Leiste.
Aufruf: python3 ig_karussell.py <rezept.json>  ->  out/<slug>-1.jpg … -N.jpg"""
import sys, os, json, html
from PIL import Image
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D); F=f"{S}/fonts/gf/ofl"
R=json.load(open(sys.argv[1])); slug=R['slug']
FONT=f"""@font-face{{font-family:P;src:url('{F}/poppins/Poppins-Bold.ttf');font-weight:700}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-SemiBold.ttf');font-weight:600}}
@font-face{{font-family:I;src:url('{F}/inter/Inter[opsz,wght].ttf');font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1440px;overflow:hidden;position:relative}}"""
def slide(img,text,size):
    t=html.escape(text).replace('\\n','<br>').replace('\n','<br>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONT}
.bg{{position:absolute;inset:0;width:1080px;height:1440px;object-fit:cover}}
.t{{position:absolute;left:60px;right:60px;top:70px;text-align:center;font-family:P;font-weight:700;font-size:{size}px;line-height:1.18;color:#fff;
  -webkit-text-stroke:7px #000;paint-order:stroke fill;text-shadow:0 4px 18px rgba(0,0,0,.45)}}
</style></head><body><img class="bg" src="{img}"><div class="t">{t}</div></body></html>"""
def liste(img):
    z=''.join(f'<div class="z"><span class="cb"></span><b>{html.escape(m)}</b>&nbsp;{html.escape(n)}</div>' for m,n in R['zutaten'])
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONT}
body{{background:#f6f5f2;font-family:I}}
.ph{{position:absolute;left:60px;top:60px;width:960px;height:520px;border-radius:34px;object-fit:cover;object-position:{R.get('pos','50% 45%')}}}
.h{{position:absolute;left:70px;top:612px;width:940px;font-weight:800;font-size:56px;color:#1c1c1e;line-height:1.1}}
.s{{position:absolute;left:70px;top:{R.get('s_top',690)}px;width:940px;font-weight:500;font-size:30px;color:#8e8e93}}
.l{{position:absolute;left:70px;top:{R.get('l_top',748)}px;width:940px}}
.z{{display:flex;align-items:center;font-size:33px;color:#1c1c1e;padding:9px 0;border-bottom:1.5px solid #e2e1dd}} .z b{{font-weight:700}}
.cb{{width:34px;height:34px;border:3px solid #c7c7cc;border-radius:50%;margin-right:20px;flex:none}}
.n{{margin-top:16px;font-size:30px;font-weight:600;color:#1c1c1e}} .n span{{color:#e0533d}}
.f{{position:absolute;left:60px;right:60px;bottom:52px;height:128px;background:#fff;border-radius:30px;box-shadow:0 4px 18px rgba(0,0,0,.08);display:flex;align-items:center;padding:0 26px;gap:22px}}
.ring{{width:96px;height:96px;border-radius:50%;padding:5px;background:conic-gradient(#feda75,#fa7e1e,#d62976,#962fbf,#4f5bd5,#feda75);flex:none}}
.ring img{{width:86px;height:86px;border-radius:50%;border:4px solid #fff;object-fit:cover}}
.u{{flex:1}} .u1{{font-weight:700;font-size:34px;color:#1c1c1e}} .u2{{font-size:26px;color:#8e8e93;font-weight:500}}
.btn{{background:#0095f6;color:#fff;font-weight:700;font-size:32px;padding:16px 38px;border-radius:16px}}
</style></head><body><img class="ph" src="{img}">
<div class="h">{html.escape(R['name'])}</div><div class="s">{html.escape(R['info'])}</div>
<div class="l">{z}<div class="n">{html.escape(R['naehr'])}</div></div>
<div class="f"><div class="ring"><img src="{D}/profil.jpg"></div><div class="u"><div class="u1">fitmitkev</div><div class="u2">Abnehmen ohne Verzicht</div></div><div class="btn">Folgen</div></div>
</body></html>"""
os.makedirs(f'{D}/out',exist_ok=True)
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1440},device_scale_factor=1)
    pages=[slide(f"{D}/roh/{s['img']}.jpg",s['text'],s.get('size',74)) for s in R['slides']]+[liste(f"{D}/roh/{R['listen_bild']}.jpg")]
    for i,h in enumerate(pages,1):
        open(f'{D}/out/_s.html','w').write(h); pg.goto(f'file://{D}/out/_s.html'); pg.wait_for_timeout(400)
        if i==len(pages):
            bot=pg.evaluate("()=>{const l=document.querySelector('.l').getBoundingClientRect(),f=document.querySelector('.f').getBoundingClientRect();return [Math.round(l.bottom),Math.round(f.top)]}")
            print('Liste unten/Leiste oben:',bot)
        pg.screenshot(path=f'{D}/out/_s.png'); Image.open(f'{D}/out/_s.png').convert('RGB').save(f'{D}/out/{slug}-{i}.jpg',quality=93)
    b.close()
print('ok',slug,len(pages))
