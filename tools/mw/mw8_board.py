# Mehrwert-Board 8 (Do 19.11. 17:30, ohne Marke/Werbung, Kev "Ja go" 18.11.): "Körniger Frischkäse – was steckt drin?" passend zum KF-Hooktest
# Herstellung Hüttenkäse: Magermilch dicklegen (Milchsäurebakterien/Lab) -> Bruch in Körner schneiden, erwärmen, waschen -> mit etwas Sahne und Salz anmachen.
# Je 100 g (Durchschnitt Handelsware): körniger Frischkäse 20 % F.i.Tr. ca. 98 kcal/12 g Eiweiß/4 g Fett; Magerquark 67/12; Skyr 63/11;
#   Frischkäse Doppelrahmstufe ca. 250 kcal/5 g Eiweiß.
import os, sys, random
from PIL import Image
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D)
F=f"{S}/fonts/gf/ofl"; VN=f"{S}/g90/assets/vorher_nachher.jpg"
NAVY="#12213f"; BLUE="#163b7d"; DARK="#0d1d42"; RED="#c1202b"; GREEN="#2e7d32"; BADGE="#c61f27"
random.seed(17)
bok=''.join(f'<div class="b" style="left:{random.randint(-40,1060)}px;top:{random.randint(-40,1300)}px;width:{(s:=random.randint(30,110))}px;height:{s}px;opacity:{random.uniform(.15,.45):.2f};filter:blur({random.randint(2,9)}px)"></div>' for _ in range(40))
STEPS=[('🥛','Milch','Magermilch wird dickgelegt'),('🔪','Schneiden','die Masse wird in kleine Körner geschnitten'),('💧','Waschen','die Körner werden erwärmt und gewaschen'),('🥄','Anmachen','mit etwas Sahne und Salz, fertig')]
def steps():
    out=''
    for i,(ic,t,d) in enumerate(STEPS):
        out+=f'<div class="stp"><div class="ic">{ic}</div><div class="stt">{t}</div><div class="std">{d}</div></div>'
        if i<len(STEPS)-1: out+='<div class="pf">➜</div>'
    return f'<div class="stps">{out}</div>'
VGL=[('Körniger Frischkäse',12,98,'#163b7d'),('Magerquark',12,67,'#7fb3e0'),('Skyr',11,63,'#e7959c'),('Frischkäse klassisch',5,250,'#f0c24b')]
def vgl():
    return ''.join(f'<div class="vr"><div class="vn">{n}</div><div class="vb"><i style="width:{max(p/12*92,34):.1f}%;background:{c}"></i><span>{p} g Eiweiß</span></div><div class="vk">{k} kcal</div></div>' for n,p,k,c in VGL)
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
.card{{position:absolute;left:40px;width:1000px;background:rgba(255,255,255,.94);border-radius:22px;box-shadow:0 8px 22px rgba(60,40,20,.22);box-sizing:border-box;padding:20px 24px 18px}}
.stps{{display:flex;align-items:flex-start;justify-content:space-between}}
.stp{{width:205px;text-align:center}}
.ic{{width:96px;height:96px;margin:0 auto;border-radius:50%;background:#f3ebdf;display:flex;align-items:center;justify-content:center;font-size:52px}}
.stt{{font-family:A;font-size:36px;color:{NAVY};letter-spacing:.5px;margin-top:8px}}
.std{{font-size:21px;font-weight:600;color:#5a4a3a;line-height:1.25;margin-top:2px}}
.pf{{font-size:40px;color:{GREEN};margin-top:26px}}
.whey{{margin-top:14px;border-top:2px solid #e3d9cb;padding-top:12px;text-align:center;font-size:27px;font-weight:700;color:{NAVY}}}
.whey span{{color:{GREEN}}}
.vr{{display:flex;align-items:center;gap:14px;margin:9px 0}}
.vn{{width:290px;font-size:26px;font-weight:700;color:{NAVY}}}
.vb{{flex:1;height:52px;border-radius:12px;background:#eee6da;position:relative;overflow:hidden}}
.vb i{{position:absolute;left:0;top:0;bottom:0;border-radius:12px}}
.vb span{{position:absolute;left:18px;top:0;line-height:52px;font-family:A;font-size:28px;color:#fff;letter-spacing:.5px;text-shadow:0 1px 3px rgba(0,0,0,.35)}}
.vk{{width:130px;text-align:right;font-size:26px;font-weight:700;color:#5a4a3a}}
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
<div class="top"><div class="hookw"><div class="hookb">Der Hype-Check:</div><div class="hook">Der Hype-Check:</div></div>
{T(['KÖRNIGER FRISCHKÄSE','WAS STECKT DRIN?'],80)}</div>
<div class="lab" id="l1" style="top:298px;background:{GREEN}">SO WIRD ER GEMACHT</div>
<div class="card" id="c1" style="top:360px">{steps()}
<div class="whey">Anderer Name im Kühlregal: <span>Hüttenkäse.</span></div></div>
<div class="lab" id="l2" style="top:728px;background:{BLUE}">JE 100 G IM VERGLEICH</div>
<div class="card" id="c2" style="top:790px">{vgl()}</div>
<div class="mid" id="mid" style="top:1110px">Püriert wird er cremig: perfekt für Soßen, Kuchen &amp; Pancakes.<br><span>Tipp: Er ist salziger als Quark, also beim Würzen sparen.</span></div>
<div class="foot"><img class="ph" src="{VN}"><div class="bd"><div class="badge">-50 kg</div><div class="ig">@fitmitkev</div></div>
<div class="msg"><div>Im Becher körnig, im Mixer cremig.<br><span>Darum ist er gerade überall.</span></div></div></div>
</body></html>"""
open(f'{D}/mw8.html','w').write(H)
out=sys.argv[1] if len(sys.argv)>1 else f'{D}/MW8-KoernigerFrischkaese.jpg'
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    pg.goto('file://'+f'{D}/mw8.html'); pg.wait_for_timeout(500)
    print(pg.evaluate('''()=>{const g=id=>document.getElementById(id).getBoundingClientRect();const t=document.querySelector('.top').getBoundingClientRect();
      return {titelUnten:Math.round(t.bottom),l1:Math.round(g('l1').top),c1:[Math.round(g('c1').top),Math.round(g('c1').bottom)],l2:Math.round(g('l2').top),c2:[Math.round(g('c2').top),Math.round(g('c2').bottom)],mid:[Math.round(g('mid').top),Math.round(g('mid').bottom)],fuss:Math.round(document.querySelector('.foot').getBoundingClientRect().top)};}'''))
    pg.screenshot(path=f'{D}/_b.png'); b.close()
Image.open(f'{D}/_b.png').convert('RGB').save(out,quality=92); os.remove(f'{D}/_b.png')
