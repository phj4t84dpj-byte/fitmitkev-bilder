# -*- coding: utf-8 -*-
# Ein Bild: Inhaltsverzeichnis beider Rezeptbücher (1080x1350 @2x)
import os, asyncio, importlib.util
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location('inh',D+'/inhalt.py')
src=open(D+'/inhalt.py').read().split('def page')[0]
ns={'__file__':D+'/inhalt.py'}; exec(src,ns); B=ns['B']; F=ns['F']; V=ns['V']
def col(b,kurz,unter):
    k=''.join(f'<div class="k"><h3 style="color:{b["farbe"]};border-color:{b["gold"]}">{t.replace("&","&amp;")}</h3><p>'+' <i style="color:{a}">•</i> '.format(a=b['akzent']).join('<s>'+y+'</s>' for y in x)+'</p></div>' for t,x in b['kap'])
    return f'<div class="col"><div class="hd" style="background:{b["farbe"]};border-bottom:6px solid {b["gold"]}"><img src="file://{V}/{b["cover"]}"><div><b>{kurz}</b><span>{unter}</span></div></div>{k}</div>'
html=f'''<html><head><style>
@font-face{{font-family:A;src:url(file://{F}/anton/Anton-Regular.ttf)}}
@font-face{{font-family:K;src:url(file://{F}/kaushanscript/KaushanScript-Regular.ttf)}}
@font-face{{font-family:P;src:url(file://{F}/poppins/Poppins-Regular.ttf);font-weight:400}}
@font-face{{font-family:P;src:url(file://{F}/poppins/Poppins-SemiBold.ttf);font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#FBF5EA;font-family:P;color:#2B2A2A;overflow:hidden;position:relative}}
.top{{text-align:center;padding:30px 0 22px}}
.top .k1{{font-family:K;font-size:46px;color:#8C1C24;line-height:1}}
.top .t{{font-family:A;font-size:60px;text-transform:uppercase;line-height:1.05;margin-top:6px;color:#2B2A2A}}
.cols{{display:flex;gap:28px;padding:0 34px}}
.col{{flex:1;display:flex;flex-direction:column;gap:13px}}
.hd{{display:flex;align-items:center;gap:16px;color:#fff;border-radius:10px;padding:12px 16px;height:132px}}
.hd img{{width:78px;border-radius:4px;border:2px solid #fff;transform:rotate(-3deg);box-shadow:0 6px 14px rgba(0,0,0,.3)}}
.hd b{{display:block;font-family:A;font-weight:400;font-size:34px;line-height:1.02;text-transform:uppercase}}
.hd span{{display:block;font-size:19px;font-weight:600;color:#F6E7D6;margin-top:4px;line-height:1.25}}
h3{{font-family:A;font-weight:400;font-size:24px;text-transform:uppercase;letter-spacing:.4px;line-height:1.05;border-bottom:3px solid;padding-bottom:4px;margin-bottom:5px}}
p{{font-size:21px;line-height:1.38}} s{{text-decoration:none;white-space:nowrap}} i{{font-style:normal;font-weight:600}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:104px;background:#2B2A2A;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 44px}}
.foot b{{font-family:A;font-weight:400;font-size:40px}}
.foot span{{font-size:23px;font-weight:600;text-align:right;line-height:1.3}}
</style></head><body>
<div class="top"><div class="k1">Was steckt drin?</div><div class="t">Alle 72 Rezepte aus meinen Büchern</div></div>
<div class="cols">{col(B['weihnachten'],'Weihnachtsbäckerei<br>in leicht','36 süße Rezepte für den Advent')}{col(B['wohlfuehl'],'Wohlfühlküche<br>in leicht','36 herzhafte Gerichte unter 500 kcal')}</div>
<div class="foot"><b>9,99 € · beide 14,99 €</b><span>Sofort als PDF<br>Link im 1. Kommentar</span></div>
</body></html>'''
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch(); pg=await br.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
        open(D+'/inhalt1.html','w').write(html); await pg.goto('file://'+D+'/inhalt1.html'); await pg.wait_for_timeout(600)
        print(await pg.evaluate("[...document.querySelectorAll('.col')].map(e=>Math.round(e.getBoundingClientRect().bottom))"),'Fuß ab 1246')
        await pg.screenshot(path=D+'/Buch-Inhalt-beide.png'); await br.close()
asyncio.run(main())
