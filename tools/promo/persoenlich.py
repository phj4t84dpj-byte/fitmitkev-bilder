# Persönlicher Buch-Beitrag Mo 16.11., 19:15 (Kevs Grund: „Viele haben danach gefragt“) – Vorher-Nachher-Foto + beide Cover, Farben wie die Promo
import asyncio, os
from playwright.async_api import async_playwright
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__)); F=os.path.join(D,'..','..','..','..','tmp')
F='/tmp/claude-0/-home-claude/62a14d94-6bfc-5e5c-b2da-15988fbe030e/scratchpad/fonts/gf/ofl'
R='/home/claude/fitmitkev-bilder'; V=R+'/verkaufsseite'
ROT='#8b1c23'; CREME='#fcf6ea'; GOLD='#c8a34b'; GRUEN='#22483b'; ROST='#a1462b'; TXT='#292929'; GELB='#f3c969'
HTML=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:A;src:url("file://{F}/anton/Anton-Regular.ttf")}}
@font-face{{font-family:K;src:url("file://{F}/kaushanscript/KaushanScript-Regular.ttf")}}
@font-face{{font-family:P;font-weight:600;src:url("file://{F}/poppins/Poppins-SemiBold.ttf")}}
@font-face{{font-family:P;font-weight:700;src:url("file://{F}/poppins/Poppins-Bold.ttf")}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{CREME};font-family:P;font-weight:600;color:{TXT};position:relative;overflow:hidden}}
.head{{position:absolute;left:0;top:0;width:1080px;height:214px;background:{ROT};border-bottom:8px solid {GOLD};text-align:center}}
.hook{{font-family:K;font-size:54px;color:{GELB};margin-top:8px;transform:rotate(-2deg)}}
.tit{{font-family:A;font-size:96px;color:#fff;line-height:1;margin-top:6px;letter-spacing:1px}}
.foto{{position:absolute;left:0;top:222px;width:1080px;height:640px;overflow:hidden;border-bottom:8px solid {GOLD}}}
.foto img{{width:1080px;position:absolute;top:-40px;left:0}}
.lab{{position:absolute;top:796px;background:rgba(18,33,63,.88);color:#fff;font-family:A;font-size:40px;padding:4px 22px;border-radius:12px}}
.badge{{position:absolute;left:470px;top:250px;width:140px;height:140px;border-radius:50%;background:#c1202b;border:6px solid #fff;color:#fff;font-family:A;font-size:44px;display:flex;align-items:center;justify-content:center;transform:rotate(-8deg);box-shadow:0 8px 18px rgba(0,0,0,.3)}}
.cov{{position:absolute;top:900px;width:206px;border-radius:5px;box-shadow:0 14px 26px rgba(60,20,10,.32)}}
.c1{{left:56px;transform:rotate(-4deg)}} .c2{{left:250px;transform:rotate(3deg)}}
.txt{{position:absolute;left:505px;top:912px;width:540px}}
.txt h2{{font-family:A;font-weight:400;font-size:62px;line-height:1.02;color:{ROT}}}
.txt p{{font-size:29px;line-height:1.3;margin-top:12px}}
.txt .preis{{display:inline-block;margin-top:16px;background:{GRUEN};color:#fff;border:4px solid {GOLD};border-radius:40px;padding:6px 26px;font-weight:700;font-size:30px}}
.foot{{position:absolute;left:0;top:1254px;width:1080px;height:96px;background:{ROST};display:flex;align-items:center;justify-content:center;color:#fff;font-size:38px;font-weight:700}}
</style></head><body>
<div class="head"><div class="hook">Ihr habt so oft danach gefragt:</div><div class="tit">MEINE REZEPTE ALS BUCH</div></div>
<div class="foto"><img src="file://{R}/misc/Kev-Vorher-Nachher-Hochzeit.jpg"></div>
<div class="badge">-50 kg</div>
<div class="lab" style="left:40px">FRÜHER: 130 KG</div><div class="lab" style="left:760px">HEUTE</div>
<img class="cov c1" src="file://{V}/cover-weihnachten.jpg"><img class="cov c2" src="file://{V}/cover-wohlfuehlkueche.jpg">
<div class="txt"><h2>72 REZEPTE,<br>DIE ICH SELBST ESSE</h2><p>Plätzchen, Stollen, Aufläufe und Braten wie bei Oma. Nur leichter.</p><div class="preis">je 9,99 € · beide 14,99 €</div></div>
<div class="foot">Sofort als PDF · Link im 1. Kommentar</div>
</body></html>'''
async def main():
    open(D+'/persoenlich.html','w').write(HTML)
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
        await pg.goto('file://'+D+'/persoenlich.html'); await pg.wait_for_timeout(500)
        await pg.screenshot(path=D+'/p.png'); await b.close()
    Image.open(D+'/p.png').convert('RGB').save(V+'/Buch-Persoenlich.jpg',quality=93); os.remove(D+'/p.png'); os.remove(D+'/persoenlich.html')
asyncio.run(main())
