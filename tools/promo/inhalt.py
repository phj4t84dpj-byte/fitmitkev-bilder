# -*- coding: utf-8 -*-
# Facebook-Werbebeitrag „Was steckt drin?“ – Inhaltsverzeichnis beider Rezeptbücher als 2 Bilder (1080x1350 @2x), im Look der Bücher
import os, asyncio
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__)); F=os.path.abspath(D+'/../fonts/gf/ofl'); V='/home/claude/fitmitkev-bilder/verkaufsseite'
B={
'weihnachten':dict(titel='Weihnachtsbäckerei<br>in leicht',cover='cover-weihnachten.jpg',farbe='#8C1C24',dunkel='#6E1017',akzent='#1E4A3A',gold='#C9A24B',
  zeile='36 süße Rezepte für den Advent',
  kap=[('Plätzchen & Lebkuchen',['Vanillekipferl','Zimtsterne','Spekulatius','Butterplätzchen','Kokosmakronen','Pfeffernüsse','Elisenlebkuchen','Aachener Printen','Mandelhörnchen','Zimt-Schoko-Knusperhäufchen','Rumkugeln']),
       ('Kuchen & Stollen',['Skyr-Kuchen mit Spekulatius','Baumkuchen','Nussecken','Skyr-Stollen ohne Hefe','Zimtschnecken-Kuchen','Glühweinkuchen','Bratapfel-Kuchen','Spekulatius-Biskuitrolle','Eierlikör-Gugelhupf','Eierlikör-Torte']),
       ('Wie vom Weihnachtsmarkt, ohne Fritteuse',['Quarkbällchen','Mutzenmandeln','Eierlikör-Berliner','Spritzkuchen','Crêpes mit Zimt']),
       ('Desserts & Bowls',['Spekulatius-Tiramisu im Glas','Bratapfel-Dessert im Glas','Lebkuchen-Mousse','Spekulatius-Eis','Stollen-Bowl','Lebkuchen-Bowl']),
       ('Adventsfrühstück',['Lebkuchen-Pancakes','Spekulatius-Overnight-Oats']),
       ('Zum Verschenken',['Eierlikör','Spekulatius-Creme'])],
  split=2),
'wohlfuehl':dict(titel='Wohlfühlküche<br>in leicht',cover='cover-wohlfuehlkueche.jpg',farbe='#A2462B',dunkel='#7E3420',akzent='#1F4E5A',gold='#D9A23A',
  zeile='36 herzhafte Gerichte, alle unter 500 kcal pro Portion',
  kap=[('Lasagne & Aufläufe',['Lasagne','Kartoffel-Hack-Auflauf','Hähnchen-Nudelauflauf','Gnocchi-Auflauf','Cordon-Bleu-Auflauf','Blumenkohl-Auflauf','Kartoffelgratin','Moussaka','Käsespätzle','Schupfnudel-Auflauf']),
       ('Omas Klassiker',['Königsberger Klopse','Frikadellen mit Rahmsoße','Rinderrouladen mit Rotkohl','Rindergulasch mit Spätzle','Hackbraten mit Käsekern','Jägerschnitzel','Schnitzel mit Kartoffelsalat','Hühnerfrikassee','Bratwurst mit Sauerkraut','Gefüllte Paprika','Züricher Geschnetzeltes']),
       ('Suppen aus einem Topf',['Käse-Lauch-Suppe','Hühnersuppe','Kartoffelsuppe','Kürbissuppe','Lasagne-Suppe']),
       ('Schnell aus der Pfanne',['Butter Chicken','Paprika-Rahmhähnchen','Cheeseburger-Pfanne','Gnocchi-Pfanne mit Hähnchen','Hackbällchen in Tomatensoße']),
       ('Fürs Sofa',['Salami-Pizza','Flammkuchen','Chicken Nuggets','Fischstäbchen mit Püree','Döner im Skyr-Fladenbrot'])],
  split=2),
}
def page(b):
    n=sum(len(x) for _,x in b['kap']); assert n==36,n
    def block(k,items): return f'<div class="k"><h3>{k.replace("&","&amp;")}</h3><ul>'+''.join(f'<li>{i}</li>' for i in items)+'</ul></div>'
    L=b['kap'][:b['split']]; R=b['kap'][b['split']:]
    return f'''<html><head><style>
@font-face{{font-family:A;src:url(file://{F}/anton/Anton-Regular.ttf)}}
@font-face{{font-family:K;src:url(file://{F}/kaushanscript/KaushanScript-Regular.ttf)}}
@font-face{{font-family:P;src:url(file://{F}/poppins/Poppins-Regular.ttf);font-weight:400}}
@font-face{{font-family:P;src:url(file://{F}/poppins/Poppins-SemiBold.ttf);font-weight:600}}
@font-face{{font-family:P;src:url(file://{F}/poppins/Poppins-Bold.ttf);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#FBF5EA;font-family:P;color:#2B2A2A;overflow:hidden;position:relative}}
.top{{background:{b['farbe']};height:330px;position:relative;border-bottom:8px solid {b['gold']};padding:44px 0 0 330px;color:#fff}}
.cover{{position:absolute;left:66px;top:30px;width:196px;border-radius:6px;transform:rotate(-3deg);box-shadow:0 14px 28px rgba(0,0,0,.35);border:3px solid #fff}}
.k1{{font-family:K;font-size:52px;color:{b['gold']};line-height:1}}
.t{{font-family:A;font-size:76px;line-height:1.02;text-transform:uppercase;margin-top:10px}}
.z{{font-size:26px;font-weight:600;margin-top:12px;color:#F6E7D6}}
.cols{{display:flex;gap:44px;padding:40px 56px 0 56px}}
.col{{flex:1;display:flex;flex-direction:column;gap:22px}}
h3{{font-family:A;font-weight:400;font-size:32px;text-transform:uppercase;color:{b['farbe']};letter-spacing:.5px;line-height:1.05;border-bottom:3px solid {b['gold']};padding-bottom:6px;margin-bottom:8px}}
ul{{list-style:none}} li{{font-size:24px;line-height:1.42;padding-left:24px;position:relative}}
li::before{{content:"";position:absolute;left:2px;top:15px;width:10px;height:10px;border-radius:50%;background:{b['akzent']}}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:120px;background:{b['akzent']};color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 56px}}
.foot b{{font-family:A;font-weight:400;font-size:44px;letter-spacing:.5px}}
.foot span{{font-size:25px;font-weight:600;text-align:right;line-height:1.3}}
</style></head><body>
<div class="top"><img class="cover" src="file://{V}/{b['cover']}"><div class="k1">Was steckt drin?</div><div class="t">{b['titel']}</div><div class="z">{b['zeile']}</div></div>
<div class="cols"><div class="col">{''.join(block(k,i) for k,i in L)}</div><div class="col">{''.join(block(k,i) for k,i in R)}</div></div>
<div class="foot"><b>9,99 € · beide 14,99 €</b><span>Sofort als PDF<br>Link im 1. Kommentar</span></div>
</body></html>'''
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch(); pg=await br.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
        for k,b in B.items():
            open(f'{D}/{k}.html','w').write(page(b)); await pg.goto(f'file://{D}/{k}.html'); await pg.wait_for_timeout(500)
            bot=await pg.evaluate("Math.max(...[...document.querySelectorAll('.col')].map(e=>e.getBoundingClientRect().bottom))")
            print(k,'Spalten bis',round(bot),'(Fuß ab 1230)')
            await pg.screenshot(path=f'{D}/Buch-Inhalt-{k}.png')
        await br.close()
asyncio.run(main())
