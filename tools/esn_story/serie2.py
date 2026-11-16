# -*- coding: utf-8 -*-
# ESN Black Week – Story-Serie 2 (hell, Shop-Look): Proteine, Riegel, Kreatin, Collagen, Vorrat
import asyncio, os
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__)); P=D+'/s2/'; IMG=D+'/img/'
F='/mnt/skills/examples/canvas-design/canvas-fonts/'; I='/usr/share/fonts/opentype/inter/'
C={50:'#f2231b',40:'#ff7a00',30:'#ffcc00',25:'#19c3a3'}
def u(n): return 'file://'+(IMG+n if n.startswith('extra') else P+n)
CSS=f'''@font-face{{font-family:ID;src:url(file://{I}InterDisplay-Black.otf)}}
@font-face{{font-family:IN;src:url(file://{I}Inter-Regular.otf);font-weight:400}}
@font-face{{font-family:IN;src:url(file://{I}Inter-SemiBold.otf);font-weight:600}}
@font-face{{font-family:IN;src:url(file://{I}Inter-Bold.otf);font-weight:700}}
@font-face{{font-family:MO;src:url(file://{F}IBMPlexMono-Regular.ttf);font-weight:400}}
@font-face{{font-family:MO;src:url(file://{F}IBMPlexMono-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:#edf1f2;color:#111;font-family:IN;overflow:hidden}}
.w{{position:absolute;left:64px;right:64px;top:168px}}
.top{{display:flex;justify-content:space-between;font-size:23px;font-weight:600;letter-spacing:3px;color:#6b7378;text-transform:uppercase}}
.kick{{margin-top:30px;font-size:28px;font-weight:700;letter-spacing:4px;text-transform:uppercase}}
.h{{font-family:ID;line-height:.92;letter-spacing:-3px;margin-top:10px}}
.bd{{display:inline-block;font-family:ID;color:#111;padding:6px 12px 4px;letter-spacing:-1px}}
.st{{color:#7d868b;text-decoration:line-through}}
.code{{position:absolute;left:250px;right:250px;top:1625px;background:#111;color:#fff;text-align:center;padding:12px 0 10px;border-radius:4px}}
.code small{{display:block;font-size:20px;font-weight:600;letter-spacing:5px;color:#a9b0b4}}
.code div{{font-family:ID;font-size:64px;line-height:1.05;letter-spacing:2px}}
.hr{{height:3px;background:#111;margin-top:26px}}
'''
TOP='<div class="top"><span>Werbung</span><span>@esncom · Black Week</span></div>'
CODE='<div class="code"><small>CODE</small><div>FITMITKEV</div></div>'
def bd(d,fs=34): return f'<span class="bd" style="background:{C[d]};font-size:{fs}px">-{d}%</span>'
S={}
# 1 Protein-Guide
PR=[('extra-creamy-480g-vanilla-speculoos.png',30,'Designer Protein Extra Creamy','480 g','Für Rezepte: Quark, Skyr, Pudding, Overnight Oats','19,53','27,90'),
    ('whey.png',25,'Designer Whey','908 g','Für den klassischen Shake mit Milch oder Wasser','37,43','49,90'),
    ('isoclear.png',25,'Isoclear','908 g','Erfrischend wie Saft, einfach mit Wasser','44,18','58,90')]
rows=''.join(f'''<div class="pr"><div class="pi"><img src="{u(n)}"></div><div class="pt"><div class="pn">{t} <span>{g}</span></div><div class="pu">{f}</div>
<div class="pp">{bd(d,30)}<b>{p} €</b><span class="st">{a} €</span></div></div></div>''' for n,d,t,g,f,p,a in PR)
S['6-Protein-Guide']=f'''<style>.h{{font-size:122px}}
.pr{{display:flex;gap:30px;align-items:center;border-bottom:2px solid #c9d0d3;padding:22px 0}}
.pi{{width:230px;height:250px;display:flex;align-items:center;justify-content:center}} .pi img{{max-width:220px;max-height:245px}}
.pn{{font-size:33px;font-weight:700;line-height:1.15}} .pn span{{font-weight:400;color:#6b7378}}
.pu{{font-size:27px;line-height:1.35;margin-top:8px;color:#333}}
.pp{{display:flex;align-items:center;gap:16px;margin-top:14px}} .pp b{{font-family:ID;font-size:54px;letter-spacing:-1px;font-weight:400}} .pp .st{{font-size:26px}}</style>
<div class="w">{TOP}<div class="kick">Proteine</div><div class="h">Welches passt<br>zu dir?</div><div class="hr"></div>{rows}
<div style="font-size:24px;color:#6b7378;margin-top:18px">Bis zu 24–25 g Eiweiß pro Portion (30 g)</div></div>{CODE}'''
# 2 Riegel-Duell
RD=[('Gewicht','45 g','55 g'),('Eiweiß','14–15 g','14 g'),('Art','weich, mit Füllung','Hafer, Nüsse, Frucht'),('12er Box','21,63 €','23,03 €'),('pro Riegel','1,80 €','1,92 €')]
tab=''.join(f'<div class="tr{" big" if i>2 else ""}"><div></div><div class="v">{b}</div><div class="l">{k}</div><div class="v">{c}</div></div>' for i,(k,b,c) in enumerate(RD))
S['7-Riegel-Duell']=f'''<style>.h{{font-size:150px}}
.duo{{display:flex;justify-content:space-between;align-items:flex-end;margin-top:26px;height:330px}}
.duo div{{width:440px;text-align:center}} .duo img{{max-width:440px;max-height:300px}}
.vs{{position:absolute;left:50%;top:520px;transform:translateX(-50%);font-family:ID;font-size:64px;background:#111;color:#fff;padding:4px 18px}}
.nm{{display:flex;justify-content:space-between;font-size:30px;font-weight:700;margin-top:14px}} .nm span{{width:440px;text-align:center}}
.tr{{display:grid;grid-template-columns:0 1fr 200px 1fr;align-items:center;border-bottom:2px solid #c9d0d3;padding:16px 0;font-size:30px;text-align:center}}
.tr .l{{font-size:22px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:#6b7378}}
.tr.big .v{{font-family:ID;font-size:46px;letter-spacing:-1px}}
.q{{margin-top:34px;text-align:center;font-family:ID;font-size:52px;letter-spacing:-1px}}</style>
<div class="w">{TOP}<div class="kick">Riegel {bd(30,30)}</div><div class="h">Riegel-Duell</div>
<div class="duo"><div><img src="{u('designerbar.png')}"></div><div><img src="{u('goatbar.png')}"></div></div>
<div class="nm"><span>Designer Bar</span><span>GOAT Bar</span></div><div class="hr" style="margin-top:14px"></div>
<div>{tab}</div><div class="q">Team Designer oder Team GOAT?</div></div>{CODE}'''
# 3 Kreatin
KR=[('kreatin-pulver.png','Pulver','250 g, 62 Portionen','11,34','18,90','0,18'),('kreatin-kapseln.png','Kapseln','300 Stück, 100 Portionen','21,54','35,90','0,22'),('kreatin-gummies.png','Gummies','120 Stück, 30 Portionen','16,74','27,90','0,56')]
cols=''.join(f'''<div class="kc"><div class="ki"><img src="{u(n)}"></div><div class="kn">{t}</div><div class="ks">{s}</div>
<div class="kp">{p} €</div><div class="st" style="font-size:24px">{a} €</div><div class="kpp"><b>{pp} €</b><br>pro Portion</div></div>''' for n,t,s,p,a,pp in KR)
S['8-Kreatin']=f'''<style>.h{{font-size:112px}} .h em{{font-style:normal;color:{C[40]}}}
.ks0{{font-size:30px;margin-top:22px;line-height:1.4;color:#333}}
.kk{{display:flex;justify-content:space-between;margin-top:34px}} .kc{{width:300px;text-align:center}}
.ki{{height:280px;display:flex;align-items:flex-end;justify-content:center}} .ki img{{max-width:270px;max-height:275px}}
.kn{{font-family:ID;font-size:48px;margin-top:20px;letter-spacing:-1px}} .ks{{font-size:22px;color:#6b7378;margin-top:2px}}
.kp{{font-family:ID;font-size:52px;margin-top:16px;letter-spacing:-1px}}
.kpp{{margin-top:16px;border-top:2px solid #c9d0d3;padding-top:12px;font-size:22px;color:#6b7378}} .kpp b{{font-family:ID;font-size:40px;color:#111;font-weight:400}}</style>
<div class="w">{TOP}<div class="kick">Kreatin {bd(40,30)}</div><div class="h">Pulver, Kapseln<br>oder <em>Gummies?</em></div><div class="hr"></div>
<div class="ks0">Bei Kapseln und Gummies stecken 3 g Kreatin in jeder Portion. Am günstigsten bleibt das Pulver.</div>
<div class="kk">{cols}</div></div>{CODE}'''
# 4 Collagen
S['9-Collagen']=f'''<style>.h{{font-size:150px}}
.cb{{display:flex;align-items:center;gap:40px;margin-top:40px}} .cb img{{width:420px}}
.cp .bdx{{font-family:ID;font-size:120px;line-height:.9;color:{C[50]};letter-spacing:-4px}}
.cp .n{{font-family:ID;font-size:96px;letter-spacing:-3px;margin-top:20px}} .cp .st{{font-size:32px}}
.cp .pp{{margin-top:22px;font-size:28px;color:#333}} .cp .pp b{{font-family:ID;font-size:44px;color:#111;font-weight:400}}
.li{{margin-top:44px;border-top:3px solid #111}} .li div{{display:flex;justify-content:space-between;border-bottom:2px solid #c9d0d3;padding:20px 0;font-size:30px}} .li span{{color:#6b7378}}</style>
<div class="w">{TOP}<div class="kick">Collagen {bd(50,30)}</div><div class="h">Collagen<br>Peptides</div>
<div class="cb"><img src="{u('collagen.png')}"><div class="cp"><div class="bdx">-50 %</div><div class="n">14,95 €</div><div class="st">statt 29,90 €</div><div class="pp"><b>0,75 €</b> pro Portion</div></div></div>
<div class="li"><div><span>Packung</span>300 g, 20 Portionen</div><div><span>Drin</span>Kollagenpeptide, Vitamin C, Zink, Kupfer</div><div><span>Sorten u. a.</span>Cola Orange, Green Apple, Lemon</div><div><span>Zubereitung</span>einfach in Wasser einrühren</div></div></div>{CODE}'''
# 5 Vorrats-Bon
BON=[('2 × Designer Protein Extra Creamy 480 g','39,06','55,80'),('1 × Designer Whey 908 g','37,43','49,90'),('2 × Designer Bar 12er Box','43,26','61,80'),('1 × Kreatin Kapseln 300 Stück','21,54','35,90'),('1 × Collagen Peptides 300 g','14,95','29,90')]
bl=''.join(f'<div class="bi"><div>{t}<br><span>statt {a} €</span></div><div>{p} €</div></div>' for t,p,a in BON)
S['10-Vorrats-Bon']=f'''<style>.h{{font-size:132px}}
.bon{{position:relative;margin-top:40px;background:#fff;padding:44px 46px 40px;font-family:MO;font-size:27px;line-height:1.35;box-shadow:0 18px 40px rgba(0,0,0,.08);
 -webkit-mask:linear-gradient(#000,#000) top/100% calc(100% - 18px) no-repeat,conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) bottom/36px 18px repeat-x}}
.bh{{text-align:center;font-weight:700;letter-spacing:3px}} .bs{{text-align:center;color:#6b7378;font-size:23px;margin-top:4px}}
.dl{{border-top:2px dashed #b9c0c3;margin:22px 0}}
.bi{{display:flex;justify-content:space-between;gap:20px;margin:14px 0}} .bi span{{color:#7d868b;font-size:22px;text-decoration:line-through}} .bi>div:last-child{{white-space:nowrap;font-weight:700}}
.sum{{display:flex;justify-content:space-between;font-weight:700;font-size:34px}} .sv{{display:flex;justify-content:space-between;margin-top:10px;font-size:27px}} .sv b{{background:{C[30]};padding:0 8px}}</style>
<div class="w">{TOP}<div class="kick">Vorrat-Beispiel</div><div class="h">Einmal voll<br>machen, bitte.</div>
<div class="bon"><div class="bh">ESN BLACK WEEK</div><div class="bs">22.11. – 02.12.2026</div><div class="dl"></div>{bl}<div class="dl"></div>
<div class="sum"><div>SUMME</div><div>156,24 €</div></div><div class="sv"><div>statt 233,30 €</div><b>77,06 € gespart</b></div></div></div>{CODE}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920})
        for k,body in S.items():
            open(f'{D}/s2_{k}.html','w').write(f'<html><head><style>{CSS}</style></head><body>{body}</body></html>')
            await pg.goto(f'file://{D}/s2_{k}.html'); await pg.wait_for_timeout(400)
            bot=await pg.evaluate("Math.max(...[...document.querySelectorAll('.w *')].map(e=>e.getBoundingClientRect().bottom))")
            wid=await pg.evaluate("Math.max(...[...document.querySelectorAll('.w *')].map(e=>e.getBoundingClientRect().right))")
            print(k,round(bot),round(wid))
            await pg.screenshot(path=f'{D}/ESN-Story-{k}.png')
        await b.close()
asyncio.run(main())
