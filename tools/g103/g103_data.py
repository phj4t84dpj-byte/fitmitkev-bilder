# -*- coding: utf-8 -*-
# G103 – Donnerstag 26.11.2026. Neue Regel (Kev 24.11., 18:05/20:05): ein Rezept frühestens nach 14 Tagen wiederholen; andere Variante = neues Rezept.
# 19 Rezepte + 2 feste (6:10 ESN-Rezept Schoko-Mousse 434673372, 13:00 ESN-Rezept Tiramisu-Bowl 434673472, beide schon eingeplant) + Buch-Beitrag B7 20:15.
# Deshalb heute KEIN Tiramisu-Skyr-Kuchen und keine Mousse als Rezept; die Frikadellen aus dem Ofen (11.11.) ruhen, weil die Kloß-Frikadellen laufen.
#
# WIEDERHOLER-TEST Tag 2 (Kev 24.11.: „Weiter, mit 14 Tagen Pause“): alle Wiederholer liefen zuletzt am 9.–12.11. (≥14 Tage Pause, gegen alle Läufe
# nach Schlüssel, Name und Stichwort geprüft). Nach Stärke des letzten Laufs sortiert, abwechselnd NEU/ALT, getrennt süß/herzhaft:
#   süß:  MandarinenSchmand 0,81 NEU · NusseckenOats 0,6 ALT · BratapfelSkyrKuchen 0,55 NEU · Engelsaugen 0,5 ALT · Apfeltaschen 0,42 NEU · ZimtschneckenPancakes 0,29 ALT
#   herz: Fruehstuecksbroetchen 0,6 NEU · GyrosAuflauf 0,6 ALT · GnocchiAuflauf 0,5 NEU · LaugenBrezeln 0,5 ALT · CordonBleu 0,4 NEU · StrammerMax 0,3 ALT · LasagneSuppe 0,30 NEU
#   (9.11. und 10.11. aus stats/posts_stand_1311.json gerechnet, 11./12.11. aus laeufe.json; Quiche 0,2 und Apfel-Quarkbällchen 0,2 bleiben draußen:
#    zu schwach, und die Quarkbällchen liefen am 23.11., die Schinken-Lauch-Klöße am 25.11.)
#
# 6 neue Rezepte:
#   KlossHirsch       – Kloßteig-Reihe, Idee 2 (Hirschgulasch mit Preiselbeeren)
#   KlossPilz         – Kloßteig-Reihe, Idee 13 (Pilzrahmsoße ohne Fleisch)
#   KlossFrikadellen  – Kloßteig-Reihe, Idee 10 (Frikadellen mit Zwiebelsoße)
#   Schneewittchen    – Omas Blechkuchen (alte Fassung G40 vom Oktober, neu gerechnet); 22.10. 31.059 Reichweite
#   JapanKaesekuchen  – „Der virale Japanese Cheesecake, nur mit Skyr“ lief am 11.10. (12.457), neues Rezept mit Skyr
#   ToastHawaii       – Omas Klassiker aus den 70ern, neu
import sys, os, copy
_D=os.path.dirname(os.path.abspath(__file__))
for g in ('g87','g88','g89','g90','g91','g92','g93','g93n','g99'): sys.path.insert(0, os.path.join(_D, '..', g))
from g90_data import NUT, PIECE, nut, Z, macros4
import g87_data, g88_data, g89_data, g90_data
for _k,_v in {'kloesse':(105,2,22.5,0.5), 'rotkohl':(60,1.2,12,0.3), 'semmelbroesel':(350,10,70,2),
              'hirsch':(113,21.4,0,3.3), 'preiselbeeren':(180,0.3,43,0.5), 'toast':(245,8.5,42,3.5), 'ananas':(60,0.4,13,0.1)}.items(): NUT.setdefault(_k,_v)
KLOESSE4='exactly four small round pale yellow matte German potato dumplings, each about the size of a golf ball, lying close together in a group, all four clearly visible'
TELLER='A round white dinner plate, the whole plate fully visible with empty table space left and right of it, with '
NEU=dict(
 KlossHirsch=dict(key='KlossHirsch', suess=False, hook='Klöße klassisch mit', titel=['HIRSCHGULASCH','& PREISELBEEREN'], portion='pro Portion', anzahl=4, vs=950,
  zutaten=[Z('500 g','Hirschgulasch','hirschgulasch','hirsch',500), Z('500 g','Kloßteig (Kühlregal)','kartoffelkloesse','kloesse',500), Z('400 g','Rotkohl (Glas)','rotkohl','rotkohl',400),
           Z('2 Stück','Zwiebeln','zwiebeln','zwiebel',st=2), Z('400 ml','Rinderbrühe','rinderbruehe','bruehe',0), Z('60 g','Preiselbeeren (Glas)','preiselbeeren','preiselbeeren',60),
           Z('1 EL','Tomatenmark','tomatenmark','tomatenmark',15), Z('1 EL','Speisestärke','speisestaerke','speisestaerke',10)],
  ex=['1 EL Öl, 2 Lorbeerblätter, 4 Wacholderbeeren', 'Salz, Pfeffer'], exnut=[(90,0,0,10)],
  intro='Hirschgulasch wie im Wirtshaus, aber ohne Sahne und ohne Mehlschwitze: Das Fleisch schmort mit Zwiebeln, Wacholder und Lorbeer in kräftiger Brühe, bis es zart ist, ein Löffel Preiselbeeren macht die Soße rund. Dazu Rotkohl und Klöße aus fertigem Kloßteig, fertig ist das Festessen: {k} kcal und {p} g Eiweiß pro Teller statt 950 im Wirtshaus!',
  schritte=['Das Hirschgulasch trocken tupfen und im heißen Öl in einem Schmortopf portionsweise rundherum kräftig anbraten. Die Zwiebeln würfeln, zugeben und 3 Minuten mitbraten. Das Tomatenmark kurz mitrösten.',
            'Mit der Brühe ablöschen, Lorbeer und angedrückte Wacholderbeeren zugeben und zugedeckt bei kleiner Hitze 75–90 Minuten schmoren, bis das Fleisch zart ist.',
            'Aus dem Kloßteig 16 kleine Klöße formen (4 pro Teller) und nach Packungsangabe in siedendem Salzwasser gar ziehen lassen (ca. 15 Minuten). Den Rotkohl in einem kleinen Topf erhitzen.',
            'Die Speisestärke in 2 EL kaltem Wasser anrühren, in die Soße rühren und kurz aufkochen. Die Preiselbeeren einrühren und mit Salz und Pfeffer abschmecken. Gulasch mit Rotkohl und Klößen anrichten.'],
  frage='Zu Wild gehören Preiselbeeren: ja oder nein?', tags='#hirschgulasch #klöße #fitmitkev',
  prompt=TELLER+'a generous portion of dark brown braised venison goulash: tender chunks of dark meat without any breading in a glossy dark brown gravy, a small spoonful of bright red lingonberry jam on top of the meat, next to it a heap of glossy dark purple-red braised red cabbage, and beside it on the same plate '+KLOESSE4+'.'),
 KlossPilz=dict(key='KlossPilz', suess=False, hook='Klöße mit', titel=['PILZRAHM-','SOSSE'], portion='pro Portion', anzahl=4, vs=750,
  zutaten=[Z('800 g','Champignons','champignons','champignons',800), Z('500 g','Kloßteig (Kühlregal)','kartoffelkloesse','kloesse',500), Z('2 Stück','Zwiebeln','zwiebeln','zwiebel',st=2),
           Z('200 ml','Kochsahne (15 %)','kochsahne','kochsahne',200), Z('300 ml','Gemüsebrühe','gemuesebruehe','bruehe',0), Z('1 EL','Speisestärke','speisestaerke','speisestaerke',10),
           Z('1 Bund','Petersilie','petersilie','petersilie',0)],
  ex=['1 EL Öl, 1 TL Paprikapulver', 'Salz, Pfeffer, Muskat'], exnut=[(90,0,0,10)],
  intro='Ganz ohne Fleisch und trotzdem ein richtiges Wirtshaus-Essen: viele scharf angebratene Champignons in einer cremigen Rahmsoße mit Zwiebeln und Petersilie, dazu Klöße aus fertigem Kloßteig, die die Soße aufnehmen. In 25 Minuten fertig: {k} kcal pro Teller statt 750 für Klöße mit Rahmschwammerl im Gasthaus!',
  schritte=['Aus dem Kloßteig 16 kleine Klöße formen (4 pro Teller) und nach Packungsangabe in siedendem Salzwasser gar ziehen lassen (ca. 15 Minuten).',
            'Die Champignons in Scheiben schneiden, die Zwiebeln fein würfeln. Die Pilze im heißen Öl in einer großen Pfanne portionsweise 5 Minuten kräftig anbraten, bis sie goldbraun sind. Die Zwiebeln zugeben und 3 Minuten mitbraten.',
            'Mit Paprikapulver bestäuben, Brühe und Kochsahne angießen und 5 Minuten köcheln lassen. Die Speisestärke in 2 EL kaltem Wasser anrühren, einrühren und kurz aufkochen. Mit Salz, Pfeffer und Muskat abschmecken.',
            'Die Petersilie hacken und unterrühren. Die Pilzrahmsoße mit den Klößen anrichten.'],
  frage='Pilze: Champignons oder Pfifferlinge?', tags='#pilzrahmsoße #klöße #vegetarisch #fitmitkev',
  prompt=TELLER+KLOESSE4+', lying in the middle of the plate, generously surrounded and half covered by a creamy light beige mushroom cream sauce with very many sliced golden-browned button mushrooms and soft onion pieces, sprinkled with plenty of fresh chopped green parsley, no meat on the plate.'),
 KlossFrikadellen=dict(key='KlossFrikadellen', suess=False, hook='Klöße mit', titel=['FRIKADELLEN IN','ZWIEBELSOSSE'], portion='pro Portion', anzahl=4, vs=900,
  zutaten=[Z('500 g','Rinderhack (mager)','rinderhack','hack',500), Z('500 g','Kloßteig (Kühlregal)','kartoffelkloesse','kloesse',500), Z('3 Stück','Zwiebeln','zwiebeln','zwiebel',st=3),
           Z('1 Stück','Ei','ei','ei',st=1), Z('30 g','Semmelbrösel','semmelbroesel','semmelbroesel',30), Z('1 EL','Senf','senf','senf',15),
           Z('400 ml','Rinderbrühe','rinderbruehe','bruehe',0), Z('1 EL','Speisestärke','speisestaerke','speisestaerke',10)],
  ex=['1 EL Öl, 1 TL Majoran', 'Salz, Pfeffer, Petersilie'], exnut=[(90,0,0,10)],
  intro='Frikadellen wie bei Oma, mit magerem Rinderhack und einer Zwiebelsoße, für die die Zwiebeln langsam goldbraun gebraten werden. Dazu Klöße aus fertigem Kloßteig, die die ganze Soße aufnehmen. In 35 Minuten auf dem Tisch: {k} kcal und {p} g Eiweiß pro Teller statt 900 für Frikadellen mit Bratkartoffeln!',
  schritte=['Eine Zwiebel fein würfeln und mit Hack, Ei, Semmelbröseln, Senf, Majoran, Salz und Pfeffer verkneten. Mit feuchten Händen 8 Frikadellen formen.',
            'Die Frikadellen im heißen Öl in einer großen Pfanne von jeder Seite 4–5 Minuten braun braten und herausnehmen. Aus dem Kloßteig 16 kleine Klöße formen (4 pro Teller) und nach Packungsangabe in siedendem Salzwasser gar ziehen lassen (ca. 15 Minuten).',
            'Die übrigen 2 Zwiebeln in feine Streifen schneiden und im Bratfett 6–8 Minuten goldbraun braten. Mit der Brühe ablöschen und 5 Minuten köcheln lassen. Die Speisestärke in 2 EL kaltem Wasser anrühren, einrühren und kurz aufkochen.',
            'Die Frikadellen in die Soße legen und 5 Minuten darin ziehen lassen. Mit den Klößen anrichten und mit Petersilie bestreuen.'],
  frage='Frikadellen, Buletten oder Fleischpflanzerl: wie sagt ihr?', tags='#frikadellen #klöße #omasrezepte #fitmitkev',
  prompt=TELLER+'two plump round browned German meat patties (Frikadellen) made of minced beef, with a browned seared surface, without any breading, partly covered with a glossy brown onion gravy with many soft golden-brown onion strips, and beside it on the same plate '+KLOESSE4+', a little chopped green parsley on the dumplings.'),
 Schneewittchen=dict(key='Schneewittchen', suess=True, hook='Von Omas Kaffeetafel:', titel=['SCHNEEWITTCHEN-','KUCHEN'], portion='pro Stück', anzahl=20, vs=420,
  zutaten=[Z('250 g','Dinkelmehl','dinkelmehl','dinkelmehl',250), Z('3 Stück','Eier','eier','ei',st=3), Z('450 g','Skyr','skyr','skyr',450), Z('140 g','Erythrit','erythrit','erythrit',140),
           Z('350 g','Sauerkirschen (Glas, abgetropft)','sauerkirschen','kirschen',350), Z('500 ml','Milch (1,5 %)','milch','milch',500), Z('1 Päckchen','Vanillepudding-Pulver','vanillepudding_pulver','puddingpulver',37),
           Z('80 g','Zartbitterschokolade','zartbitterschokolade','schokolade',80)],
  ex=['1 Päckchen Backpulver, 15 g Backkakao', '1 TL Kokosöl'], exnut=[(52,3,1.5,3),(40,0,0,4.5)],
  intro='Der Schneewittchenkuchen von Omas Kaffeetafel: saftiger Marmorboden, Sauerkirschen, eine dicke Vanillecreme und obendrauf Schokolade mit Wellen. Mit Skyr statt Butter und Sahne, und das ganze Blech reicht für 20 Stücke: {k} kcal pro Stück statt 420 vom Bäcker!',
  schritte=['Die Eier mit 100 g Erythrit schaumig schlagen und 200 g Skyr unterrühren. Mehl und Backpulver mischen und unterheben. Ein Drittel des Teigs mit dem Kakao verrühren.',
            'Den hellen Teig auf ein Backblech (30 × 40 cm) mit Backpapier streichen, den dunklen darauf verteilen und mit einer Gabel marmorieren. Die Kirschen darauf verteilen und bei 180 °C Ober-/Unterhitze 25 Minuten backen. Auskühlen lassen.',
            'Die Milch mit dem Puddingpulver und 40 g Erythrit nach Packungsangabe kochen, abkühlen lassen, glatt rühren und 250 g Skyr unterrühren. Auf den Kuchen streichen und 1 Stunde kalt stellen.',
            'Die Schokolade mit dem Kokosöl schmelzen, über die Creme streichen und mit einer Gabel Wellen ziehen. Fest werden lassen und in 20 Stücke schneiden.'],
  frage='Wer kennt den noch von Omas Kaffeetafel?', tags='#schneewittchenkuchen #blechkuchen #fitmitkev',
  prompt='Two square pieces of German Schneewittchen sheet cake on a small white plate seen from the side at eye level, the cut side facing the camera showing clearly separated layers: a marbled light and dark chocolate sponge base with dark red sour cherries baked into it, a thick layer of smooth pale yellow vanilla cream on top, and a thin layer of dark chocolate with a wavy pattern made with a fork on the very top, the rest of the sheet cake on a baking tray blurred in the background, a small cake fork beside the plate.'),
 JapanKaesekuchen=dict(key='JapanKaesekuchen', suess=True, hook='Wackelt wie eine Wolke:', titel=['JAPANISCHER','KÄSEKUCHEN'], portion='pro Stück', anzahl=10, vs=330,
  zutaten=[Z('500 g','Skyr','skyr','skyr',500), Z('4 Stück','Eier','eier','ei',st=4), Z('150 g','Frischkäse light','frischkaese_light','frischkaese',150),
           Z('60 g','Speisestärke','speisestaerke','speisestaerke',60), Z('70 g','Erythrit','erythrit','erythrit',70), Z('1 Stück','Zitrone (Abrieb)','zitrone','zitrone',0),
           Z('1 TL','Vanilleextrakt','vanilleextrakt','vanille',0)],
  ex=['1 Prise Salz', 'Puder-Erythrit zum Bestäuben'], exnut=[],
  intro='Der japanische Käsekuchen ist so luftig, dass er beim Anschneiden wackelt. Das Geheimnis: steif geschlagenes Eiweiß und ein Wasserbad im Ofen. Bei mir mit Skyr statt Sahnequark und ohne Butter, Boden braucht er keinen: {k} kcal und {p} g Eiweiß pro Stück statt 330 im Café!',
  schritte=['Den Ofen auf 160 °C Ober-/Unterhitze vorheizen. Eine Springform (20 cm) mit Backpapier auslegen und außen dicht mit Alufolie umwickeln. Ein tiefes Blech mit 2 cm heißem Wasser auf die unterste Schiene stellen.',
            'Die Eier trennen. Skyr, Frischkäse, Eigelb, Speisestärke, Vanille und Zitronenabrieb glatt rühren.',
            'Das Eiweiß mit einer Prise Salz steif schlagen, dabei nach und nach das Erythrit einrieseln lassen. In drei Portionen vorsichtig unter die Skyrmasse heben.',
            'In die Form füllen, ins Wasserbad stellen und 60 Minuten backen. Den Ofen ausschalten und den Kuchen bei leicht geöffneter Tür 30 Minuten ruhen lassen, dann ganz auskühlen lassen und mit Puder-Erythrit bestäuben.'],
  frage='Käsekuchen: fluffig wie eine Wolke oder lieber cremig und fest?', tags='#japanischerkäsekuchen #käsekuchen #fitmitkev',
  prompt='A tall round fluffy Japanese cotton cheesecake on a white cake plate seen from the front at eye level, very tall and airy with straight smooth pale golden sides and an evenly golden-brown top lightly dusted with white powdered sugar, one wedge cut out and lying on a small white plate in front showing a very airy, soft, pale yellow, fine and spongy crumb, a lemon half beside the plate.'),
 ToastHawaii=dict(key='ToastHawaii', suess=False, hook='Wie in den 70ern:', titel=['TOAST','HAWAII'], portion='pro Portion (2 Toasts)', anzahl=4, vs=650,
  zutaten=[Z('8 Scheiben','Vollkorntoast','toastbrot','toast',200), Z('8 Scheiben','Kochschinken','kochschinken','kochschinken',200), Z('8 Ringe','Ananas (Dose, ohne Zucker)','ananas','ananas',240),
           Z('8 Scheiben','Käsescheiben light','kaesescheiben','kaesescheiben',160)],
  ex=['1 TL Paprikapulver', 'Pfeffer, Schnittlauch'], exnut=[],
  intro='Toast Hawaii wie früher auf jeder Party: Toast, Schinken, eine Scheibe Ananas und Käse, der im Ofen goldbraun verläuft. Mit Vollkorntoast und Käse light statt Butter und Scheibletten. 5 Minuten belegen, 10 Minuten Ofen, fertig: {k} kcal und {p} g Eiweiß für zwei Toasts statt 650!',
  schritte=['Den Ofen auf 200 °C Ober-/Unterhitze vorheizen. Die Toastscheiben auf einem Backblech mit Backpapier leicht vortoasten (3 Minuten).',
            'Die Ananasringe gut abtropfen lassen und mit Küchenpapier trocken tupfen. Jeden Toast mit 1 Scheibe Schinken, 1 Ananasring und 1 Scheibe Käse belegen.',
            'Mit etwas Paprikapulver und Pfeffer bestreuen und 8–10 Minuten überbacken, bis der Käse verläuft und goldbraun wird. Mit Schnittlauch bestreut servieren.'],
  frage='Toast Hawaii: mit Kirsche obendrauf oder ohne?', tags='#toasthawaii #partyfood #fitmitkev',
  prompt='A white plate with two slices of golden toasted whole grain toast bread, each topped with a slice of pink cooked ham, one round yellow pineapple ring and a slice of melted golden-brown bubbling cheese flowing over the edges, the pineapple ring shape visible under the melted cheese, sprinkled with a little paprika powder and chopped green chives, nothing else on the toast, a knife and fork beside the plate.'),
)
for _k,_r in NEU.items(): _r['kurz']=['–','–','–']

# Wiederholer-Test, Gruppe NEU: Rezeptdaten unverändert aus dem ersten Bau, nur Schreibschrift-Zeile (hook) und Bild-Prompt sind neu.
_A={}
for _m in (g87_data, g88_data, g89_data, g90_data):
    for _r in _m.R: _A[_r['key']]=_r
def neu_bild(key, hook, prompt, suess):
    r=copy.deepcopy(_A[key]); r['hook_alt']=r['hook']; r['prompt_alt']=r.get('prompt'); r['hook']=hook; r['prompt']=prompt; r['suess']=suess; r['kurz']=['–','–','–']
    for f in ('fb','hinweis','n','buch'): r.pop(f,None)
    return r
TEST=dict(
 MandarinenSchmand=neu_bild('MandarinenSchmand','Omas Blechkuchen, leicht:',
  'Several square pieces of mandarin sour cream sheet cake on a rectangular white platter seen from above at a 45 degree angle, each piece with a thin golden sponge base, a thick creamy white smooth set topping and bright orange mandarin segments arranged in neat rows on and in the topping, the cut edges clearly showing the layers, a few loose mandarin segments on the table beside the platter.', True),
 BratapfelSkyrKuchen=neu_bild('BratapfelSkyrKuchen','Duftet nach Bratapfel:',
  'Two slices of crustless baked apple cheesecake on a small white plate seen from the front at eye level, the cut side facing the camera showing a thin cookie crumb base and a tall creamy pale filling with soft apple cubes, raisins and swirls of cinnamon, toasted golden almond flakes on top, a small cake fork on the plate, a red apple and a cinnamon stick lying beside the plate.', True),
 Apfeltaschen=neu_bild('Apfeltaschen','Ohne Blätterteig:',
  'Six golden baked apple turnovers arranged in a circle on a round white plate seen from above at a 45 degree angle, half-moon shaped hand pies with fork-crimped edges and a glossy golden egg-washed crust, the one in front broken in half showing a filling of soft apple cubes with cinnamon and raisins, a fresh red apple lying beside the plate.', True),
 Fruehstuecksbroetchen=neu_bild('Fruehstuecksbroetchen','Sonntags frisch aus dem Ofen:',
  'A round woven bread basket lined with a white linen napkin, filled with homemade round bread rolls with a golden brown crust and one long slash on top, some rolls topped with blue-black poppy seeds and some with golden sesame seeds, one roll cut in half lying on the table in front of the basket showing a soft white fluffy crumb.', False),
 GnocchiAuflauf=neu_bild('GnocchiAuflauf','Ofen an, fertig:',
  'Close-up of a white rectangular ceramic baking dish with a freshly baked gnocchi casserole seen from above at a 45 degree angle, the dish fully visible: bubbling golden brown melted mozzarella cheese on top, small potato gnocchi and red tomato minced beef sauce with red bell pepper pieces peeking out between the cheese, a serving spoon lifting one portion out of the corner with stretchy melted cheese.', False),
 CordonBleu=neu_bild('CordonBleu','Außen knusprig, innen Käse:',
  'Two golden crispy breaded chicken cordon bleu lying on a white plate, the front one cut through the middle showing layers of white chicken, pink ham and melted cheese flowing out of the center, next to a few boiled peeled yellow potatoes, a fork and knife beside the plate.', False),
 LasagneSuppe=neu_bild('LasagneSuppe','Schmeckt wie Lasagne:',
  'A deep white soup plate seen from above at a 45 degree angle, the whole plate fully visible, filled with chunky rich red tomato and minced beef soup with many wavy broken lasagna pasta sheets, a spoonful of white cream cheese melting in the middle, melted grated cheese and a few fresh green basil leaves on top, a spoon lying beside the plate.', False),
)
R=[NEU[k] for k in ('KlossHirsch','KlossPilz','KlossFrikadellen','Schneewittchen','JapanKaesekuchen','ToastHawaii')]+list(TEST.values())

if __name__=='__main__':
    for r in R:
        k,p,c,f=macros4(r); assert r['vs']>k and len(r['zutaten'])<=8 and k<=500, r['key']
        if r['key'] in NEU:
            txt=r['intro']+' '.join(r['schritte'])+r['frage']
            for w in ('abnehm','esn ','melly','gta','ohne zucker','satt','miracel'): assert w not in txt.lower(), (r['key'],w)
        else:
            a=_A[r['key']]; assert macros4(a)==(k,p,c,f) and a['titel']==r['titel'] and a['hook']!=r['hook'], r['key']
        print(f"{r['key']:22s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P {c:3d}K {f:2d}F {r['portion']} × {r['anzahl']} vs {r['vs']} | {r['hook']} {' '.join(r['titel'])}{'  (Test NEU, vorher: '+r['hook_alt']+')' if r['key'] in TEST else ''}")
    print('ok')
