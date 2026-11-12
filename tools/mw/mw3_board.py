# Mehrwert-Board 3 (1080x1350, Ausgabe 2160x2700) im warmen Board-Look: "Brot macht dick?"
# Zwei Abendbrote mit gleich viel Brot (2 Scheiben Vollkornbrot, 215 kcal) – der Unterschied liegt nur im Belag.
# Werte: Vollkornbrot 215 kcal/100 g, Butter 740/100 g (20 g = 150), Gouda 360/100 g (50 g = 180),
#        Frischkäse light 150/100 g (30 g = 45), Putenschinken 105/100 g (40 g = 40), Gurke + Tomate (100 g) = 15.
import os, sys, random
from PIL import Image
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D)
F=f"{S}/fonts/gf/ofl"; VN=f"{S}/g90/assets/vorher_nachher.jpg"
NAVY="#12213f"; BLUE="#163b7d"; DARK="#0d1d42"; RED="#c1202b"; GREEN="#2e7d32"; BADGE="#c61f27"
random.seed(12)
bok=''.join(f'<div class="b" style="left:{random.randint(-40,1060)}px;top:{random.randint(-40,1300)}px;width:{(s:=random.randint(30,110))}px;height:{s}px;opacity:{random.uniform(.15,.45):.2f};filter:blur({random.randint(2,9)}px)"></div>' for _ in range(40))
BROT=('2 Scheiben Vollkornbrot (100 g)',215,'#a8652c','#fff')
OHNE=[BROT,('20 g Butter',150,'#f0c24b',NAVY),('2 Scheiben Gouda (50 g)',180,'#e07b24','#fff')]
MIT =[BROT,('30 g Frischkäse light',45,'#7fb3e0',NAVY),('2 Scheiben Putenschinken (40 g)',40,'#e7959c',NAVY),('Gurke und Tomate',15,'#4f9d4f','#fff')]
K=940/545   # px pro kcal: die volle Breite entspricht dem schweren Abendbrot
def card(items):
    bar=''.join(f'<div class="seg" style="width:{v*K:.1f}px;background:{c};color:{tc}">{v if v*K>=70 else ""}</div>' for n,v,c,tc in items)
    rest=545-sum(v for n,v,c,tc in items)
    if rest>0: bar+=f'<div class="seg rest" style="width:{rest*K:.1f}px">{rest} kcal gespart</div>'
    rows=''.join(f'<div class="it"><span class="dot" style="background:{c}"></span><span class="nm">{n}</span><span class="kc">{v} kcal</span></div>' for n,v,c,tc in items)
    return f'<div class="bar">{bar}</div><div class="list">{rows}</div>'
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
.top{{position:absolute;left:0;top:22px;width:1080px;text-align:center}}
.hookw{{display:inline-block;position:relative;transform:rotate(-4deg)}}
.hook,.hookb{{font-family:K;font-size:56px;line-height:1.15;white-space:nowrap}}
.hook{{color:#fff;position:relative;z-index:2}}
.hookb{{position:absolute;left:0;top:0;color:{NAVY};-webkit-text-stroke:9px {NAVY};text-shadow:3px 4px 0 {NAVY};z-index:1}}
.tw{{position:relative;font-family:A;line-height:1.04;letter-spacing:1px;margin-top:12px}}
.t-fi{{position:relative;color:#fff;z-index:3}}
.t-ol{{position:absolute;left:0;top:0;width:100%;color:{BLUE};-webkit-text-stroke:11px {BLUE};z-index:2}}
.t-sh{{position:absolute;left:6px;top:7px;width:100%;color:{DARK};-webkit-text-stroke:11px {DARK};z-index:1}}
.lab{{position:absolute;left:40px;width:1000px;height:56px;border-radius:16px;color:#fff;font-family:A;font-size:36px;letter-spacing:1px;display:flex;align-items:center;justify-content:center}}
.card{{position:absolute;left:40px;width:1000px;background:rgba(255,255,255,.94);border-radius:22px;box-shadow:0 8px 22px rgba(60,40,20,.22);box-sizing:border-box;padding:18px 30px 16px}}
.bar{{display:flex;height:66px;border-radius:14px;overflow:hidden;width:940px;background:#eee6da}}
.seg{{height:66px;display:flex;align-items:center;justify-content:center;font-family:A;font-size:30px;letter-spacing:.5px;border-right:3px solid #fff;box-sizing:border-box}}
.seg:last-child{{border-right:none}}
.rest{{background:repeating-linear-gradient(135deg,#eef4ea 0 12px,#e2eedc 12px 24px);color:{GREEN};font-family:P;font-weight:700;font-size:26px;letter-spacing:0}}
.list{{margin-top:12px}}
.it{{display:flex;align-items:center;font-size:25px;font-weight:600;color:{NAVY};line-height:1.5}}
.dot{{width:22px;height:22px;border-radius:6px;margin-right:14px;flex:none}}
.nm{{flex:1}} .kc{{font-weight:700}}
.sum{{display:flex;align-items:center;justify-content:flex-end;gap:16px;margin-top:8px;border-top:2px solid #e3d9cb;padding-top:10px;font-size:26px;font-weight:700;color:{NAVY}}}
.sum b{{font-family:A;font-weight:400;font-size:40px;letter-spacing:1px;padding:2px 18px 4px;border-radius:12px;color:#fff}}
.mid{{position:absolute;left:40px;width:1000px;text-align:center;font-size:27px;font-weight:700;color:{NAVY};line-height:1.25}}
.mid span{{color:{RED}}}
.foot{{position:absolute;left:40px;top:1188px;width:1000px;height:136px;display:flex;align-items:center;gap:18px}}
.ph{{width:128px;height:132px;border-radius:14px;border:4px solid #fff;object-fit:cover;flex:none}}
.bd{{flex:none;display:flex;flex-direction:column;align-items:center;gap:6px}}
.badge{{background:{BADGE};color:#fff;font-family:A;font-size:40px;padding:0 20px 2px;border-radius:12px;line-height:1.15}}
.ig{{font-family:K;font-size:30px;color:{NAVY}}}
.msg{{flex:1;background:{NAVY};color:#fff;border-radius:22px;height:120px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:30px;font-weight:700;line-height:1.2;padding:0 20px}}
.msg span{{color:#ffd98a}}
</style></head><body>{bok}
<div class="top"><div class="hookw"><div class="hookb">Der Mythos:</div><div class="hook">Der Mythos:</div></div>
{T(['BROT MACHT DICK?'],92)}</div>
<div class="lab" id="l1" style="top:226px;background:{RED}">ABENDBROT MIT BUTTER & KÄSE</div>
<div class="card" id="c1" style="top:288px">{card(OHNE)}
<div class="sum">Gleiches Brot, schwerer Belag <b style="background:{RED}">= 545 KCAL</b></div></div>
<div class="lab" id="l2" style="top:640px;background:{GREEN}">ABENDBROT LEICHT BELEGT</div>
<div class="card" id="c2" style="top:702px">{card(MIT)}
<div class="sum">Gleiches Brot, leichter Belag <b style="background:{GREEN}">= 315 KCAL</b></div></div>
<div class="mid" id="mid" style="top:1102px">Das Brot ist in beiden gleich: 215 kcal.<br><span>Die 230 kcal Unterschied liegen nur im Belag.</span></div>
<div class="foot"><img class="ph" src="{VN}"><div class="bd"><div class="badge">-50 kg</div><div class="ig">@fitmitkev</div></div>
<div class="msg"><div>Brot ist nicht das Problem.<br><span>Der Belag entscheidet.</span></div></div></div>
</body></html>"""
open(f'{D}/mw3.html','w').write(H)
out=sys.argv[1] if len(sys.argv)>1 else f'{D}/MW3-Brot.jpg'
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    pg.goto('file://'+f'{D}/mw3.html'); pg.wait_for_timeout(500)
    print(pg.evaluate('''()=>{const g=id=>document.getElementById(id).getBoundingClientRect();const t=document.querySelector('.top').getBoundingClientRect();
      return {titelUnten:Math.round(t.bottom),l1:Math.round(g('l1').top),c1:[Math.round(g('c1').top),Math.round(g('c1').bottom)],l2:Math.round(g('l2').top),c2:[Math.round(g('c2').top),Math.round(g('c2').bottom)],mid:[Math.round(g('mid').top),Math.round(g('mid').bottom)],fuss:Math.round(document.querySelector('.foot').getBoundingClientRect().top)};}'''))
    pg.screenshot(path=f'{D}/_b.png'); b.close()
Image.open(f'{D}/_b.png').convert('RGB').save(out,quality=92); os.remove(f'{D}/_b.png')
