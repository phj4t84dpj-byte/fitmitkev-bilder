# 17:30-Beitrag GTA-6-Tag (Do 19.11.2026): „GTA-Abend: Lieferdienst gegen selbst gemacht“ im Gamer-Look, ohne Marke/Werbung.
# Zahlen = die Vergleichswerte und Nährwerte der vier Rezepte vom selben Tag (gta_data.py): Cheeseburger 650 → 360/34 g · Nachos 700 → 420/34 g ·
#   Milchshake 450 → 215/23 g · Donut 300 → 160/8 g. Summen: 2.100 kcal gegen 1.155 kcal und 99 g Eiweiß.
import os, sys
from PIL import Image
from playwright.sync_api import sync_playwright
import gta_data as G
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D)
F=f"{S}/fonts/gf/ofl"; VN=f"{D}/assets/vorher_nachher.jpg"
PINK="#ff2e9a"; CYAN="#19e3ff"; GREEN="#62ff7e"; BG="13,8,32"
by={r['key']:r for r in G.R}
ROWS=[('🍔','Cheeseburger','Cheeseburger'),('🧀','Nachos','OfenNachos'),('🥤','Milchshake','ErdbeerShake'),('🍩','Donut','Donuts')]
L=[];Rr=[];sl=sr=sp=0
for ic,nm,key in ROWS:
    k,p,c,f=G.macros4(by[key]); v=by[key]['vs']; sl+=v; sr+=k; sp+=p
    L.append((ic,nm,v)); Rr.append((ic,nm,k,p))
assert (sl,sr,sp)==(2100,1155,99),(sl,sr,sp)
fm=lambda n:f"{n:,}".replace(',','.')
def rows(items,right):
    o=''
    for it in items:
        sub=f'<div class="rp">{it[3]} g Eiweiß</div>' if right else ''
        o+=f'<div class="r"><div class="ic">{it[0]}</div><div class="rn">{it[1]}{sub}</div><div class="rk">{it[2]} kcal</div></div>'
    return o
def T(lines,size):
    Ls='<br>'.join(lines)
    return f'<div class="tw" style="font-size:{size}px"><div class="t-sh">{Ls}</div><div class="t-ol">{Ls}</div><div class="t-fi">{Ls}</div></div>'
H=f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:A;src:url('{F}/anton/Anton-Regular.ttf')}}
@font-face{{font-family:K;src:url('{F}/kaushanscript/KaushanScript-Regular.ttf')}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-Bold.ttf');font-weight:700}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-SemiBold.ttf');font-weight:600}}
*{{box-sizing:border-box}}
body{{margin:0;width:1080px;height:1350px;overflow:hidden;position:relative;font-family:P;
  background:radial-gradient(circle at 12% 30%,rgba(255,46,154,.30) 0,rgba(255,46,154,0) 34%),radial-gradient(circle at 92% 62%,rgba(25,227,255,.26) 0,rgba(25,227,255,0) 36%),
  radial-gradient(circle at 55% 100%,rgba(123,47,247,.35) 0,rgba(123,47,247,0) 45%),rgb({BG})}}
.top{{position:absolute;left:0;top:34px;width:1080px;text-align:center}}
.hook{{display:inline-block;transform:rotate(-3deg);font-family:K;font-size:58px;line-height:1.15;color:#fff;text-shadow:0 0 6px #fff,0 0 14px {PINK},0 0 30px {PINK},0 0 54px {PINK}}}
.tw{{position:relative;font-family:A;line-height:1.06;letter-spacing:1px;margin-top:10px;filter:drop-shadow(0 0 18px rgba(255,46,154,.45))}}
.t-fi{{position:relative;color:#fff;z-index:3}}
.t-ol{{position:absolute;left:0;top:0;width:100%;color:{PINK};-webkit-text-stroke:11px {PINK};z-index:2}}
.t-sh{{position:absolute;left:7px;top:8px;width:100%;color:{CYAN};-webkit-text-stroke:11px {CYAN};z-index:1}}
.card{{position:absolute;top:340px;width:490px;height:640px;border-radius:26px;background:rgba(255,255,255,.07);border:4px solid;padding:0 22px}}
.c1{{left:40px;border-color:{PINK};box-shadow:0 0 26px rgba(255,46,154,.55)}}
.c2{{left:550px;border-color:{GREEN};box-shadow:0 0 26px rgba(98,255,126,.5)}}
.ch{{margin:0 -22px;height:92px;border-radius:20px 20px 0 0;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:A;letter-spacing:1px;color:#fff;line-height:1.1}}
.c1 .ch{{background:{PINK}}} .c2 .ch{{background:#1faa4b}}
.ch small{{font-family:P;font-weight:700;font-size:20px;letter-spacing:.5px;opacity:.95}}
.ch b{{font-weight:400;font-size:40px}}
.r{{display:flex;align-items:center;gap:14px;height:90px;border-bottom:2px solid rgba(255,255,255,.14)}}
.ic{{width:64px;height:64px;flex:none;border-radius:50%;background:rgba(255,255,255,.12);display:flex;align-items:center;justify-content:center;font-size:36px}}
.rn{{flex:1;font-size:27px;font-weight:700;color:#fff;line-height:1.15}}
.rp{{font-size:19px;font-weight:600;color:{GREEN}}}
.rk{{font-family:A;font-size:32px;color:#fff;letter-spacing:.5px;white-space:nowrap}}
.sum{{text-align:center;margin-top:16px}}
.sum .a{{font-size:21px;font-weight:700;color:#d8d2ff;letter-spacing:1px}}
.sum .b{{font-family:A;font-size:76px;line-height:1.05;letter-spacing:1px}}
.c1 .sum .b{{color:#ff7fb0}} .c2 .sum .b{{color:{GREEN}}}
.sum .c{{font-size:23px;font-weight:700;color:#fff;margin-top:2px}}
.vs{{position:absolute;left:490px;top:336px;width:100px;height:100px;border-radius:50%;background:rgb({BG});border:4px solid {CYAN};box-shadow:0 0 22px rgba(25,227,255,.8);
  display:flex;align-items:center;justify-content:center;font-family:A;font-size:44px;color:#fff;z-index:5}}
.mid{{position:absolute;left:40px;top:1006px;width:1000px;text-align:center;font-size:31px;font-weight:700;color:#fff;line-height:1.25}}
.mid span{{color:{GREEN}}}
.foot{{position:absolute;left:40px;top:1116px;width:1000px;height:190px;display:flex;align-items:center;gap:18px}}
.ph{{width:150px;height:154px;border-radius:16px;border:4px solid #fff;object-fit:cover;flex:none;box-shadow:0 0 0 3px {CYAN},0 0 22px rgba(25,227,255,.7)}}
.bd{{flex:none;display:flex;flex-direction:column;align-items:center;gap:6px}}
.badge{{background:#c61f27;color:#fff;font-family:A;font-size:40px;padding:0 20px 2px;border-radius:12px;line-height:1.15}}
.ig{{font-family:K;font-size:30px;color:#fff}}
.msg{{flex:1;background:rgba(255,255,255,.08);border:3px solid {CYAN};color:#fff;border-radius:22px;height:130px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:28px;font-weight:700;line-height:1.25;padding:0 18px;box-shadow:0 0 16px rgba(25,227,255,.5)}}
.msg span{{color:{GREEN}}}
.frame{{position:absolute;left:12px;top:12px;width:1056px;height:1326px;border-radius:30px;border:5px solid transparent;
  background:linear-gradient(135deg,{CYAN},{PINK} 50%,{CYAN}) border-box;-webkit-mask:linear-gradient(#000 0 0) padding-box,linear-gradient(#000 0 0);
  -webkit-mask-composite:xor;mask-composite:exclude;filter:drop-shadow(0 0 10px rgba(255,46,154,.8))}}
</style></head><body>
<div class="top"><div class="hook">Der GTA-6-Abend:</div>{T(['LIEFERDIENST GEGEN','SELBST GEMACHT'],84)}</div>
<div class="card c1"><div class="ch"><small>🎮 SPIELER 1</small><b>BESTELLT</b></div>{rows(L,False)}
<div class="sum"><div class="a">ZUSAMMEN</div><div class="b">{fm(sl)} kcal</div></div></div>
<div class="vs">VS</div>
<div class="card c2"><div class="ch"><small>🎮 SPIELER 2</small><b>SELBST GEMACHT</b></div>{rows(Rr,True)}
<div class="sum"><div class="a">ZUSAMMEN</div><div class="b">{fm(sr)} kcal</div><div class="c">und {sp} g Eiweiß</div></div></div>
<div class="mid">Gleiches Essen, gleicher Spaß.<br><span>Aber {fm(sl-sr)} kcal weniger.</span></div>
<div class="foot"><img class="ph" src="{VN}"><div class="bd"><div class="badge">-50 kg</div><div class="ig">@fitmitkev</div></div>
<div class="msg"><div>Alle 4 Rezepte findest du<br><span>heute auf meiner Seite.</span></div></div></div>
<div class="frame"></div>
</body></html>"""
open(f'{D}/out/mwgta.html','w').write(H)
out=f'{D}/out/GTA-Abend-Vergleich.jpg'
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    pg.goto('file://'+f'{D}/out/mwgta.html'); pg.wait_for_timeout(500)
    print(pg.evaluate('''()=>{const g=s=>{const r=document.querySelector(s).getBoundingClientRect();return [Math.round(r.top),Math.round(r.bottom)]};
      return {top:g('.top'),c1:g('.c1'),sum1:g('.c1 .sum'),sum2:g('.c2 .sum'),mid:g('.mid'),foot:g('.foot')}}'''))
    pg.screenshot(path=f'{D}/out/_b.png'); b.close()
Image.open(f'{D}/out/_b.png').convert('RGB').save(out,quality=92); os.remove(f'{D}/out/_b.png'); print(out)
