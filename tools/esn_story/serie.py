# -*- coding: utf-8 -*-
# ESN Black Week – Story-Serie (5 Stories) im Look der Rabatt-Übersicht
import asyncio, os
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__)); IMG=D+'/img/'; BI=D+'/bundle/'
F='/mnt/skills/examples/canvas-design/canvas-fonts/'; I='/usr/share/fonts/opentype/inter/'
C={50:'#f2231b',40:'#ff7a00',30:'#ffcc00',25:'#19c3a3',20:'#3d8bff'}
def im(n): return 'file://'+(BI+n if n.endswith('.jpg') else IMG+n)
CSS=f'''@font-face{{font-family:BS;src:url(file://{F}BigShoulders-Bold.ttf)}}
@font-face{{font-family:IN;src:url(file://{I}Inter-Regular.otf);font-weight:400}}
@font-face{{font-family:IN;src:url(file://{I}Inter-SemiBold.otf);font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:#0b0b0b;color:#fff;font-family:IN;overflow:hidden}}
.w{{position:absolute;left:64px;right:64px;top:168px}}
.top{{display:flex;justify-content:space-between;font-size:23px;font-weight:600;letter-spacing:3px;color:#8c8c8c;text-transform:uppercase}}
.h{{font-family:BS;line-height:.84;margin-top:20px;text-transform:uppercase}}
.sub{{display:flex;justify-content:space-between;align-items:baseline;margin-top:18px;border-top:3px solid #fff;padding-top:14px}}
.sub b{{font-size:29px;font-weight:600;letter-spacing:5px}}
.sub span{{font-size:26px;color:#bdbdbd}}
.tile{{position:relative;background:radial-gradient(ellipse at 50% 45%,#5a5a5a,#1c1c1c 78%);border-radius:6px;display:flex;align-items:center;justify-content:center;overflow:hidden}}
.tile img.co{{max-width:84%;max-height:84%;filter:drop-shadow(0 8px 10px rgba(0,0,0,.6))}}
.tile img.ph{{width:100%;height:100%;object-fit:cover}}
.bd{{position:absolute;left:0;top:0;color:#0b0b0b;font-family:BS;font-size:30px;line-height:1;padding:5px 8px 3px;border-bottom-right-radius:6px}}
.st{{color:#9a9a9a;text-decoration:line-through}}
.code{{position:absolute;left:250px;right:250px;top:1625px;border:3px solid #fff;text-align:center;padding:10px 0 8px}}
.code small{{display:block;font-size:20px;font-weight:600;letter-spacing:5px;color:#bdbdbd}}
.code div{{font-family:BS;font-size:80px;line-height:1;letter-spacing:4px}}
.p{{font-size:32px;line-height:1.4;color:#e6e6e6}}
'''
TOP='<div class="top"><span>Werbung</span><span>@esncom</span></div>'
CODE='<div class="code"><small>CODE</small><div>FITMITKEV</div></div>'
def tile(n,w,h,d=None):
    c='ph' if n.endswith('.jpg') else 'co'
    b=f'<div class="bd" style="background:{C[d]}">-{d}%</div>' if d else ''
    return f'<div class="tile" style="width:{w}px;height:{h}px"><img class="{c}" src="{im(n)}">{b}</div>'
NEU=[('extra-creamy-black-edition-ultra-dark.png','Ultra Dark Chocolate','19,53','27,90'),
 ('extra-creamy-480g-vanilla-speculoos.png','Vanilla Speculoos','19,53','27,90'),
 ('extra-creamy-480g-strawberry-cream.png','Strawberry Cream','19,53','27,90'),
 ('extra-creamy-480g-cinnamon-cereal.png','Cinnamon Cereal','19,53','27,90'),
 ('designer-bar-mint-box.png','Designer Bar Dark Chocolate Mint','21,63','30,90')]
S={}
# 1 Ankündigung (Sa 21.11.)
S['1-Ankuendigung']=f'''<style>.h{{font-size:250px}} .tile{{flex:1}} .h span{{color:#ffcc00}}
.row{{display:flex;gap:12px;margin-top:40px}}
.nl{{margin-top:44px;font-family:BS;font-size:48px}}</style>
<div class="w">{TOP}<div class="h">Morgen<br><span>12 Uhr</span></div>
<div class="sub"><b>ESN BLACK WEEK</b><span>bis Mi 02.12., 17:30 Uhr</span></div>
<p class="p" style="margin-top:30px">Einmal im Jahr. Hier holen sich viele Stammkunden ihren Vorrat, ich auch.</p>
<div class="nl">NEU DABEI</div><div class="row" style="margin-top:12px">{"".join(tile(n,178,190) for n,*_ in NEU)}</div></div>{CODE}'''
# 2 Neue Sorten (So 22.11.)
cards=''.join(f'<div class="nc">{tile(n,"100%" and 292,250,30)}<div class="nn">{t}</div><div class="np"><b>{p} €</b> <span class="st">{a} €</span></div></div>' for n,t,p,a in NEU)
S['2-Neue-Sorten']=f'''<style>.h{{font-size:230px}}
.g{{display:flex;flex-wrap:wrap;gap:22px 20px;margin-top:30px}} .nc{{width:292px}}
.nn{{font-size:24px;line-height:1.2;margin-top:10px;color:#e6e6e6;min-height:58px}} .np{{font-size:26px;margin-top:2px}} .np b{{font-family:BS;font-size:46px;font-weight:400}}
.q{{position:absolute;left:64px;right:64px;top:1400px;font-family:BS;font-size:62px;line-height:1;text-align:center}}</style>
<div class="w">{TOP}<div class="h">Neu</div>
<div class="sub"><b>IN DER BLACK WEEK</b><span>ab 22.11., 12 Uhr</span></div>
<div class="g">{cards}</div></div>
<div class="q">WELCHE PROBIERST DU ZUERST?</div>{CODE}'''
# 3 So bestellst du (So 22.11.)
ST=[(25,'Link-Sticker in dieser Story antippen'),(30,'Lieblingsprodukte in den Warenkorb legen'),(40,'Im Warenkorb den Code <b>FITMITKEV</b> eintragen')]
steps=''.join(f'<div class="s"><div class="n" style="color:{C[c]}">{i+1}</div><div class="t">{t}</div></div>' for i,(c,t) in enumerate(ST))
S['3-So-bestellst-du']=f'''<style>.h{{font-size:172px;line-height:1}}
.s{{display:flex;align-items:center;gap:34px;border-bottom:1px solid #333;padding:26px 0}} .n{{font-family:BS;font-size:170px;line-height:.8;width:100px}}
.t{{font-size:40px;line-height:1.3}} .t b{{font-weight:600}}
.tip{{margin-top:40px;border:2px solid #333;padding:22px 26px;font-size:29px;line-height:1.4;color:#d6d6d6}} .tip b{{color:#fff;font-weight:600}}</style>
<div class="w">{TOP}<div class="h">So bestellst<br>du über mich</div>
<div class="sub"><b>ESN BLACK WEEK</b><span>22.11. – 02.12.</span></div>
<div style="margin-top:14px">{steps}</div>
<div class="tip"><b>Tipp für die 2. Bestellung:</b> Ab 30 € ist der Versand gratis mit dem Code <b>SHIPAGAIN</b>.</div></div>{CODE}'''
# 4 Preis pro Portion
PP=[('extra-creamy-480g-vanilla-speculoos.png',30,'Designer Protein Extra Creamy','480 g, 16 Portionen','1,22','pro Shake'),
 ('designer-bar-mint-box.png',30,'Designer Bar','12er Box','1,80','pro Riegel'),
 ('peanutbutter.jpg',30,'Peanut Butter','1 kg, 30 Portionen','0,30','pro Portion'),
 ('kreatin.jpg',40,'Ultrapure Kreatin','500 g, 142 Portionen','0,13','pro Portion'),
 ('magnesium.jpg',30,'Magnesium Complex','90 Kapseln, 30 Portionen','0,39','pro Portion'),
 ('omega3.jpg',30,'Omega-3','60 Kapseln, 20 Portionen','0,59','pro Portion')]
rows=''.join(f'<div class="r">{tile(n,128,128,d)}<div class="nm"><b>{t}</b><span>{s}</span></div><div class="pr"><b>{p} €</b><span>{u}</span></div></div>' for n,d,t,s,p,u in PP)
S['4-Preis-pro-Portion']=f'''<style>.h{{font-size:170px}}
.r{{display:flex;align-items:center;gap:24px;border-bottom:1px solid #333;padding:14px 0}}
.nm{{flex:1;display:flex;flex-direction:column}} .nm b{{font-size:30px;font-weight:600}} .nm span{{font-size:24px;color:#a8a8a8;margin-top:4px}}
.pr{{text-align:right;display:flex;flex-direction:column}} .pr b{{font-family:BS;font-size:76px;line-height:.9;font-weight:400}} .pr span{{font-size:22px;color:#a8a8a8}}</style>
<div class="w">{TOP}<div class="h">Was kostet<br>eine Portion?</div>
<div class="sub"><b>MIT BLACK-WEEK-PREIS</b><span>22.11. – 02.12.</span></div>
<div style="margin-top:8px">{rows}</div></div>{CODE}'''
# 5 Letzte Chance (Mi 2.12.)
RC=[(40,'Kreatin, Protein Porridge'),(30,'Designer Protein, Designer Bar, Omega-3, Magnesium'),(25,'Flexpresso, Designer Whey, Isoclear')]
rc=''.join(f'<div class="rc"><div class="pc" style="color:{C[p]}">-{p}<span>%</span></div><div class="it">{t}</div></div>' for p,t in RC)
S['5-Letzte-Chance']=f'''<style>.h{{font-size:190px;white-space:nowrap}} .h span{{color:#f2231b}}
.rc{{display:flex;align-items:center;border-top:1px solid #333;padding:16px 0}} .rc:last-child{{border-bottom:1px solid #333}}
.pc{{width:210px;font-family:BS;font-size:96px;line-height:.9}} .pc span{{font-size:54px}} .it{{font-size:29px;line-height:1.3;color:#e6e6e6}}</style>
<div class="w">{TOP}<div class="h">Letzter Tag<br><span>bis 17:30 Uhr</span></div>
<div class="sub"><b>ESN BLACK WEEK</b><span>heute, Mi 02.12.</span></div>
<p class="p" style="margin-top:28px">Danach gibt es diese Preise erst wieder in einem Jahr.</p>
<div style="margin-top:30px">{rc}</div></div>{CODE}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920})
        for k,body in S.items():
            open(f'{D}/serie_{k}.html','w').write(f'<html><head><style>{CSS}</style></head><body>{body}</body></html>')
            await pg.goto(f'file://{D}/serie_{k}.html'); await pg.wait_for_timeout(400)
            bot=await pg.evaluate("Math.max(...[...document.querySelectorAll('.w *')].map(e=>e.getBoundingClientRect().bottom))")
            wid=await pg.evaluate("Math.max(...[...document.querySelectorAll('.w *')].map(e=>e.getBoundingClientRect().right))")
            print(k,'bottom',round(bot),'right',round(wid))
            await pg.screenshot(path=f'{D}/ESN-Story-{k}.png')
        await b.close()
asyncio.run(main())
