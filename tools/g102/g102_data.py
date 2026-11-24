# -*- coding: utf-8 -*-
# G102 – Mittwoch 25.11.2026. Morgen-Check Di 24.11.: Montag 1.299.579 Aufrufe (zweiter Tag über 1 Mio.) → Stufenplan bleibt bei 22.
# 19 Rezepte + 2 feste (6:10 ESN-Rezept Zimt-Grießbrei, 13:00 ESN-Rezept Schoko-Eis, beide schon eingeplant, ohne ESN-Zeile) + Buch-Beitrag 20:15.
#
# WIEDERHOLER-TEST (Kev 23.11.: „Ab Mittwoch testen“), Tag 1 von 4 (Mi 25.–Sa 28.11.):
#   Gruppe NEU – gleiches Rezept, gleiche Kalorien, gleicher 1. Kommentar, gleiche Hashtags, aber NEUES FOTO (anderer Blickwinkel / andere Anrichtung)
#                und NEUE Schreibschrift-Zeile; im Beitragstext ein anderes Emoji. Boards G102-<Key>-ohneBox.
#                MilchschnitteBowl, Gewuerzkuchen, BlitzKaesekuchen, Zupfkuchen (süß) · GyrosBowl, KaeseLauchSuppe (herzhaft)
#   Gruppe ALT – unverändert Board und Text vom letzten Lauf: Mutzen, Zimtsterne, ZimtschneckenSkyrKuchen, KokosMandelTiramisu (süß) ·
#                GebratenerReis, Gulasch, KoernerBroetchen (herzhaft). Stehen nur in plan102.py.
#   Die Gruppen sind nach der Stärke des letzten Laufs abwechselnd verteilt (süß: 25,9 / 14,7 / 14,7 / 9,7 / 3,2 / 2,9 / 2,3 / 1,3-fach).
#
# 6 neue Rezepte:
#   KlossKasseler   – Kloßteig-Reihe, Idee 5 (Kasseler mit Sauerkraut)
#   KlossScheiben   – Kloßteig-Reihe, Idee 19 (gebratene Kloßscheiben mit Schinken und Spiegelei)
#   KlossLauch      – Kloßteig-Reihe, Idee 16 (mit Schinken und Lauch überbacken; Idee 13 Pilzrahmsoße auf Donnerstag geschoben, weil am Di schon Jägerschnitzel in Pilzrahmsoße lief)
#   WinterWoelkchen – Mitbewerber-Check 24.11.: „Winterwölkchen“ 7.071 (14,1-fach); unsere Kokos-Wölkchen am Mo 23.11. 46.431 (5,3-fach). Gleicher Platz 10:20 wie Kokos (Mo) und Eierlikör (Di).
#   DoenerKartoffeln – Verwandter der Pizza-Kartoffeln (So 22.11., 73.793 = 4,1-fach) und des Döner-Kuchens (37.042 = 2,1-fach)
#   NudelsalatNacht – Verwandter des Schichtsalats über Nacht (Mo 23.11., 61.084 = 7,0-fach), gleicher Platz 8:20
import sys, os, copy
_D=os.path.dirname(os.path.abspath(__file__))
for g in ('g87','g88','g89','g90','g91','g92','g93','g93n','g99'): sys.path.insert(0, os.path.join(_D, '..', g))
from g90_data import NUT, PIECE, nut, Z, macros4
import g87_data, g88_data, g89_data, g93n_data
for _k,_v in {'kloesse':(105,2,22.5,0.5), 'kasseler':(125,21,0,4.5), 'sauerkraut':(20,1.5,2,0.3), 'salat':(14,1,2,0.2)}.items(): NUT.setdefault(_k,_v)
KLOESSE4='exactly four small round pale yellow matte German potato dumplings, each about the size of a golf ball, lying close together in a group, all four clearly visible'
TELLER='A round white dinner plate, the whole plate fully visible with empty table space left and right of it, with '
NEU=dict(
 KlossKasseler=dict(key='KlossKasseler', suess=False, hook='Klöße klassisch mit', titel=['KASSELER UND','SAUERKRAUT'], portion='pro Portion', anzahl=4, vs=800,
  zutaten=[Z('500 g','Kasseler (mager)','kasseler','kasseler',500), Z('500 g','Kloßteig (Kühlregal)','kartoffelkloesse','kloesse',500), Z('500 g','Sauerkraut','sauerkraut','sauerkraut',500),
           Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1), Z('1 Stück','Apfel','apfel','apfel',st=1), Z('200 ml','Gemüsebrühe','gemuesebruehe','bruehe',0), Z('2 TL','Senf','senf','senf',10)],
  ex=['1 EL Öl, 2 Lorbeerblätter, ½ TL Kümmel', 'Pfeffer, Petersilie'], exnut=[(90,0,0,10)],
  intro='Kasseler mit Sauerkraut und Klößen, wie es früher sonntags auf den Tisch kam: Das Kasseler zieht direkt im Sauerkraut gar und bleibt dadurch saftig, ein Apfel nimmt dem Kraut die Säure. Mit fertigem Kloßteig steht alles in 35 Minuten auf dem Tisch: {k} kcal und {p} g Eiweiß pro Teller statt 800 im Gasthaus!',
  schritte=['Die Zwiebel würfeln und im heißen Öl 3 Minuten anschwitzen. Den Apfel schälen und grob raspeln. Apfel, Sauerkraut, Brühe, Lorbeer und Kümmel zugeben und zugedeckt 10 Minuten köcheln lassen.',
            'Das Kasseler in 8 Scheiben schneiden, auf das Sauerkraut legen und zugedeckt bei kleiner Hitze 15 Minuten gar ziehen lassen.',
            'Aus dem Kloßteig 16 kleine Klöße formen (4 pro Teller) und nach Packungsangabe in siedendem Salzwasser gar ziehen lassen (ca. 15 Minuten).',
            'Das Kasseler herausnehmen, den Senf unter das Sauerkraut rühren und mit Pfeffer abschmecken. Je 2 Scheiben Kasseler mit Sauerkraut und Klößen anrichten, etwas Petersilie darüber.'],
  frage='Kasseler: mit Sauerkraut oder mit Grünkohl?', tags='#kasseler #sauerkraut #fitmitkev',
  prompt='A round white dinner plate, the whole plate fully visible with empty table space left and right of it, with two thick slices of juicy pink cured smoked pork loin (German Kasseler), smooth pink meat without any breading and without sauce, lying overlapping, next to a generous heap of German sauerkraut: long thin soft pale yellowish-white strands of cooked finely shredded white cabbage, moist and glossy, clearly recognizable as cabbage strands, not rice, not pasta, not noodles, and beside it on the same plate exactly four small round pale yellow matte German potato dumplings, each about the size of a golf ball, lying close together in a group, all four clearly visible, a little chopped green parsley on the dumplings.'),   # Job-Schlüssel KlossKasselerB, Seed 4 (erster Prompt malte das Sauerkraut körnig wie Reis)
 KlossScheiben=dict(key='KlossScheiben', suess=False, hook='Klöße mal anders:', titel=['GEBRATEN MIT','SPIEGELEI'], portion='pro Portion', anzahl=4, vs=750,
  zutaten=[Z('750 g','Kloßteig (Kühlregal)','kartoffelkloesse','kloesse',750), Z('200 g','Kochschinken','kochschinken','kochschinken',200), Z('2 Stück','Zwiebeln','zwiebeln','zwiebel',st=2),
           Z('4 Stück','Eier','eier','ei',st=4), Z('1 EL','Öl','oel','oel',10), Z('1 Bund','Schnittlauch','schnittlauch','schnittlauch',0)],
  ex=['1 TL Paprikapulver', 'Salz, Pfeffer'], exnut=[],
  intro='Klöße aus der Pfanne statt aus dem Topf: Den fertigen Kloßteig zu einer Rolle formen, in Scheiben schneiden und goldbraun braten. Außen knusprig, innen weich, dazu Schinken, Zwiebeln und ein Spiegelei. Schmeckt wie Bratkartoffeln, nur ohne Schälen und Vorkochen, und steht in 20 Minuten auf dem Tisch: {k} kcal und {p} g Eiweiß pro Teller statt 750 für Bratkartoffeln mit Speck und Spiegelei!',
  schritte=['Den Kloßteig mit feuchten Händen zu einer Rolle (ca. 6 cm dick) formen und in 24 Scheiben schneiden. Schinken und Zwiebeln würfeln.',
            'Die Hälfte vom Öl in einer großen beschichteten Pfanne erhitzen und die Kloßscheiben portionsweise von jeder Seite 3–4 Minuten goldbraun braten. Erst wenden, wenn sie sich von selbst lösen. Herausnehmen und warm stellen.',
            'Zwiebeln und Schinken im restlichen Öl 4 Minuten anbraten, mit Paprikapulver, Salz und Pfeffer würzen und unter die Kloßscheiben mischen.',
            'In derselben Pfanne 4 Spiegeleier braten. Je 6 Kloßscheiben mit Schinken und Zwiebeln anrichten, ein Spiegelei daraufsetzen und mit Schnittlauch bestreuen.'],
  frage='Klöße: lieber gekocht oder gebraten?', tags='#klöße #spiegelei #fitmitkev',
  prompt=TELLER+'six round golden-brown pan-fried slices cut from a potato dumpling roll, each slice a flat thick disc about as wide as a small orange with a crisp golden crust, arranged overlapping, mixed with small pink diced ham cubes and soft browned onion pieces, on top one sunny-side-up fried egg with a bright yellow yolk, sprinkled with chopped green chives.'),
 KlossLauch=dict(key='KlossLauch', suess=False, hook='Klöße überbacken mit', titel=['SCHINKEN','UND LAUCH'], portion='pro Portion', anzahl=4, vs=780,
  zutaten=[Z('750 g','Kloßteig (Kühlregal)','kartoffelkloesse','kloesse',750), Z('400 g','Lauch','lauch','lauch',400), Z('150 g','Kochschinken','kochschinken','kochschinken',150),
           Z('150 g','Frischkäse light','frischkaese_light','frischkaese',150), Z('150 ml','Milch (1,5 %)','milch','milch',150), Z('100 ml','Gemüsebrühe','gemuesebruehe','bruehe',0),
           Z('100 g','Reibekäse light','reibekaese_light','reibekaese',100)],
  ex=['1 TL Öl, Muskat', 'Salz, Pfeffer'], exnut=[(45,0,0,5)],
  intro='Klöße aus dem Ofen: Acht große Klöße sitzen in einer cremigen Lauchsoße mit Schinken, obendrauf Käse, der im Ofen goldbraun wird. Die Soße ist aus Frischkäse und Milch statt aus Sahne, der Kloßteig kommt fertig aus dem Kühlregal. 15 Minuten Arbeit, den Rest macht der Ofen: {k} kcal und {p} g Eiweiß pro Portion statt 780 für das Schinken-Lauch-Gratin mit Sahne!',
  schritte=['Den Ofen auf 200 °C Ober-/Unterhitze vorheizen. Aus dem Kloßteig 8 große Klöße formen (2 pro Portion) und in siedendem Salzwasser 15 Minuten vorgaren.',
            'Den Lauch in Ringe schneiden, gründlich waschen und im Öl 5 Minuten andünsten. Den Schinken würfeln und kurz mitbraten. Frischkäse, Milch und Brühe einrühren, einmal aufkochen und mit Muskat, Salz und Pfeffer abschmecken.',
            'Die Lauchsoße in eine Auflaufform (ca. 20 × 30 cm) geben, die Klöße hineinsetzen, mit dem Käse bestreuen und 15–20 Minuten überbacken, bis der Käse goldbraun ist.'],
  frage='Klöße: aus dem Topf oder aus dem Ofen?', tags='#klöße #lauch #überbacken #auflauf #fitmitkev',
  prompt='Close-up food photo of a white rectangular ceramic baking dish with two handles, the whole dish fully visible and filling most of the frame, with a little empty table space left and right of it, seen from above at a 45 degree angle, nothing else on the table. In the dish exactly eight large round pale yellow German potato dumplings arranged in two straight rows of four dumplings each, each dumpling the size of a tennis ball with a smooth matte surface, sitting in a creamy white leek sauce with many green and white leek rings and small pink ham cubes, the round shape of every dumpling clearly visible. A light layer of melted cheese with golden brown spots from the oven on top of the dumplings and the sauce, the dumplings still clearly recognizable as round balls.'),   # Job-Schlüssel KlossLauchB, Seed 10 (genau acht Klöße in zwei Reihen; erster Prompt lieferte 7, 9 oder 12)
 WinterWoelkchen=dict(key='WinterWoelkchen', suess=True, hook='Ohne Butter, ohne Mehl:', titel=['WINTER-','WÖLKCHEN'], portion='pro Stück', anzahl=30, vs=80,
  zutaten=[Z('200 g','Magerquark','magerquark','quark',200), Z('100 g','Gemahlene Mandeln','gemahlene_mandeln','mandeln',100), Z('80 g','Speisestärke','speisestaerke','speisestaerke',80),
           Z('60 g','Erythrit','erythrit','erythrit',60), Z('1 Stück','Ei','ei','ei',st=1), Z('2 TL','Zimt','zimt','zimt',0), Z('1 TL','Vanilleextrakt','vanilleextrakt','vanille',0)],
  ex=['1 TL Backpulver, 1 Prise Salz', 'Puder-Erythrit und etwas Zimt zum Bestäuben'], exnut=[],
  intro='Nach den Kokos-Wölkchen kommt die Wintersorte: mit Zimt, Vanille und gemahlenen Mandeln. Sie zergehen genauso auf der Zunge und kommen wieder ganz ohne Butter und Mehl aus. Der Quark hält sie saftig, die Stärke macht sie mürbe. In 10 Minuten gerührt, 15 Minuten im Ofen: {k} kcal pro Wölkchen statt 80 für ein Butterplätzchen!',
  schritte=['Quark, Ei, Erythrit, Vanille und eine Prise Salz glatt rühren. Mandeln, Speisestärke, Zimt und Backpulver mischen und unterrühren. Den Teig 10 Minuten quellen lassen.',
            'Mit zwei Teelöffeln 30 kleine Häufchen auf ein Backblech mit Backpapier setzen und mit feuchten Fingern rund formen.',
            'Bei 170 °C Ober-/Unterhitze 15–18 Minuten backen, bis die Unterseite leicht goldgelb ist. Abkühlen lassen und mit Puder-Erythrit und einem Hauch Zimt bestäuben.'],
  frage='Wölkchen: Kokos, Eierlikör oder Zimt, welche Sorte ist deine?', tags='#wölkchen #zimt #fitmitkev',
  prompt='A white plate piled high with many small round pale beige soft cookies, each cookie a smooth slightly domed mound with fine cracks, thickly dusted with white powdered sugar and a little brown cinnamon, the bottoms pale golden, three whole cookies lying on the table in front of the plate, all cookies whole and unbroken, two cinnamon sticks lying beside the plate.'),   # Job-Schlüssel WinterWoelkchenB, Seed 6 (erster Prompt zeigte ein aufgebrochenes Plätzchen, das gefüllt aussah)
 DoenerKartoffeln=dict(key='DoenerKartoffeln', suess=False, hook='Döner trifft Ofenkartoffel:', titel=['DÖNER-','KARTOFFELN'], portion='pro Portion', anzahl=4, vs=900,
  zutaten=[Z('800 g','Kartoffeln','kartoffeln','kartoffeln',800), Z('500 g','Hähnchenbrust','haehnchenbrust','haehnchen',500), Z('2 EL','Döner- oder Gyrosgewürz','gyrosgewuerz','gyrosgewuerz',0),
           Z('200 g','Skyr','skyr','skyr',200), Z('1 Zehe','Knoblauch','knoblauch','knoblauch',3), Z('150 g','Eisbergsalat','eisbergsalat','salat',150),
           Z('2 Stück','Tomaten','frische_tomaten','tomate',200), Z('1 Stück','Rote Zwiebel','rote_zwiebel','zwiebel',st=1)],
  ex=['1 EL Öl, 1 TL Paprikapulver', 'Salz, Pfeffer'], exnut=[(90,0,0,10)],
  intro='Alles, was in einen Döner gehört, nur auf knusprigen Ofenkartoffeln statt im Brot: gewürztes Hähnchen, Salat, Tomate, Zwiebel und eine Knoblauchsoße aus Skyr. Kartoffeln und Fleisch backen zusammen auf einem Blech, in der Zeit ist der Rest geschnitten. Ein großer Teller: {k} kcal und {p} g Eiweiß pro Portion statt 900 für den Dönerteller mit Pommes!',
  schritte=['Die Kartoffeln in 2 cm große Würfel schneiden, mit der Hälfte vom Öl, Paprikapulver und Salz mischen und auf einem Backblech mit Backpapier bei 220 °C Ober-/Unterhitze 15 Minuten backen.',
            'Die Hähnchenbrust in dünne Streifen schneiden, mit dem Gewürz und dem restlichen Öl mischen, zu den Kartoffeln aufs Blech geben und alles weitere 15 Minuten backen, bis die Kartoffeln goldbraun sind.',
            'Den Skyr mit gepresstem Knoblauch, Salz, Pfeffer und 2–3 EL Wasser glatt rühren. Den Salat in feine Streifen schneiden, die Tomaten in Spalten schneiden, die Zwiebel in dünne Ringe schneiden.',
            'Salat, Tomaten und Zwiebel auf den heißen Kartoffeln verteilen und die Knoblauchsoße darüber geben.'],
  frage='Döner: mit Knoblauchsoße, Kräutersoße oder scharf?', tags='#döner #kartoffeln #fitmitkev',
  prompt='Close view of a dark baking tray lined with white baking paper, seen from above at a 45 degree angle, filled with many small golden brown crispy roasted potato cubes and browned thin strips of spiced chicken breast, the middle topped with finely shredded green iceberg lettuce, fresh red tomato wedges and thin red onion rings, generously drizzled with white yogurt garlic sauce in zigzag lines, crispy bare potato cubes clearly visible all around the edge.'),
 NudelsalatNacht=dict(key='NudelsalatNacht', suess=False, hook='Zieht über Nacht durch:', titel=['OMAS','NUDELSALAT'], portion='pro Portion', anzahl=4, vs=700,
  zutaten=[Z('250 g','Spirelli','spirelli','nudeln',250), Z('150 g','Putenschinken','putenschinken','putenschinken',150), Z('200 g','Erbsen (TK)','erbsen','erbsen',200),
           Z('1 Stück','Rote Paprika','rote_paprika','paprika_st',st=1), Z('150 g','Gewürzgurken','gewuerzgurken','gurken',150), Z('3 Stück','Eier','eier','ei',st=3),
           Z('250 g','Skyr','skyr','skyr',250), Z('2 TL','Senf','senf','senf',10)],
  ex=['5 EL Gurkenwasser, 1 EL Essig', 'Salz, Pfeffer, Schnittlauch'], exnut=[],
  intro='Nudelsalat wie bei Oma auf jeder Feier: mit Erbsen, Gewürzgurken, Paprika, Schinken und Ei. Am Abend vorher anrühren, über Nacht durchziehen lassen, am nächsten Tag schmeckt er am besten. Die Soße ist aus Skyr, Senf und Gurkenwasser statt aus Mayonnaise: {k} kcal und {p} g Eiweiß pro Portion statt 700 für den Nudelsalat mit Mayo und Fleischwurst!',
  schritte=['Die Nudeln nach Packungsangabe bissfest kochen, in der letzten Minute die Erbsen mitkochen. Abgießen und kalt abschrecken. Die Eier 10 Minuten hart kochen und abschrecken.',
            'Schinken, Paprika und Gewürzgurken klein würfeln. Den Skyr mit Senf, Gurkenwasser, Essig, Salz und Pfeffer glatt rühren.',
            'Nudeln, Erbsen, Schinken, Paprika und Gurken mit der Soße mischen, abdecken und über Nacht in den Kühlschrank stellen.',
            'Vor dem Servieren durchrühren, bei Bedarf noch einen Schuss Gurkenwasser zugeben und abschmecken. Die Eier halbieren, obendrauf legen und mit Schnittlauch bestreuen.'],
  frage='Nudelsalat: mit Mayo, mit Joghurt oder mit Essig und Öl?', tags='#nudelsalat #partysalat #fitmitkev',
  prompt='A large clear glass salad bowl filled to the top with creamy pasta salad made of spiral fusilli pasta in a light white yogurt dressing, mixed with green peas, small red bell pepper cubes, small diced pickled gherkins and small pink ham cubes, halved hard-boiled eggs with yellow yolks arranged on top, sprinkled with chopped green chives. A large serving spoon lies beside the bowl.'),
)
for _k,_r in NEU.items(): _r['kurz']=['–','–','–']

# Wiederholer-Test, Gruppe NEU: Rezeptdaten unverändert aus dem ersten Bau, nur Schreibschrift-Zeile (hook) und Bild-Prompt sind neu.
_A={}
for _m in (g87_data, g88_data, g89_data, g93n_data):
    for _r in _m.R: _A[_r['key']]=_r
def neu_bild(key, hook, prompt, suess):
    r=copy.deepcopy(_A[key]); r['hook_alt']=r['hook']; r['prompt_alt']=r.get('prompt'); r['hook']=hook; r['prompt']=prompt; r['suess']=suess; r['kurz']=['–','–','–']
    for f in ('fb','hinweis','n','buch'): r.pop(f,None)
    return r
GLAS='A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, '
TEST=dict(
 MilchschnitteBowl=neu_bild('MilchschnitteBowl','Kindheit zum Löffeln:',
  GLAS+'seen from the front slightly from above, completely full and untouched, the layers clearly visible through the glass: a layer of moist dark chocolate sponge cake at the bottom and a thick layer of smooth white milk cream on top, the smooth top generously dusted with dark cocoa powder, a clean teaspoon lying on the table in front of the dish, plain and simple.', True),
 Gewuerzkuchen=neu_bild('Gewuerzkuchen','Duftet nach Advent:',
  'Three square pieces of moist dark brown spice sheet cake stacked on a small white plate, each piece covered with a glossy dark chocolate glaze on top, the moist dark brown crumb clearly visible from the side, a few cake crumbs on the plate, two cinnamon sticks lying beside the plate.', True),
 BlitzKaesekuchen=neu_bild('BlitzKaesekuchen','Eine Schüssel, kein Mixer:',
  'One tall slice of baked cheesecake on a small white dessert plate seen from the front at eye level, the cut side facing the camera showing the creamy white smooth filling, a thin golden cookie crumb base at the bottom and a golden-brown top, a small fork lying on the plate, behind it out of focus the rest of the round cheesecake on a wooden board.', True),
 Zupfkuchen=neu_bild('Zupfkuchen','Schoko trifft Käsekuchen:',
  'A whole round Russian Zupfkuchen cake on a round wooden board seen from above at a 45 degree angle, the top showing a pale yellow baked cheesecake surface with many irregular dark chocolate dough patches scattered over it and a dark chocolate rim, two slices cut and pulled slightly out of the cake showing the thick creamy white cheesecake filling and the thin dark chocolate base.', True),
 GyrosBowl=neu_bild('GyrosBowl','Wie beim Griechen:',
  GLAS+'freshly baked, seen from above at a 45 degree angle, completely full and untouched: the top covered with a baked white tzatziki yogurt layer with golden browned melted cheese spots, browned spiced chicken gyros strips with red bell pepper strips and onion peeking out around the edges, white rice visible at the bottom through the glass, a few fresh cucumber slices lying beside the dish.', False),
 KaeseLauchSuppe=neu_bild('KaeseLauchSuppe','Ein Topf, 30 Minuten:',
  'A deep white soup plate, the whole plate fully visible, seen from above at a 45 degree angle, filled with thick creamy pale yellow cheese and leek soup with plenty of browned minced beef crumbles, many bright green and white leek rings and small soft potato cubes, a little grated cheese melting on top, freshly ground black pepper, a silver spoon lying beside the plate.', False),
)
R=[NEU[k] for k in ('KlossKasseler','KlossScheiben','KlossLauch','WinterWoelkchen','DoenerKartoffeln','NudelsalatNacht')]+list(TEST.values())

if __name__=='__main__':
    for r in R:
        k,p,c,f=macros4(r); assert r['vs']>k and len(r['zutaten'])<=8 and k<=500, r['key']
        if r['key'] in NEU:
            txt=r['intro']+' '.join(r['schritte'])+r['frage']
            for w in ('abnehm','esn ','melly','gta','ohne zucker','satt','miracel'): assert w not in txt.lower(), (r['key'],w)
        else:
            a=_A[r['key']]; assert macros4(a)==(k,p,c,f) and a['titel']==r['titel'] and a['hook']!=r['hook'], r['key']
        print(f"{r['key']:20s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P {c:3d}K {f:2d}F {r['portion']} × {r['anzahl']} vs {r['vs']} | {r['hook']} {' '.join(r['titel'])}{'  (Test NEU, vorher: '+r['hook_alt']+')' if r['key'] in TEST else ''}")
    print('ok')
