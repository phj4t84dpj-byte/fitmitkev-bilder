# -*- coding: utf-8 -*-
# GTA-6-Tag, Do 19.11.2026 (Erscheinungstag von GTA VI). Kev 18.11., 22:14: „Lass uns morgen nur GTA-VI-Rezepte hochladen, ich brauche dafür den Gamer-Look,
#   Rezepte die Gamer lieben, über den Tellerrand schauen“. Dialog 22:35: Look ok · ESN 6:10/13:00 bleiben · alter Donnerstag-Plan (G97) auf Freitag · Kev schaut alle Bilder vor dem Go.
# 19 Rezepte: 13 neu (Florida/Miami = Vorbild der Spielwelt + typisches Zocker-Essen), 6 bewährte mit neuem Bild im Gamer-Look (SmashWrap, Pizzabrötchen, Mac and Cheese, Döner,
#   Quarkbällchen, Lava-Cookies). Jedes Rezept mit anderem Gamer-Hook (Hook-Test). Ansprache: Leserinnen 45–64, deren Mann/Sohn/Enkel zockt.
# Kev 18.11., 23:02: „Ich möchte immer GTA VI im Bild stehen haben“ → jeder Hook enthält „GTA VI“, dazu das Schild unten rechts; Texte ebenfalls „GTA VI“.
# Keine Logos, keine Figuren, keine Spielszenen im Bild – „GTA“ nur als normaler Text. Hashtags: #gta6 immer dabei, Gruppe A (3) / B (4–5) wie gewohnt gemischt.
import sys, os, copy
_D=os.path.dirname(os.path.abspath(__file__))
for g in ('g87','g88','g89','g90','g91','g92','g93','g93n','g94'): sys.path.insert(0, os.path.join(_D, '..', g))
from g90_data import NUT, PIECE, nut, Z, macros4
import g87_data, g91_data, g92_data, g94_data
_A={}
for m in (g87_data, g91_data, g92_data, g94_data):
    for r in m.R: _A[r['key']]=r
def alt(key, **kw):
    r=copy.deepcopy(_A[key])
    for x in ('fb','hinweis','n','buch','vorhanden'): r.pop(x,None)
    r.update(kw); return r
for _k,_v in {'butterkekse':(435,7,73,12), 'tortilla':(300,9,50,7), 'toast':(260,8,48,3.5), 'erdbeeren':(33,0.8,5.5,0.4), 'erdnussmus':(620,26,12,50),
            'datteln':(290,2,65,0.5), 'semmelbroesel':(360,11,72,2), 'zuckerstreusel':(400,0,98,1), 'gefluegelwiener':(200,14,1,15)}.items(): NUT.setdefault(_k,_v)   # bestehende Werte nicht überschreiben
GLAS=("A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, "
      "layers visible through the glass; about one quarter eaten from the back corner, exactly one plain straight metal teaspoon resting inside the dish, nothing on the spoon, no other cutlery. Inside: ")
R=[
 # 1 · 06:50
 dict(key='FrenchToast', suess=True, hook='Frühstück zum GTA-VI-Start:', titel=['FRENCH-TOAST-','STICKS'], portion='pro Portion', anzahl=2, vs=550,
  zutaten=[Z('4 Scheiben','Vollkorn-Toast','toastbrot','toast',100), Z('2 Stück','Eier','eier','ei',st=2), Z('100 ml','Milch (1,5 %)','milch','milch',100),
           Z('1 TL','Zimt','zimt','zimt',0), Z('15 g','Erythrit','erythrit','erythrit',15), Z('150 g','Skyr','skyr','skyr',150),
           Z('1 TL','Vanilleextrakt','vanilleextrakt','vanille',0), Z('1 TL','Öl','oel','oel',5)],
  ex=[],
  intro='French Toast gehört in jedes amerikanische Diner, und genau so ein Frühstück passt zu dem Tag, an dem GTA VI erscheint. Bei mir als Sticks zum Dippen: Toast in Ei-Zimt-Milch gewendet, goldbraun gebraten, dazu ein Vanille-Skyr-Dip. {k} kcal und {p} g Eiweiß pro Portion statt 550 für French Toast mit Butter und Sirup!',
  schritte=['Eier, Milch, Zimt und 10 g Erythrit in einem tiefen Teller verquirlen. Jede Toastscheibe in 3 Streifen schneiden.',
            'Die Streifen kurz in der Eiermilch wenden und in einer beschichteten Pfanne mit dem Öl von allen Seiten goldbraun braten.',
            'Skyr mit Vanille und 5 g Erythrit glatt rühren und als Dip zu den Sticks servieren.'],
  frage='French Toast oder Arme Ritter: Wie heißt das bei euch?', tags='#gta6 #frenchtoast #armeritter #frühstück #fitmitkev',
  prompt='A stack of golden brown French toast sticks (thick strips of toast fried in egg with cinnamon) on a white plate, dusted with a little cinnamon, a small white bowl of thick white vanilla yogurt dip beside, a few sticks leaning against the bowl.'),
 # 2 · 07:30
 dict(key='Cubano', suess=False, hook='Aus Vice City in GTA VI:', titel=['KUBANISCHES','SANDWICH'], portion='pro Stück', anzahl=2, vs=650,
  zutaten=[Z('2 Stück','Ciabatta-Brötchen','broetchen','broetchen',160), Z('60 g','Kochschinken','kochschinken','kochschinken',60),
           Z('60 g','Putenschinken','putenschinken','putenschinken',60), Z('2 Scheiben','Käse light','kaese_light','kaesescheiben',40),
           Z('2 Stück','Gewürzgurken','gewuerzgurken','gurken',60), Z('2 TL','Senf','senf','senf',10), Z('1 TL','Öl','oel','oel',5)],
  ex=[],
  intro='Das Cuban Sandwich kommt aus Miami, der Stadt, die in GTA VI als Vice City zu sehen ist: Schinken, Käse, Gewürzgurken und Senf in einem knusprig gepressten Brötchen. Ich nehme Kochschinken und Putenschinken statt fettem Schweinebraten und drücke es in der Pfanne mit einem Topf flach: {k} kcal und {p} g Eiweiß pro Sandwich statt 650 für das Sandwich aus dem Diner!',
  schritte=['Die Brötchen aufschneiden und innen dünn mit Senf bestreichen. Die Gewürzgurken in dünne Scheiben schneiden.',
            'Die Unterseiten mit Kochschinken, Putenschinken, Gurkenscheiben und Käse belegen und die Deckel daraufsetzen.',
            'Eine Pfanne mit dem Öl erhitzen, die Sandwiches hineinlegen und mit einem schweren Topf flach drücken. Von jeder Seite 3–4 Minuten goldbraun rösten, bis der Käse schmilzt, und halbieren.'],
  frage='Wer zockt bei euch heute GTA VI: Mann, Sohn oder du selbst?', tags='#gta6 #sandwich #fitmitkev',
  prompt='Two pressed toasted Cuban sandwiches on a wooden board, golden crispy flattened white bread rolls, cut in half and the halves placed side by side so the filling is clearly visible from the side: many thin pink ham slices, melted yellow cheese, green pickle slices and a stripe of yellow mustard, a small white bowl of pickle slices beside.'),
 # 3 · 08:15
 dict(key='Donuts', suess=True, hook='Für die GTA-VI-Pause:', titel=['OFEN-','DONUTS'], portion='pro Stück', anzahl=6, vs=300,
  zutaten=[Z('150 g','Dinkelmehl','dinkelmehl','dinkelmehl',150), Z('200 g','Skyr','skyr','skyr',200), Z('1 Stück','Ei','ei','ei',st=1),
           Z('50 g','Erythrit','erythrit','erythrit',50), Z('2 TL','Backpulver','backpulver','backpulver',0),
           Z('40 g','Zartbitterschokolade','zartbitterschokolade','schokolade',40), Z('1 TL','Bunte Zuckerstreusel','zuckerstreusel','zuckerstreusel',5),
           Z('1 TL','Vanilleextrakt','vanilleextrakt','vanille',0)],
  ex=[],
  intro='Donuts gehören zu Amerika wie der Controller zum Zocker. Meine kommen aus dem Ofen statt aus der Fritteuse: Skyr-Teig in die Donutform, 12 Minuten backen, in Zartbitterschokolade tunken und Streusel drauf. Genau richtig zum Start von GTA VI: {k} kcal und {p} g Eiweiß pro Donut statt 300 für den Donut vom Bäcker!',
  schritte=['Mehl, Skyr, Ei, Erythrit, Backpulver und Vanille zu einem glatten Teig verrühren.',
            'Den Teig in eine gefettete Donutform (6 Mulden) füllen und bei 180 °C Ober-/Unterhitze 12–14 Minuten backen. Kurz abkühlen lassen und aus der Form lösen.',
            'Die Schokolade schmelzen, die Donuts mit der Oberseite eintauchen und mit den Zuckerstreuseln bestreuen.'],
  frage='Donuts: mit Schokolade oder mit Zuckerguss?', tags='#gta6 #donuts #fitmitkev',
  prompt='Six baked ring donuts on a wooden board, the tops dipped in glossy dark chocolate glaze and decorated with a few colorful sugar sprinkles, one donut leaning upright in front, one donut with a bite taken out showing the soft pale baked crumb.'),
 # 4 · 08:55
 alt('Pizzabroetchen', hook='Für deinen GTA-VI-Zocker:', tags='#gta6 #pizzabrötchen #pizza #fingerfood #fitmitkev',
  intro='Heute erscheint GTA VI, und in vielen Wohnzimmern wird stundenlang gezockt. Stell einfach ein Blech Pizzabrötchen daneben: Skyr-Teig ohne Hefe, mit Frischkäse, Salami, Paprika und Käse überbacken, in 30 Minuten fertig. 10 Stück: {k} kcal und {p} g Eiweiß pro Brötchen statt 280 für das Pizzabrötchen mit Kräuterbutter vom Lieferdienst!',
  frage='Für wen backst du heute die Pizzabrötchen: für den Zocker oder für dich?',
  prompt='Golden brown baked pizza rolls on a wooden board: round fluffy bread rolls topped with melted golden cheese, small pieces of red salami and red bell pepper cubes, one roll broken open in front showing the soft inside, a small white bowl of white herb dip beside.'),
 # 5 · 09:35
 dict(key='KeyLimeBowl', suess=True, hook='Aus der Welt von GTA VI:', titel=['KEY-LIME-PIE-','BOWL'], portion='die ganze Bowl', anzahl=1, vs=800,
  zutaten=[Z('4 Stück','Butterkekse','butterkekse','butterkekse',33), Z('250 g','Skyr','skyr','skyr',250), Z('1 Stück','Ei','ei','ei',st=1),
           Z('15 g','Vanillepudding-Pulver','vanillepudding_pulver','puddingpulver',15), Z('20 g','Erythrit','erythrit','erythrit',20),
           Z('1 Stück','Limette (Saft und Abrieb)','limette','zitrone',30)],
  ex=[],
  intro='Key Lime Pie ist der Kuchen aus Florida, dem Vorbild für die Welt von GTA VI: frisch, cremig und ein bisschen sauer. Bei mir als Bowl nur für dich, mit Skyr statt gezuckerter Kondensmilch: {k} kcal und {p} g Eiweiß die ganze Bowl statt 800 für zwei Stücke Key Lime Pie!',
  schritte=['Die Butterkekse fein zerbröseln und in eine kleine gefettete Glasform (15 × 10 cm) drücken.',
            '200 g Skyr, Ei, Puddingpulver, Erythrit, den Limettensaft und die Hälfte vom Abrieb glatt rühren, auf den Keksboden füllen und bei 170 °C Ober-/Unterhitze 22 Minuten backen.',
            'Abkühlen lassen, 1 Stunde kalt stellen, die restlichen 50 g Skyr als Haube daraufgeben und mit dem restlichen Limettenabrieb bestreuen.'],
  frage='Key Lime Pie: Hast du den schon mal probiert?', tags='#gta6 #keylimepie #bowl #käsekuchen #fitmitkev',
  prompt=GLAS+'a thin golden biscuit crumb base at the bottom, a thick smooth pale lime-green creamy baked cheesecake layer, on top three small swirls of white cream, fine bright green lime zest and two thin fresh lime slices, two halved green limes beside the dish.'),
 # 6 · 10:15
 dict(key='HotDog', suess=False, hook='Zum GTA-VI-Start:', titel=['HOT DOG','IN LEICHT'], portion='pro Stück', anzahl=4, vs=450,
  zutaten=[Z('4 Stück','Hot-Dog-Brötchen','broetchen','broetchen',240), Z('4 Stück','Geflügel-Wiener','gefluegel_wiener','gefluegelwiener',200),
           Z('2 Stück','Gewürzgurken','gewuerzgurken','gurken',60), Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1), Z('100 g','Skyr','skyr','skyr',100),
           Z('2 EL','Ketchup','ketchup','ketchup',30), Z('2 TL','Senf','senf','senf',10), Z('1 TL','Öl','oel','oel',5)],
  ex=[],
  intro='Hot Dogs vom Straßenstand gehören zu Amerika wie Wolkenkratzer und gelbe Taxis, also genau das richtige Essen zum Start von GTA VI. Meine Version: Geflügel-Wiener im warmen Brötchen, dazu selbst geröstete Zwiebeln aus der Pfanne, Gewürzgurken und eine Senf-Skyr-Soße statt Remoulade. {k} kcal und {p} g Eiweiß pro Hot Dog statt 450 für den vom Imbiss!',
  schritte=['Die Zwiebel in feine Ringe schneiden und im Öl bei mittlerer Hitze 8 Minuten goldbraun rösten. Die Gewürzgurken in Scheiben schneiden.',
            'Die Wiener in heißem Wasser 5 Minuten erwärmen (nicht kochen). Die Brötchen kurz im Ofen oder Toaster aufbacken und längs einschneiden.',
            'Skyr mit Senf verrühren. Die Wiener in die Brötchen legen und mit Senf-Skyr-Soße, Ketchup, Gurkenscheiben und Röstzwiebeln belegen.'],
  frage='Hot Dog: mit Röstzwiebeln oder ohne?', tags='#gta6 #hotdog #fitmitkev',
  prompt='Three hot dogs side by side on a wooden board: soft long buns, each filled with a sausage, topped with a zigzag of ketchup and mustard, green pickle slices and golden brown fried onion pieces, a small white bowl of fried onions beside.'),
 # 7 · 10:55
 dict(key='ErdbeerShake', suess=True, hook='Pink wie GTA VI:', titel=['ERDBEER-','MILCHSHAKE'], portion='pro Glas', anzahl=2, vs=450,
  zutaten=[Z('300 g','Erdbeeren (TK)','erdbeeren','erdbeeren',300), Z('300 g','Skyr','skyr','skyr',300), Z('300 ml','Milch (1,5 %)','milch','milch',300),
           Z('20 g','Erythrit','erythrit','erythrit',20), Z('1 TL','Vanilleextrakt','vanilleextrakt','vanille',0)],
  ex=[],
  intro='Ein dicker Erdbeer-Milchshake wie im amerikanischen Diner, pink wie die Neonlichter von Vice City in GTA VI. Die gefrorenen Erdbeeren machen ihn so cremig, dass du kein Eis brauchst: alles in den Mixer, 1 Minute, fertig. {k} kcal und {p} g Eiweiß pro Glas statt 450 für den Shake mit Eis und Sahne!',
  schritte=['Die gefrorenen Erdbeeren 5 Minuten antauen lassen.',
            'Erdbeeren, Skyr, Milch, Erythrit und Vanille im Mixer 1 Minute cremig pürieren.',
            'In 2 große Gläser füllen und sofort servieren.'],
  frage='Milchshake: Erdbeere, Schoko oder Vanille?', tags='#gta6 #milchshake #erdbeeren #fitmitkev',
  prompt='Two tall classic milkshake glasses filled with thick creamy pink strawberry milkshake, each topped with a small swirl of white cream and a fresh strawberry, a paper straw in each glass, a few strawberries beside.'),
 # 8 · 11:40
 dict(key='Cheeseburger', suess=False, hook='GTA VI ohne Lieferdienst:', titel=['CHEESEBURGER','WIE VOM DRIVE-IN'], portion='pro Stück', anzahl=4, vs=650,
  zutaten=[Z('4 Stück','Burger-Brötchen','broetchen','broetchen',240), Z('400 g','Rinderhack (mager)','rinderhack','hack',400),
           Z('4 Scheiben','Cheddar light','cheddar_light','kaesescheiben',80), Z('2 Stück','Gewürzgurken','gewuerzgurken','gurken',60),
           Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1), Z('80 g','Skyr','skyr','skyr',80), Z('2 EL','Ketchup','ketchup','ketchup',30), Z('2 TL','Senf','senf','senf',10)],
  ex=['4 Blätter Salat, 1 Tomate, Salz, Pfeffer'],
  intro='Wenn heute alle GTA VI spielen, klingelt überall der Lieferdienst. Diesen Burger machst du in 20 Minuten selbst: saftiges Patty aus magerem Hack, geschmolzener Cheddar, Gewürzgurken und Burgersoße aus Skyr, Ketchup und Senf. {k} kcal und {p} g Eiweiß pro Burger statt 650 für den Cheeseburger vom Drive-in!',
  schritte=['Das Hack mit Salz und Pfeffer würzen, zu 4 flachen Pattys formen und in einer heißen beschichteten Pfanne von jeder Seite 3 Minuten braten. Den Cheddar auflegen und kurz schmelzen lassen.',
            'Skyr mit Ketchup und Senf verrühren. Die Zwiebel in feine Ringe und die Gewürzgurken in Scheiben schneiden.',
            'Die Brötchen aufschneiden und kurz toasten. Mit Soße, Salat, Tomate, Patty, Gurken und Zwiebeln belegen.'],
  frage='Burger: selbst gemacht oder bestellt?', tags='#gta6 #cheeseburger #burger #abendessen #fitmitkev',
  prompt='Two homemade cheeseburgers on a wooden board: toasted sesame buns, a juicy browned beef patty with melted yellow cheddar cheese, green lettuce, a tomato slice, pickle slices, onion rings and pink burger sauce, one burger cut in half showing the layers.'),
 # 9 · 12:20
 alt('MacCheese', hook='Mittagspause von GTA VI:', tags='#gta6 #macandcheese #fitmitkev',
  intro='Mac and Cheese ist das amerikanische Wohlfühlessen schlechthin und damit genau richtig zum Start von GTA VI. Richtig cremig, aber mit Skyr und Käse light statt Sahne und Butter, dazu Hähnchen für ordentlich Eiweiß und eine goldbraune Käsekruste aus dem Ofen: {k} kcal und {p} g Eiweiß pro Portion statt 800 für die Käsenudeln mit Sahne!',
  prompt='A round white ceramic baking dish with creamy macaroni and cheese with small browned chicken pieces under a golden brown bubbly melted cheese crust, one portion served on a white plate in front with stretchy melted cheese and creamy elbow macaroni clearly visible, a fork beside.'),
 # 10 · 13:40
 dict(key='Quesadilla', suess=False, hook='Eine Hand frei für GTA VI:', titel=['HÄHNCHEN-','QUESADILLA'], portion='pro Stück', anzahl=2, vs=700,
  zutaten=[Z('2 Stück','Vollkorn-Tortillas','tortilla','tortilla',120), Z('200 g','Hähnchenbrust','haehnchenbrust','haehnchen',200),
           Z('60 g','Reibekäse light','reibekaese_light','reibekaese',60), Z('1 Stück','Rote Paprika','rote_paprika','paprika_st',st=1),
           Z('70 g','Mais (Dose)','mais','mais',70), Z('100 g','Skyr','skyr','skyr',100), Z('1 TL','Paprikapulver','paprikapulver','vanille',0), Z('1 TL','Öl','oel','oel',5)],
  ex=['Salz, Pfeffer, ½ TL Kreuzkümmel'],
  intro='Das perfekte Zocker-Essen zum Start von GTA VI: Man isst es mit einer Hand und hat die andere frei für den Controller. Tortilla gefüllt mit Hähnchen, Paprika, Mais und geschmolzenem Käse, in der Pfanne knusprig gebraten, dazu ein Skyr-Dip. {k} kcal und {p} g Eiweiß pro Quesadilla statt 700 für die aus dem Restaurant!',
  schritte=['Die Hähnchenbrust in kleine Würfel schneiden, mit Salz, Pfeffer, Paprikapulver und Kreuzkümmel würzen und im Öl 5 Minuten braten. Paprikawürfel und Mais 2 Minuten mitbraten.',
            'Je eine Tortilla-Hälfte mit Käse, der Hähnchen-Mischung und wieder Käse belegen und zuklappen.',
            'In einer beschichteten Pfanne ohne Fett von jeder Seite 2–3 Minuten goldbraun braten, bis der Käse schmilzt. In Ecken schneiden und mit dem Skyr als Dip servieren.'],
  frage='Quesadilla: mit Hähnchen oder lieber vegetarisch?', tags='#gta6 #quesadilla #fitmitkev',
  prompt='Golden brown crispy pan-fried quesadilla wedges stacked on a wooden board, the cut sides clearly showing the filling of melted stretchy cheese, pieces of browned chicken, red bell pepper cubes and yellow sweet corn between two tortilla layers, a small white bowl of white yogurt dip beside.'),
 # 11 · 14:15
 dict(key='SnickersBowl', suess=True, hook='GTA-VI-Snack nur für dich:', titel=['SNICKERS-','BOWL'], portion='die ganze Bowl', anzahl=1, vs=735,
  zutaten=[Z('25 g','Zarte Haferflocken','zarte_haferflocken','haferflocken',25), Z('200 g','Skyr','skyr','skyr',200), Z('10 g','Erdnussmus','erdnussmus','erdnussmus',10),
           Z('3 Stück','Datteln (entsteint)','datteln','datteln',24), Z('15 g','Erythrit','erythrit','erythrit',15),
           Z('10 g','Zartbitterschokolade','zartbitterschokolade','schokolade',10), Z('2 EL','Milch (1,5 %)','milch','milch',30)],
  ex=['10 g gesalzene Erdnüsse'], exnut_=[(60,2.5,1,5)],
  intro='Der Schokoriegel, der in keiner Zocker-Schublade fehlt, als Bowl nur für dich: Haferboden, Skyr-Creme, Karamell aus Datteln und Erdnussmus, obendrauf Schokolade und gesalzene Erdnüsse. Ohne Backen in 10 Minuten geschichtet, passend zum Start von GTA VI: {k} kcal und {p} g Eiweiß die ganze Bowl statt 735 für drei Snickers!',
  schritte=['Die Haferflocken mit der Milch und 1 fein gehackten Dattel verkneten und als Boden in eine kleine Glasform (15 × 10 cm) drücken.',
            '2 Datteln mit 2 EL heißem Wasser 5 Minuten einweichen, mit einer Gabel zu Karamell zerdrücken und mit dem Erdnussmus verrühren. Skyr mit Erythrit glatt rühren, auf den Boden streichen und das Erdnuss-Karamell darauf verteilen.',
            'Die Schokolade schmelzen, darüber träufeln, mit den gehackten Erdnüssen bestreuen und 30 Minuten kalt stellen.'],
  frage='Snickers, Mars oder Twix: Was liegt bei euch in der Schublade?', tags='#gta6 #snickers #bowl #ohnebacken #fitmitkev',
  prompt=GLAS+'an oat base at the bottom, a thick white cream layer, a layer of golden brown caramel on top, drizzled with dark chocolate and sprinkled with chopped roasted peanuts, a few peanuts and two dates beside the dish.'),
 # 12 · 14:55
 dict(key='PopcornChicken', suess=False, hook='Statt Chips zu GTA VI:', titel=['POPCORN-','CHICKEN'], portion='pro Portion', anzahl=3, vs=600,
  zutaten=[Z('500 g','Hähnchenbrust','haehnchenbrust','haehnchen',500), Z('60 g','Cornflakes (ungesüßt)','cornflakes','cornflakes',60), Z('1 Stück','Ei','ei','ei',st=1),
           Z('150 g','Skyr','skyr','skyr',150), Z('1 TL','Paprikapulver','paprikapulver','vanille',0), Z('1 EL','Ketchup','ketchup','ketchup',15),
           Z('1 Zehe','Knoblauch','knoblauch','knoblauch',3)],
  ex=['Salz, Pfeffer, Schnittlauch'],
  intro='Der Zocker-Snack schlechthin, nur ohne Fritteuse: kleine Hähnchenwürfel in knuspriger Cornflakes-Panade aus dem Ofen, dazu ein Knoblauch-Skyr-Dip. Perfekt zum Naschen nebenbei, wenn heute GTA VI läuft: {k} kcal und {p} g Eiweiß pro Portion statt 600 für die Box vom Imbiss!',
  schritte=['Die Hähnchenbrust in mundgerechte Würfel schneiden und mit Salz, Pfeffer und Paprikapulver würzen. Die Cornflakes in einem Gefrierbeutel fein zerdrücken.',
            'Die Würfel erst im verquirlten Ei, dann in den Cornflakes wenden und auf ein Backblech mit Backpapier legen. Bei 200 °C Ober-/Unterhitze 15–18 Minuten knusprig backen und nach der Hälfte wenden.',
            'Skyr mit gepresstem Knoblauch, Salz, Pfeffer und Schnittlauch verrühren und mit dem Ketchup als Dip dazu servieren.'],
  frage='Knusper-Hähnchen: mit Ketchup oder mit Knoblauch-Dip?', tags='#gta6 #popcornchicken #hähnchen #fingerfood #fitmitkev',
  prompt='A paper-lined basket piled with small bite-sized crispy golden brown breaded chicken pieces (popcorn chicken) with a crunchy cornflake crust, a small white bowl of white garlic yogurt dip with chives and a small white bowl of ketchup beside, a few pieces lying in front.'),
 # 13 · 15:35
 alt('Quarkbaellchen', hook='Snack für die GTA-VI-Nacht:', tags='#gta6 #quarkbällchen #fitmitkev',
  intro='Der Snack für die lange GTA-VI-Nacht: Quarkbällchen wie von der Kirmes, nur aus dem Ofen statt aus dem Fett, innen fluffig, außen in Zimt gewälzt. Sechs Zutaten, eine Schüssel, in 25 Minuten fertig: {k} kcal und {p} g Eiweiß pro Bällchen statt 150 für eins von der Kirmes!',
  prompt='A white paper bag lying on its side with many round golden brown German quark doughnut balls rolled in cinnamon sugar spilling out onto a wooden board, one ball in front broken open showing the fluffy pale yellow crumb inside, a small bowl of cinnamon sugar beside.'),
 # 14 · 16:50
 alt('SmashWrap', hook='GTA VI pausieren, reinbeißen:', tags='#gta6 #smashburger #wrap #abendessen #fitmitkev',
  intro='Wer heute GTA VI zockt, braucht Essen, das in eine Hand passt. Smash-Burger zum Falten: Das Hack wird direkt auf die Tortilla gedrückt und in der Pfanne kross gebraten, dann Cheddar, Gurke, Zwiebel und Burgersoße aus Skyr drauf und zuklappen. In 15 Minuten fertig: {k} kcal und {p} g Eiweiß pro Wrap statt 850 für den Smash-Burger mit Pommes!',
  prompt='Two folded smash burger wraps cut in half and stacked on a wooden board: golden crispy flour tortillas folded over a thin browned beef patty with melted yellow cheddar cheese, pickle slices, onion and pink burger sauce, the filling clearly visible on the cut sides, a small white bowl of pickle slices beside.'),
 # 15 · 18:10
 dict(key='OfenNachos', suess=False, hook='Wenn heute alle GTA VI zocken:', titel=['OFEN-','NACHOS'], portion='pro Portion', anzahl=4, vs=700,
  zutaten=[Z('4 Stück','Vollkorn-Tortillas','tortilla','tortilla',240), Z('300 g','Rinderhack (mager)','rinderhack','hack',300),
           Z('1 Stück','Rote Paprika','rote_paprika','paprika_st',st=1), Z('140 g','Mais (Dose)','mais','mais',140),
           Z('80 g','Reibekäse light','reibekaese_light','reibekaese',80), Z('200 g','Passierte Tomaten','passierte_tomaten','tomaten',200),
           Z('200 g','Skyr','skyr','skyr',200)],
  ex=['Salz, Pfeffer, 1 TL Paprikapulver, ½ TL Kreuzkümmel, Schnittlauch'],
  intro='Heute erscheint GTA VI, und bei vielen wird bis spät in die Nacht gezockt. Statt Chipstüte gibt es Nachos vom Blech: Tortilla-Ecken knusprig gebacken, darauf Hack, Paprika, Mais und Käse, dazu Salsa und ein Skyr-Dip. {k} kcal und {p} g Eiweiß pro Portion statt 700 für Nachos mit Käsesoße!',
  schritte=['Die Tortillas in je 8 Dreiecke schneiden, auf einem Backblech mit Backpapier verteilen und bei 200 °C Ober-/Unterhitze 6–8 Minuten knusprig backen.',
            'Das Hack in einer beschichteten Pfanne krümelig braten, Paprikawürfel und Mais 3 Minuten mitbraten und mit Salz, Pfeffer, Paprikapulver und Kreuzkümmel würzen.',
            'Die Hack-Mischung über die Chips verteilen, mit Käse bestreuen und 5 Minuten überbacken. Passierte Tomaten mit Salz und Pfeffer als Salsa und Skyr mit Salz, Pfeffer und Schnittlauch als Dip dazu reichen.'],
  frage='Wer sieht seinen Mann oder Sohn heute Abend nicht mehr? 🙋‍♀️', tags='#gta6 #nachos #fitmitkev',
  prompt='A black baking tray piled with homemade crispy oven-baked tortilla chip triangles topped with browned ground beef, golden melted cheese, small red bell pepper cubes, yellow sweet corn and fresh chopped green chives, a small white bowl of thick white yogurt dip and a small white bowl of red tomato salsa beside the tray.'),
 # 16 · 18:50
 alt('Doener', hook='Für den GTA-VI-Abend:', tags='#gta6 #döner #hähnchen #abendessen #fitmitkev',
  intro='Nach ein paar Stunden GTA VI kommt der Hunger auf Döner. Den hier machst du selbst: knuspriges Hähnchen, frischer Salat und Knoblauchsoße im warmen Fladenbrot aus Skyr-Teig, das ohne Hefe in 15 Minuten gebacken ist. {k} kcal und {p} g Eiweiß pro Döner statt 900 für den vom Imbiss!',
  prompt='Two homemade doner kebabs in golden brown oval flatbread pockets standing upright on a wooden board, generously filled with crispy browned strips of chicken, shredded green iceberg lettuce, tomato slices, cucumber slices and red onion rings, with white garlic yogurt sauce drizzled on top, a small bowl of white yogurt sauce beside.'),
 # 17 · 19:25
 alt('LavaCookies', hook='Nachschub für die GTA-VI-Nacht:', tags='#gta6 #cookies #fitmitkev',
  intro='Nachschub für alle, die heute bis spät GTA VI spielen: Schoko-Cookies mit einem Kern aus Erdnussmus, der beim Aufbrechen herausläuft. Aus Haferflocken, ohne Mehl, ohne Butter und ohne Zucker, in 10 Minuten gebacken: {k} kcal und {p} g Eiweiß pro Cookie statt 380 für einen gefüllten Cookie vom Café!',
  prompt='Six thick dark chocolate cookies on a wooden board, one cookie broken in half in front with a liquid golden brown peanut butter core flowing out, a few dark chocolate drops beside.'),
 # 18 · 20:05
 dict(key='MozzarellaSticks', suess=False, hook='Für den GTA-VI-Spieleabend:', titel=['MOZZARELLA-','STICKS'], portion='pro Portion', anzahl=2, vs=550,
  zutaten=[Z('250 g','Mozzarella light','mozzarella_light','mozzarella',250), Z('1 Stück','Ei','ei','ei',st=1), Z('60 g','Semmelbrösel','semmelbroesel','semmelbroesel',60),
           Z('20 g','Dinkelmehl','dinkelmehl','dinkelmehl',20), Z('1 TL','Italienische Kräuter','italienische_kraeuter','vanille',0),
           Z('200 g','Passierte Tomaten','passierte_tomaten','tomaten',200), Z('1 Zehe','Knoblauch','knoblauch','knoblauch',3)],
  ex=['Salz, Pfeffer, ½ TL Paprikapulver'],
  intro='Mozzarella-Sticks sind der Klassiker für jeden Spieleabend, erst recht am Tag, an dem GTA VI erscheint: außen knusprig, innen zieht der Käse Fäden. Meine kommen aus dem Ofen statt aus der Fritteuse, mit Mozzarella light und einem schnellen Tomaten-Dip. {k} kcal und {p} g Eiweiß pro Portion statt 550 für die frittierten vom Lieferdienst!',
  schritte=['Den Mozzarella gut abtropfen lassen und in 12 dicke Stifte schneiden. Erst in Mehl, dann im verquirlten Ei und in den mit Kräutern, Salz und Paprikapulver gewürzten Semmelbröseln wenden. Ei und Brösel einmal wiederholen.',
            'Die Sticks 30 Minuten ins Gefrierfach legen, damit der Käse beim Backen nicht ausläuft. Dann auf Backpapier bei 220 °C Ober-/Unterhitze 8–10 Minuten goldbraun backen.',
            'Die passierten Tomaten mit gepresstem Knoblauch, Salz und Pfeffer 5 Minuten köcheln und als Dip dazu servieren.'],
  frage='Mozzarella-Sticks: mit Tomaten-Dip oder mit Knoblauch-Dip?', tags='#gta6 #mozzarellasticks #fingerfood #snack #fitmitkev',
  prompt='A pile of golden brown crispy breaded mozzarella sticks on a small wooden board, one stick pulled apart in front showing long strings of melted white cheese, a small white bowl of red tomato dipping sauce beside.'),
 # 19 · 20:45
 dict(key='BananensplitGlas', suess=True, hook='Nach der GTA-VI-Mission:', titel=['BANANENSPLIT','IM GLAS'], portion='pro Glas', anzahl=2, vs=500,
  zutaten=[Z('2 Stück','Bananen','banane','banane',st=2), Z('300 g','Skyr','skyr','skyr',300), Z('150 g','Erdbeeren (TK)','erdbeeren','erdbeeren',150),
           Z('15 g','Erythrit','erythrit','erythrit',15), Z('20 g','Zartbitterschokolade','zartbitterschokolade','schokolade',20),
           Z('10 g','Mandelblättchen','mandelblaettchen','mandelblaettchen',10), Z('1 TL','Vanilleextrakt','vanilleextrakt','vanille',0)],
  ex=[],
  intro='Bananensplit wie in der Eisdiele, nur ohne Eis und Sahne: Bananenscheiben, Vanille-Skyr und warme Erdbeersoße im Glas geschichtet, obendrauf Schokolade und Mandeln. Die Belohnung nach einem langen GTA-VI-Abend: {k} kcal und {p} g Eiweiß pro Glas statt 500 für den Eisbecher!',
  schritte=['Die Erdbeeren in einem kleinen Topf 5 Minuten erwärmen und mit einer Gabel grob zerdrücken. Skyr mit Erythrit und Vanille glatt rühren.',
            'Die Bananen in Scheiben schneiden und abwechselnd mit Vanille-Skyr und Erdbeersoße in 2 Gläser schichten.',
            'Die Schokolade schmelzen, darüber träufeln und mit den Mandelblättchen bestreuen.'],
  frage='Bananensplit: Kennt ihr den noch aus der Eisdiele?', tags='#gta6 #bananensplit #dessert #fitmitkev',
  prompt='Two clear dessert glasses layered with banana slices, thick white vanilla cream and red strawberry sauce visible through the glass, topped with a drizzle of dark chocolate sauce and toasted flaked almonds, exactly one plain straight metal teaspoon lying beside the glasses, half a banana beside.'),
]
for _r in R:
    _r['kurz']=_r.get('kurz') or ['–','–','–']
    _r['exnut']=_r.pop('exnut_',None) or _r.get('exnut') or []
ZEITEN=['06:50','07:30','08:15','08:55','09:35','10:15','10:55','11:40','12:20','13:40','14:15','14:55','15:35','16:50','18:10','18:50','19:25','20:05','20:45']
FEST={'06:10':'ESN Schoko-Mousse (eingeplant, bleibt)','13:00':'ESN Tiramisu-Bowl (eingeplant, bleibt)','17:30':'GTA-VI-Abend: Lieferdienst gegen selbst gemacht (Vergleich im Gamer-Look)'}
NAME={'FrenchToast':'French-Toast-Sticks','Cubano':'Kubanisches Sandwich wie in Miami','Donuts':'Donuts aus dem Ofen','Pizzabroetchen':'Pizzabrötchen wie vom Lieferdienst',
      'KeyLimeBowl':'Key-Lime-Pie-Bowl nur für dich','HotDog':'Hot Dog in leicht','ErdbeerShake':'Erdbeer-Milchshake wie im Diner','Cheeseburger':'Cheeseburger wie vom Drive-in',
      'MacCheese':'Mac and Cheese in leicht','Quesadilla':'Hähnchen-Quesadilla','SnickersBowl':'Snickers-Bowl nur für dich','PopcornChicken':'Popcorn-Chicken aus dem Ofen',
      'Quarkbaellchen':'Quarkbällchen ohne Fritteuse','SmashWrap':'Smash-Burger-Wrap','OfenNachos':'Ofen-Nachos für den Zocker-Abend','Doener':'Döner im Skyr-Fladenbrot',
      'LavaCookies':'Erdnuss-Lava-Cookies','MozzarellaSticks':'Mozzarella-Sticks aus dem Ofen','BananensplitGlas':'Bananensplit im Glas'}
FORM={'FrenchToast':'2 Portionen','Cubano':'2 Sandwiches','Donuts':'6 Stück, Donutform','Pizzabroetchen':'10 Stück, Backblech','KeyLimeBowl':'1 Portion, Glasform 15 × 10 cm',
      'HotDog':'4 Stück','ErdbeerShake':'2 Gläser','Cheeseburger':'4 Stück','MacCheese':'4 Portionen, Auflaufform','Quesadilla':'2 Stück','SnickersBowl':'1 Portion, Glasform 15 × 10 cm',
      'PopcornChicken':'3 Portionen, Backblech','Quarkbaellchen':'12 Stück, Backblech','SmashWrap':'4 Wraps','OfenNachos':'4 Portionen, Backblech','Doener':'4 Stück',
      'LavaCookies':'6 Stück, Backblech','MozzarellaSticks':'2 Portionen, Backblech','BananensplitGlas':'2 Gläser'}
# Titelzeile / Nährwert-Zeile
LAB={'FrenchToast':('pro Portion','pro Portion'),'Cubano':('pro Sandwich','pro Sandwich'),'Donuts':('pro Donut','pro Donut'),'Pizzabroetchen':('pro Stück','pro Stück'),
     'KeyLimeBowl':('die ganze Bowl','pro Bowl'),'HotDog':('pro Hot Dog','pro Hot Dog'),'ErdbeerShake':('pro Glas','pro Glas'),'Cheeseburger':('pro Burger','pro Burger'),
     'MacCheese':('pro Portion','pro Portion'),'Quesadilla':('pro Stück','pro Stück'),'SnickersBowl':('die ganze Bowl','pro Bowl'),'PopcornChicken':('pro Portion','pro Portion'),
     'Quarkbaellchen':('pro Stück','pro Stück'),'SmashWrap':('pro Wrap','pro Wrap'),'OfenNachos':('pro Portion','pro Portion'),'Doener':('pro Döner','pro Döner'),
     'LavaCookies':('pro Cookie','pro Cookie'),'MozzarellaSticks':('pro Portion','pro Portion'),'BananensplitGlas':('pro Glas','pro Glas')}
if __name__=='__main__':
    assert len(R)==19==len(ZEITEN) and len({r['key'] for r in R})==19
    for i,r in enumerate(R,1):
        k,p,c,f=macros4(r); nt=len(r['tags'].split())
        assert r['vs']>k and len(r['zutaten'])<=8, r['key']
        assert r['tags'].split()[0]=='#gta6' and r['tags'].split()[-1]=='#fitmitkev' and 3<=nt<=5
        txt=(r['intro']+' '.join(r['schritte'])).lower()
        for w in ('abnehm','esn','satt macht','sättig'): assert w not in txt, (r['key'],w)
        assert r['key'] in NAME and r['key'] in FORM and r['key'] in LAB
        print(f"{i:2d} {ZEITEN[i-1]} {r['key']:17s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P {c:3d}KH {f:3d}F  vs {r['vs']}  {nt}#  {r['hook']}")
    print('ok', sum(r['suess'] for r in R),'süß')
