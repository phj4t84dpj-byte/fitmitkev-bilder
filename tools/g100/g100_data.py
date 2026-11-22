# -*- coding: utf-8 -*-
# G100 – Montag 23.11.2026. Morgen-Check So 22.11.: Samstag 699.058 Aufrufe (über Freitag) → Stufenplan bleibt bei 22.
# 20 Rezepte + 2 feste (6:10 ESN-Rezept Zimtschnecken-Overnight-Oats, 13:00 ESN-Rezept Schokopudding, beide schon eingeplant, ohne ESN-Zeile).
# 4 neue Rezepte:
#   KokosWoelkchen   – Mitbewerber-Check 22.11.: „3 Zutaten Kokoswölkchen“ bei „Unsere Weihnachtsbäckerei“ 4.660 Interaktionen nach 42 h (7,7-fach), dritte Wölkchen-Sorte in Folge;
#                      bewusst kein Eischnee-Teig (das wären unsere Kokosmakronen vom 20.11.), sondern weicher Quark-Stärke-Teig.
#   Schichtsalat     – „Übernachtsalat“ bei Lecker Zuhause 2,6-fach; unser „Schichtsalat im Glas“ lief am 17.11. (12.350, ca. Tagesmedian) – hier die große Schüssel über Nacht.
#   HackNudeln       – Verwandter des Freitags-Siegers „Gebratene Nudeln“ (25.720 Reichweite, 3,2-fach), mit Hack statt Hähnchen; Text verweist darauf.
#   PizzaWrap        – Verwandter des Freitags-Zweiten „Wrap aus körnigem Frischkäse“ (20.782, 2,6-fach), als Pizza gefüllt und überbacken.
# 16 Wiederholer (7-Tage-Regel, gegen alle Tage seit dem letzten Lauf geprüft; Zahlen ausgereift am 22.11. abgerufen) stehen mit Uhrzeiten in plan100.py.
import sys, os
_D=os.path.dirname(os.path.abspath(__file__))
for g in ('g87','g88','g89','g90','g91','g92','g93','g93n','g99'): sys.path.insert(0, os.path.join(_D, '..', g))
from g90_data import NUT, PIECE, nut, Z, macros4
for _k,_v in {'eisbergsalat':(14,1,2,0.2), 'weisskohl':(25,1.3,4,0.2), 'sojasauce':(60,8,6,0), 'kloesse':(105,2,22.5,0.5), 'rind':(120,21,0,4), 'rotkohl':(60,1.2,12,0.3)}.items(): NUT.setdefault(_k,_v)   # bestehende Werte nicht überschreiben

NEU=dict(
 KokosWoelkchen=dict(key='KokosWoelkchen', suess=True, hook='Nur 5 Zutaten:', titel=['KOKOS-','WÖLKCHEN'], portion='pro Stück', anzahl=30, vs=95,
  zutaten=[Z('200 g','Magerquark','magerquark','quark',200), Z('120 g','Kokosraspel','kokosraspel','kokosraspel',120), Z('60 g','Speisestärke','speisestaerke','speisestaerke',60),
           Z('60 g','Erythrit','erythrit','erythrit',60), Z('1 Stück','Ei','ei','ei',st=1)],
  ex=['1 TL Backpulver, 1 Prise Salz', 'etwas Puder-Erythrit zum Bestäuben'],
  intro='Wölkchen heißen so, weil sie auf der Zunge zergehen. Meine Kokos-Variante braucht nur 5 Zutaten und kommt ganz ohne Butter und Mehl aus: Der Quark hält sie saftig, die Stärke macht sie mürbe. In 10 Minuten gerührt, 15 Minuten im Ofen: {k} kcal pro Stück statt 95 für eine Kokosmakrone vom Bäcker!',
  schritte=['Quark, Ei, Erythrit und eine Prise Salz glatt rühren. Kokosraspel, Speisestärke und Backpulver mischen und unterrühren. Den Teig 10 Minuten quellen lassen.',
            'Mit zwei Teelöffeln 30 kleine Häufchen auf ein Backblech mit Backpapier setzen und mit feuchten Fingern rund formen.',
            'Bei 170 °C Ober-/Unterhitze 15–18 Minuten backen, bis die Unterseite leicht goldgelb ist. Oben sollen die Wölkchen hell bleiben. Abkühlen lassen und mit Puder-Erythrit bestäuben.'],
  frage='Wölkchen: lieber mit Kokos oder pur?', tags='#kokoswölkchen #wölkchen #plätzchen #weihnachtsbäckerei #fitmitkev',
  prompt='A white plate piled high with many small round snow-white coconut cookies, each cookie a soft slightly domed mound with a rough surface of fine white shredded coconut, lightly dusted with white powdered sugar, the bottoms pale golden, a few cookies lying on the table in front of the plate, one cookie broken in half showing the soft moist white crumb inside, a small white bowl of shredded coconut beside.'),
 Schichtsalat=dict(key='Schichtsalat', suess=False, hook='Am Vorabend gemacht:', titel=['SCHICHTSALAT','ÜBER NACHT'], portion='pro Portion', anzahl=6, vs=520,
  zutaten=[Z('1 Kopf','Eisbergsalat','eisbergsalat','eisbergsalat',400), Z('1 Dose','Mais','mais','mais',285), Z('200 g','Kochschinken','kochschinken','kochschinken',200),
           Z('4 Stück','Eier','eier','ei',st=4), Z('1 Stange','Lauch','lauch','lauch',150), Z('2 Stück','Äpfel','aepfel','apfel',st=2),
           Z('100 g','Reibekäse light','reibekaese_light','reibekaese',100), Z('400 g','Skyr','skyr','skyr',400)],
  ex=['2 TL Senf, 2 EL Zitronensaft', 'Salz, Pfeffer'],
  intro='Der Schichtsalat, der auf keiner Feier fehlen darf: Eisbergsalat, Lauch, Mais, Apfel, Schinken und Eier, obendrauf eine cremige Soße und Käse. Am Abend vorher schichten, über Nacht durchziehen lassen und am nächsten Tag nur noch auf den Tisch stellen. Die Soße ist aus Skyr statt aus Salatcreme: {k} kcal und {p} g Eiweiß pro Portion statt 520 für die Portion mit Salatcreme!',
  schritte=['Die Eier 10 Minuten hart kochen, abschrecken und in Scheiben schneiden. Den Eisbergsalat in feine Streifen schneiden, den Lauch in dünne Ringe, Äpfel und Schinken in kleine Würfel. Den Mais (Dose mit 285 g) abtropfen lassen.',
            'In einer großen Glasschüssel nacheinander schichten: die Hälfte vom Eisbergsalat, die Eier, den restlichen Salat mit dem Lauch, dann Mais, Apfel und Schinken.',
            'Den Skyr mit Senf, Zitronensaft, Salz, Pfeffer und 2–3 EL Wasser glatt rühren und als geschlossene Schicht darauf verstreichen. Mit dem Käse bestreuen, abdecken und über Nacht in den Kühlschrank stellen. Erst beim Servieren durchheben.'],
  frage='Schichtsalat: mit Apfel oder mit Ananas?', tags='#schichtsalat #übernachtsalat #partysalat #salat #fitmitkev',
  prompt='A large straight-sided clear glass salad bowl seen from the side, filled with clearly separated horizontal layers visible through the glass: at the bottom finely shredded pale green iceberg lettuce, then thin green and white leek rings, yellow sweet corn, small diced apple, pink diced cooked ham, round slices of hard-boiled egg pressed against the glass, on top a thick smooth white creamy dressing layer covered with finely grated pale yellow cheese. A large serving spoon lies beside the bowl.'),
 HackNudeln=dict(key='HackNudeln', suess=False, hook='Eine Pfanne, 20 Minuten:', titel=['GEBRATENE NUDELN','MIT HACK'], portion='pro Portion', anzahl=4, vs=850,
  zutaten=[Z('250 g','Mie-Nudeln','nudeln','nudeln',250), Z('400 g','Rinderhack','rinderhack','hack',400), Z('2 Stück','Karotten','karotten','karotten',150),
           Z('1 Stück','Paprika','paprika','paprika_st',st=1), Z('200 g','Weißkohl','weisskohl','weisskohl',200), Z('4 EL','Sojasauce','sojasauce','sojasauce',40),
           Z('1 EL','Öl','oel','oel',10), Z('2 Zehen','Knoblauch','knoblauch','knoblauch',6)],
  ex=['1 TL Ingwer, 2 Frühlingszwiebeln'],
  intro='Am Freitag waren die gebratenen Nudeln euer Lieblingsrezept. Hier kommt die Variante mit Hack: Mie-Nudeln, krümelig gebratenes Rinderhack, Karotten, Paprika und Weißkohl, dazu Sojasauce und Knoblauch. Alles aus einer Pfanne und in 20 Minuten fertig: {k} kcal und {p} g Eiweiß pro Portion statt 850 für die Box vom Imbiss!',
  schritte=['Die Mie-Nudeln nach Packung garen und abgießen. Mageres Rinderhack (5 % Fett) im Öl in einer großen Pfanne krümelig und kräftig braun braten.',
            'Karotten, Paprika und Weißkohl in feine Streifen schneiden, mit Knoblauch und Ingwer zum Hack geben und 4 Minuten mitbraten.',
            'Nudeln und Sojasauce zugeben, alles 2 Minuten kräftig durchschwenken und mit Frühlingszwiebeln bestreuen.'],
  frage='Gebratene Nudeln: mit Hack oder mit Hähnchen?', tags='#gebratenenudeln #hackfleisch #asiatisch #pfannengericht #fitmitkev',
  prompt='A black wok with Chinese stir-fried egg noodles mixed with plenty of browned crumbled minced beef, thin orange carrot strips, red bell pepper strips and pale green cabbage strips, glossy with soy sauce, sprinkled with green spring onion rings, one portion served in a white bowl in front with chopsticks resting on it.'),
 PizzaWrap=dict(key='PizzaWrap', suess=False, hook='Aus körnigem Frischkäse:', titel=['PIZZA-WRAP','OHNE MEHL'], portion='pro Wrap', anzahl=2, vs=650,
  zutaten=[Z('250 g','Körniger Frischkäse','huettenkaese','huettenkaese',250), Z('2 Stück','Eier','eier','ei',st=2), Z('2 TL','Italienische Kräuter','italienische_kraeuter','vanille',0),
           Z('4 EL','Passierte Tomaten','passierte_tomaten','tomaten',60), Z('60 g','Mozzarella light','mozzarella_light','mozzarella',60), Z('40 g','Salami','salami','salami',40)],
  ex=['Salz, Pfeffer'],
  intro='Der Wrap aus körnigem Frischkäse war am Freitag euer zweitliebstes Rezept. Hier kommt er als Pizza: derselbe Teig aus nur zwei Zutaten, dünn gebacken, dann mit Tomatensoße, Mozzarella und Salami belegt, eingerollt und kurz überbacken, bis der Käse zerläuft. Kein Mehl, kein Kneten: {k} kcal und {p} g Eiweiß pro Wrap statt 650 für die Pizza-Rolle vom Bäcker!',
  schritte=['Den Ofen auf 200 °C Ober-/Unterhitze vorheizen. Körnigen Frischkäse, Eier, die Hälfte der Kräuter und eine Prise Salz im Mixer ganz glatt pürieren.',
            'Die Masse auf einem Backblech mit Backpapier zu einem dünnen Rechteck (ca. 30 × 25 cm) verstreichen und 30–35 Minuten backen, bis die Oberfläche goldbraun und fest ist. Kurz abkühlen lassen und halbieren.',
            'Jede Hälfte mit passierten Tomaten bestreichen, mit den restlichen Kräutern würzen, mit geriebenem Mozzarella und Salami belegen und einrollen. Die Wraps mit der Naht nach unten 5 Minuten zurück in den Ofen geben, bis der Käse geschmolzen ist.'],
  frage='Pizza-Wrap: mit Salami oder mit Schinken?', tags='#pizzawrap #körnigerfrischkäse #ohnemehl #pizza #fitmitkev',
  prompt='Two rolled wraps made of thin golden brown baked flatbread with a slightly blistered speckled surface, each cut in half diagonally, the halves stacked on a wooden board with the cut sides facing the camera, showing a filling of red tomato sauce, stretchy melted white mozzarella cheese and round slices of red salami, a little melted cheese pulling between the halves, a few dried oregano flakes on top, a small white bowl of red tomato sauce beside.'),
 Frikassee=dict(key='Frikassee', suess=False, hook='Wie bei Oma:', titel=['HÜHNERFRIKASSEE','MIT KNÖDELN'], portion='pro Portion', anzahl=4, vs=750,
  zutaten=[Z('500 g','Hähnchenbrust','haehnchenbrust','haehnchen',500), Z('500 g','Kloßteig (Kühlregal)','kartoffelkloesse','kloesse',500), Z('250 g','Champignons','champignons','champignons',250),
           Z('150 g','Erbsen (TK)','erbsen','erbsen',150), Z('2 Stück','Karotten','karotten','karotten',150), Z('500 ml','Hühnerbrühe','huehnerbruehe','bruehe',0),
           Z('100 ml','Kochsahne (15 %)','kochsahne','kochsahne',100), Z('2 EL','Speisestärke','speisestaerke','speisestaerke',20)],
  ex=['10 g Butter, 1 EL Zitronensaft', 'Salz, Pfeffer, Muskat, Petersilie'],
  intro='Hühnerfrikassee wie bei Oma: zartes Hähnchen, Champignons, Erbsen und Karotten in heller, cremiger Soße mit einem Spritzer Zitrone. Dazu gibt es Knödel statt Reis, die nehmen die Soße so schön auf. Ein Schuss Kochsahne reicht, den Rest macht die Brühe: {k} kcal und {p} g Eiweiß pro Teller statt 750 im Gasthaus!',
  schritte=['Die Hähnchenbrust in der Brühe 15 Minuten leise gar ziehen lassen, herausnehmen und in mundgerechte Stücke schneiden. Die Brühe aufheben.',
            'Aus dem Kloßteig 16 kleine Knödel formen (4 pro Teller) und nach Packungsangabe in siedendem Salzwasser gar ziehen lassen (ca. 15 Minuten).',
            'Champignons und Karotten in Scheiben schneiden und in der Butter 5 Minuten anbraten. Mit 400 ml der Brühe und der Kochsahne aufgießen und 5 Minuten köcheln lassen. Die Speisestärke in 3 EL kaltem Wasser anrühren, einrühren und kurz aufkochen.',
            'Hähnchen und Erbsen zugeben und 3 Minuten heiß werden lassen. Mit Zitronensaft, Salz, Pfeffer und Muskat abschmecken und mit den Knödeln und gehackter Petersilie servieren.'],
  frage='Hühnerfrikassee: mit Knödeln oder mit Reis?', tags='#hühnerfrikassee #omasrezepte #fitmitkev',
  prompt='A deep white plate with creamy chicken fricassee: tender white chicken breast pieces, sliced mushrooms, green peas and round orange carrot slices in a light ivory cream sauce, sprinkled with fresh chopped green parsley, and beside the fricassee on the same plate exactly four small round pale yellow German potato dumplings, each about the size of a golf ball, lying close together in a group, all four clearly visible. One small lemon wedge lying on the rim of the plate.'),
)
for _k,_r in NEU.items(): _r['kurz']=['–','–','–']; _r['exnut']=[]
NEU['Frikassee']['exnut']=[(75,0,0,8)]   # 10 g Butter
# ---- Kloßteig-Reihe (Kev 22.11., 16:06: „ab morgen eine Rezeptreihe mit Kloßteig-Rezepten … fertiger Kloßteig“; seine drei Vorgaben für den Start) ----
# Einheitlicher Auftakt „Klöße mit“ als Schreibschrift-Zeile, der Titel nennt die Variante → die Reihe ist auf einen Blick erkennbar. 4 kleine Klöße pro Teller (Kev 15:57).
KLOSS=dict(
 KlossPaprika=dict(key='KlossPaprika', suess=False, hook='Klöße mit', titel=['PAPRIKA-SAHNE-','HÄHNCHEN'], portion='pro Portion', anzahl=4, vs=780,
  zutaten=[Z('500 g','Hähnchenbrust','haehnchenbrust','haehnchen',500), Z('500 g','Kloßteig (Kühlregal)','kartoffelkloesse','kloesse',500), Z('2 Stück','Rote Paprika','rote_paprika','paprika_st',st=2),
           Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1), Z('200 ml','Kochsahne (15 %)','kochsahne','kochsahne',200), Z('200 ml','Gemüsebrühe','gemuesebruehe','bruehe',0),
           Z('2 EL','Tomatenmark','tomatenmark','tomatenmark',30), Z('1 EL','Paprikapulver','paprikapulver','vanille',0)],
  ex=['1 EL Öl, 1 TL Speisestärke', 'Salz, Pfeffer, Petersilie'],
  intro='Paprika-Sahne-Hähnchen kennt ihr mit Reis. Probiert es mal mit Klößen: Die nehmen die cremige Paprikasoße auf wie nichts anderes. Mit fertigem Kloßteig aus dem Kühlregal steht alles in 30 Minuten auf dem Tisch, und für die Soße reicht ein Becher Kochsahne: {k} kcal und {p} g Eiweiß pro Teller statt 780 für die Variante mit Schlagsahne!',
  schritte=['Aus dem Kloßteig 16 kleine Klöße formen (4 pro Teller) und nach Packungsangabe in siedendem Salzwasser gar ziehen lassen (ca. 15 Minuten).',
            'Die Hähnchenbrust in mundgerechte Stücke schneiden, salzen, pfeffern und im heißen Öl in einer großen Pfanne rundum goldbraun anbraten. Herausnehmen.',
            'Die Zwiebel würfeln, die Paprika in Streifen schneiden und beides in derselben Pfanne 4 Minuten anbraten. Tomatenmark und Paprikapulver 1 Minute mitrösten, mit Brühe und Kochsahne ablöschen und 8 Minuten köcheln lassen. Die Speisestärke in 2 EL kaltem Wasser anrühren, einrühren und kurz aufkochen.',
            'Das Hähnchen zurück in die Soße geben und 3 Minuten heiß werden lassen. Mit Salz und Pfeffer abschmecken und mit den Klößen und gehackter Petersilie servieren.'],
  frage='Paprika-Sahne-Hähnchen: mit Klößen, Reis oder Nudeln?', tags='#paprikasahnehähnchen #klöße #fitmitkev',
  prompt='A round white dinner plate, the whole plate fully visible with empty table space left and right of it, with one golden seared chicken breast fillet and red bell pepper strips in a creamy orange-red paprika cream sauce, sprinkled with fresh chopped green parsley, and beside it on the same plate exactly four small round pale yellow matte German potato dumplings, each about the size of a golf ball, lying close together in a group, all four clearly visible.'),
 KlossGulasch=dict(key='KlossGulasch', suess=False, hook='Klöße klassisch mit', titel=['ROTKOHL','UND GULASCH'], portion='pro Portion', anzahl=4, vs=900,
  zutaten=[Z('500 g','Rindergulasch (mager)','rindergulasch','rind',500), Z('500 g','Kloßteig (Kühlregal)','kartoffelkloesse','kloesse',500), Z('600 g','Rotkohl (Glas)','rotkohl','rotkohl',600),
           Z('2 Stück','Zwiebeln','zwiebeln','zwiebel',st=2), Z('2 EL','Tomatenmark','tomatenmark','tomatenmark',30), Z('500 ml','Rinderbrühe','rinderbruehe','bruehe',0),
           Z('1 EL','Paprikapulver','paprikapulver','vanille',0), Z('1 EL','Speisestärke','speisestaerke','speisestaerke',10)],
  ex=['1 EL Öl, 2 Lorbeerblätter', 'Salz, Pfeffer, Majoran'],
  intro='Klöße, Rotkohl und Gulasch: Mehr Winter passt nicht auf einen Teller. Das Gulasch schmort mit vielen Zwiebeln, bis das Fleisch zerfällt, und die Soße braucht weder Mehlschwitze noch Sahne. Die Klöße sind aus fertigem Kloßteig in 15 Minuten gemacht, der Rotkohl kommt aus dem Glas: {k} kcal und {p} g Eiweiß pro Teller statt 900 im Gasthaus!',
  schritte=['Das Rindergulasch in kleine Würfel (ca. 2 cm) schneiden, dann wird es schneller weich. Im heißen Öl in einem Topf portionsweise kräftig anbraten. Die Zwiebeln würfeln und 5 Minuten mitbraten. Tomatenmark und Paprikapulver 1 Minute mitrösten.',
            'Mit der Brühe ablöschen, Lorbeer und Majoran zugeben und zugedeckt bei kleiner Hitze 75–90 Minuten schmoren, bis das Fleisch zart ist. Die Speisestärke in 2 EL kaltem Wasser anrühren, einrühren und kurz aufkochen. Mit Salz und Pfeffer abschmecken.',
            'Aus dem Kloßteig 16 kleine Klöße formen (4 pro Teller) und nach Packungsangabe in siedendem Salzwasser gar ziehen lassen (ca. 15 Minuten). Den Rotkohl erwärmen und alles zusammen anrichten.'],
  frage='Zum Gulasch: Klöße, Nudeln oder Kartoffeln?', tags='#gulasch #rotkohl #klöße #omasrezepte #fitmitkev',
  prompt='A round white dinner plate, the whole plate fully visible with empty table space left and right of it, with a portion of dark red-brown beef goulash with tender beef chunks in glossy dark brown gravy, beside it a portion of shiny purple braised red cabbage, and on the same plate exactly four small round pale yellow matte German potato dumplings, each about the size of a golf ball, lying close together in a group, all four clearly visible, a little chopped green parsley on the dumplings.'),
 KlossTomMozz=dict(key='KlossTomMozz', suess=False, hook='Klöße mit', titel=['TOMATE-MOZZARELLA','ÜBERBACKEN'], portion='pro Portion', anzahl=4, vs=700,
  zutaten=[Z('750 g','Kloßteig (Kühlregal)','kartoffelkloesse','kloesse',750), Z('500 g','Passierte Tomaten','passierte_tomaten','tomaten',500), Z('250 g','Mozzarella light','mozzarella_light','mozzarella',250),
           Z('3 Stück','Tomaten','frische_tomaten','tomate',300), Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1), Z('2 Zehen','Knoblauch','knoblauch','knoblauch',6),
           Z('2 TL','Italienische Kräuter','italienische_kraeuter','vanille',0), Z('1 Handvoll','Basilikum','basilikum','vanille',0)],
  ex=['1 EL Olivenöl', 'Salz, Pfeffer'],
  intro='Klöße mal ganz anders: in fruchtiger Tomatensoße, mit Tomatenscheiben und Mozzarella belegt und im Ofen überbacken, bis der Käse goldgelb zerläuft. Schmeckt wie Gnocchi-Auflauf, ist aber aus fertigem Kloßteig in 15 Minuten vorbereitet, den Rest macht der Ofen: {k} kcal und {p} g Eiweiß pro Portion statt 700 für den Gnocchi-Auflauf beim Italiener!',
  schritte=['Den Ofen auf 200 °C Ober-/Unterhitze vorheizen. Aus dem Kloßteig 12 Klöße formen (3 pro Portion) und in siedendem Salzwasser 10 Minuten vorgaren.',
            'Zwiebel und Knoblauch fein würfeln und im Olivenöl 3 Minuten anschwitzen. Passierte Tomaten und Kräuter zugeben, mit Salz und Pfeffer würzen und 5 Minuten köcheln lassen. Die Soße in eine Auflaufform (ca. 20 × 30 cm) geben.',
            'Die Klöße in die Soße setzen. Tomaten und Mozzarella in Scheiben schneiden und darauf verteilen. 15–20 Minuten überbacken, bis der Käse goldgelb ist, und mit Basilikum bestreuen.'],
  frage='Klöße: lieber überbacken oder klassisch mit Soße?', tags='#klöße #tomatemozzarella #fitmitkev',
  prompt='A white rectangular ceramic baking dish with two handles, both handles fully visible, the whole dish centered with empty table space left and right of it, seen from above at a 45 degree angle, filled with round pale yellow German potato dumplings sitting in bright red tomato sauce, between and on the dumplings slices of red tomato topped with round slices of melted white mozzarella cheese with golden brown spots from the oven, fresh green basil leaves scattered on top. In front of the baking dish a small white plate with exactly three round potato dumplings in red tomato sauce, topped with a slice of tomato and melted mozzarella.'),
)
for _k,_r in KLOSS.items(): _r['kurz']=['–','–','–']; _r['exnut']=[(90,0,0,10)]   # 1 EL Öl
KLOSS['KlossPaprika']['exnut']=[(90,0,0,10),(17,0,4,0)]   # dazu 1 TL Speisestärke
R=[NEU['KokosWoelkchen'], NEU['Schichtsalat'], NEU['HackNudeln'], NEU['PizzaWrap'], NEU['Frikassee'], KLOSS['KlossPaprika'], KLOSS['KlossGulasch'], KLOSS['KlossTomMozz']]   # Frikassee: Kev 22.11., 15:49 „Rinder Rouladen bitte raus – dafür Knödel mit Hühnerfrikassee rein“; 15:57 „Bitte auf dem Teller 4 Knödel“ → 16 kleine Knödel aus 500 g Kloßteig, 4 pro Teller

if __name__=='__main__':
    for r in R:
        k,p,c,f=macros4(r); assert r['vs']>k and len(r['zutaten'])<=8 and k<=500, r['key']
        txt=r['intro']+' '.join(r['schritte'])+r['frage']
        for w in ('abnehm','esn ','melly','gta','ohne zucker','satt','miracel'): assert w not in txt.lower(), (r['key'],w)
        print(f"{r['key']:16s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P {c:3d}K {f:2d}F {r['portion']} × {r['anzahl']} vs {r['vs']}")
    print('ok')
