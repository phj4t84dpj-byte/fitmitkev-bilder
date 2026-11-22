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
for _k,_v in {'eisbergsalat':(14,1,2,0.2), 'weisskohl':(25,1.3,4,0.2), 'sojasauce':(60,8,6,0)}.items(): NUT.setdefault(_k,_v)   # bestehende Werte nicht überschreiben

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
            'In einer großen Glasschüssel nacheinander schichten: Eisbergsalat, Lauch, Mais, Apfel, Schinken und Eier.',
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
)
for _k,_r in NEU.items(): _r['kurz']=['–','–','–']; _r['exnut']=[]
R=[NEU['KokosWoelkchen'], NEU['Schichtsalat'], NEU['HackNudeln'], NEU['PizzaWrap']]

if __name__=='__main__':
    for r in R:
        k,p,c,f=macros4(r); assert r['vs']>k and len(r['zutaten'])<=8 and k<=500, r['key']
        txt=r['intro']+' '.join(r['schritte'])+r['frage']
        for w in ('abnehm','esn ','melly','gta','ohne zucker','satt','miracel'): assert w not in txt.lower(), (r['key'],w)
        print(f"{r['key']:16s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P {c:3d}K {f:2d}F {r['portion']} × {r['anzahl']} vs {r['vs']}")
    print('ok')
