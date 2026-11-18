# -*- coding: utf-8 -*-
# G97 – Donnerstag 19.11.2026 (ESN-Start), Stufenplan 23 Beiträge: 20 Rezepte + 2 ESN-Rezepte (6:10, 13:00, schon eingeplant) + 17:30 persönlicher Beitrag (offen).
# Auswahl nach der 7-Tage-Regel: Donnerstag 12.11. (G90) genau 7 Tage später (ohne Schokomousse/Tiramisu-Skyr-Kuchen – am selben Tag laufen
#   ESN-Schoko-Mousse und ESN-Tiramisu-Bowl) + ausgeruhte Treffer vom 9./10.11. (Nussecken-Bowl 152k, Schwarzwälder, Bienenstich, Bratapfel-Skyr, Senfeier, Käse-Lauch-Suppe).
# Alle ohne Box (Kev 16.11.). 1 Buch-Zeile (Kokosmakronen → Weihnachtsbäckerei), keine ESN-Zeile in diesen 20.
# Hashtag-Gruppen gegenüber Mittwoch getauscht: A (2–3) = 1,2,5,6,9,11,14,15,17,18 · B (4–5) = übrige (je 5 süß / 5 herzhaft).
import sys, os, copy
_D=os.path.dirname(os.path.abspath(__file__))
for g in ('g87','g88','g89','g90','g91','g92','g93','g93n','g94','g95'): sys.path.insert(0, os.path.join(_D, '..', g))
from g90_data import NUT, PIECE, nut, Z, macros4
import g87_data, g88_data, g90_data
_A={}
for m in (g87_data, g88_data, g90_data):
    for r in m.R: _A[r['key']]=r
def alt(key, tags, **kw):
    r=copy.deepcopy(_A[key]); r['tags']=tags; r['kurz']=r.get('kurz') or ['–','–','–']
    for x in ('fb','hinweis','n','buch'): r.pop(x,None)
    r.update(kw); return r
BUCH='📖 Diese Kokosmakronen findest du auch in meinem Rezeptbuch „Weihnachtsbäckerei in leicht“, zusammen mit 35 weiteren Rezepten: https://fitmitkev.de/rezeptbuecher'
_mw=_A['MaulwurfBowl']['intro'].replace('Euer Wunsch aus den Kommentaren: Maulwurfkuchen','Maulwurfkuchen')

# ---- Kev 18.11., 11:41: „Lass bereits ab morgen mit körnigem Frischkäse anfangen, teste verschiedene Hooks“ ----
# 3 neue Rezepte ersetzen Strammer Max (#3), Käse-Lauch-Suppe (#7) und Mohn-Streuselkuchen (#18). Hook-Test (Schriftzug über dem Titel):
#   H1 „Aus körnigem Frischkäse:“ (Kevs Favorit) · H2 „Der Trend aus dem Netz:“ · H3 „Geheimzutat:“ – ab Freitag rotieren.
NUT.update({'eisbergsalat':(14,1,2,0.2), 'butterkekse':(435,7,73,12)})
KF=dict(
 KFFladen=dict(key='KFFladen', suess=False, hook='Aus körnigem Frischkäse:', titel=['FLADENBROT MIT','NUR 2 ZUTATEN'], portion='pro Wrap', anzahl=2, vs=550,
  zutaten=[Z('250 g','Körniger Frischkäse','huettenkaese','huettenkaese',250), Z('2 Stück','Eier','eier','ei',st=2),
           Z('1 TL','Italienische Kräuter','italienische_kraeuter','vanille',0), Z('80 g','Putenschinken','putenschinken','putenschinken',80),
           Z('40 g','Frischkäse light','frischkaese_light','frischkaese',40), Z('50 g','Eisbergsalat','eisbergsalat','eisbergsalat',50),
           Z('½ Stück','Salatgurke','salatgurke','gurke',100)],
  ex=['Salz, Pfeffer, ½ TL Paprikapulver'],
  intro='Das Fladenbrot, das gerade überall im Netz auftaucht: nur körniger Frischkäse und Eier, glatt püriert und dünn aufs Blech gestrichen. Kein Mehl, kein Kneten, keine Gehzeit. Gefüllt mit Putenschinken, Salat und Gurke wird daraus ein Wrap: {k} kcal und {p} g Eiweiß pro Wrap statt 550 für den Wrap vom Bäcker!',
  schritte=['Den Ofen auf 200 °C Ober-/Unterhitze vorheizen. Körnigen Frischkäse, Eier, Kräuter, Salz und Paprikapulver im Mixer ganz glatt pürieren.',
            'Die Masse auf einem Backblech mit Backpapier zu einem dünnen Rechteck (ca. 30 × 25 cm) verstreichen und 30–35 Minuten backen, bis die Oberfläche goldbraun und fest ist. Kurz abkühlen lassen und halbieren.',
            'Jede Hälfte mit Frischkäse bestreichen, mit Putenschinken, Salat und Gurkenscheiben belegen und einrollen.'],
  frage='Fladenbrot aus körnigem Frischkäse: Hast du das schon ausprobiert?', tags='#körnigerfrischkäse #hüttenkäse #wrap #ohnemehl #fitmitkev',
  prompt='Two homemade golden brown thin flatbreads baked from blended cottage cheese and egg, with a slightly blistered speckled golden surface, one rolled up like a wrap and cut in half, filled with pink turkey ham slices, crisp green iceberg lettuce and cucumber slices, the two halves standing upright in front on a wooden board showing the filling, the second flat golden flatbread lying behind, a small white bowl of cottage cheese beside.'),
 KFKaesenudeln=dict(key='KFKaesenudeln', suess=False, hook='Geheimzutat:', titel=['KÄSENUDELN MIT','KÖRNIGEM FRISCHKÄSE'], portion='pro Portion', anzahl=4, vs=750,
  zutaten=[Z('250 g','Nudeln (roh)','nudeln','nudeln',250), Z('400 g','Körniger Frischkäse','huettenkaese','huettenkaese',400),
           Z('100 ml','Milch (1,5 %)','milch','milch',100), Z('80 g','Reibekäse light','reibekaese_light','reibekaese',80),
           Z('300 g','Brokkoli','brokkoli','brokkoli',300), Z('1 TL','Senf','senf','senf',5)],
  ex=['Salz, Pfeffer, Muskat, ½ TL Paprikapulver'],
  intro='Cremige Käsenudeln wie Mac and Cheese, aber die Soße ist aus körnigem Frischkäse: einfach mit Milch glatt pürieren, Käse rein, fertig. Keine Sahne, keine Mehlschwitze, dazu Brokkoli. Ein Topf, 20 Minuten: {k} kcal und {p} g Eiweiß pro Portion statt 750 für Mac and Cheese mit Sahne!',
  schritte=['Die Nudeln in Salzwasser bissfest kochen, in den letzten 4 Minuten die Brokkoli-Röschen mitgaren und alles abgießen.',
            'Körnigen Frischkäse, Milch und Senf im Mixer ganz glatt pürieren, in den heißen Topf geben und bei kleiner Hitze mit dem Reibekäse schmelzen lassen (nicht kochen). Mit Salz, Pfeffer, Muskat und Paprikapulver würzen.',
            'Nudeln und Brokkoli unter die Käsesoße heben und sofort servieren.'],
  frage='Käsenudeln: mit Brokkoli oder lieber mit Schinken?', tags='#körnigerfrischkäse #käsenudeln #macandcheese #familienessen #fitmitkev',
  prompt='A wide white ceramic bowl filled with creamy short macaroni pasta in a smooth glossy pale yellow cheese sauce with bright green broccoli florets mixed in, a little melted grated cheese, black pepper and paprika on top, a fork beside the bowl, a small white bowl of cottage cheese and a few broccoli florets beside.'),
 KFKaesekuchen=dict(key='KFKaesekuchen', suess=True, hook='Der Trend aus dem Netz:', titel=['KÄSEKUCHEN AUS','KÖRNIGEM FRISCHKÄSE'], portion='pro Stück', anzahl=8, vs=350,
  zutaten=[Z('600 g','Körniger Frischkäse','huettenkaese','huettenkaese',600), Z('3 Stück','Eier','eier','ei',st=3),
           Z('1 Päckchen','Vanillepudding-Pulver','vanillepudding_pulver','puddingpulver',37), Z('70 g','Erythrit','erythrit','erythrit',70),
           Z('1 Stück','Zitrone (Abrieb)','zitrone','zitrone',0), Z('1 TL','Vanilleextrakt','vanilleextrakt','vanille',0),
           Z('80 g','Butterkekse','butterkekse','butterkekse',80), Z('20 g','Butter','butter','butter',20)],
  ex=[],
  intro='Käsekuchen aus körnigem Frischkäse: püriert wird er so cremig, dass niemand die Körnchen erkennt. Dünner Keksboden, ohne Quark, ohne Zucker, die Füllung einfach im Mixer: {k} kcal und {p} g Eiweiß pro Stück statt 350 für das Stück Käsekuchen vom Bäcker!',
  schritte=['Den Ofen auf 160 °C Ober-/Unterhitze vorheizen. Butterkekse fein zerbröseln, mit der geschmolzenen Butter mischen und in eine Springform (20 cm) mit Backpapier drücken.',
            'Körnigen Frischkäse, Eier, Puddingpulver, Erythrit, Zitronenabrieb und Vanille im Mixer 1–2 Minuten ganz glatt pürieren, auf den Boden gießen und 50–55 Minuten backen, bis die Mitte nur noch leicht wackelt.',
            'Im ausgeschalteten Ofen bei leicht geöffneter Tür abkühlen lassen und mindestens 3 Stunden kalt stellen.'],
  frage='Käsekuchen aus körnigem Frischkäse: Würdest du den Unterschied schmecken?', tags='#körnigerfrischkäse #käsekuchen #fitmitkev',
  prompt='A round crustless German cheesecake about 5 cm tall with a golden brown top and slightly browned edges on a white cake stand seen from the side, one slice cut and placed on a small white plate in front showing the smooth creamy pale yellow inside, a little fresh lemon zest on top, one plain straight teaspoon on the plate, a small white bowl of cottage cheese and half a lemon beside.'),
)
for _k,_r in KF.items(): _r['kurz']=['–','–','–']; _r['exnut']=[]

# ---- Kev 18.11., 11:48: „Alles was schlecht läuft bitte raus und teste dafür Neues – Daten der letzten 14 Tage“ ----
# Letzter Lauf (Reichweite ÷ Median des Tages, Metricool 18.11.): Quiche 0,24 · Strammer Max 0,27 · Cordon Bleu 0,35 · Bratapfel-Skyr-Kuchen 0,50 ·
#   Engelsaugen 0,51 · Gnocchi-Auflauf 0,52 · Frühstücksbrötchen 0,58 · Senfeier 0,91 (10k) · Käse-Lauch-Suppe 0,96 (11k, Suppen allgemein schwach) · Mohn-Streusel 1,09 (12k).
#   Raus damit, ersetzt durch 10 neue Tests (3× körniger Frischkäse oben + 7 neue Rezepte aus den Treffer-Familien: Bowls „nur für dich“, Kalter Hund,
#   Lasagne, Pizza, Cheeseburger, gebratene Nudeln, herzhafte Waffeln).
NUT.update({'schokolade':(530,8,30,40), 'weisskohl':(25,1.4,4,0.2), 'sojasauce':(60,8,6,0), 'blaubeeren':(40,0.6,6,0.4)})
NEU=dict(
 PizzaWaffeln=dict(key='PizzaWaffeln', suess=False, hook='Herzhaft aus dem Waffeleisen:', titel=['PIZZA-','WAFFELN'], portion='pro Waffel', anzahl=6, vs=280,
  zutaten=[Z('150 g','Dinkelmehl','dinkelmehl','dinkelmehl',150), Z('200 g','Skyr','skyr','skyr',200), Z('2 Stück','Eier','eier','ei',st=2),
           Z('1 TL','Backpulver','backpulver','backpulver',4), Z('60 g','Salami','salami','salami',60), Z('60 g','Reibekäse light','reibekaese_light','reibekaese',60),
           Z('1 TL','Pizza-Kräuter','pizza_kraeuter','vanille',0), Z('150 g','Passierte Tomaten','passierte_tomaten','tomaten',150)],
  ex=['Salz, Pfeffer'],
  intro='Pizza aus dem Waffeleisen: Skyr-Teig mit Salami und Käse direkt im Teig, außen knusprig, innen saftig, zum Dippen eine schnelle Tomatensoße. Fertig in 15 Minuten und perfekt für die Brotdose: {k} kcal und {p} g Eiweiß pro Waffel statt 280 für ein Stück Pizza vom Blech!',
  schritte=['Mehl, Skyr, Eier, Backpulver, Pizza-Kräuter und eine Prise Salz zu einem dicken Teig verrühren. Salami klein schneiden und mit dem Käse unterheben.',
            'Das Waffeleisen leicht einfetten und aus dem Teig nacheinander 6 Waffeln je 3–4 Minuten goldbraun backen.',
            'Passierte Tomaten mit Salz, Pfeffer und etwas Pizza-Kräutern kurz aufkochen und als Dip zu den Waffeln servieren.'],
  frage='Pizza-Waffeln: mit Salami oder mit Schinken?', tags='#pizzawaffeln #waffeln #fitmitkev',
  prompt='A stack of golden brown savory heart-shaped waffles with visible pieces of red salami and melted cheese baked into the batter, one waffle broken open showing the soft inside with salami pieces, a small bowl of red tomato dipping sauce beside, a few basil leaves, on a wooden board.'),
 CheeseburgerBowl=dict(key='CheeseburgerBowl', suess=False, hook='Nur für dich:', titel=['CHEESEBURGER-','BOWL'], portion='die ganze Bowl', anzahl=1, vs=850,
  zutaten=[Z('125 g','Rinderhack (mager)','rinderhack','hack',125), Z('150 g','Kartoffeln','kartoffeln','kartoffeln',150), Z('½ Stück','Zwiebel','zwiebel','zwiebel',st=0.5),
           Z('20 g','Reibekäse light','reibekaese_light','reibekaese',20), Z('2 Stück','Gewürzgurken','gewuerzgurken','gurken',40),
           Z('50 g','Skyr','skyr','skyr',50), Z('1 EL','Ketchup','ketchup','ketchup',15), Z('1 TL','Senf','senf','senf',5)],
  ex=['½ Tomate, Salz, Pfeffer, ½ TL Paprikapulver'],
  intro='Cheeseburger mit Pommes als Bowl nur für dich, aus dem Ofen: unten knusprige Ofen-Pommes, darauf ein saftiges Patty mit geschmolzenem Käse, Tomate und Gewürzgurken, obendrauf die Burgersoße aus Skyr, Ketchup und Senf. {k} kcal und {p} g Eiweiß die ganze Bowl statt 850 für Burger mit Pommes!',
  schritte=['Kartoffeln in Pommes-Stifte schneiden, salzen und in einer kleinen gefetteten Glasform (15 × 10 cm) bei 220 °C Ober-/Unterhitze 20 Minuten knusprig backen.',
            'Hack mit fein gehackter Zwiebel, Salz, Pfeffer und Paprikapulver verkneten, zu einem flachen Patty formen und in einer beschichteten Pfanne von jeder Seite 3 Minuten braten. Auf die Pommes setzen, Käse darauf und 3 Minuten im Ofen schmelzen lassen.',
            'Skyr mit Ketchup und Senf verrühren, mit ein paar Tomatenscheiben und den Gewürzgurken auf das Patty geben.'],
  frage='Cheeseburger: mit Gurke oder ohne?', tags='#cheeseburger #bowl #fitmitkev',
  prompt='A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, layers visible through the glass: golden crispy roasted potato cubes at the bottom, browned ground beef with onions and melted cheese on top, pickle slices and a drizzle of pink burger sauce, one plain fork beside the dish, a small bowl of pickles beside.'),
 KalterHundBowl=dict(key='KalterHundBowl', suess=True, hook='Nur für dich:', titel=['KALTER-HUND-','BOWL'], portion='die ganze Bowl', anzahl=1, vs=600,
  zutaten=[Z('6 Stück','Butterkekse','butterkekse','butterkeks',st=6), Z('150 g','Skyr','skyr','skyr',150), Z('10 g','Backkakao','backkakao','kakao',10),
           Z('15 g','Erythrit','erythrit','erythrit',15), Z('15 g','Zartbitterschokolade','zartbitterschokolade','schokolade',15), Z('2 EL','Milch (1,5 %)','milch','milch',30)],
  ex=[],
  intro='Kalter Hund wie bei Oma, nur als Bowl für dich allein: Butterkekse und Schoko-Skyr-Creme in Schichten, obendrauf geschmolzene Zartbitterschokolade. Ohne Kokosfett, ohne Backen, über Nacht im Kühlschrank: {k} kcal und {p} g Eiweiß die ganze Bowl statt 600 für zwei Stücke Kalter Hund!',
  schritte=['Skyr, Backkakao, Erythrit und Milch zu einer glatten Schoko-Creme rühren.',
            'In einer kleinen Glasform (15 × 10 cm) abwechselnd Butterkekse und Creme schichten, mit Creme abschließen.',
            'Die Schokolade schmelzen, darüber streichen und mindestens 3 Stunden kalt stellen.'],
  frage='Kalter Hund: Kennst du ihn noch von Kindergeburtstagen?', tags='#kalterhund #bowl #fitmitkev',
  prompt='A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, many thin layers visible through the glass: pale butter biscuits alternating with dark chocolate cream, a glossy dark chocolate layer on top; about one quarter eaten from the back corner, one plain straight teaspoon resting inside, nothing on the spoon, two butter biscuits beside the dish.'),
 LasagneRoellchen=dict(key='LasagneRoellchen', suess=False, hook='Mal anders:', titel=['LASAGNE-','RÖLLCHEN'], portion='pro Portion', anzahl=4, vs=750,
  zutaten=[Z('8 Stück','Lasagneplatten','lasagneplatten','lasagneplatten',160), Z('400 g','Rinderhack (mager)','rinderhack','hack',400),
           Z('400 g','Passierte Tomaten','passierte_tomaten','tomaten',400), Z('250 g','Skyr','skyr','skyr',250), Z('1 Stück','Ei','ei','ei',st=1),
           Z('125 g','Mozzarella light','mozzarella_light','mozzarella',125), Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1), Z('1 TL','Italienische Kräuter','italienische_kraeuter','vanille',0)],
  ex=['Salz, Pfeffer, 1 Knoblauchzehe'],
  intro='Lasagne mal anders: Die Platten werden gekocht, mit Hacksoße und Skyr-Creme bestrichen und aufgerollt. Nebeneinander in der Form, Tomatensoße und Mozzarella drüber, ab in den Ofen. Sieht nach Restaurant aus, ist aber einfacher als jede Lasagne: {k} kcal und {p} g Eiweiß pro Portion statt 750 für Lasagne mit Béchamel!',
  schritte=['Die Lasagneplatten 6 Minuten in Salzwasser vorkochen und nebeneinander auf ein Brett legen. Hack mit Zwiebel und Knoblauch anbraten, 200 g passierte Tomaten zugeben und würzen.',
            'Skyr mit Ei, Salz und Pfeffer verrühren. Jede Platte mit Skyr-Creme und Hacksoße bestreichen, aufrollen und hochkant in eine Auflaufform setzen.',
            'Restliche Tomaten mit Kräutern darüber gießen, mit Mozzarella belegen und bei 200 °C Ober-/Unterhitze 25 Minuten überbacken.'],
  frage='Lasagne: klassisch geschichtet oder als Röllchen?', tags='#lasagneröllchen #fitmitkev',
  prompt='A rectangular white ceramic baking dish with eight lasagne roll-ups standing upright side by side, each spiral clearly showing layers of pasta, meat sauce and white cream, covered with red tomato sauce and golden browned melted mozzarella, fresh basil on top, two rolls served on a white plate in front, a fork beside.'),
 PizzaAuflauf=dict(key='PizzaAuflauf', suess=False, hook='Pizza trifft Auflauf:', titel=['PIZZA-','NUDELAUFLAUF'], portion='pro Portion', anzahl=4, vs=850,
  zutaten=[Z('250 g','Nudeln (roh)','nudeln','nudeln',250), Z('400 g','Passierte Tomaten','passierte_tomaten','tomaten',400), Z('60 g','Salami','salami','salami',60),
           Z('200 g','Champignons','champignons','champignons',200), Z('1 Stück','Paprika','paprika','paprika_st',st=1), Z('125 g','Mozzarella light','mozzarella_light','mozzarella',125),
           Z('100 g','Skyr','skyr','skyr',100), Z('1 TL','Pizza-Kräuter','pizza_kraeuter','vanille',0)],
  ex=['Salz, Pfeffer'],
  intro='Pizza und Nudelauflauf in einer Form: Nudeln in Tomatensoße mit Champignons und Paprika, obendrauf Salami und Mozzarella wie auf der Pizza. Die Soße wird mit Skyr cremig, ganz ohne Sahne: {k} kcal und {p} g Eiweiß pro Portion statt 850 für eine Pizza vom Lieferdienst!',
  schritte=['Die Nudeln 2 Minuten kürzer als auf der Packung kochen. Champignons in Scheiben und Paprika in Würfel schneiden.',
            'Passierte Tomaten mit Skyr, Pizza-Kräutern, Salz und Pfeffer verrühren, mit Nudeln und Gemüse mischen und in eine Auflaufform (20 × 30 cm) geben.',
            'Mit Salami und Mozzarella belegen und bei 200 °C Ober-/Unterhitze 20 Minuten backen, bis der Käse goldbraun ist.'],
  frage='Pizza-Auflauf: mit Salami oder mit Schinken?', tags='#pizzaauflauf #nudelauflauf #pizza #familienessen #fitmitkev',
  prompt='A rectangular white ceramic baking dish with a pasta bake topped like a pizza: golden browned bubbling melted mozzarella with slices of red salami, sliced mushrooms and bits of red bell pepper, short pasta in red tomato sauce visible at the edge, one portion served on a white plate in front, oregano sprinkled on top, a fork beside.'),
 ChowMein=dict(key='ChowMein', suess=False, hook='Wie vom Asia-Imbiss:', titel=['GEBRATENE','NUDELN'], portion='pro Portion', anzahl=4, vs=800,
  zutaten=[Z('250 g','Mie-Nudeln','nudeln','nudeln',250), Z('400 g','Hähnchenbrust','haehnchenbrust','haehnchen',400), Z('2 Stück','Karotten','karotten','karotten',150),
           Z('1 Stück','Paprika','paprika','paprika_st',st=1), Z('200 g','Weißkohl','weisskohl','weisskohl',200), Z('4 EL','Sojasauce','sojasauce','sojasauce',40),
           Z('1 EL','Öl','oel','oel',10), Z('2 Zehen','Knoblauch','knoblauch','knoblauch',6)],
  ex=['1 TL Ingwer, 2 Frühlingszwiebeln'],
  intro='Gebratene Nudeln wie vom Asia-Imbiss, nur ohne Fett-Schwimmbad: Mie-Nudeln mit Hähnchen, Karotten, Paprika und Weißkohl scharf aus der Pfanne, dazu Sojasauce und Knoblauch. 20 Minuten, eine Pfanne: {k} kcal und {p} g Eiweiß pro Portion statt 800 für die Box vom Imbiss!',
  schritte=['Die Mie-Nudeln nach Packung garen und abgießen. Hähnchen in Streifen schneiden und im Öl in einer großen Pfanne scharf anbraten.',
            'Karotten, Paprika und Weißkohl in feine Streifen schneiden, mit Knoblauch und Ingwer 4 Minuten mitbraten.',
            'Nudeln und Sojasauce zugeben, alles 2 Minuten kräftig durchschwenken und mit Frühlingszwiebeln bestreuen.'],
  frage='Gebratene Nudeln: mit Hähnchen oder mit Ei?', tags='#gebratenenudeln #chowmein #asiatisch #hähnchen #fitmitkev',
  prompt='A black wok with Chinese stir-fried egg noodles (chow mein) with browned chicken strips, thin orange carrot strips, red bell pepper strips and green cabbage, glossy with soy sauce, sprinkled with green spring onion rings and sesame, one portion served in a white bowl in front with chopsticks resting on it.'),
 KFPancakes=dict(key='KFPancakes', suess=True, hook='Aus körnigem Frischkäse:', titel=['FLUFFIGE','PANCAKES'], portion='pro Portion', anzahl=2, vs=550,
  zutaten=[Z('200 g','Körniger Frischkäse','huettenkaese','huettenkaese',200), Z('2 Stück','Eier','eier','ei',st=2), Z('60 g','Zarte Haferflocken','zarte_haferflocken','haferflocken',60),
           Z('1 TL','Backpulver','backpulver','backpulver',4), Z('15 g','Erythrit','erythrit','erythrit',15), Z('150 g','Blaubeeren (TK)','blaubeeren','blaubeeren',150)],
  ex=['1 TL Öl für die Pfanne'],
  intro='Pancakes aus körnigem Frischkäse: Alles kommt in den Mixer, kein Mehl, kein Zucker, und sie werden so fluffig wie im Café. Dazu warme Blaubeeren (TK) aus der Pfanne: {k} kcal und {p} g Eiweiß pro Portion statt 550 für Pancakes mit Sirup!',
  schritte=['Körnigen Frischkäse, Eier, Haferflocken, Backpulver und Erythrit im Mixer glatt pürieren und 5 Minuten quellen lassen.',
            'Eine beschichtete Pfanne mit wenig Öl auspinseln und aus dem Teig 8 kleine Pancakes von jeder Seite 2 Minuten goldbraun backen.',
            'Die Blaubeeren in einem kleinen Topf 3 Minuten erwärmen und über die Pancakes geben.'],
  frage='Pancakes: mit Blaubeeren oder mit Apfelmus?', tags='#körnigerfrischkäse #pancakes #frühstück #fitmitkev',
  prompt='A tall stack of six thick fluffy golden pancakes on a white plate, warm blueberry compote with whole blueberries running down the sides, a few fresh blueberries on the plate, one plain straight fork beside the plate, a small white bowl of cottage cheese beside.'),
)
for _k,_r in NEU.items(): _r['kurz']=['–','–','–']; _r['exnut']=[]
R=[
 NEU['PizzaWaffeln'],                       # 1 A herz
 alt('ZimtschneckenOats','#overnightoats #zimtschnecken #fitmitkev'),                 # 2 A süß
 KF['KFFladen'],                                                                    # 3 B herz (körniger Frischkäse, Hook H1)
 alt('NusseckenBowl','#nussecken #bowl #backen #lecker #fitmitkev'),                  # 4 B süß
 NEU['CheeseburgerBowl'],                                              # 5 A herz
 NEU['KalterHundBowl'],                             # 6 A süß
 KF['KFKaesenudeln'],                                                               # 7 B herz (körniger Frischkäse, Hook H3)
 alt('SpekKaeseBowl','#spekulatius #käsekuchen #bowl #fitmitkev'),                    # 8 B süß
 alt('Lasagne','#lasagne #auflauf #fitmitkev'),                                       # 9 A herz
 NEU['PizzaAuflauf'],                         # 10 B herz
 alt('Kokosmakronen','#kokosmakronen #plätzchen #fitmitkev', hinweis=BUCH),           # 11 A süß
 NEU['ChowMein'],            # 12 B herz
 alt('ZimtstreuselSkyr','#skyrkuchen #zimtstreusel #backen #fitmitkev'),              # 13 B süß
 NEU['LasagneRoellchen'],                                # 14 A herz
 alt('SchwarzwaelderSkyr','#schwarzwälderkirsch #fitmitkev'),                         # 15 A süß
 alt('MaulwurfBowl','#maulwurfkuchen #bowl #backen #fitmitkev', hook='Nur für dich:', intro=_mw),   # 16 B süß
 alt('CheeseburgerLasagne','#cheeseburger #lasagne #fitmitkev'),                      # 17 A herz
 KF['KFKaesekuchen'],                                                               # 18 A süß (körniger Frischkäse, Hook H2)
 alt('Kaesespaetzle','#käsespätzle #hütte #omasrezepte #fitmitkev'),                  # 19 B herz
 NEU['KFPancakes'],      # 20 B süß
]
ZEITEN=['06:50','07:30','08:15','08:55','09:35','10:15','10:55','11:40','12:20',
        '13:40','14:15','14:55','15:35','16:15','16:50',
        '18:10','18:50','19:25','20:05','20:45']
FEST={'06:10':'ESN Schoko-Mousse (eingeplant)','13:00':'ESN Tiramisu-Bowl (eingeplant)','17:30':'persönlicher Beitrag „Was ich an einem Tag esse“ (offen)'}
GRUPPE_A={1,2,5,6,9,11,14,15,17,18}
HASHTAG_SOLL={i+1:len(r['tags'].split()) for i,r in enumerate(R)}
OHNE_BOX=set(range(1,21))
VORHANDEN=set()
if __name__=='__main__':
    assert len(R)==20 and len({r['key'] for r in R})==20 and len(ZEITEN)==20
    SW=[False,True,False,True,False,True,False,True,False,False,True,False,True,False,True,True,False,True,False,True]
    for i,r in enumerate(R,1):
        k,p,c,f=macros4(r); nt=len(r['tags'].split())
        assert (nt<=3)==(i in GRUPPE_A) and (2<=nt<=5), (i,r['key'],nt)
        assert r['tags'].split()[-1]=='#fitmitkev'
        assert r['suess']==SW[i-1], ('süß/herzhaft',i,r['key'])
        assert r['vs']>k and len(r['zutaten'])<=8, r['key']
        txt=r['intro']+' '.join(r['schritte'])+r.get('hinweis','')
        for w in ('abnehm','martin','wunsch','11.11','donnerstag','esn'): assert w not in txt.lower(), (r['key'],w)
        print(f"{i:2d} {ZEITEN[i-1]} {r['key']:22s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P {r['portion']:14s} vs {r['vs']} {nt}#{'  BUCH' if r.get('hinweis') else ''}")
    ga=[r for i,r in enumerate(R,1) if i in GRUPPE_A]; assert sum(r['suess'] for r in ga)==5
    print('ok')
