# Mehrwert-Board 5 (1080x1350, Ausgabe 2160x2700) im warmen Board-Look: "Wie viel Eiweiß brauchst du am Tag?" (Eiweiß-Woche, ohne Marke)
# Oben: Tabelle Bedarf nach Körpergewicht (DGE-Referenzwerte: 0,8 g/kg für Erwachsene bis 64, 1,0 g/kg ab 65; DGE-Position Sport: 1,2–2,0 g/kg).
# Dazu Kevs Coaching-Tipp (14.11.): bei starkem Übergewicht Eiweißziel nach der Körpergröße, Beispiel 160 cm / 110 kg = ca. 140–160 g.
# Unten: Eiweiß je Portion (Werte aus der Nährwert-Tabelle der Rezepte; Eiweißpulver 22–24 g je 30 g).
import os, sys, random
from PIL import Image
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D)
F=f"{S}/fonts/gf/ofl"; VN=f"{S}/g90/assets/vorher_nachher.jpg"
NAVY="#12213f"; BLUE="#163b7d"; DARK="#0d1d42"; RED="#c1202b"; GREEN="#2e7d32"; BADGE="#c61f27"
random.seed(14)
bok=''.join(f'<div class="b" style="left:{random.randint(-40,1060)}px;top:{random.randint(-40,1300)}px;width:{(s:=random.randint(30,110))}px;height:{s}px;opacity:{random.uniform(.15,.45):.2f};filter:blur({random.randint(2,9)}px)"></div>' for _ in range(40))
KG=[60,70,80,90]
ROWS=[('bis 64 Jahre','0,8 g',0.8,NAVY),('ab 65 Jahren','1,0 g',1.0,BLUE),('mit regelmäßigem Sport','ab 1,2 g',1.2,GREEN)]
th=''.join(f'<th>{k} kg</th>' for k in KG)
tr=''.join(f'<tr><td class="rl"><b style="background:{c}">{f}</b>{t}</td>'+''.join(f'<td class="v">{round(k*x)} g</td>' for k in KG)+'</tr>' for t,f,x,c in ROWS)
table=f'<table><tr><th class="rl">pro kg Körpergewicht</th>{th}</tr>{tr}</table>'
FOOD=[('150 g Hähnchenbrust',35),('250 g Magerquark',30),('200 g Hüttenkäse',24),('30 g Eiweißpulver',23),('200 g Skyr',22),('2 Eier',15)]
mx=max(v for _,v in FOOD)
bars=''.join(f'<div class="fr"><div class="fn">{t}</div><div class="fb"><i style="width:{v/mx*100:.1f}%"></i></div><div class="fv">{v} g</div></div>' for t,v in FOOD)
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
.card{{position:absolute;left:40px;width:1000px;background:rgba(255,255,255,.94);border-radius:22px;box-shadow:0 8px 22px rgba(60,40,20,.22);box-sizing:border-box;padding:16px 30px 16px}}
table{{border-collapse:collapse;width:100%}}
th{{font-size:23px;font-weight:700;color:#6b6257;padding:2px 0 8px;text-align:center}}
th.rl{{text-align:left;font-weight:600}}
td{{border-top:2px solid #e3d9cb;padding:11px 0;font-size:25px;font-weight:600;color:{NAVY}}}
td.rl{{white-space:nowrap}}
td.rl b{{display:inline-block;min-width:112px;text-align:center;font-family:A;font-weight:400;font-size:28px;letter-spacing:1px;color:#fff;border-radius:10px;padding:1px 10px 3px;margin-right:14px}}
td.v{{text-align:center;font-weight:700;font-size:29px}}
.fr{{display:flex;align-items:center;margin:4px 0;font-size:25px;font-weight:600;color:{NAVY}}}
.fn{{width:330px;flex:none}}
.fb{{flex:1;height:26px;background:#efe7db;border-radius:8px;overflow:hidden}}
.fb i{{display:block;height:100%;background:{RED};border-radius:8px}}
.fv{{width:86px;flex:none;text-align:right;font-weight:700;font-size:28px}}
.tip{{position:absolute;left:40px;width:1000px;box-sizing:border-box;background:#fff6e0;border:3px solid #e9a23b;border-radius:22px;padding:14px 26px 16px;font-size:25px;font-weight:600;color:{NAVY};line-height:1.32;box-shadow:0 8px 22px rgba(60,40,20,.18)}}
.tip b{{font-weight:700;color:{RED}}}
.tip u{{text-decoration:none;font-weight:700;background:{GREEN};color:#fff;border-radius:8px;padding:0 10px 2px;white-space:nowrap}}
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
<div class="top"><div class="hookw"><div class="hookb">Einfach ausgerechnet:</div><div class="hook">Einfach ausgerechnet:</div></div>
{T(['WIE VIEL EIWEISS AM TAG?'],84)}</div>
<div class="lab" id="l1" style="top:226px;background:{NAVY}">SO VIEL BRAUCHST DU AM TAG</div>
<div class="card" id="c1" style="top:288px">{table}</div>
<div class="lab" id="l2" style="top:590px;background:{RED}">SO VIEL EIWEISS STECKT DRIN</div>
<div class="card" id="c2" style="top:652px">{bars}</div>
<div class="tip" id="tip" style="top:980px"><b>Mein Tipp bei starkem Übergewicht:</b> Rechne mit deiner Körpergröße statt mit dem Gewicht. Beispiel aus dem Coaching: 160 cm und 110 kg = etwa <u>140 bis 160 g</u> Eiweiß am Tag.</div>
<div class="mid" id="mid" style="top:1134px">Mit 20 bis 30 g pro Mahlzeit kommst du gut hin.</div>
<div class="foot"><img class="ph" src="{VN}"><div class="bd"><div class="badge">-50 kg</div><div class="ig">@fitmitkev</div></div>
<div class="msg"><div>Dein Gewicht mal 0,8:<br><span>Das ist dein Minimum am Tag.</span></div></div></div>
</body></html>"""
open(f'{D}/mw5.html','w').write(H)
out=sys.argv[1] if len(sys.argv)>1 else f'{D}/MW5-Eiweiss.jpg'
with sync_playwright() as pw:
    b_=pw.chromium.launch(); pg=b_.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    pg.goto('file://'+f'{D}/mw5.html'); pg.wait_for_timeout(500)
    print(pg.evaluate('''()=>{const g=id=>document.getElementById(id).getBoundingClientRect();const t=document.querySelector('.top').getBoundingClientRect();
      return {titelUnten:Math.round(t.bottom),l1:Math.round(g('l1').top),c1:[Math.round(g('c1').top),Math.round(g('c1').bottom)],l2:Math.round(g('l2').top),c2:[Math.round(g('c2').top),Math.round(g('c2').bottom)],tip:[Math.round(g('tip').top),Math.round(g('tip').bottom)],mid:[Math.round(g('mid').top),Math.round(g('mid').bottom)],fuss:Math.round(document.querySelector('.foot').getBoundingClientRect().top)};}'''))
    pg.screenshot(path=f'{D}/_b.png'); b_.close()
Image.open(f'{D}/_b.png').convert('RGB').save(out,quality=92); os.remove(f'{D}/_b.png')
