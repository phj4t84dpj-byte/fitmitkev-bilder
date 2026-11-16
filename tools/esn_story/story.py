# -*- coding: utf-8 -*-
# ESN Black Week Rabattübersicht – IG-Story 1080x1920, Aufbau nach esnstory1 im Black-Week-Look
import asyncio, os
from playwright.async_api import async_playwright
B=os.path.abspath('img')+'/'
F='/mnt/skills/examples/canvas-design/canvas-fonts/'
P='/home/claude/fitmitkev-bilder/tools/instagram/karussell/profil.jpg'
TIERS=[('-50','#ff5e4d',['Samples (30 g)','einige Vitalstoffe']),
 ('-40','#ff9e2c',['Protein Porridge','Kreatin (Kapseln, Pulver, Sticks, Gummies)']),
 ('-30','#ffc83c',['Designer Protein Extra Creamy · Omega-3 · Magnesium','Designer Bar · Oatbar · GOAT Bar (12er Box)','Pancake & Waffle Mix · Rice Pudding · Peanut Butter']),
 ('-25','#00a8a8',['Flexpresso · Designer Whey · Iso Whey · Isoclear','Protein Cold Brew · Protein Matcha']),
 ('-20','#7d8ba0',['Shaker & Zubehör'])]
NEU=[('extra-creamy-black-edition-ultra-dark.png','Ultra Dark Chocolate','#ff5e4d'),
 ('extra-creamy-480g-vanilla-speculoos.png','Vanilla Speculoos','#ff9e2c'),
 ('extra-creamy-480g-strawberry-cream.png','Strawberry Cream','#ff7a9a'),
 ('extra-creamy-480g-cinnamon-cereal.png','Cinnamon Cereal','#ffc83c'),
 ('designer-bar-mint-box.png','Bar Dark Chocolate Mint','#00c2a8')]
rows=''.join(f'''<div class="tier"><div class="pct" style="background:{c}"><span>{p}</span><small>%</small></div>
<div class="items">{''.join(f'<div>{i}</div>' for i in it)}</div></div>''' for p,c,it in TIERS)
cards=''.join(f'''<div class="card"><img src="file://{B}{f}"><div class="fl" style="color:{c}">{n}</div></div>''' for f,n,c in NEU)
html=f'''<html><head><style>
@font-face{{font-family:O;src:url(file://{F}Outfit-Bold.ttf);font-weight:700}}
@font-face{{font-family:O;src:url(file://{F}Outfit-Regular.ttf);font-weight:400}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;font-family:O;color:#fff;overflow:hidden;
background:radial-gradient(circle at 92% 6%,rgba(255,158,44,.38),transparent 34%),radial-gradient(circle at 0% 100%,rgba(0,168,168,.30),transparent 38%),#14181f}}
.wrap{{position:absolute;left:52px;right:52px;top:135px}}
.pill{{display:inline-block;background:#fff;color:#181e26;font-weight:700;font-size:24px;letter-spacing:3px;padding:8px 24px;border-radius:40px}}
.head{{position:relative;margin-top:18px}}
.h1{{font-weight:700;font-size:124px;line-height:1;letter-spacing:2px}}
.h2{{font-weight:700;font-size:40px;color:#ff5e4d;letter-spacing:1.5px;margin-top:10px;display:flex;align-items:center;gap:14px}}
.h2 img{{width:66px;height:66px;border-radius:50%;border:4px solid #ffc83c;object-fit:cover}}
.date{{margin-top:10px;font-size:29px}}
.date b{{color:#ffc83c}}
.hero{{position:absolute;right:50px;top:-75px;height:225px;filter:drop-shadow(0 18px 40px rgba(255,158,44,.45))}}
.badge{{position:absolute;right:0px;top:120px;background:#ff9e2c;color:#181e26;font-weight:700;font-size:26px;padding:8px 18px;border-radius:30px;transform:rotate(-6deg)}}
.big{{position:relative;display:flex;align-items:flex-end;gap:22px;margin-top:6px}}
.bis{{font-size:38px;letter-spacing:4px;padding-bottom:26px}}
.num{{font-weight:700;font-size:170px;line-height:.9;color:#ff5e4d;text-shadow:0 0 60px rgba(255,94,77,.55)}}
.num small{{font-size:95px}}
.tiers{{margin-top:22px;display:flex;flex-direction:column;gap:10px}}
.tier{{display:flex;gap:20px;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.12);border-radius:22px;padding:10px 16px;align-items:center}}
.pct{{min-width:140px;height:72px;border-radius:18px;display:flex;align-items:center;justify-content:center;color:#14181f;font-weight:700}}
.pct span{{font-size:50px}} .pct small{{font-size:30px;margin-left:2px}}
.items{{font-size:27px;line-height:1.28}}
.sec{{margin-top:20px;font-size:26px;letter-spacing:3px;font-weight:700;color:#ffc83c}}
.sec span{{color:#fff;font-weight:400;letter-spacing:1px}}
.cards{{display:flex;gap:10px;margin-top:10px}}
.card{{flex:1;background:#fff;border-radius:22px;padding:10px 6px 12px;text-align:center}}
.card img{{width:150px;height:130px;object-fit:contain}}
.fl{{font-size:20px;font-weight:700;line-height:1.15;margin-top:4px;filter:brightness(.85)}}
.ship{{margin-top:14px;background:rgba(0,168,168,.18);border:2px solid #00a8a8;border-radius:20px;padding:10px 18px;font-size:26px;text-align:center}}
.ship b{{color:#ffc83c}}
.cta{{position:absolute;left:130px;right:130px;top:1605px;background:#181e26;border-radius:30px;padding:10px;box-shadow:0 0 70px rgba(255,200,60,.35)}}
.cta>div{{border:3px solid #ffc83c;border-radius:22px;text-align:center;padding:10px 14px}}
.cta .l{{font-size:24px;letter-spacing:3px;color:#cfd6e0}}
.cta .c{{font-size:60px;color:#ffc83c;letter-spacing:4px;line-height:1.05}}
</style></head><body><div class="wrap">
<div class="pill">WERBUNG · @ESNCOM</div>
<div class="head">
<div class="h1">BLACK WEEK</div>
<div class="h2"><img src="file://{P}">MEINE RABATT-ÜBERSICHT</div>
<div class="date"><b>So 22.11., 12 Uhr</b> bis <b>Mi 2.12., 17:30 Uhr</b></div></div>
<div class="big"><img class="hero" src="file://{B}extra-creamy-black-edition-ultra-dark.png"><div class="badge">NEU: BLACK EDITION</div><div class="bis">BIS ZU</div><div class="num">-70<small>%</small></div></div>
<div class="tiers">{rows}</div>
<div class="sec">NEU AM START <span>· Dosen (480 g) 19,53 € statt 27,90 €</span></div>
<div class="cards">{cards}</div>
<div class="ship">📦 Ab der 2. Bestellung: Versand ab 30 € gratis mit <b>SHIPAGAIN</b></div>
</div>
<div class="cta"><div><div class="l">MEIN CODE</div><div class="c">FITMITKEV</div></div></div>
</body></html>'''
open('story.html','w').write(html)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file://'+os.path.abspath('story.html')); await pg.wait_for_timeout(500)
        h=await pg.evaluate("[document.querySelector('.ship').getBoundingClientRect().bottom, document.querySelector('.cta').getBoundingClientRect().bottom]")
        print('ship bottom',h)
        await pg.screenshot(path='ESN-BlackWeek-Rabatte-Story.png'); await b.close()
asyncio.run(main())
