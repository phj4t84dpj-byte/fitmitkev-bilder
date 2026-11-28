# Mehrwert-Board 9 (So 29.11.2026, 17:45): „Plätzchen-Check“ – 10 Weihnachtsplätzchen, ca. kcal pro Stück (je nach Größe).
# Freigestellte Fotos (Higgsfield, rembg) liegen im Arbeitsbereich: env CUT = Ordner mit cut_<key>.png
import os, sys, random
from PIL import Image
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D)
F=f"{S}/fonts/gf/ofl"; VN=f"{S}/g90/assets/vorher_nachher.jpg"; CUT=os.environ['CUT']
NAVY="#12213f"; BLUE="#163b7d"; DARK="#0d1d42"; RED="#c1202b"; GREEN="#2e7d32"; ORANGE="#d9711c"; BADGE="#c61f27"
random.seed(9)
bok=''.join(f'<div class="b" style="left:{random.randint(-40,1060)}px;top:{random.randint(-40,1300)}px;width:{(s:=random.randint(30,110))}px;height:{s}px;opacity:{random.uniform(.15,.45):.2f};filter:blur({random.randint(2,9)}px)"></div>' for _ in range(26))
P=[('vanillekipferl','Vanillekipferl',40),('spekulatius','Spekulatius',40),('butterplaetzchen','Butterplätzchen',40),('zimtsterne','Zimtstern',45),('dominosteine','Dominostein',45),
   ('spritzgebaeck','Spritzgebäck',50),('kokosmakronen','Kokosmakrone',55),('florentiner','Florentiner',80),('spitzbuben','Spitzbube',85),('lebkuchen','Elisenlebkuchen',140)]
def col(k): return GREEN if k<=45 else (ORANGE if k<=85 else RED)
def card(c):
    key,nm,k=c
    return f'<div class="c"><div class="im"><img src="{CUT}/cut_{key}.png"></div><div class="k" style="background:{col(k)}">ca. {k} kcal</div><div class="nm">{nm}</div></div>'
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
.sub{{font-size:27px;font-weight:700;color:{NAVY};margin-top:10px;text-shadow:0 0 10px rgba(255,255,255,.8)}}
.row{{position:absolute;left:40px;width:1000px;display:flex;justify-content:space-between}}
.c{{width:188px;background:rgba(255,255,255,.95);border-radius:20px;padding:10px 8px 12px;box-sizing:border-box;text-align:center;box-shadow:0 8px 22px rgba(60,40,20,.22)}}
.im{{height:225px;display:flex;align-items:center;justify-content:center}}
.im img{{max-width:168px;max-height:220px;object-fit:contain;filter:drop-shadow(0 6px 6px rgba(60,40,20,.25))}}
.k{{display:inline-block;margin-top:8px;color:#fff;font-family:A;font-size:29px;letter-spacing:.5px;line-height:1.25;padding:0 10px;border-radius:12px;white-space:nowrap}}
.nm{{font-size:19px;font-weight:700;color:{NAVY};line-height:1.15;margin-top:6px;white-space:nowrap}}
.note{{position:absolute;left:40px;top:1048px;width:1000px;text-align:center;font-size:29px;font-weight:700;color:{NAVY};line-height:1.3}}
.note span{{color:{RED}}}
.foot{{position:absolute;left:40px;top:1188px;width:1000px;height:136px;display:flex;align-items:center;gap:18px}}
.ph{{width:128px;height:132px;border-radius:14px;border:4px solid #fff;object-fit:cover;flex:none}}
.bd{{flex:none;display:flex;flex-direction:column;align-items:center;gap:6px}}
.badge{{background:{BADGE};color:#fff;font-family:A;font-size:40px;padding:0 20px 2px;border-radius:12px;line-height:1.15}}
.ig{{font-family:K;font-size:30px;color:{NAVY}}}
.msg{{flex:1;background:{NAVY};color:#fff;border-radius:22px;height:120px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:29px;font-weight:700;line-height:1.2;padding:0 20px}}
.msg span{{color:#ffd98a}}
</style></head><body>{bok}
<div class="top"><div class="hookw"><div class="hookb">Der Plätzchen-Check:</div><div class="hook">Der Plätzchen-Check:</div></div>
{T(['SO VIEL HAT 1 PLÄTZCHEN'],92)}<div class="sub">ca. kcal pro Stück, je nach Größe</div></div>
<div class="row" style="top:282px">{''.join(card(c) for c in P[:5])}</div>
<div class="row" style="top:660px">{''.join(card(c) for c in P[5:])}</div>
<div class="note">Ein <span>Elisenlebkuchen</span> hat mehr als <span>3 Vanillekipferl</span> zusammen.</div>
<div class="foot"><img class="ph" src="{VN}"><div class="bd"><div class="badge">-50 kg</div><div class="ig">@fitmitkev</div></div>
<div class="msg"><div>Leg dir deine <span>3 Lieblinge</span> auf einen Teller,<br>statt aus der Dose zu naschen.</div></div></div>
</body></html>"""
open(f'{D}/mw9.html','w').write(H)
out=sys.argv[1]
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    pg.goto('file://'+f'{D}/mw9.html'); pg.wait_for_timeout(600)
    print(pg.evaluate('''()=>{const r=[...document.querySelectorAll('.row')].map(e=>e.getBoundingClientRect());const t=document.querySelector('.top').getBoundingClientRect().bottom;const n=document.querySelector('.note').getBoundingClientRect();return {titelUnten:t,r1:[r[0].top,r[0].bottom],r2:[r[1].top,r[1].bottom],note:[n.top,n.bottom],nmBreit:Math.max(...[...document.querySelectorAll('.nm')].map(e=>e.scrollWidth))};}'''))
    pg.screenshot(path=f'{D}/_b.png'); b.close()
Image.open(f'{D}/_b.png').convert('RGB').save(out,quality=92); os.remove(f'{D}/_b.png')
print('ok',out)
