# Promo-Bild Rezeptbücher (Facebook 4:5) – Kevs Entwurf vom 14.11. in denselben Farben, aber: Paket-Preis verdeckt nichts mehr, dazu vier Gerichte aus den Büchern
import asyncio, os
from playwright.async_api import async_playwright
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__)); F=os.path.join(D,'..','fonts','gf','ofl'); V='/home/claude/fitmitkev-bilder/verkaufsseite'
ROT='#8b1c23'; CREME='#fcf6ea'; GOLD='#c8a34b'; GRUEN='#22483b'; ROST='#a1462b'; TXT='#292929'; GELB='#f3c969'
FOOD=[('vanillekipferl','Vanillekipferl'),('skyr-kuchen','Skyr-Kuchen'),('rouladen','Rouladen'),('doener','Döner')]
food=''.join(f'<div class="f"><img src="file://{V}/{k}.jpg"><span>{n}</span></div>' for k,n in FOOD)
HTML=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:A;src:url("file://{F}/anton/Anton-Regular.ttf")}}
@font-face{{font-family:K;src:url("file://{F}/kaushanscript/KaushanScript-Regular.ttf")}}
@font-face{{font-family:P;font-weight:600;src:url("file://{F}/poppins/Poppins-SemiBold.ttf")}}
@font-face{{font-family:P;font-weight:700;src:url("file://{F}/poppins/Poppins-Bold.ttf")}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{CREME};font-family:P;font-weight:600;color:{TXT};position:relative;overflow:hidden}}
.head{{position:absolute;left:0;top:0;width:1080px;height:236px;background:{ROT};border-bottom:8px solid {GOLD};text-align:center}}
.hook{{font-family:K;font-size:56px;color:{GELB};margin-top:8px;transform:rotate(-2deg)}}
.tit{{font-family:A;font-size:106px;color:#fff;line-height:1;margin-top:8px;letter-spacing:1px}}
.cov{{position:absolute;top:268px;width:384px;border-radius:6px;box-shadow:0 18px 34px rgba(60,20,10,.32)}}
.c1{{left:112px;transform:rotate(-3deg)}} .c2{{left:584px;transform:rotate(3deg)}}
.einzel{{position:absolute;top:786px;width:384px;text-align:center}}
.einzel b{{display:inline-block;background:#fff;border:4px solid {GOLD};border-radius:40px;padding:4px 30px 5px;font-weight:700;font-size:35px;color:{ROT};box-shadow:0 6px 14px rgba(60,20,10,.18)}}
.paket{{position:absolute;left:150px;top:868px;width:780px;height:104px;background:{GRUEN};border:5px solid {GOLD};border-radius:56px;display:flex;align-items:center;justify-content:center;gap:22px;box-shadow:0 10px 22px rgba(20,40,30,.28)}}
.paket i{{font-family:K;font-style:normal;font-size:44px;color:{GELB}}}
.paket b{{font-family:A;font-weight:400;font-size:74px;color:#fff;line-height:1;white-space:nowrap}}
.paket u{{text-decoration:none;font-size:25px;color:#fff;line-height:1.15;text-align:left}}
.sub{{position:absolute;left:0;top:992px;width:1080px;text-align:center;font-size:30px;font-weight:700;color:{TXT}}}
.sub span{{color:{ROT}}}
.food{{position:absolute;left:54px;top:1046px;width:972px;display:flex;gap:16px}}
.f{{position:relative;width:231px;height:150px;border-radius:18px;overflow:hidden;border:4px solid #fff;box-shadow:0 6px 16px rgba(60,20,10,.22)}}
.f img{{width:100%;height:100%;object-fit:cover;display:block}}
.f span{{position:absolute;left:0;right:0;bottom:0;padding:16px 0 5px;text-align:center;color:#fff;font-size:21px;font-weight:700;background:linear-gradient(to top,rgba(30,15,10,.82),rgba(30,15,10,0))}}
.foot{{position:absolute;left:0;top:1254px;width:1080px;height:96px;background:{ROST};display:flex;align-items:center;justify-content:center;gap:28px;color:#fff;font-size:35px;font-weight:700}}
.foot em{{font-family:A;font-style:normal;font-weight:400;font-size:42px;color:{GELB};letter-spacing:1px}}
.line{{position:absolute;left:0;top:1209px;width:1080px;text-align:center;font-size:24px;color:{TXT}}}
</style></head><body>
<div class="head"><div class="hook">Na, Hunger? Endlich da:</div><div class="tit">MEINE REZEPTBÜCHER</div></div>
<img class="cov c1" src="file://{V}/cover-weihnachten.jpg"><img class="cov c2" src="file://{V}/cover-wohlfuehlkueche.jpg">
<div class="einzel" style="left:112px"><b>9,99 €</b></div><div class="einzel" style="left:584px"><b>9,99 €</b></div>
<div class="paket"><i>beide zusammen</i><b>14,99 €</b><u>4,99 €<br>gespart</u></div>
<div class="sub">72 Rezepte, <span>alle in leicht</span></div>
<div class="food">{food}</div>
<div class="line">Plätzchen, Stollen &amp; Co. ab 30 kcal pro Stück · Hauptgerichte unter 500 kcal</div>
<div class="foot">Sofort als PDF · Link im 1. Kommentar <em>FITMITKEV</em></div>
</body></html>'''
async def main():
    open(D+'/promo.html','w').write(HTML)
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
        await pg.goto('file://'+D+'/promo.html'); await pg.wait_for_timeout(500)
        await pg.screenshot(path=D+'/promo.png'); await b.close()
    Image.open(D+'/promo.png').convert('RGB').save(D+'/Promo-Rezeptbuecher-v2.jpg',quality=93)
asyncio.run(main())
