# -*- coding: utf-8 -*-
# "Kevs Empfehlungen" – ESN Black Week Bundles, IG-Story 1080x1920 im Look der Rabatt-Übersicht
import asyncio, os
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__))
IMG=D+'/img/'; BI=D+'/bundle/'
F='/mnt/skills/examples/canvas-design/canvas-fonts/'; I='/usr/share/fonts/opentype/inter/'
COL={50:'#f2231b',40:'#ff7a00',30:'#ffcc00',25:'#19c3a3',20:'#3d8bff'}
def src(n):
    for p in (BI+n, IMG+n):
        if os.path.exists(p): return 'file://'+p
    return ''
BUNDLES=[('Protein-Bundle','109,70','79,49',[('extra-creamy-480g-vanilla-speculoos.png',30,'Extra Creamy<br>Vanilla Speculoos'),('extra-creamy-black-edition-ultra-dark.png',30,'Extra Creamy<br>Ultra Dark Choc'),('flexpresso.jpg',25,'Flexpresso<br>908 g')]),
 ('Snack-Bundle','74,70','52,29',[('designer-bar-mint-box.png',30,'Designer Bar<br>Dark Choc Mint'),('designerbar-box.jpg',30,'Designer Bar<br>Maple Walnut'),('peanutbutter.jpg',30,'Peanut Butter<br>1 kg')]),
 ('Vitalstoff-Bundle','63,70','41,60',[('kreatin.jpg',40,'Ultrapure<br>Kreatin 500 g'),('omega3.jpg',30,'Omega-3<br>60 Kapseln'),('magnesium.jpg',30,'Magnesium<br>90 Kapseln')])]
def prod(f,d,n):
    s=src(f); ph=f.endswith('.jpg')
    im=(f'<img class="ph2" src="{s}">' if ph else f'<img class="co" src="{s}">') if s else '<div class="ph"></div>'
    return f'<div class="pr"><div class="pi">{im}<div class="bd" style="background:{COL[d]}">-{d}%</div></div><div class="pn">{n}</div></div>'
sec=''.join(f'''<div class="b"><div class="bh">{t}</div><div class="br"><div class="ps">{"".join(prod(*x) for x in it)}</div>
<div class="pz"><div class="st">statt {a} €</div><div class="nw">{n} €</div><div class="lb">BLACK-WEEK-PREIS</div></div></div></div>''' for t,a,n,it in BUNDLES)
html=f'''<html><head><style>
@font-face{{font-family:BS;src:url(file://{F}BigShoulders-Bold.ttf)}}
@font-face{{font-family:IN;src:url(file://{I}Inter-Regular.otf);font-weight:400}}
@font-face{{font-family:IN;src:url(file://{I}Inter-SemiBold.otf);font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:#0b0b0b;color:#fff;font-family:IN;overflow:hidden}}
.w{{position:absolute;left:64px;right:64px;top:168px}}
.top{{display:flex;justify-content:space-between;font-size:23px;font-weight:600;letter-spacing:3px;color:#8c8c8c;text-transform:uppercase}}
.h{{font-family:BS;font-size:108px;line-height:.82;margin-top:20px;text-transform:uppercase;white-space:nowrap}}
.sub{{display:flex;justify-content:space-between;align-items:baseline;margin-top:16px;border-top:3px solid #fff;padding-top:14px}}
.sub b{{font-size:29px;font-weight:600;letter-spacing:5px}}
.sub span{{font-size:26px;color:#bdbdbd}}
.b{{border-bottom:1px solid #333;padding:16px 0 14px}}
.bh{{font-family:BS;font-size:54px;line-height:1;text-transform:uppercase;letter-spacing:.5px}}
.br{{display:flex;align-items:center;margin-top:12px}}
.ps{{display:flex;gap:14px}}
.pr{{width:182px;text-align:center}}
.pi{{position:relative;height:182px;background:radial-gradient(ellipse at 50% 45%,#5a5a5a,#1c1c1c 78%);border-radius:6px;display:flex;align-items:center;justify-content:center;overflow:hidden}}
.pi img.co{{max-width:150px;max-height:146px;margin-top:14px;filter:drop-shadow(0 8px 10px rgba(0,0,0,.6))}}
.pi img.ph2{{width:100%;height:100%;object-fit:cover}}
.ph{{width:110px;height:140px;background:#ccc}}
.bd{{position:absolute;left:0;top:0;color:#0b0b0b;font-family:BS;font-size:28px;line-height:1;padding:5px 8px 3px;border-bottom-right-radius:6px}}
.pn{{font-size:19px;line-height:1.2;margin-top:8px;color:#d6d6d6}}
.pz{{flex:1;text-align:right}}
.st{{font-size:28px;color:#9a9a9a;text-decoration:line-through}}
.nw{{font-family:BS;font-size:100px;line-height:.95;margin-top:4px}}
.lb{{font-size:18px;font-weight:600;letter-spacing:3px;color:#bdbdbd;margin-top:4px}}
.all{{display:flex;justify-content:space-between;align-items:center;margin-top:20px}}
.all .l{{font-family:BS;font-size:62px;line-height:1;text-transform:uppercase}}
.all .l small{{display:block;font-family:IN;font-size:27px;color:#9a9a9a;text-decoration:line-through;margin-top:8px;text-transform:none}}
.all .r{{text-align:right}}
.all .r .n{{font-family:BS;font-size:100px;line-height:.9}}
.all .r .s{{display:inline-block;margin-top:10px;background:#ffcc00;color:#0b0b0b;font-weight:600;font-size:26px;padding:6px 14px}}
.code{{position:absolute;left:250px;right:250px;top:1625px;border:3px solid #fff;text-align:center;padding:10px 0 8px}}
.code small{{display:block;font-size:20px;font-weight:600;letter-spacing:5px;color:#bdbdbd}}
.code div{{font-family:BS;font-size:80px;line-height:1;letter-spacing:4px}}
</style></head><body><div class="w">
<div class="top"><span>Werbung</span><span>@esncom</span></div>
<div class="h">Meine Empfehlungen</div>
<div class="sub"><b>BLACK WEEK BUNDLES</b><span>22.11., 12 Uhr – 02.12., 17:30 Uhr</span></div>
{sec}
<div class="all"><div class="l">Alles zusammen<small>statt 248,10 €</small></div><div class="r"><div class="n">173,38 €</div><div class="s">74,72 € gespart</div></div></div>
</div>
<div class="code"><small>CODE</small><div>FITMITKEV</div></div>
</body></html>'''
open(D+'/bundle_story.html','w').write(html)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file://'+D+'/bundle_story.html'); await pg.wait_for_timeout(500)
        print(await pg.evaluate("[document.querySelector('.all').getBoundingClientRect().bottom,document.querySelector('.code').getBoundingClientRect().bottom]"))
        await pg.screenshot(path=D+'/ESN-BlackWeek-Meine-Empfehlungen-Story.png'); await b.close()
asyncio.run(main())
