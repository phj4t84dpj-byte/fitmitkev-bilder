# -*- coding: utf-8 -*-
# Startbild 30-Tage-Challenge „Gesunde Routinen“ (1080x1350 @2x), Karopapier + Kugelschreiber
import os, random
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); F=D+'/../fonts/gf/ofl'
INK='#1d3a8a'; RED='#c62828'
random.seed(7)
def wob(x1,y1,x2,y2,j=2.2):  # leicht zittrige Kugelschreiber-Linie
    mx=(x1+x2)/2+random.uniform(-j,j); my=(y1+y2)/2+random.uniform(-j,j)
    return f'M{x1:.1f},{y1:.1f} Q{mx:.1f},{my:.1f} {x2:.1f},{y2:.1f}'
def box(x,y,s):
    p=[wob(x,y,x+s,y+1),wob(x+s,y,x+s-1,y+s),wob(x+s,y+s,x,y+s-1),wob(x,y+s,x+1,y-2)]
    return ''.join(f'<path d="{d}"/>' for d in p)
# 30 Kästchen
cells=''; nums=''
S=82; G=13; X0=(1080-(10*S+9*G))/2; Y0=0
for i in range(30):
    r,c=divmod(i,10); x=X0+c*(S+G); y=Y0+r*(S+G)
    cells+=box(x+4,y+4,S-8)
    nums+=f'<div class="n" style="left:{x+11}px;top:{y+6}px">{i+1}</div>'
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:P;src:url(file://{F}/poppins/Poppins-Medium.ttf);font-weight:500}}
@font-face{{font-family:P;src:url(file://{F}/poppins/Poppins-Bold.ttf);font-weight:700}}
@font-face{{font-family:P;src:url(file://{F}/poppins/Poppins-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:C;src:url(file://{F}/caveat/Caveat[wght].ttf)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:P;color:#24262b;
background-color:#fbf7ee;background-image:linear-gradient(rgba(70,120,190,.16) 1.5px,transparent 1.5px),linear-gradient(90deg,rgba(70,120,190,.16) 1.5px,transparent 1.5px);background-size:36px 36px;background-position:-2px -2px}}
.h{{font-family:C;font-weight:600;color:{INK}}}
.top{{position:absolute;left:0;right:0;top:46px;text-align:center}}
.k{{font-size:62px;line-height:1;transform:rotate(-2deg)}}
.t1{{font-weight:800;font-size:132px;line-height:1;letter-spacing:-2px;margin-top:40px}}
.t1 span{{position:relative;display:inline-block;padding:0 18px}}
.t2{{font-weight:800;font-size:66px;line-height:1.05;letter-spacing:.5px;color:{RED};margin-top:36px}}
.hab{{position:absolute;left:96px;right:60px;top:432px}}
.r{{display:flex;align-items:center;gap:26px;height:104px}}
.cb{{width:70px;height:70px;flex:none;position:relative}}
.r b{{display:block;font-size:42px;font-weight:700;line-height:1.1}}
.r i{{display:block;font-style:normal;font-family:C;font-weight:500;font-size:36px;color:{INK};line-height:1.1;margin-top:2px}}
.trk{{position:absolute;left:0;right:0;top:790px;height:400px}}
.tl{{position:absolute;left:0;right:0;top:762px;text-align:center;font-size:46px}}
.n{{position:absolute;font-family:C;font-weight:600;font-size:28px;color:{INK};opacity:.85}}
.foot{{position:absolute;left:0;right:0;top:1180px;text-align:center;font-size:50px;line-height:1.15}}
svg{{position:absolute;left:0;top:0;overflow:visible}}
svg path{{fill:none;stroke:{INK};stroke-width:3.2;stroke-linecap:round;stroke-linejoin:round}}
</style></head><body>
<div class="top"><div class="k h">Meine Challenge für dich:</div>
<div class="t1"><span id="z">30 TAGE</span></div>
<div class="t2">GESUNDE ROUTINEN</div></div>
<div class="hab">
 <div class="r"><div class="cb"><svg width="70" height="70">{box(6,6,58)}</svg></div><div><b>5.000 Schritte am Tag</b><i>Spaziergang, Einkauf, Treppe – alles zählt</i></div></div>
 <div class="r"><div class="cb"><svg width="70" height="70">{box(6,6,58)}</svg></div><div><b>Mehr Gemüse</b><i>zu jeder Hauptmahlzeit eine Handvoll</i></div></div>
 <div class="r"><div class="cb"><svg width="70" height="70">{box(6,6,58)}</svg></div><div><b>Mehr Eiweiß</b><i>Skyr, Quark, Eier, Fisch, Fleisch oder Linsen</i></div></div>
</div>
<div class="tl h">Jeden Tag geschafft? Kästchen abhaken!</div>
<div class="trk"><svg width="1080" height="400" style="top:66px">{cells}</svg><div style="position:absolute;left:0;top:66px">{nums}</div></div>
<div class="foot h">Speicher dir das Bild –<br>wir starten zusammen! Kev</div>
<svg width="1080" height="1350" id="ov"></svg>
</body></html>'''
open(D+'/start.html','w').write(html)
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    pg.goto('file://'+D+'/start.html'); pg.wait_for_timeout(600)
    r=pg.evaluate("(()=>{const e=document.getElementById('z').getBoundingClientRect();return [e.left,e.top,e.width,e.height]})()")
    x,y,w,h=r; cx=x+w/2; cy=y+h/2+4; rx=w/2+34; ry=h/2+16
    # Kugelschreiber-Kringel um „30 TAGE“ (zweimal, leicht versetzt) + Unterstrich unter GESUNDE ROUTINEN
    import math
    def ell(rx,ry,a0,a1,dx,dy):
        pts=[(cx+dx+rx*math.cos(t)*(1+0.012*math.sin(5*t)),cy+dy+ry*math.sin(t)) for t in [a0+(a1-a0)*k/60 for k in range(61)]]
        return 'M'+' L'.join(f'{px:.1f},{py:.1f}' for px,py in pts)
    d1=ell(rx,ry,-2.9,3.5,0,0); d2=ell(rx+8,ry+6,-2.6,3.3,-4,3)
    t2=pg.evaluate("(()=>{const e=document.querySelector('.t2').getBoundingClientRect();return [e.left,e.bottom,e.width]})()")
    ux,uy,uw=t2; ux+=uw*0.18; uw*=0.64
    u=f'M{ux:.1f},{uy+4:.1f} Q{ux+uw/2:.1f},{uy+12:.1f} {ux+uw:.1f},{uy+2:.1f}'
    pg.evaluate(f"""document.getElementById('ov').innerHTML='<path d="{d1}"/><path d="{d2}" style="opacity:.75"/><path d="{u}" style="stroke:{RED};stroke-width:5"/>'""")
    bot=pg.evaluate("(()=>{const c=[...document.querySelectorAll('.n')];return Math.max(...c.map(e=>e.getBoundingClientRect().top))})()")
    print('letzte Zahl oben',round(bot))
    print('Fuss',pg.evaluate("document.querySelector('.foot').getBoundingClientRect().bottom"))
    pg.screenshot(path=D+'/Challenge-30-Tage-Start.png'); b.close()
from PIL import Image
Image.open(D+'/Challenge-30-Tage-Start.png').convert('RGB').save(D+'/Challenge-30-Tage-Start.jpg',quality=92)
