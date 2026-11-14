# Buch-Beitrag Sonntag 15.11.: "Ein Blick ins Buch" (Facebook 4:5) – drei echte Buchseiten, gleiche Farben wie das Promo-Bild
import asyncio, os
from playwright.async_api import async_playwright
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__)); F=os.path.join(D,'..','fonts','gf','ofl'); V='/home/claude/fitmitkev-bilder/verkaufsseite'
ROT='#8b1c23'; CREME='#fcf6ea'; GOLD='#c8a34b'; GRUEN='#22483b'; ROST='#a1462b'; TXT='#292929'; GELB='#f3c969'
HAKEN='<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#22483b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
PUNKTE=['Jedes Rezept auf einer eigenen Seite, mit Foto','Zutaten zum Abhaken, Schritte in großer Schrift','Kalorien und Eiweiß pro Stück oder Portion']
pk=''.join(f'<div class="p"><span>{HAKEN}</span>{t}</div>' for t in PUNKTE)
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
.s{{position:absolute;border-radius:8px;box-shadow:0 18px 36px rgba(60,20,10,.34);border:3px solid #fff}}
.l{{left:36px;top:338px;width:384px;transform:rotate(-6deg)}}
.r{{left:660px;top:338px;width:384px;transform:rotate(6deg)}}
.m{{left:305px;top:262px;width:470px;z-index:2;box-shadow:0 22px 44px rgba(60,20,10,.42)}}
.pk{{position:absolute;left:0;top:958px;width:1080px;display:flex;flex-direction:column;align-items:center;gap:9px;z-index:3}}
.p{{display:flex;align-items:center;gap:14px;font-size:29px;font-weight:700;color:{TXT}}}
.p span{{flex:0 0 38px;height:38px;border-radius:50%;background:{GELB};display:flex;align-items:center;justify-content:center}}
.preis{{position:absolute;left:150px;top:1128px;width:780px;height:92px;background:{GRUEN};border:5px solid {GOLD};border-radius:50px;display:flex;align-items:center;justify-content:center;gap:20px;box-shadow:0 10px 22px rgba(20,40,30,.28);z-index:3}}
.preis i{{font-family:K;font-style:normal;font-size:40px;color:{GELB}}}
.preis b{{font-family:A;font-weight:400;font-size:62px;color:#fff;line-height:1;white-space:nowrap}}
.preis u{{text-decoration:none;font-size:23px;color:#fff;line-height:1.15;text-align:left}}
.foot{{position:absolute;left:0;top:1254px;width:1080px;height:96px;background:{ROST};display:flex;align-items:center;justify-content:center;gap:28px;color:#fff;font-size:35px;font-weight:700}}
.foot em{{font-family:A;font-style:normal;font-weight:400;font-size:42px;color:{GELB};letter-spacing:1px}}
</style></head><body>
<div class="head"><div class="hook">Meine Rezeptbücher:</div><div class="tit">EIN BLICK INS BUCH</div></div>
<img class="s l" src="file://{V}/seite-lasagne.jpg"><img class="s r" src="file://{V}/seite-erythrit.jpg"><img class="s m" src="file://{V}/seite-skyr-kuchen.jpg">
<div class="pk">{pk}</div>
<div class="preis"><i>72 Rezepte</i><b>14,99 €</b><u>beide Bücher<br>einzeln je 9,99 €</u></div>
<div class="foot">Sofort als PDF · Link im 1. Kommentar <em>FITMITKEV</em></div>
</body></html>'''
async def main():
    open(D+'/blick.html','w').write(HTML)
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
        await pg.goto('file://'+D+'/blick.html'); await pg.wait_for_timeout(500)
        await pg.screenshot(path=D+'/blick.png'); await b.close()
    Image.open(D+'/blick.png').convert('RGB').save(D+'/Buch-Blick-ins-Buch.jpg',quality=93)
    Image.open(D+'/blick.png').convert('RGB').resize((540,675)).save(D+'/_blick_klein.jpg',quality=88)
asyncio.run(main())
