# Stories zum Buch-Start (9:16, 1080 x 1920): 1 Start, 2 Blick ins Buch, 3 Gerichte. Jede steht für sich und hat ein freies Feld für den Link-Sticker.
import asyncio, os
from playwright.async_api import async_playwright
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__)); F=os.path.join(D,'..','fonts','gf','ofl'); V='/home/claude/fitmitkev-bilder/verkaufsseite'
ROT='#8b1c23'; CREME='#fcf6ea'; GOLD='#c8a34b'; GRUEN='#22483b'; ROST='#a1462b'; TXT='#292929'; GELB='#f3c969'
XMP=b'''<?xpacket begin="\xef\xbb\xbf" id="W5M0MpCehiHzreSzNTczkc9d"?><x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description rdf:about="" xmlns:Iptc4xmpExt="http://iptc.org/std/Iptc4xmpExt/2008-02-29/" xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/" Iptc4xmpExt:DigitalSourceType="http://cv.iptc.org/newscodes/digitalsourcetype/compositeWithTrainedAlgorithmicMedia" photoshop:Credit="Fitmitkev"/></rdf:RDF></x:xmpmeta><?xpacket end="w"?>'''
PFEIL='<svg width="54" height="64" viewBox="0 0 54 64" fill="none" stroke="#8b1c23" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"><path d="M27 6v48M8 36l19 20 19-20"/></svg>'
HAKEN='<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#22483b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
CSS=f'''
@font-face{{font-family:A;src:url("file://{F}/anton/Anton-Regular.ttf")}}
@font-face{{font-family:K;src:url("file://{F}/kaushanscript/KaushanScript-Regular.ttf")}}
@font-face{{font-family:P;font-weight:600;src:url("file://{F}/poppins/Poppins-SemiBold.ttf")}}
@font-face{{font-family:P;font-weight:700;src:url("file://{F}/poppins/Poppins-Bold.ttf")}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:{CREME};font-family:P;font-weight:600;color:{TXT};position:relative;overflow:hidden}}
.head{{position:absolute;left:0;top:0;width:1080px;height:600px;background:{ROT};border-bottom:10px solid {GOLD};text-align:center;padding-top:236px}}
.hook{{font-family:K;font-size:70px;color:{GELB};transform:rotate(-2deg);line-height:1.1}}
.tit{{font-family:A;font-size:132px;color:#fff;line-height:1.02;margin-top:10px;letter-spacing:1px}}
.cov{{position:absolute;top:650px;width:410px;border-radius:8px;box-shadow:0 22px 40px rgba(60,20,10,.34)}}
.c1{{left:100px;transform:rotate(-3deg)}} .c2{{left:570px;transform:rotate(3deg)}}
.einzel{{position:absolute;top:1222px;width:410px;text-align:center}}
.einzel b{{display:inline-block;background:#fff;border:5px solid {GOLD};border-radius:44px;padding:4px 34px 6px;font-weight:700;font-size:42px;color:{ROT};box-shadow:0 6px 14px rgba(60,20,10,.18)}}
.paket{{position:absolute;left:90px;top:1318px;width:900px;height:118px;background:{GRUEN};border:6px solid {GOLD};border-radius:62px;display:flex;align-items:center;justify-content:center;gap:24px;box-shadow:0 10px 22px rgba(20,40,30,.28)}}
.paket i{{font-family:K;font-style:normal;font-size:50px;color:{GELB}}}
.paket b{{font-family:A;font-weight:400;font-size:84px;color:#fff;line-height:1;white-space:nowrap}}
.paket u{{text-decoration:none;font-size:28px;color:#fff;line-height:1.15;text-align:left}}
.link{{position:absolute;left:0;top:1462px;width:1080px;display:flex;flex-direction:column;align-items:center;gap:6px}}
.link .z{{display:flex;align-items:center;gap:18px;font-size:38px;font-weight:700;color:{ROT}}}
.feld{{width:640px;height:118px;border:5px dashed {GOLD};border-radius:26px;background:rgba(255,255,255,.75)}}
.fuss{{position:absolute;left:0;top:1700px;width:1080px;height:220px;background:{ROST};text-align:center;padding-top:22px;font-family:A;font-size:44px;letter-spacing:2px;color:{GELB}}}
.s{{position:absolute;border-radius:10px;box-shadow:0 20px 40px rgba(60,20,10,.36);border:4px solid #fff}}
.l{{left:40px;top:722px;width:400px;transform:rotate(-6deg)}} .r{{left:640px;top:722px;width:400px;transform:rotate(6deg)}}
.m{{left:292px;top:640px;width:496px;z-index:2;box-shadow:0 24px 48px rgba(60,20,10,.45)}}
.pk{{position:absolute;left:0;top:1366px;width:1080px;display:flex;flex-direction:column;align-items:center;gap:6px;z-index:3}}
.p{{display:flex;align-items:center;gap:14px;font-size:32px;font-weight:700}}
.p span{{flex:0 0 42px;height:42px;border-radius:50%;background:{GELB};display:flex;align-items:center;justify-content:center}}
.grid{{position:absolute;left:70px;top:650px;width:940px;display:grid;grid-template-columns:1fr 1fr;gap:20px}}
.f{{position:relative;height:372px;border-radius:22px;overflow:hidden;border:5px solid #fff;box-shadow:0 8px 18px rgba(60,20,10,.24)}}
.f img{{width:100%;height:100%;object-fit:cover;display:block}}
.f div{{position:absolute;left:0;right:0;bottom:0;padding:44px 0 10px;text-align:center;color:#fff;background:linear-gradient(to top,rgba(30,15,10,.88),rgba(30,15,10,0))}}
.f div b{{display:block;font-size:30px;font-weight:700;line-height:1.15}}
.f div em{{font-style:normal;font-family:A;font-size:38px;color:{GELB};letter-spacing:.5px}}
.f div s{{font-family:P;font-size:22px;color:#e8d9c8;margin-left:8px}}
'''
def seite(inhalt): return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{inhalt}<div class="fuss">FITMITKEV</div></body></html>'
def linkfeld(top,text='Hier geht\'s zu den Büchern'): return f'<div class="link" style="top:{top}px"><div class="z">{text}{PFEIL}</div><div class="feld"></div></div>'
S1=seite(f'''<div class="head"><div class="hook">Na, Hunger? Endlich da:</div><div class="tit">MEINE<br>REZEPTBÜCHER</div></div>
<img class="cov c1" src="file://{V}/cover-weihnachten.jpg"><img class="cov c2" src="file://{V}/cover-wohlfuehlkueche.jpg">
<div class="einzel" style="left:100px"><b>9,99 €</b></div><div class="einzel" style="left:570px"><b>9,99 €</b></div>
<div class="paket"><i>beide zusammen</i><b>14,99 €</b><u>4,99 €<br>gespart</u></div>'''+linkfeld(1462))
PUNKTE=['Jedes Rezept auf einer eigenen Seite','Zutaten zum Abhaken, große Schrift']
S2=seite(f'''<div class="head"><div class="hook">Meine Rezeptbücher:</div><div class="tit">EIN BLICK<br>INS BUCH</div></div>
<img class="s l" src="file://{V}/seite-lasagne.jpg"><img class="s r" src="file://{V}/seite-erythrit.jpg"><img class="s m" src="file://{V}/seite-skyr-kuchen.jpg">
<div class="pk">'''+''.join(f'<div class="p"><span>{HAKEN}</span>{t}</div>' for t in PUNKTE)+'</div>'+linkfeld(1466,'72 Rezepte · ab 9,99 €'))
FOOD=[('skyr-kuchen','Skyr-Kuchen mit Spekulatius','125 kcal','380'),('quarkbaellchen','Quarkbällchen ohne Fritteuse','65 kcal','150'),('lasagne','Lasagne in leicht','340 kcal','750'),('rouladen','Rouladen mit Rotkohl','375 kcal','850')]
S3=seite(f'''<div class="head"><div class="hook">Meine Rezeptbücher:</div><div class="tit">72 REZEPTE,<br>ALLE IN LEICHT</div></div>
<div class="grid">'''+''.join(f'<div class="f"><img src="file://{V}/{k}.jpg"><div><b>{n}</b><em>{c}</em><s>statt {v}</s></div></div>' for k,n,c,v in FOOD)+'</div>'+linkfeld(1470,'Beide Bücher zusammen 14,99 €'))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920},device_scale_factor=1)
        for name,h in (('Story-1-Start',S1),('Story-2-Blick-ins-Buch',S2),('Story-3-Gerichte',S3)):
            open(f'{D}/{name}.html','w').write(h); await pg.goto(f'file://{D}/{name}.html'); await pg.wait_for_timeout(500)
            await pg.screenshot(path=f'{D}/{name}.png')
            Image.open(f'{D}/{name}.png').convert('RGB').save(f'{D}/{name}.jpg',quality=94,xmp=XMP)
        await b.close()
asyncio.run(main())
