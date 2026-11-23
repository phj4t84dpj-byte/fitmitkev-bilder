# -*- coding: utf-8 -*-
# G101 – Dienstag 24.11.2026. Morgen-Check Mo 23.11.: Sonntag 1.137.401 Aufrufe (erster Tag über 1 Mio. der Woche) → Stufenplan bleibt bei 22.
# 19 Rezepte + 2 feste (6:10 ESN-Rezept Tiramisu im Glas, 13:00 ESN-Rezept Cheesecake im Glas, beide schon eingeplant, ohne ESN-Zeile) + Buch-Beitrag 20:15.
# 4 neue Rezepte:
#   KlossJaeger         – Kloßteig-Reihe, Idee 9; dazu Mitbewerber-Check 23.11.: Jägerschnitzel bei Leckeria +1,7-fach seit gestern, Semmelknödel mit Lauchsoße 1,7-fach.
#   KlossSauerbraten    – Kloßteig-Reihe, Idee 1 (Sauerbraten mit Klößen lief bei Leckeria am 20.11. 8,5-fach).
#   EierlikoerWoelkchen – Mitbewerber-Check 23.11.: „Winterwölkchen“ 5.566 (10,8-fach), „Eierlikör Wölkchen“ 877 nach 20 h (1,7-fach) bei „Unsere Weihnachtsbäckerei“;
#                         unsere Quark-Wölkchen (So 22.11.) 14.331 = 1,2-fach, Kokos-Wölkchen laufen Mo 23.11.
#   Buletten            – Mitbewerber-Check 22./23.11.: „Buletten mit Speck-Kartoffelsalat“ bei Leckeria 5,3-fach; hier mit magerem Hack und warmem Brühe-Kartoffelsalat.
# Dazu aus der Kloßteig-Reihe das fertige, von Kev am 22.11. freigegebene Board „Klöße mit Tomate-Mozzarella überbacken“ (tools/g100, Key KlossTomMozz).
# 14 Wiederholer (7-Tage-Regel vom Di 17.11. und ausgeruhte Treffer; mit g101/lauf.py gegen alle Läufe seit 9.11. geprüft) stehen mit Uhrzeiten in plan101.py.
import sys, os
_D=os.path.dirname(os.path.abspath(__file__))
for g in ('g87','g88','g89','g90','g91','g92','g93','g93n','g99'): sys.path.insert(0, os.path.join(_D, '..', g))
from g90_data import NUT, PIECE, nut, Z, macros4
for _k,_v in {'kloesse':(105,2,22.5,0.5), 'rind':(120,21,0,4), 'semmelbroesel':(350,10,70,2)}.items(): NUT.setdefault(_k,_v)
KLOESSE4='exactly four small round pale yellow matte German potato dumplings, each about the size of a golf ball, lying close together in a group, all four clearly visible'
TELLER='A round white dinner plate, the whole plate fully visible with empty table space left and right of it, with '
NEU=dict(
 KlossJaeger=dict(key='KlossJaeger', suess=False, hook='Klöße mit', titel=['JÄGER-','SCHNITZEL'], portion='pro Portion', anzahl=4, vs=850,
  zutaten=[Z('500 g','Hähnchenbrust','haehnchenbrust','haehnchen',500), Z('500 g','Kloßteig (Kühlregal)','kartoffelkloesse','kloesse',500), Z('400 g','Champignons','champignons','champignons',400),
           Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1), Z('150 ml','Kochsahne (15 %)','kochsahne','kochsahne',150), Z('300 ml','Gemüsebrühe','gemuesebruehe','bruehe',0),
           Z('1 EL','Tomatenmark','tomatenmark','tomatenmark',15), Z('1 EL','Speisestärke','speisestaerke','speisestaerke',10)],
  ex=['1 EL Öl, 1 TL Paprikapulver', 'Salz, Pfeffer, Petersilie'], exnut=[(90,0,0,10)],
  intro='Jägerschnitzel wie im Gasthaus, nur ohne Panade und ohne schwere Sahnesoße: zarte Hähnchenschnitzel in Pilzrahmsoße mit vielen Champignons. Dazu Klöße aus fertigem Kloßteig, die jede Soße aufnehmen. In 30 Minuten fertig: {k} kcal und {p} g Eiweiß pro Teller statt 850 im Gasthaus!',
  schritte=['Aus dem Kloßteig 16 kleine Klöße formen (4 pro Teller) und nach Packungsangabe in siedendem Salzwasser gar ziehen lassen (ca. 15 Minuten).',
            'Die Hähnchenbrust waagerecht in 4 dünne Schnitzel schneiden, salzen, pfeffern und im heißen Öl von jeder Seite 3–4 Minuten goldbraun braten. Herausnehmen.',
            'Die Zwiebel würfeln, die Champignons in Scheiben schneiden und beides in derselben Pfanne 6 Minuten kräftig anbraten. Tomatenmark und Paprikapulver kurz mitrösten, mit Brühe und Kochsahne ablöschen und 5 Minuten köcheln lassen. Die Speisestärke in 2 EL kaltem Wasser anrühren, einrühren und kurz aufkochen.',
            'Die Schnitzel in die Soße legen, 2 Minuten heiß werden lassen und mit den Klößen und gehackter Petersilie servieren.'],
  frage='Jägerschnitzel: paniert oder natur?', tags='#jägerschnitzel #pilzrahmsoße #klöße #omasrezepte #fitmitkev',
  prompt=TELLER+'one thin flat pan-seared natural chicken breast fillet without any breading, its surface smooth and glossy golden brown like grilled chicken breast, half covered with a creamy light brown mushroom cream sauce with many sliced browned mushrooms, sprinkled with fresh chopped green parsley, and beside it on the same plate '+KLOESSE4+'.'),   # Job-Schlüssel KlossJaegerB, Seed 14 (erster Prompt malte das Schnitzel paniert)
 KlossSauerbraten=dict(key='KlossSauerbraten', suess=False, hook='Klöße mit', titel=['SCHNELLEM','SAUERBRATEN'], portion='pro Portion', anzahl=4, vs=900,
  zutaten=[Z('500 g','Rinderhüfte (mager)','rinderbraten','rind',500), Z('500 g','Kloßteig (Kühlregal)','kartoffelkloesse','kloesse',500), Z('2 Stück','Zwiebeln','zwiebeln','zwiebel',st=2),
           Z('400 ml','Rinderbrühe','rinderbruehe','bruehe',0), Z('30 g','Rosinen','rosinen','rosinen',30), Z('1 EL','Tomatenmark','tomatenmark','tomatenmark',15),
           Z('1 TL','Lebkuchengewürz','lebkuchengewuerz','vanille',0), Z('1 EL','Speisestärke','speisestaerke','speisestaerke',10)],
  ex=['4 EL Rotweinessig, 1 EL Öl, 2 Lorbeerblätter', 'Salz, Pfeffer, 2 TL Erythrit, Petersilie'], exnut=[(90,0,0,10)],
  intro='Sauerbraten ohne tagelanges Einlegen: Dünne Scheiben vom Rind kommen nur kurz in die Pfanne, die süß-saure Soße mit Rosinen und Lebkuchengewürz kocht in 15 Minuten. Schmeckt wie sonntags bei Oma und steht in 40 Minuten auf dem Tisch. Dazu Klöße aus fertigem Kloßteig: {k} kcal und {p} g Eiweiß pro Teller statt 900 im Gasthaus!',
  schritte=['Die Rinderhüfte quer zur Faser in dünne Scheiben schneiden, die Zwiebeln in Ringe. Das Fleisch im heißen Öl portionsweise 1–2 Minuten scharf anbraten und herausnehmen.',
            'Die Zwiebeln in derselben Pfanne 5 Minuten bräunen, das Tomatenmark kurz mitrösten. Mit Essig und Brühe ablöschen, Lorbeer, Rosinen und Lebkuchengewürz zugeben und 15 Minuten köcheln lassen. Die Speisestärke in 2 EL kaltem Wasser anrühren, einrühren, kurz aufkochen und mit Salz, Pfeffer und Erythrit süß-sauer abschmecken.',
            'Aus dem Kloßteig 16 kleine Klöße formen (4 pro Teller) und nach Packungsangabe in siedendem Salzwasser gar ziehen lassen (ca. 15 Minuten). Das Fleisch in der Soße 2 Minuten heiß werden lassen und mit den Klößen und etwas Petersilie servieren.'],
  frage='Sauerbraten: mit Rosinen oder ohne?', tags='#sauerbraten #klöße #fitmitkev',
  prompt=TELLER+'thin slices of tender braised beef in a glossy dark brown sweet-and-sour gravy with a few dark raisins and soft browned onion rings, and beside it on the same plate '+KLOESSE4+', a little chopped green parsley on the dumplings.'),
 EierlikoerWoelkchen=dict(key='EierlikoerWoelkchen', suess=True, hook='Zergehen auf der Zunge:', titel=['EIERLIKÖR-','WÖLKCHEN'], portion='pro Stück', anzahl=36, vs=85,
  zutaten=[Z('150 g','Dinkelmehl','dinkelmehl','dinkelmehl',150), Z('80 g','Speisestärke','speisestaerke','speisestaerke',80), Z('60 g','Butter (weich)','butter','butter',60),
           Z('100 g','Magerquark','magerquark','quark',100), Z('80 ml','Eierlikör','eierlikoer','eierlikoer',80), Z('60 g','Erythrit','erythrit','erythrit',60), Z('1 Stück','Ei','ei','ei',st=1)],
  ex=['1 TL Backpulver, 1 TL Vanilleextrakt', '1 Prise Salz, Puder-Erythrit zum Bestäuben'], exnut=[],
  intro='Wölkchen, die auf der Zunge zergehen: außen zart, innen weich und mit einem Schuss Eierlikör. Der Teig ist in 10 Minuten gerührt, ausgerollt wird nichts. Quark und Speisestärke machen sie locker, so reichen 60 g Butter für 36 Stück: {k} kcal pro Wölkchen statt 85 für das klassische Eierlikör-Plätzchen!',
  schritte=['Die weiche Butter mit Erythrit, Ei und Vanille cremig rühren, dann Quark und Eierlikör unterrühren.',
            'Mehl, Speisestärke, Backpulver und Salz mischen und kurz unterrühren, bis ein weicher Teig entsteht. Mit zwei Teelöffeln 36 kleine Häufchen auf zwei Bleche mit Backpapier setzen.',
            'Bei 170 °C Ober-/Unterhitze 12–14 Minuten backen, die Wölkchen sollen hell bleiben. Abkühlen lassen und mit Puder-Erythrit bestäuben.'],
  frage='Eierlikör-Wölkchen oder Kokos-Wölkchen: Welche backst du zuerst?', tags='#wölkchen #eierlikör #fitmitkev',
  prompt='A white plate piled high with many small round pale cream-coloured soft cookies, each cookie a smooth slightly domed mound with fine cracks, thickly dusted with white powdered sugar, the bottoms pale golden, a few cookies lying on the table in front of the plate, one cookie broken in half showing the soft pale yellow crumb inside, a small glass of thick pale yellow egg liqueur beside the plate.'),
 Buletten=dict(key='Buletten', suess=False, hook='Wie in Berlin:', titel=['BULETTEN MIT','KARTOFFELSALAT'], portion='pro Portion', anzahl=4, vs=820,
  zutaten=[Z('500 g','Rinderhack (mager)','rinderhack','hack',500), Z('800 g','Kartoffeln','kartoffeln','kartoffeln',800), Z('2 Stück','Zwiebeln','zwiebeln','zwiebel',st=2),
           Z('1 Stück','Ei','ei','ei',st=1), Z('30 g','Semmelbrösel','semmelbroesel','semmelbroesel',30), Z('60 g','Putenschinken','putenschinken','putenschinken',60),
           Z('200 ml','Gemüsebrühe','gemuesebruehe','bruehe',0), Z('3 TL','Senf','senf','senf',15)],
  ex=['3 EL Essig, 1 EL Öl, Schnittlauch', 'Salz, Pfeffer, 1 TL Paprikapulver'], exnut=[(90,0,0,10)],
  intro='Buletten wie in Berlin, außen kross und innen saftig, dazu warmer Kartoffelsalat ohne Mayo: Die Kartoffeln ziehen in heißer Brühe mit Essig, Senf und Zwiebeln, statt Speck kommen knusprige Schinkenwürfel dazu. Zwei dicke Buletten und eine große Portion Salat: {k} kcal und {p} g Eiweiß pro Portion statt 820 in der Kneipe!',
  schritte=['Die Kartoffeln mit Schale 20–25 Minuten kochen, pellen und noch warm in grobe Würfel schneiden. Eine Zwiebel fein würfeln, den Schinken würfeln und beides in 1 TL Öl 4 Minuten anbraten. Mit Brühe und Essig ablöschen, 2 TL Senf einrühren, aufkochen und heiß über die Kartoffeln gießen. 15 Minuten ziehen lassen, mit Salz, Pfeffer und Schnittlauch abschmecken.',
            'Die zweite Zwiebel fein würfeln und mit Hack, Ei, Semmelbröseln, 1 TL Senf, Paprikapulver, Salz und Pfeffer verkneten. Mit nassen Händen 8 Buletten formen.',
            'Die Buletten im restlichen Öl bei mittlerer Hitze von jeder Seite 5–6 Minuten braten und mit dem warmen Kartoffelsalat servieren. Wer mag, gibt einen Klecks Senf dazu.'],
  frage='Buletten, Frikadellen oder Fleischpflanzerl: Wie heißen sie bei dir?', tags='#buletten #kartoffelsalat #fitmitkev',
  prompt=TELLER+'two thick round golden-brown pan-fried German meat patties with a crisp crust and beside them a large portion of warm potato salad made of sliced boiled potatoes glistening with broth, with small diced onions, tiny browned ham cubes and chopped green chives, a small dollop of yellow mustard on the rim of the plate.'),
)
for _k,_r in NEU.items(): _r['kurz']=['–','–','–']
R=[NEU['KlossJaeger'], NEU['KlossSauerbraten'], NEU['EierlikoerWoelkchen'], NEU['Buletten']]

if __name__=='__main__':
    for r in R:
        k,p,c,f=macros4(r); assert r['vs']>k and len(r['zutaten'])<=8 and k<=500, r['key']
        txt=r['intro']+' '.join(r['schritte'])+r['frage']
        for w in ('abnehm','esn ','melly','gta','ohne zucker','satt','miracel'): assert w not in txt.lower(), (r['key'],w)
        print(f"{r['key']:20s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P {c:3d}K {f:2d}F {r['portion']} × {r['anzahl']} vs {r['vs']}")
    print('ok')
