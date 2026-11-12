# Mehrwert-Board 2 (1080x1350, Ausgabe 2160x2700) im warmen Board-Look: "Was ein Wochenende kostet"
# Zwei Wochen-Diagramme (Kalorien über/unter dem Tagesbedarf): ohne Plan (+600 kcal) und mit Plan (-900 kcal).
import os, sys, random
from PIL import Image
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D)
F=f"{S}/fonts/gf/ofl"; VN=f"{S}/g90/assets/vorher_nachher.jpg"
NAVY="#12213f"; BLUE="#163b7d"; DARK="#0d1d42"; RED="#c1202b"; GREEN="#2e7d32"; BADGE="#c61f27"; ORANGE="#d9822b"
random.seed(11)
bok=''.join(f'<div class="b" style="left:{random.randint(-40,1060)}px;top:{random.randint(-40,1300)}px;width:{(s:=random.randint(30,110))}px;height:{s}px;opacity:{random.uniform(.15,.45):.2f};filter:blur({random.randint(2,9)}px)"></div>' for _ in range(40))
TAGE=['Mo','Di','Mi','Do','Fr','Sa','So']
OHNE=[(-300,''),(-300,''),(-300,''),(-300,''),(-300,''),(1200,'Pizza, Bier,<br>Chips'),(900,'Brunch,<br>Kuchen')]
MIT =[(-300,''),(-300,''),(-300,''),(-300,''),(-300,''),(300,'Pizza aus<br>Skyr-Teig'),(300,'Kuchen-<br>Bowl')]
K=0.075   # px pro kcal
def fmt(v): return ('+' if v>0 else '−')+f'{abs(v):,}'.replace(',','.')
def chart(week, up_col):
    cols=''
    for t,(v,note) in zip(TAGE,week):
        h=abs(v)*K; col=GREEN if v<0 else up_col
        bar=(f'<div class="bar" style="bottom:0;height:{h}px;background:{col}"></div><div class="val" style="bottom:{h+6}px;color:{col}">{fmt(v)}</div>' if v>0 else
             f'<div class="bar" style="top:0;height:{h}px;background:{col}"></div><div class="val" style="top:{h+6}px;color:{col}">{fmt(v)}</div>')
        half='up' if v>0 else 'dn'
        cols+=(f'<div class="col"><div class="up">{bar if half=="up" else ""}</div><div class="dn">{bar if half=="dn" else ""}</div>'
               f'<div class="day">{t}</div><div class="note">{note}</div></div>')
    return f'<div class="chart">{cols}<div class="base"></div></div>'
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
.card{{position:absolute;left:40px;width:1000px;background:rgba(255,255,255,.94);border-radius:22px;box-shadow:0 8px 22px rgba(60,40,20,.22);box-sizing:border-box;padding:14px 26px 14px}}
.cap{{font-size:19px;font-weight:600;color:#6b6257;text-align:center}}
.chart{{position:relative;display:flex;justify-content:space-between;margin-top:4px}}
.col{{width:124px;text-align:center}}
.up{{position:relative;height:{int(1200*K)+44}px}}
.dn{{position:relative;height:{int(300*K)+44}px}}
.bar{{position:absolute;left:22px;width:80px;border-radius:8px}}
.up .bar{{border-radius:8px 8px 3px 3px}} .dn .bar{{border-radius:3px 3px 8px 8px}}
.val{{position:absolute;left:0;width:124px;font-family:A;font-size:30px;line-height:1}}
.day{{font-size:26px;font-weight:700;color:{NAVY};line-height:1.1;margin-top:2px}}
.note{{font-size:17px;font-weight:600;color:#6b6257;line-height:1.15;height:40px}}
.base{{position:absolute;left:0;right:0;top:{int(1200*K)+44}px;height:3px;background:{NAVY};opacity:.55}}
.sum{{display:flex;align-items:center;justify-content:center;gap:16px;margin-top:8px;font-size:27px;font-weight:700;color:{NAVY}}}
.sum b{{font-family:A;font-weight:400;font-size:40px;letter-spacing:1px;padding:2px 18px 4px;border-radius:12px;color:#fff}}
.foot{{position:absolute;left:40px;top:1188px;width:1000px;height:136px;display:flex;align-items:center;gap:18px}}
.ph{{width:128px;height:132px;border-radius:14px;border:4px solid #fff;object-fit:cover;flex:none}}
.bd{{flex:none;display:flex;flex-direction:column;align-items:center;gap:6px}}
.badge{{background:{BADGE};color:#fff;font-family:A;font-size:40px;padding:0 20px 2px;border-radius:12px;line-height:1.15}}
.ig{{font-family:K;font-size:30px;color:{NAVY}}}
.msg{{flex:1;background:{NAVY};color:#fff;border-radius:22px;height:120px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:30px;font-weight:700;line-height:1.2;padding:0 20px}}
.msg span{{color:#ffd98a}}
</style></head><body>{bok}
<div class="top"><div class="hookw"><div class="hookb">Die Wochen-Rechnung:</div><div class="hook">Die Wochen-Rechnung:</div></div>
{T(['WAS EIN WOCHENENDE KOSTET'],78)}</div>
<div class="lab" id="l1" style="top:212px;background:{RED}">SO LÄUFT ES BEI DEN MEISTEN</div>
<div class="card" id="c1" style="top:274px"><div class="cap">Kalorien über bzw. unter deinem Tagesbedarf</div>{chart(OHNE,RED)}
<div class="sum">Woche: −1.500 &nbsp;·&nbsp; Wochenende: +2.100 <b style="background:{RED}">= +600 KCAL</b></div></div>
<div class="lab" id="l2" style="top:700px;background:{GREEN}">SO LÄUFT ES MIT PLAN</div>
<div class="card" id="c2" style="top:762px"><div class="cap">Pizza und Kuchen gibt es trotzdem, nur leichter gemacht</div>{chart(MIT,ORANGE)}
<div class="sum">Woche: −1.500 &nbsp;·&nbsp; Wochenende: +600 <b style="background:{GREEN}">= −900 KCAL</b></div></div>
<div class="foot"><img class="ph" src="{VN}"><div class="bd"><div class="badge">-50 kg</div><div class="ig">@fitmitkev</div></div>
<div class="msg"><div>Das Wochenende ist nicht verboten.<br><span>Es braucht nur einen Plan.</span></div></div></div>
</body></html>"""
open(f'{D}/mw2.html','w').write(H)
out=sys.argv[1] if len(sys.argv)>1 else f'{D}/MW2-Wochenende.jpg'
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    pg.goto('file://'+f'{D}/mw2.html'); pg.wait_for_timeout(500)
    print(pg.evaluate('''()=>{const g=id=>document.getElementById(id).getBoundingClientRect();const t=document.querySelector('.top').getBoundingClientRect();const tw=document.querySelector('.tw .t-fi');
      return {titelUnten:Math.round(t.bottom),titelBreite:Math.round(tw.scrollWidth),l1:Math.round(g('l1').top),c1:[Math.round(g('c1').top),Math.round(g('c1').bottom)],l2:Math.round(g('l2').top),c2:[Math.round(g('c2').top),Math.round(g('c2').bottom)],fuss:Math.round(document.querySelector('.foot').getBoundingClientRect().top)};}'''))
    pg.screenshot(path=f'{D}/_b.png'); b.close()
Image.open(f'{D}/_b.png').convert('RGB').save(out,quality=92); os.remove(f'{D}/_b.png')
