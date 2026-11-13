# Mehrwert-Board 4 (1080x1350, Ausgabe 2160x2700) im warmen Board-Look: "Die Waage schwankt – normal!"
# Oben: 14 Tage auf der Waage (Tageswerte springen, Trend fällt). Unten: vier Gründe, die nur Wasser/Inhalt sind.
# Zahlen: Tagesschwankungen von 1–2 kg sind üblich; 1 kg Körperfett entspricht rund 7.000 kcal.
import os, sys, random
from PIL import Image
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D)
F=f"{S}/fonts/gf/ofl"; VN=f"{S}/g90/assets/vorher_nachher.jpg"
NAVY="#12213f"; BLUE="#163b7d"; DARK="#0d1d42"; RED="#c1202b"; GREEN="#2e7d32"; BADGE="#c61f27"
random.seed(14)
bok=''.join(f'<div class="b" style="left:{random.randint(-40,1060)}px;top:{random.randint(-40,1300)}px;width:{(s:=random.randint(30,110))}px;height:{s}px;opacity:{random.uniform(.15,.45):.2f};filter:blur({random.randint(2,9)}px)"></div>' for _ in range(40))
W=[82.4,82.9,82.1,82.0,83.0,82.3,81.9,82.6,81.8,81.6,82.5,81.7,81.4,81.3]
CW,CH=940,250; PL,PR,PT,PB=70,24,26,40; lo,hi=81.0,83.4
X=lambda i: PL+i*(CW-PL-PR)/(len(W)-1); Y=lambda v: PT+(hi-v)/(hi-lo)*(CH-PT-PB)
n=len(W); mx=(n-1)/2; my=sum(W)/n
b=sum((i-mx)*(w-my) for i,w in enumerate(W))/sum((i-mx)**2 for i in range(n)); a=my-b*mx
t0,t1=a,a+b*(n-1)
grid=''.join(f'<line x1="{PL}" x2="{CW-PR}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="#e3d9cb" stroke-width="2"/><text x="{PL-12}" y="{Y(v)+7:.1f}" text-anchor="end" class="ax">{str(v).replace(".",",")}</text>' for v in (81.0,82.0,83.0))
pts=' '.join(f'{X(i):.1f},{Y(w):.1f}' for i,w in enumerate(W))
dots=''.join(f'<circle cx="{X(i):.1f}" cy="{Y(w):.1f}" r="{9 if i in (4,10) else 7}" fill="{RED if i in (4,10) else NAVY}" stroke="#fff" stroke-width="3"/>' for i,w in enumerate(W))
days=''.join(f'<text x="{X(i):.1f}" y="{CH-8}" text-anchor="middle" class="ax">{i+1}</text>' for i in range(n))
svg=f'''<svg width="{CW}" height="{CH}" viewBox="0 0 {CW} {CH}">{grid}
<line x1="{X(0):.1f}" y1="{Y(t0):.1f}" x2="{X(n-1):.1f}" y2="{Y(t1):.1f}" stroke="{GREEN}" stroke-width="7" stroke-dasharray="16 10" stroke-linecap="round"/>
<polyline points="{pts}" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linejoin="round"/>{dots}{days}
<text x="{X(4)+16:.1f}" y="{Y(83.0)-10:.1f}" class="an" fill="{RED}">+1 kg nach dem Pizza-Abend</text>
<text x="{X(10)+2:.1f}" y="{Y(82.5)-18:.1f}" class="an" fill="{RED}" text-anchor="middle">+0,9 kg</text>
</svg>'''
G=[('#7fb3e0','Salz','bindet Wasser, vor allem nach salzigem Essen am Abend'),
   ('#e07b24','Kohlenhydrate','jedes gespeicherte Gramm hält rund 3 g Wasser fest'),
   ('#a8652c','Magen und Darm','Essen und Trinken wiegen selbst 1 bis 2 kg'),
   ('#c1202b','Hormone und Muskelkater','der Körper lagert Wasser ein')]
rows=''.join(f'<div class="it"><span class="dot" style="background:{c}"></span><div><b>{t}:</b> {x}</div></div>' for c,t,x in G)
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
.ax{{font-family:P;font-weight:600;font-size:19px;fill:#6b6257}}
.an{{font-family:P;font-weight:700;font-size:22px}}
.leg{{display:flex;justify-content:space-between;align-items:center;font-size:21px;font-weight:600;color:#6b6257;margin-top:2px}}
.leg i{{display:inline-block;width:46px;height:0;border-top:6px dashed {GREEN};vertical-align:middle;margin-right:10px}}
.leg u{{display:inline-block;width:46px;height:5px;background:{NAVY};vertical-align:middle;margin-right:10px;text-decoration:none}}
.sum{{display:flex;align-items:center;justify-content:flex-end;gap:16px;margin-top:8px;border-top:2px solid #e3d9cb;padding-top:10px;font-size:26px;font-weight:700;color:{NAVY}}}
.sum b{{font-family:A;font-weight:400;font-size:40px;letter-spacing:1px;padding:2px 18px 4px;border-radius:12px;color:#fff}}
.it{{display:flex;align-items:flex-start;font-size:25px;font-weight:600;color:{NAVY};line-height:1.3;margin:17px 0}}
.it b{{font-weight:700}}
.dot{{width:22px;height:22px;border-radius:6px;margin:6px 14px 0 0;flex:none}}
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
<div class="top"><div class="hookw"><div class="hookb">Kein Grund zur Panik:</div><div class="hook">Kein Grund zur Panik:</div></div>
{T(['DIE WAAGE SCHWANKT'],92)}</div>
<div class="lab" id="l1" style="top:226px;background:{NAVY}">14 TAGE AUF DER WAAGE (IN KG)</div>
<div class="card" id="c1" style="top:288px">{svg}
<div class="leg"><span><u></u>jeden Morgen gewogen</span><span><i></i>der Trend</span></div>
<div class="sum">Einzelne Tage springen, der Trend fällt <b style="background:{GREEN}">−1,1 KG</b></div></div>
<div class="lab" id="l2" style="top:716px;background:{RED}">DAS STECKT HINTER DEN SPRÜNGEN</div>
<div class="card" id="c2" style="top:778px">{rows}</div>
<div class="mid" id="mid" style="top:1072px">1 kg Körperfett sind rund 7.000 kcal.<br><span>Über Nacht kommt das nicht dazu.</span></div>
<div class="foot"><img class="ph" src="{VN}"><div class="bd"><div class="badge">-50 kg</div><div class="ig">@fitmitkev</div></div>
<div class="msg"><div>Schau auf den Wochenschnitt,<br><span>nicht auf den einzelnen Tag.</span></div></div></div>
</body></html>"""
open(f'{D}/mw4.html','w').write(H)
out=sys.argv[1] if len(sys.argv)>1 else f'{D}/MW4-Waage.jpg'
with sync_playwright() as pw:
    b_=pw.chromium.launch(); pg=b_.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    pg.goto('file://'+f'{D}/mw4.html'); pg.wait_for_timeout(500)
    print('Trend',round(t0,2),'->',round(t1,2),'=',round(t1-t0,2))
    print(pg.evaluate('''()=>{const g=id=>document.getElementById(id).getBoundingClientRect();const t=document.querySelector('.top').getBoundingClientRect();
      return {titelUnten:Math.round(t.bottom),l1:Math.round(g('l1').top),c1:[Math.round(g('c1').top),Math.round(g('c1').bottom)],l2:Math.round(g('l2').top),c2:[Math.round(g('c2').top),Math.round(g('c2').bottom)],mid:[Math.round(g('mid').top),Math.round(g('mid').bottom)],fuss:Math.round(document.querySelector('.foot').getBoundingClientRect().top)};}'''))
    pg.screenshot(path=f'{D}/_b.png'); b_.close()
Image.open(f'{D}/_b.png').convert('RGB').save(out,quality=92); os.remove(f'{D}/_b.png')
