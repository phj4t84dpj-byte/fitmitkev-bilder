# -*- coding: utf-8 -*-
# ESN Black Week Rabatt-Übersicht – IG-Story 1080x1920, schlichter Print-Look (schwarz/weiß, keine Glows)
import asyncio, os
from playwright.async_api import async_playwright
B=os.path.abspath('img')+'/'
F='/mnt/skills/examples/canvas-design/canvas-fonts/'
I='/usr/share/fonts/opentype/inter/'
TIERS=[('50',['Samples (30 g)','ausgewählte Vitalstoffe']),
 ('40',['Protein Porridge','Kreatin – Kapseln, Pulver, Sticks, Gummies']),
 ('30',['Designer Protein Extra Creamy, Omega-3, Magnesium','Designer Bar, Oatbar, GOAT Bar (12er Box)','Pancake & Waffle Mix, Rice Pudding, Peanut Butter']),
 ('25',['Flexpresso, Designer Whey, Iso Whey, Isoclear','Protein Cold Brew, Protein Matcha']),
 ('20',['Shaker und Zubehör'])]
NEU=[('extra-creamy-black-edition-ultra-dark.png','Ultra Dark<br>Chocolate'),
 ('extra-creamy-480g-vanilla-speculoos.png','Vanilla<br>Speculoos'),
 ('extra-creamy-480g-strawberry-cream.png','Strawberry<br>Cream'),
 ('extra-creamy-480g-cinnamon-cereal.png','Cinnamon<br>Cereal'),
 ('designer-bar-mint-box.png','Bar Dark<br>Choc Mint')]
rows=''.join(f'<div class="row{" l" if p=="20" else ""}"><div class="p">-{p}<span>%</span></div><div class="it">{"<br>".join(it)}</div></div>' for p,it in TIERS)
cards=''.join(f'<div class="nc"><div class="im"><img src="file://{B}{f}"></div><div class="nn">{n}</div></div>' for f,n in NEU)
html=f'''<html><head><style>
@font-face{{font-family:BS;src:url(file://{F}BigShoulders-Bold.ttf)}}
@font-face{{font-family:IN;src:url(file://{I}Inter-Regular.otf);font-weight:400}}
@font-face{{font-family:IN;src:url(file://{I}Inter-SemiBold.otf);font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:#0b0b0b;color:#fff;font-family:IN;overflow:hidden}}
.w{{position:absolute;left:64px;right:64px;top:168px}}
.top{{display:flex;justify-content:space-between;font-size:23px;font-weight:600;letter-spacing:3px;color:#8c8c8c;text-transform:uppercase}}
.h{{font-family:BS;font-size:196px;line-height:.8;letter-spacing:0;margin-top:20px;white-space:nowrap;text-transform:uppercase}}
.sub{{display:flex;justify-content:space-between;align-items:baseline;margin-top:18px;border-top:3px solid #fff;padding-top:16px}}
.sub b{{font-size:31px;font-weight:600;letter-spacing:5px}}
.sub span{{font-size:27px;color:#bdbdbd}}
.hero{{position:relative;height:262px;margin-top:14px}}
.bis{{position:absolute;left:4px;top:18px;font-size:30px;font-weight:600;letter-spacing:5px;color:#bdbdbd}}
.big{{position:absolute;left:0;top:72px;font-family:BS;font-size:205px;line-height:.85}}
.big span{{font-size:115px}}
.tub{{position:absolute;right:10px;top:8px;height:232px}}
.row{{display:flex;border-top:1px solid #333;padding:11px 0 10px;align-items:center}}
.row.l{{border-bottom:1px solid #333}}
.p{{width:200px;font-family:BS;font-size:80px;line-height:.9}}
.p span{{font-size:46px}}
.it{{font-size:26px;line-height:1.3;color:#e6e6e6}}
.neu{{display:flex;justify-content:space-between;align-items:baseline;margin-top:20px}}
.neu b{{font-family:BS;font-size:52px;letter-spacing:1px}}
.neu span{{font-size:25px;color:#bdbdbd}}
.ncs{{display:flex;justify-content:space-between;margin-top:12px}}
.nc{{width:180px;text-align:center}}
.im{{height:112px;display:flex;align-items:flex-end;justify-content:center}}
.im img{{max-height:112px;max-width:160px}}
.nn{{font-size:20px;line-height:1.2;margin-top:8px;color:#e6e6e6}}
.ship{{margin-top:18px;font-size:24px;color:#bdbdbd;text-align:center}}
.ship b{{color:#fff;font-weight:600}}
.code{{position:absolute;left:250px;right:250px;top:1625px;border:3px solid #fff;text-align:center;padding:10px 0 8px}}
.code small{{display:block;font-size:20px;font-weight:600;letter-spacing:5px;color:#bdbdbd}}
.code div{{font-family:BS;font-size:80px;line-height:1;letter-spacing:4px}}
</style></head><body><div class="w">
<div class="top"><span>Werbung</span><span>@esncom</span></div>
<div class="h">Black Week</div>
<div class="sub"><b>RABATT-ÜBERSICHT</b><span>22.11., 12 Uhr – 02.12., 17:30 Uhr</span></div>
<div class="hero"><div class="bis">BIS ZU</div><div class="big">-70<span>%</span></div><img class="tub" src="file://{B}extra-creamy-black-edition-ultra-dark.png"></div>
{rows}
<div class="neu"><b>NEU</b><span>Dosen 480 g: 19,53 € statt 27,90 €</span></div>
<div class="ncs">{cards}</div>
<div class="ship">Ab der 2. Bestellung versandkostenfrei ab 30 € mit <b>SHIPAGAIN</b></div>
</div>
<div class="code"><small>CODE</small><div>FITMITKEV</div></div>
</body></html>'''
open('story2.html','w').write(html)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file://'+os.path.abspath('story2.html')); await pg.wait_for_timeout(500)
        print(await pg.evaluate("[document.querySelector('.ship').getBoundingClientRect().bottom, document.querySelector('.code').getBoundingClientRect().bottom]"))
        await pg.screenshot(path='ESN-BlackWeek-Rabatt-Uebersicht-Story.png'); await b.close()
asyncio.run(main())
