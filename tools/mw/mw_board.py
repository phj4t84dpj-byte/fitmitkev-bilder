# Mehrwert-Board 1080x1350 (Ausgabe 2160x2700) im warmen Board-Look: "So viel sind 100 kcal"
import os, sys, random
from PIL import Image
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D)
F=f"{S}/fonts/gf/ofl"; VN=f"{S}/g90/assets/vorher_nachher.jpg"
NAVY="#12213f"; BLUE="#163b7d"; DARK="#0d1d42"; RED="#c1202b"; GREEN="#2e7d32"; BADGE="#c61f27"
random.seed(11)
bok=''.join(f'<div class="b" style="left:{random.randint(-40,1060)}px;top:{random.randint(-40,1300)}px;width:{(s:=random.randint(30,110))}px;height:{s}px;opacity:{random.uniform(.15,.45):.2f};filter:blur({random.randint(2,9)}px)"></div>' for _ in range(40))
ROW1=[('erdbeeren','300 g','Erdbeeren'),('huettenkaese','100 g','Hüttenkäse'),('kartoffeln','140 g','Kartoffeln')]
ROW2=[('chips','18 g','Chips (ca. 10 Stück)'),('schokolade','18 g','Schokolade'),('gummibaerchen','30 g','Gummibärchen')]
def cards(row):
    return ''.join(f'<div class="c"><img src="{D}/raw/{k}.jpg"><div class="g">{g}</div><div class="nm">{n}</div></div>' for k,g,n in row)
def T(lines,size):
    L='<br>'.join(lines)
    return f'<div class="tw" style="font-size:{size}px"><div class="t-sh">{L}</div><div class="t-ol">{L}</div><div class="t-fi">{L}</div></div>'
H=f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:A;src:url('{F}/anton/Anton-Regular.ttf')}}
@font-face{{font-family:K;src:url('{F}/kaushanscript/KaushanScript-Regular.ttf')}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-Bold.ttf');font-weight:700}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-SemiBold.ttf');font-weight:600}}
body{{margin:0;width:1080px;height:1350px;overflow:hidden;position:relative;font-family:P;background:radial-gradient(ellipse at 70% 30%,#d9c3a5 0%,#c7ab89 45%,#b0926f 100%)}}
.b{{position:absolute;border-radius:50%;background:radial-gradient(circle,#fff3c9 0%,#ffd98a 55%,rgba(255,210,120,0) 72%)}}
.top{{position:absolute;left:0;top:26px;width:1080px;text-align:center}}
.hookw{{display:inline-block;position:relative;transform:rotate(-4deg)}}
.hook,.hookb{{font-family:K;font-size:58px;line-height:1.15;white-space:nowrap}}
.hook{{color:#fff;position:relative;z-index:2}}
.hookb{{position:absolute;left:0;top:0;color:{NAVY};-webkit-text-stroke:9px {NAVY};text-shadow:3px 4px 0 {NAVY};z-index:1}}
.tw{{position:relative;font-family:A;line-height:1.04;letter-spacing:1px;margin-top:2px}}
.t-fi{{position:relative;color:#fff;z-index:3}}
.t-ol{{position:absolute;left:0;top:0;width:100%;color:{BLUE};-webkit-text-stroke:11px {BLUE};z-index:2}}
.t-sh{{position:absolute;left:6px;top:7px;width:100%;color:{DARK};-webkit-text-stroke:11px {DARK};z-index:1}}
.lab{{position:absolute;left:40px;width:1000px;height:58px;border-radius:16px;color:#fff;font-family:A;font-size:38px;letter-spacing:1px;display:flex;align-items:center;justify-content:center}}
.row{{position:absolute;left:40px;width:1000px;display:flex;justify-content:space-between}}
.c{{width:318px;background:rgba(255,255,255,.94);border-radius:22px;padding:10px 10px 12px;box-sizing:border-box;text-align:center;box-shadow:0 8px 22px rgba(60,40,20,.22)}}
.c img{{width:298px;height:250px;object-fit:cover;border-radius:14px;display:block}}
.g{{font-family:A;font-size:40px;color:{RED};line-height:1.1;margin-top:8px}}
.nm{{font-size:25px;font-weight:600;color:{NAVY};line-height:1.15}}
.foot{{position:absolute;left:40px;top:1188px;width:1000px;height:136px;display:flex;align-items:center;gap:18px}}
.ph{{width:128px;height:132px;border-radius:14px;border:4px solid #fff;object-fit:cover;flex:none}}
.bd{{flex:none;display:flex;flex-direction:column;align-items:center;gap:6px}}
.badge{{background:{BADGE};color:#fff;font-family:A;font-size:40px;padding:0 20px 2px;border-radius:12px;line-height:1.15}}
.ig{{font-family:K;font-size:30px;color:{NAVY}}}
.msg{{flex:1;background:{NAVY};color:#fff;border-radius:22px;height:120px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:30px;font-weight:700;line-height:1.2;padding:0 20px}}
.msg span{{color:#ffd98a}}
</style></head><body>{bok}
<div class="top"><div class="hookw"><div class="hookb">Gleiche Kalorien:</div><div class="hook">Gleiche Kalorien:</div></div>
{T(['SO VIEL SIND 100 KCAL'],96)}</div>
<div class="lab" style="top:252px;background:{GREEN}">MACHT LANGE SATT</div>
<div class="row" style="top:324px">{cards(ROW1)}</div>
<div class="lab" style="top:712px;background:{RED}">IST IN EINER SEKUNDE WEG</div>
<div class="row" style="top:784px">{cards(ROW2)}</div>
<div class="foot"><img class="ph" src="{VN}"><div class="bd"><div class="badge">-50 kg</div><div class="ig">@fitmitkev</div></div>
<div class="msg"><div>Satt wirst du von <span>Menge</span>,<br>nicht von Verzicht.</div></div></div>
</body></html>"""
open(f'{D}/mw1.html','w').write(H)
out=sys.argv[1] if len(sys.argv)>1 else f'{D}/MW1-100kcal.jpg'
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    pg.goto('file://'+f'{D}/mw1.html'); pg.wait_for_timeout(500)
    print(pg.evaluate('''()=>{const r=[...document.querySelectorAll('.row')].map(e=>e.getBoundingClientRect().bottom);const f=document.querySelector('.foot').getBoundingClientRect().top;const t=document.querySelector('.top').getBoundingClientRect().bottom;return {titelUnten:t,reihe1Unten:r[0],reihe2Unten:r[1],fussOben:f};}'''))
    pg.screenshot(path=f'{D}/_b.png'); b.close()
Image.open(f'{D}/_b.png').convert('RGB').save(out,quality=92); os.remove(f'{D}/_b.png')
