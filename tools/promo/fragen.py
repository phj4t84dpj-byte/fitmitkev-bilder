# Buch-Beitrag Di 17.11., 19:15 „Eure Fragen zu den Büchern“ – 4 Fragen mit Antwort + beide Cover, Farben wie die Promo (Vorlage persoenlich.py)
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
.qa{{position:absolute;left:40px;width:640px;background:#fff;border-radius:22px;border:3px solid {GOLD};padding:18px 26px 20px;box-shadow:0 8px 20px rgba(80,40,10,.14)}}
.q{{font-family:K;font-size:40px;color:{ROT};line-height:1.15}}
.a{{font-size:28px;line-height:1.3;margin-top:6px}}
.a b{{color:{GRUEN};font-weight:700}}
.cov{{position:absolute;width:300px;border-radius:6px;box-shadow:0 16px 30px rgba(60,20,10,.32)}}
.c1{{left:722px;top:270px;transform:rotate(4deg)}} .c2{{left:740px;top:720px;transform:rotate(-3deg)}}
.foot{{position:absolute;left:0;top:1254px;width:1080px;height:96px;background:{ROST};display:flex;align-items:center;justify-content:center;color:#fff;font-size:38px;font-weight:700}}
</style></head><body>
<div class="head"><div class="hook">Ihr habt gefragt, ich antworte:</div><div class="tit" style="font-size:80px;margin-top:14px">EURE FRAGEN ZU DEN BÜCHERN</div></div>
<div class="qa" style="top:262px"><div class="q">„Ist das ein gedrucktes Buch?“</div><div class="a">Nein, du bekommst beide Bücher <b>sofort als PDF</b>. Für Handy und Tablet oder zum Ausdrucken.</div></div>
<div class="qa" style="top:510px"><div class="q">„Stehen die Kalorien dabei?“</div><div class="a">Ja, bei jedem Rezept <b>kcal und Eiweiß pro Portion</b>, dazu eine Zutatenliste zum Abhaken.</div></div>
<div class="qa" style="top:758px"><div class="q">„Brauche ich besondere Zutaten?“</div><div class="a">Nein, alles gibt es <b>im normalen Supermarkt</b>: Skyr, Quark, Dinkelmehl, Erythrit.</div></div>
<div class="qa" style="top:1006px"><div class="q">„Was kosten die Bücher?“</div><div class="a">Je <b>9,99 €</b>, beide zusammen <b>14,99 €</b>. Je 36 Rezepte, also 72 insgesamt.</div></div>
<img class="cov c1" src="file://{V}/cover-weihnachten.jpg"><img class="cov c2" src="file://{V}/cover-wohlfuehlkueche.jpg">
<div class="foot">Noch eine Frage? Schreib sie in die Kommentare ⤵️</div>
</body></html>'''
async def main():
    open(D+'/fragen.html','w').write(HTML)
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
        await pg.goto('file://'+D+'/fragen.html'); await pg.wait_for_timeout(500)
        await pg.screenshot(path=D+'/p.png'); await b.close()
    Image.open(D+'/p.png').convert('RGB').save(V+'/Buch-Fragen.jpg',quality=93); os.remove(D+'/p.png'); os.remove(D+'/fragen.html')
asyncio.run(main())
