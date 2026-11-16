# -*- coding: utf-8 -*-
# ESN Black Week – Story-Serie 3 (farbig): Preis pro Portion, Top 10, Starter-Paket, Black Friday, Fragen
import asyncio, os
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__))
def u(n):
    for p in (D+'/s3/',D+'/s2/'):
        if os.path.exists(p+n+'.png'): return 'file://'+p+n+'.png'
    raise SystemExit('fehlt '+n)
I='/usr/share/fonts/opentype/inter/'
C={50:'#f2231b',40:'#ff7a00',30:'#ffcc00',25:'#19c3a3'}
CSS=f'''@font-face{{font-family:ID;src:url(file://{I}InterDisplay-Black.otf)}}
@font-face{{font-family:IN;src:url(file://{I}Inter-Regular.otf);font-weight:400}}
@font-face{{font-family:IN;src:url(file://{I}Inter-SemiBold.otf);font-weight:600}}
@font-face{{font-family:IN;src:url(file://{I}Inter-Bold.otf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;font-family:IN;overflow:hidden}}
.w{{position:absolute;left:64px;right:64px;top:168px}}
.top{{display:flex;justify-content:space-between;font-size:23px;font-weight:600;letter-spacing:3px;text-transform:uppercase;opacity:.7}}
.kick{{margin-top:28px;font-size:28px;font-weight:700;letter-spacing:4px;text-transform:uppercase}}
.h{{font-family:ID;line-height:.92;letter-spacing:-3px;margin-top:8px}}
.bd{{display:inline-block;font-family:ID;color:#111;background:#fff;padding:4px 10px 2px;letter-spacing:-1px;border-radius:3px}}
.code{{position:absolute;left:270px;right:270px;top:1640px;text-align:center;padding:10px 0 8px;border-radius:4px}}
.code small{{display:block;font-size:19px;font-weight:600;letter-spacing:5px;opacity:.7}}
.code div{{font-family:ID;font-size:56px;line-height:1.05;letter-spacing:2px}}
.th{{width:96px;height:96px;display:flex;align-items:center;justify-content:center;flex:none}} .th img{{max-width:96px;max-height:96px}}
'''
TOP='<div class="top"><span>Werbung</span><span>@esncom · Black Week</span></div>'
def code(bg,fg): return f'<div class="code" style="background:{bg};color:{fg}"><small>CODE</small><div>FITMITKEV</div></div>'
def bd(d,fs=26): return f'<span class="bd" style="font-size:{fs}px">-{d}%</span>'
S={}
# 11 Preis pro Portion – gelb
PP=[('flexpresso','Flexpresso','908 g, 30 Portionen','1,35','Kaffee'),('extracreamy-vanilla','Designer Protein Extra Creamy','480 g, 16 Portionen','1,22','Shake'),
 ('whey','Designer Whey','908 g, 30 Portionen','1,25','Shake'),('isoclear','Isoclear','908 g, 30 Portionen','1,47','Shake'),
 ('designerbar','Designer Bar','12er Box','1,80','Riegel'),('goatbar','GOAT Bar','12er Box','1,92','Riegel'),
 ('kreatin-kapseln','Kreatin Kapseln','300 Stück, 100 Portionen','0,22','Portion'),('omega3','Omega-3','300 Kapseln, 100 Portionen','0,39','Portion'),
 ('d3k2','Vitamin D3 + K2','120 Kapseln, 120 Portionen','0,13','Kapsel'),('collagen','Collagen Peptides','300 g, 20 Portionen','0,75','Portion')]
rows=''.join(f'<div class="r"><div class="th"><img src="{u(n)}"></div><div class="nm"><b>{t}</b><span>{s}</span></div><div class="pr"><b>{p} €</b><span>pro {e}</span></div></div>' for n,t,s,p,e in PP)
S['11-Preis-pro-Portion']=f'''<style>body{{background:#ffcc00;color:#111}} .h{{font-size:112px}}
.ex{{font-size:26px;line-height:1.35;margin-top:16px}}
.r{{display:flex;align-items:center;gap:22px;border-bottom:2px solid rgba(0,0,0,.18);padding:8px 0}} .r:first-child{{border-top:3px solid #111}}
.nm{{flex:1;display:flex;flex-direction:column}} .nm b{{font-size:28px}} .nm span{{font-size:21px;opacity:.7}}
.pr{{text-align:right;display:flex;flex-direction:column}} .pr b{{font-family:ID;font-size:54px;line-height:.95;font-weight:400;letter-spacing:-1px}} .pr span{{font-size:19px;opacity:.7}}</style>
<div class="w">{TOP}<div class="kick">Black Week</div><div class="h">Preis pro Portion</div>
<div class="ex">So gerechnet: Black-Week-Preis geteilt durch die Portionen in der Packung.</div>
<div style="margin-top:18px">{rows}</div></div>{code('#111','#ffcc00')}'''
# 12 Top 10 – türkis
TT=[('flexpresso','Flexpresso','908 g',25,'40,43'),('designerbar','Designer Bar','12er Box',30,'21,63'),('extracreamy-vanilla','Extra Creamy','480 g',30,'19,53'),
 ('isoclear','Isoclear','908 g',25,'44,18'),('kreatin-kapseln','Kreatin Kapseln','300 Stück',40,'21,54'),('omega3','Omega-3','300 Kapseln',30,'39,13'),
 ('d3k2','Vitamin D3 + K2','120 Kapseln',30,'16,03'),('magnesium','Magnesium Complex','90 Kapseln',30,'11,83'),('collagen','Collagen Peptides','300 g',50,'14,95'),('peanutbutter','Peanut Butter','1 kg',30,'9,03')]
cards=''.join(f'<div class="c"><div class="no">{i+1}</div><div class="ci"><img src="{u(n)}"></div><div class="ct"><b>{t}</b><span>{s}</span><div class="cp">{p} €</div>{bd(d,22)}</div></div>' for i,(n,t,s,d,p) in enumerate(TT))
S['12-Meine-Top-10']=f'''<style>body{{background:#19c3a3;color:#0b0b0b}} .h{{font-size:150px}}
.g{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:28px}}
.c{{position:relative;background:#fff;border-radius:6px;display:flex;align-items:center;gap:12px;padding:12px 14px;height:196px}}
.no{{position:absolute;left:12px;top:8px;font-family:ID;font-size:34px;color:#19c3a3}}
.ci{{width:150px;height:170px;display:flex;align-items:center;justify-content:center;flex:none}} .ci img{{max-width:140px;max-height:165px}}
.ct{{display:flex;flex-direction:column;align-items:flex-start}} .ct b{{font-size:25px;line-height:1.15}} .ct span{{font-size:19px;opacity:.6}}
.cp{{font-family:ID;font-size:46px;letter-spacing:-1px;margin:6px 0 6px}} .c .bd{{background:#111;color:#fff}}</style>
<div class="w">{TOP}<div class="kick">Mit Black-Week-Preis</div><div class="h">Meine Top 10</div>
<div class="g">{cards}</div></div>{code('#0b0b0b','#fff')}'''
# 13 Starter-Paket – orange
SP=[('flexpresso','Flexpresso','für die Proteine am Morgen','40,43','53,90',''),
 ('designerbar','Designer Bar','Schoki-Snack für zwischendurch, unter 2 g Zucker','21,63','30,90',''),
 ('extracreamy-vanilla','Designer Protein Extra Creamy','für meine Rezepte','19,53','27,90',''),
 ('isoclear','Isoclear','nach dem Training, einfach mit Wasser','44,18','58,90',''),
 ('kreatin-pulver','Kreatin Pulver 250 g','täglich als feste Routine','11,34','18,90',''),
 ('omega3','Omega-3, 60 Kapseln','EPA und DHA tragen zu einer normalen Herzfunktion bei.¹','11,83','16,90','hc'),
 ('d3k2','Vitamin D3 + K2','Vitamin D trägt zu einer normalen Funktion des Immunsystems bei.','16,03','22,90','hc')]
sp=''.join(f'<div class="r"><div class="th"><img src="{u(n)}"></div><div class="nm"><b>{t}</b><span class="{c}">{f}</span></div><div class="pr"><span class="st">{a} €</span><b>{p} €</b></div></div>' for n,t,f,p,a,c in SP)
S['13-Starter-Paket']=f'''<style>body{{background:#ff7a00;color:#111}} .h{{font-size:132px}} .th{{width:120px;height:120px}} .th img{{max-width:120px;max-height:120px}}
.r{{display:flex;align-items:center;gap:22px;border-bottom:2px solid rgba(0,0,0,.2);padding:9px 0}} .r:first-child{{border-top:3px solid #111}}
.nm{{flex:1;display:flex;flex-direction:column}} .nm b{{font-size:31px}} .nm span{{font-size:24px;line-height:1.3}} .nm span.hc{{font-weight:600}}
.pr{{text-align:right;display:flex;flex-direction:column}} .pr b{{font-family:ID;font-size:52px;font-weight:400;letter-spacing:-1px;line-height:1}} .pr .st{{font-size:23px;text-decoration:line-through;opacity:.65}}
.tot{{display:flex;justify-content:space-between;align-items:center;margin-top:22px;background:#111;color:#fff;padding:18px 24px;border-radius:6px}}
.tot .a{{font-size:26px}} .tot .a s{{opacity:.6}} .tot .b{{font-family:ID;font-size:74px;letter-spacing:-2px;line-height:1}} .tot .sv{{display:inline-block;background:#ffcc00;color:#111;font-weight:700;font-size:24px;padding:4px 10px;margin-top:8px}}
.fn{{font-size:19px;margin-top:12px;opacity:.75;line-height:1.3}}</style>
<div class="w">{TOP}<div class="kick">Für Einsteiger</div><div class="h">Starter-Paket</div>
<div style="margin-top:22px">{sp}</div>
<div class="tot"><div class="a">vorher <s>230,30 €</s><br><span class="sv">65,33 € gespart</span></div><div class="b">164,97 €</div></div>
<div class="fn">¹ Die positive Wirkung stellt sich bei einer täglichen Aufnahme von 250 mg EPA und DHA ein.</div></div>{code('#111','#ff7a00')}'''
# 14 Black Friday – rot
BF=[('collagen',50,'Collagen Peptides','300 g','14,95'),('kreatin-gummies',40,'Kreatin Gummies','120 Stück','16,74'),('porridge',40,'Protein Porridge','alle Sorten',''),('designerbar',30,'Designer Bar','12er Box','21,63')]
bf=''.join(f'<div class="b"><div class="bi"><img src="{u(n)}"></div><div class="bp">-{d}<span>%</span></div><div class="bn"><b>{t}</b><br>{s}{(" · "+p+" €") if p else ""}</div></div>' for n,d,t,s,p in BF)
S['14-Black-Friday']=f'''<style>body{{background:#f2231b;color:#fff}} .h{{font-size:190px;line-height:.86}}
.g{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:34px}}
.b{{background:#0b0b0b;border-radius:6px;padding:18px;height:470px;display:flex;flex-direction:column}}
.bi{{height:250px;display:flex;align-items:center;justify-content:center}} .bi img{{max-width:240px;max-height:240px}}
.bp{{font-family:ID;font-size:96px;line-height:1;letter-spacing:-3px;margin-top:10px;color:#ffcc00}} .bp span{{font-size:56px}}
.bn{{font-size:24px;line-height:1.3;margin-top:6px;opacity:.9}} .bn b{{font-size:27px}}</style>
<div class="w">{TOP}<div class="kick">Fr 27.11. · nur noch bis Mi 17:30 Uhr</div><div class="h">Black<br>Friday</div>
<div class="g">{bf}</div></div>{code('#0b0b0b','#fff')}'''
# 15 Fragen – blau
FQ=[('Wie lange läuft die Black Week?','Von So 22.11., 12 Uhr bis Mi 02.12., 17:30 Uhr.'),
 ('Wie viel Rabatt gibt es?','Proteine und Riegel -25 bis -30 %, Kreatin -40 %, Collagen -50 %.'),
 ('Brauche ich deinen Code?','Die Rabatte gibt es automatisch. Mit FITMITKEV im Warenkorb unterstützt du mich.'),
 ('Was kostet der Versand?','Bei der 2. Bestellung in der Black Week ab 30 € gratis mit SHIPAGAIN.'),
 ('Was nimmst du selbst?','Flexpresso, Designer Bar, Extra Creamy und Kreatin. Mehr in meinen Top 10.')]
fq=''.join(f'<div class="q"><div class="qq">{q}</div><div class="qa">{a}</div></div>' for q,a in FQ)
S['15-Fragen']=f'''<style>body{{background:#3d8bff;color:#fff}} .h{{font-size:150px}}
.q{{border-top:3px solid rgba(255,255,255,.5);padding:26px 0}} .qq{{font-family:ID;font-size:52px;letter-spacing:-1px;line-height:1.08}} .qa{{font-size:33px;line-height:1.4;margin-top:10px}}</style>
<div class="w">{TOP}<div class="kick">Black Week</div><div class="h">Eure Fragen</div><div style="margin-top:20px">{fq}</div></div>{code('#0b0b0b','#fff')}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920})
        for k,body in S.items():
            open(f'{D}/s3_{k}.html','w').write(f'<html><head><style>{CSS}</style></head><body>{body}</body></html>')
            await pg.goto(f'file://{D}/s3_{k}.html'); await pg.wait_for_timeout(400)
            bot=await pg.evaluate("Math.max(...[...document.querySelectorAll('.w *')].map(e=>e.getBoundingClientRect().bottom))")
            wid=await pg.evaluate("Math.max(...[...document.querySelectorAll('.w *')].map(e=>e.getBoundingClientRect().right))")
            print(k,round(bot),round(wid))
            await pg.screenshot(path=f'{D}/ESN-Story-{k}.png')
        await b.close()
asyncio.run(main())
