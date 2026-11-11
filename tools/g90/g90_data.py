# -*- coding: utf-8 -*-
# G90 – Donnerstag 12.11.2026, 16 Beiträge 6:10–20:45 (Kev 11.11. per Dialog: „16 wie am Montag“; Zeitfenster wie Mittwoch)
# Reset Tag 4: keine Werbung, kein Höflich-Titel, Hashtag-Test 2–3 gegen 4–5 mit GETAUSCHTEN Gruppen (Mi: 1,2,5,6 … = 2–3 → Do: 1,2,5,6 … = 4–5)
# Auswahl nach der Auswertung vom 11.11. (Reichweite ÷ Tagesmedian, alle Läufe seit 8.10.):
#   bewährte Volltreffer, die 7–12 Tage nicht liefen: Zimtschnecken-Oats (1.11., ×28) · Engelsaugen (1.11., ×20) · Spekulatius-Käsekuchen-Bowl
#   (27.10. ×15, 31.10. ×11) · Schokomousse 4 Zutaten (31.10. ×25, 5.11. ×11) · Skyr-Kuchen mit Zimt-Streuseln (25.10. ×12, 3.11. ×32) ·
#   Kokosmakronen (18.10., 31.10. ×11) · Cheeseburger-Lasagne (29.10. ×28) · Käsespätzle (31.10. 20:45, ×15) · Lasagne in leicht (23./26.10.)
#   + Community-Wunsch Maulwurfkuchen-Bowl + neue Varianten der Gewinner vom Montag (Cordon bleu, Auflauf) + Strammer Max (4.11., ×3,9).
#   Kalter Hund (alle 4–5 Tage ×13–28) und Spekulatius-Skyr-Kuchen bleiben fürs Wochenende.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'g89'))
from g89_data import NUT, PIECE, nut, Z, macros4, BOWL
NUT.update({
 'gnocchi':(160,4,34,0.5), 'cornflakes':(380,7,84,1), 'brot':(215,7,40,1.5), 'huettenkaese':(95,12,2.5,4.3),
 'spaetzle':(160,6,30,2), 'espresso':(2,0,0,0),
})
PIECE.update({'banane':(120,(110,1.3,25,0.4)), 'eigelb':(20,(65,3,0.1,5.5))})

R = [
# 1 · 06:10 · süß · Oats (Wiederholung des Treffers vom 1.11., 6:01 Uhr, 292 k)
dict(key='ZimtschneckenOats', suess=True, hook='Zimtschnecke im Glas:', titel=['ZIMTSCHNECKEN-','OVERNIGHT OATS'], portion='pro Glas', anzahl=2, vs=450,
 zutaten=[Z('100 g','Zarte Haferflocken','zarte_haferflocken','haferflocken',100), Z('300 g','Skyr','skyr','skyr',300), Z('200 ml','Milch (1,5 %)','milch','milch',200),
          Z('2 TL','Zimt','zimt','zimt',0), Z('20 g','Erythrit','erythrit','erythrit',20), Z('60 g','Frischkäse light','frischkaese_light','frischkaese',60),
          Z('1 TL','Vanilleextrakt','vanilleextrakt','vanille',0)],
 ex=[],
 intro='Schmeckt wie eine Zimtschnecke mit Frosting, ist aber ein Frühstück, das bis mittags satt macht: Haferflocken, Skyr und Zimt über Nacht im Glas, morgens ein Frischkäse-Swirl obendrauf. Abends in 5 Minuten gerührt: {k} kcal und {p} g Eiweiß pro Glas statt 450 für die Zimtschnecke mit Guss vom Bäcker!',
 schritte=['Haferflocken, 240 g Skyr, Milch, Zimt, Erythrit und Vanille verrühren und auf 2 Gläser verteilen.',
           'Über Nacht (mindestens 4 Stunden) in den Kühlschrank stellen.',
           'Morgens 60 g Skyr mit dem Frischkäse glatt rühren, als Frosting-Swirl auf die Oats geben und mit etwas Zimt bestäuben.'],
 frage='Zimtschnecke: lieber im Glas zum Löffeln oder frisch vom Bäcker?', tags='#overnightoats #zimtschnecken #frühstück #haferflocken #fitmitkev',
 prompt='Two glass jars with overnight oats seen from the side at eye level, creamy light beige cinnamon oats with visible brown cinnamon swirls through the glass, each topped with a thick white cream cheese frosting swirl and a dusting of brown cinnamon, two cinnamon sticks beside the jars, a spoon beside.'),
# 2 · 07:10 · herzhaft · Brötchen (schlichte Brötchen ohne Hefe: 20.10. 65 k, 10.10. 52 k, Montag 34 k)
dict(key='Fruehstuecksbroetchen', suess=False, hook='In 30 Minuten:', titel=['FRÜHSTÜCKS-','BRÖTCHEN'], portion='pro Stück', anzahl=8, vs=280,
 zutaten=[Z('300 g','Dinkelmehl','dinkelmehl','dinkelmehl',300), Z('300 g','Skyr','skyr','skyr',300), Z('1 Päckchen','Backpulver','backpulver','backpulver',0),
          Z('1 TL','Salz','salz','salz',0), Z('1 EL','Mohn','mohn','mohn',10), Z('1 EL','Sesam','sesam','sesam',10)],
 ex=[],
 intro='Frische Brötchen zum Frühstück, ohne zum Bäcker zu laufen: Skyr und Dinkelmehl verkneten, formen, Mohn und Sesam drauf, ab in den Ofen. Ohne Hefe, ohne Gehzeit, in 30 Minuten auf dem Tisch: {k} kcal und {p} g Eiweiß pro Brötchen statt 280 für das Croissant vom Bäcker!',
 schritte=['Mehl, Backpulver und Salz mischen, Skyr dazugeben und zu einem glatten Teig kneten (klebt er, 1–2 EL Mehl dazu).',
           '8 runde Brötchen formen, auf ein Backblech mit Backpapier setzen, mit Wasser bestreichen, mit Mohn und Sesam bestreuen und alle einmal längs einschneiden.',
           'Bei 200 °C Ober-/Unterhitze 20–22 Minuten goldbraun backen.'],
 frage='Brötchen: Mohn, Sesam oder ganz ohne?', tags='#brötchen #frühstück #ohnehefe #backen #fitmitkev',
 prompt='Homemade round bread rolls on baking paper on a light wooden board, golden brown crust with one long slash on top, some rolls topped with blue-black poppy seeds and some with golden sesame seeds, one roll in front cut open showing a soft white fluffy crumb, a small dish of butter beside.'),
# 3 · 08:05 · süß · Plätzchen (Wiederholung des Treffers vom 1.11., 7:20 Uhr, 210 k)
dict(key='Engelsaugen', suess=True, hook='Wie bei Oma:', titel=['ENGELS-','AUGEN'], portion='pro Stück', anzahl=30, vs=90,
 zutaten=[Z('250 g','Dinkelmehl','dinkelmehl','dinkelmehl',250), Z('100 g','Butter (kalt)','butter','butter',100), Z('80 g','Skyr','skyr','skyr',80),
          Z('70 g','Erythrit','erythrit','erythrit',70), Z('1 Stück','Eigelb','eigelb','eigelb',st=1), Z('1 TL','Vanilleextrakt','vanilleextrakt','vanille',0),
          Z('60 g','Himbeer-Fruchtaufstrich','fruchtaufstrich','fruchtaufstrich',60)],
 ex=['Prise Salz'],
 intro='Engelsaugen wie bei Oma, auch Husarenkrapfen genannt: mürbe Kugeln mit einem roten Klecks in der Mitte. Mit halb so viel Butter wie im Original, dafür Skyr im Teig, und keiner merkt den Unterschied. 30 Stück vom Blech: {k} kcal und {p} g Eiweiß pro Stück statt 90 für das Engelsauge vom Bäcker!',
 schritte=['Mehl, kalte Butter in Würfeln, Skyr, Erythrit, Eigelb, Vanille und Salz zügig zu einem glatten Teig kneten und 30 Minuten kalt stellen.',
           '30 Kugeln formen, auf ein Backblech mit Backpapier setzen und mit dem Stiel eines Kochlöffels eine Mulde hineindrücken.',
           'Fruchtaufstrich in die Mulden füllen und bei 170 °C Ober-/Unterhitze 12–14 Minuten backen.'],
 frage='Wie heißen sie bei euch: Engelsaugen, Husarenkrapfen oder Kulleraugen?', tags='#engelsaugen #plätzchen #fitmitkev',
 prompt='Homemade thumbprint cookies (German Engelsaugen): small round pale golden shortbread cookies, each with a glossy red raspberry jam filled dimple in the center, piled on a white plate, a few cookies lying on the wooden table in front, a small glass jar of red raspberry jam beside.'),
# 4 · 09:05 · herzhaft · Ei-Klassiker (4.11., 7:30 Uhr: ×3,9 zum Tagesmedian)
dict(key='StrammerMax', suess=False, hook='In 10 Minuten:', titel=['STRAMMER','MAX'], portion='pro Portion', anzahl=2, vs=700,
 zutaten=[Z('4 Scheiben','Vollkornbrot','vollkornbrot','brot',160), Z('4 Stück','Eier','eier','ei',st=4), Z('120 g','Putenschinken','putenschinken','putenschinken',120),
          Z('40 g','Käse light (gerieben)','reibekaese_light','reibekaese',40), Z('1 TL','Öl','oel','oel',5), Z('2 Stück','Gewürzgurken','gewuerzgurken','gurken',60),
          Z('1 EL','Schnittlauch','schnittlauch','schnittlauch',0)],
 ex=['Salz, Pfeffer'],
 intro='Strammer Max wie früher in der Kneipe: geröstetes Brot, Schinken, Käse und obendrauf ein Spiegelei mit weichem Eigelb. Mit Putenschinken, Käse light und nur einem Teelöffel Öl, in 10 Minuten fertig: {k} kcal und {p} g Eiweiß pro Portion (2 Brote) statt 700 für den Strammen Max mit Butter und Speck!',
 schritte=['Brotscheiben toasten oder in der Pfanne ohne Fett anrösten und mit dem Schinken belegen.',
           'Eier im Öl in einer beschichteten Pfanne als Spiegeleier braten, salzen und pfeffern.',
           'Käse auf den Schinken streuen, je ein heißes Spiegelei daraufsetzen, mit Schnittlauch bestreuen und mit Gewürzgurken servieren.'],
 frage='Strammer Max: mit Gewürzgurke oder mit Tomate?', tags='#strammermax #spiegelei #fitmitkev',
 prompt='A white plate with two slices of toasted rustic brown whole grain bread, each topped with slices of pink ham, a little melted cheese and a sunny-side-up fried egg with a bright yellow runny yolk, sprinkled with chopped chives, two pickled gherkins beside on the plate, a fork beside.'),
# 5 · 10:05 · süß · Bowl (Community-Wunsch)
dict(key='MaulwurfBowl', suess=True, hook='Euer Wunsch:', titel=['MAULWURFKUCHEN-','BOWL'], portion='die ganze Bowl', anzahl=1, vs=800,
 zutaten=[Z('1 Stück','Ei','ei','ei',st=1), Z('20 g','Dinkelmehl','dinkelmehl','dinkelmehl',20), Z('10 g','Backkakao','backkakao','kakao',10),
          Z('25 g','Erythrit','erythrit','erythrit',25), Z('½ Stück','Banane','banane','banane',st=0.5), Z('150 g','Skyr','skyr','skyr',150),
          Z('30 g','Frischkäse light','frischkaese_light','frischkaese',30), Z('10 g','Zartbitterschokolade','zartbitterschokolade','schokolade',10)],
 ex=['½ TL Backpulver', '1 TL Vanilleextrakt'],
 intro='Euer Wunsch aus den Kommentaren: Maulwurfkuchen als Bowl nur für dich. Unten ein saftiger Schokoboden, darauf Bananenscheiben, ein Hügel aus Skyr-Creme und obendrauf die Schokobrösel wie beim Original. Ohne Sahne: {k} kcal und {p} g Eiweiß die ganze Bowl statt 800 für zwei Stücke Maulwurfkuchen mit Sahne!',
 schritte=['Ei mit 15 g Erythrit schaumig schlagen, Mehl, Kakao, Backpulver und 30 g Skyr unterrühren, in eine kleine gefettete Glasform (15 × 10 cm) füllen und bei 180 °C Ober-/Unterhitze 12–14 Minuten backen.',
           'Abkühlen lassen, mit einem Löffel die obere Schicht abheben und fein zerbröseln. Banane in Scheiben auf den Boden legen.',
           '120 g Skyr, Frischkäse, 10 g Erythrit und Vanille cremig rühren, als Hügel auf die Bananen streichen, mit den Schokobröseln und der geraspelten Schokolade bedecken und 1 Stunde kalt stellen.'],
 frage='Maulwurfkuchen: Gab es den bei euch auch auf jedem Kindergeburtstag?', tags='#maulwurfkuchen #bowl #backen #fitmitkev',
 prompt=BOWL+'Inside: a dark chocolate sponge cake base, a layer of banana slices visible through the glass, a thick mound of white cream on top completely covered with dark chocolate cake crumbs and dark chocolate shavings, half a banana beside the dish.'),
# 6 · 11:00 · herzhaft · Lasagne (23.10. 250 k, 26.10. 86 k)
dict(key='Lasagne', suess=False, hook='Der Klassiker:', titel=['LASAGNE','IN LEICHT'], portion='pro Portion', anzahl=6, vs=750,
 zutaten=[Z('9 Stück','Lasagneplatten','lasagneplatten','lasagneplatten',160), Z('500 g','Rinderhack (mager)','rinderhack','hack',500), Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1),
          Z('2 Stück','Karotten','karotten','karotten',150), Z('700 g','Passierte Tomaten','passierte_tomaten','tomaten',700), Z('400 g','Skyr','skyr','skyr',400),
          Z('1 Stück','Ei','ei','ei',st=1), Z('125 g','Mozzarella light','mozzarella_light','mozzarella',125)],
 ex=['Salz, Pfeffer, Oregano', '1 Zehe Knoblauch'],
 intro='Die Lasagne, die bei mir jede Woche läuft: Bolognese aus magerem Hack, statt Béchamel eine Skyr-Ei-Creme, obendrauf Mozzarella light. Schmeckt wie beim Italiener und reicht für die ganze Familie: {k} kcal und {p} g Eiweiß pro Portion statt 750 für die Lasagne im Restaurant!',
 schritte=['Hack mit gewürfelter Zwiebel und Karotten krümelig anbraten, passierte Tomaten zugeben, mit Salz, Pfeffer, Oregano und Knoblauch würzen und 10 Minuten köcheln.',
           'Skyr mit Ei verrühren und salzen. In einer Auflaufform (20 × 30 cm) abwechselnd Hacksoße, Lasagneplatten und Skyr-Creme schichten, mit Creme abschließen und Mozzarella darüber verteilen.',
           'Bei 180 °C Ober-/Unterhitze 35 Minuten backen und 10 Minuten ruhen lassen.'],
 frage='Lasagne: das Eckstück oder lieber aus der Mitte?', tags='#lasagne #auflauf #familienessen #fitmitkev',
 prompt='A white ceramic rectangular baking dish with a classic lasagna with a golden brown melted cheese top, one square portion lifted out onto a white plate in front showing distinct layers of pasta sheets, red minced beef tomato sauce and white cream from the side, a fork beside.'),
# 7 · 12:00 · süß · Bowl (27.10. 153 k, 31.10. 82 k)
dict(key='SpekKaeseBowl', suess=True, hook='Nur für dich:', titel=['SPEKULATIUS-','KÄSEKUCHEN-BOWL'], portion='die ganze Bowl', anzahl=1, vs=700,
 zutaten=[Z('250 g','Skyr','skyr','skyr',250), Z('1 Stück','Ei','ei','ei',st=1), Z('15 g','Vanillepudding-Pulver','vanillepudding_pulver','puddingpulver',15),
          Z('20 g','Erythrit','erythrit','erythrit',20), Z('4 Stück','Spekulatius','spekulatius','spekulatius',st=4)],
 ex=[],
 intro='Mein Spekulatius-Käsekuchen als Bowl nur für dich: Spekulatius-Boden, cremige Skyr-Masse, Spekulatius-Brösel obendrauf. Nur 5 Zutaten, ohne Sahne und ohne Butter: {k} kcal und {p} g Eiweiß die ganze Bowl statt 700 für zwei Stücke Käsekuchen vom Bäcker!',
 schritte=['2 Spekulatius fein zerbröseln und in eine kleine gefettete Glasform (15 × 10 cm) drücken.',
           'Skyr, Ei, Puddingpulver und Erythrit glatt rühren, auf den Boden füllen und bei 170 °C Ober-/Unterhitze 25 Minuten backen.',
           'Abkühlen lassen, 1 Stunde kalt stellen und mit 2 zerbröselten Spekulatius bestreuen.'],
 frage='Spekulatius: Ab wann darf er bei euch auf den Tisch?', tags='#spekulatius #fitmitkev',
 prompt=BOWL+'Inside: a baked creamy pale cheesecake with a light golden top on a thin brown spiced cookie crumb base, the top sprinkled with crumbled brown speculoos cookies, two whole speculoos cookies (thin rectangular brown spiced Christmas biscuits with an embossed pattern) beside the dish.'),
# 8 · 13:00 · herzhaft · neue Variante des Montags-Gewinners Cordon-bleu-Auflauf (13:00 Uhr, 67 k)
dict(key='CordonBleu', suess=False, hook='Wie im Gasthaus:', titel=['CORDON BLEU','AUS DEM OFEN'], portion='pro Portion', anzahl=4, vs=850,
 zutaten=[Z('600 g','Hähnchenbrust','haehnchenbrust','haehnchen',600), Z('4 Scheiben','Putenschinken','putenschinken','putenschinken',80), Z('4 Scheiben','Käse light','kaese_light','kaesescheiben',100),
          Z('1 Stück','Ei','ei','ei',st=1), Z('60 g','Cornflakes (ungesüßt)','cornflakes','cornflakes',60), Z('1 TL','Paprikapulver','paprikapulver','zimt',0),
          Z('1 EL','Öl','oel','oel',10), Z('600 g','Kartoffeln','kartoffeln','kartoffeln',600)],
 ex=['Salz, Pfeffer', '4 Zahnstocher'],
 intro='Cordon bleu wie im Gasthaus: knusprig paniert, mit Schinken und Käse, der aus der Mitte läuft. Aus dem Ofen statt aus der Pfanne, mit Cornflakes-Panade und einem Löffel Öl, dazu Salzkartoffeln: {k} kcal und {p} g Eiweiß pro Portion statt 850 für Cordon bleu mit Pommes!',
 schritte=['Kartoffeln schälen und in Salzwasser 20 Minuten kochen. Die 4 Hähnchenbrustfilets (je ca. 150 g) seitlich tief einschneiden, je 1 Scheibe Schinken und Käse hineinlegen, mit Zahnstochern verschließen, salzen und pfeffern.',
           'Cornflakes fein zerdrücken und mit Paprikapulver mischen. Hähnchen durch das verquirlte Ei ziehen, in den Cornflakes wenden und gut andrücken.',
           'Auf ein Backblech mit Backpapier legen, mit dem Öl beträufeln und bei 200 °C Ober-/Unterhitze 25 Minuten backen (Airfryer: 18 Minuten bei 190 °C). Mit den Kartoffeln servieren.'],
 frage='Cordon bleu: mit Kartoffeln, Pommes oder Salat?', tags='#cordonbleu #fitmitkev',
 prompt='A white plate with a golden crispy breaded chicken cordon bleu cut in half, showing melted cheese and pink ham inside flowing out, served next to boiled peeled yellow potatoes, a fork beside, a second whole golden breaded cordon bleu on a baking tray blurred in the background.'),
# 9 · 13:55 · süß · Dessert (31.10. 187 k, 5.11. 77 k)
dict(key='SchokoMousse', suess=True, hook='In 5 Minuten:', titel=['SCHOKOMOUSSE','AUS 4 ZUTATEN'], portion='pro Glas', anzahl=4, vs=380,
 zutaten=[Z('500 g','Skyr','skyr','skyr',500), Z('25 g','Backkakao','backkakao','kakao',25), Z('40 g','Erythrit','erythrit','erythrit',40),
          Z('40 g','Zartbitterschokolade','zartbitterschokolade','schokolade',40)],
 ex=[],
 intro='Schokomousse ohne Sahne und ohne Ei: Skyr, Kakao, Erythrit und etwas geschmolzene Zartbitterschokolade, 2 Minuten luftig aufgeschlagen. In 5 Minuten fertig, 4 Gläser: {k} kcal und {p} g Eiweiß pro Glas statt 380 für Mousse au Chocolat mit Sahne!',
 schritte=['Schokolade schmelzen und kurz abkühlen lassen.',
           'Skyr, Kakao und Erythrit mit dem Mixer 2 Minuten luftig aufschlagen, die flüssige Schokolade unterrühren.',
           'In 4 Gläser füllen und 1 Stunde kalt stellen.'],
 frage='Schokomousse: pur oder mit Früchten?', tags='#schokomousse #dessert #schokolade #skyr #fitmitkev',
 prompt='Two small glasses of thick airy dark chocolate mousse seen from the side at eye level, smooth swirled top with a few dark chocolate shavings, a few squares of dark chocolate beside the glasses, a small spoon beside, two more glasses of chocolate mousse blurred in the background.'),
# 10 · 14:55 · herzhaft · herzhaft zur Kaffeezeit (neu, Board wie ein Kuchen: Stück vorn)
dict(key='SchinkenLauchQuiche', suess=False, hook='Herzhaft zum Kaffee:', titel=['SCHINKEN-LAUCH-','QUICHE'], portion='pro Stück', anzahl=8, vs=450,
 zutaten=[Z('200 g','Dinkelmehl','dinkelmehl','dinkelmehl',200), Z('350 g','Skyr','skyr','skyr',350), Z('3 Stück','Eier','eier','ei',st=3),
          Z('100 ml','Milch (1,5 %)','milch','milch',100), Z('150 g','Kochschinken','kochschinken','kochschinken',150), Z('1 Stange','Lauch','lauch','lauch',150),
          Z('100 g','Reibekäse light','reibekaese_light','reibekaese',100), Z('1 TL','Backpulver','backpulver','backpulver',0)],
 ex=['½ TL Salz für den Teig', 'Salz, Pfeffer, Muskat'],
 intro='Quiche wie in Frankreich, nur ohne Butterteig und ohne Sahne: Boden aus Skyr-Teig, darauf Schinken und Lauch in einem cremigen Eierguss, mit Käse überbacken. Schmeckt warm und kalt, 8 Stücke: {k} kcal und {p} g Eiweiß pro Stück statt 450 für die Quiche vom Bäcker!',
 schritte=['Mehl, 150 g Skyr, Backpulver und ½ TL Salz zu einem Teig kneten, in eine gefettete Tarte- oder Springform (26 cm) drücken, einen 3 cm hohen Rand formen und bei 200 °C Ober-/Unterhitze 10 Minuten vorbacken.',
           'Lauch in Ringe schneiden und in einer beschichteten Pfanne 3 Minuten dünsten, Schinken würfeln. Beides mit der Hälfte vom Käse auf dem Boden verteilen.',
           'Eier, Milch und 200 g Skyr verquirlen, mit Salz, Pfeffer und Muskat würzen, darübergießen, restlichen Käse darauf und bei 180 °C 30–35 Minuten goldbraun backen.'],
 frage='Quiche: warm aus dem Ofen oder kalt am nächsten Tag?', tags='#quiche #herzhaftbacken #schinken #lauch #fitmitkev',
 prompt='A round savory quiche in a white ceramic tart dish seen from the side slightly elevated, golden brown baked egg and cheese filling with visible pink ham cubes and green leek rings, a raised golden crust edge, one slice cut and placed on a small white plate in front showing the creamy pale yellow filling with ham and leek from the side, a fork beside.'),
# 11 · 15:55 · süß · der verlässlichste Volltreffer (25.10. 15:44 Uhr 263 k, 3.11. 15:10 Uhr 272 k)
dict(key='ZimtstreuselSkyr', suess=True, hook='Euer Liebling:', titel=['SKYR-KUCHEN MIT','ZIMT-STREUSELN'], portion='pro Stück', anzahl=8, vs=380,
 zutaten=[Z('750 g','Skyr','skyr','skyr',750), Z('3 Stück','Eier','eier','ei',st=3), Z('1 Päckchen','Vanillepudding-Pulver','vanillepudding_pulver','puddingpulver',37),
          Z('90 g','Erythrit','erythrit','erythrit',90), Z('60 g','Dinkelmehl','dinkelmehl','dinkelmehl',60), Z('30 g','Butter (kalt)','butter','butter',30),
          Z('2 TL','Zimt','zimt','zimt',0)],
 ex=[],
 intro='Cremiger Skyr-Kuchen zwischen knusprigen Zimt-Streuseln: unten ein dünner Streuselboden, oben eine dicke Streuselschicht. Einer der beliebtesten Kuchen hier auf der Seite, ohne Sahne: {k} kcal und {p} g Eiweiß pro Stück statt 380 für den Streuselkuchen vom Bäcker!',
 schritte=['Mehl, 30 g Erythrit, Zimt und die kalte Butter in Stückchen zu Streuseln reiben. Ein Drittel davon als dünnen Boden in eine Springform (20 cm) mit Backpapier drücken.',
           'Skyr, Eier, Puddingpulver und 60 g Erythrit glatt rühren, auf den Streuselboden füllen und die restlichen Streusel darüber verteilen.',
           'Bei 170 °C Ober-/Unterhitze 50 Minuten backen, im Ofen abkühlen lassen und mindestens 3 Stunden kalt stellen.'],
 frage='Streusel: Sind sie für euch auch das Beste am Kuchen?', tags='#skyrkuchen #zimtstreusel #fitmitkev',
 prompt='A round cheesecake about 5 cm tall on a white cake stand seen from the side, the top completely covered with golden brown cinnamon crumble streusel, one slice cut and placed on a small white plate in front showing the creamy white filling, the thin crumb base and the thick streusel layer from the side, two cinnamon sticks beside, a fork beside.'),
# 12 · 16:50 · herzhaft · Auflauf zur Abendessen-Planung (26.10. 13:30 Uhr 28 k, ×2,9)
dict(key='GnocchiAuflauf', suess=False, hook='Alles aus einer Form:', titel=['GNOCCHI-','AUFLAUF'], portion='pro Portion', anzahl=4, vs=800,
 zutaten=[Z('500 g','Gnocchi (Kühlregal)','gnocchi','gnocchi',500), Z('400 g','Rinderhack (mager)','rinderhack','hack',400), Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1),
          Z('400 g','Passierte Tomaten','passierte_tomaten','tomaten',400), Z('1 Stück','Rote Paprika','rote_paprika','paprika_st',st=1), Z('150 g','Skyr','skyr','skyr',150),
          Z('125 g','Mozzarella light','mozzarella_light','mozzarella',125), Z('2 TL','Italienische Kräuter','italienische_kraeuter','zimt',0)],
 ex=['Salz, Pfeffer', '1 Zehe Knoblauch', 'frische Kräuter zum Garnieren'],
 intro='Gnocchi-Auflauf für die ganze Familie: Gnocchi aus dem Kühlregal kommen roh in eine Hack-Tomaten-Soße mit Paprika, Skyr macht sie cremig, Mozzarella obendrauf. Eine Pfanne, eine Form, 35 Minuten: {k} kcal und {p} g Eiweiß pro Portion statt 800 für Gnocchi in Sahnesoße!',
 schritte=['Hack mit gewürfelter Zwiebel und Paprika krümelig anbraten, passierte Tomaten, Kräuter, Salz, Pfeffer und Knoblauch zugeben und 5 Minuten köcheln, dann den Skyr unterrühren.',
           'Gnocchi roh unter die Soße heben und alles in eine Auflaufform (20 × 30 cm) geben.',
           'Mozzarella darüber verteilen und bei 200 °C Ober-/Unterhitze 20–25 Minuten überbacken.'],
 frage='Gnocchi: aus der Pfanne oder überbacken?', tags='#gnocchi #auflauf #fitmitkev',
 prompt='A white ceramic rectangular baking dish with a gnocchi casserole: small potato gnocchi in a red minced beef tomato sauce with red bell pepper pieces, topped with melted golden brown mozzarella cheese, one portion served on a white plate in front, a fork beside.'),
# 13 · 17:50 · süß · Plätzchen (18.10. 119 k, 31.10. 16:15 Uhr 87 k = ×11,5)
dict(key='Kokosmakronen', suess=True, hook='Nur 3 Zutaten:', titel=['KOKOS-','MAKRONEN'], portion='pro Stück', anzahl=25, vs=110,
 zutaten=[Z('200 g','Kokosraspel','kokosraspel','kokosraspel',200), Z('3 Stück','Eiweiß','eiweiss','eiweiss',105), Z('80 g','Erythrit','erythrit','erythrit',80)],
 ex=['Prise Salz'],
 intro='Drei Zutaten, kein Mehl, kein zugesetzter Zucker: Eiweiß steif schlagen, Kokosraspel und Erythrit unterheben, 15 Minuten backen. Außen knusprig, innen saftig, 25 Stück vom Blech: {k} kcal und {p} g Eiweiß pro Makrone statt 110 für die Kokosmakrone vom Bäcker!',
 schritte=['Eiweiß mit einer Prise Salz steif schlagen, Erythrit langsam einrieseln lassen und weiterschlagen, bis die Masse glänzt.',
           'Kokosraspel vorsichtig unterheben.',
           'Mit zwei Teelöffeln 25 Häufchen auf ein Backblech mit Backpapier setzen und bei 160 °C Ober-/Unterhitze 15 Minuten backen, bis die Spitzen goldbraun sind.'],
 frage='Kokosmakronen: pur oder mit Schokoboden?', tags='#kokosmakronen #plätzchen #weihnachtsbäckerei #fitmitkev',
 prompt='Homemade coconut macaroons: small rough white mounds of shredded coconut with golden brown toasted tips, piled on a white plate, a few macaroons lying on the wooden table in front, one broken open showing the moist white inside, a little shredded coconut scattered beside.'),
# 14 · 18:50 · herzhaft · Wiederholung des Treffers vom 29.10., 19:00 Uhr (216 k); Montag: Cheeseburger-Auflauf 85 k
dict(key='CheeseburgerLasagne', suess=False, hook='Burger trifft Lasagne:', titel=['CHEESEBURGER-','LASAGNE'], portion='pro Portion', anzahl=4, vs=900,
 zutaten=[Z('8 Stück','Lasagneplatten','lasagneplatten','lasagneplatten',150), Z('400 g','Rinderhack (mager)','rinderhack','hack',400), Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1),
          Z('400 g','Passierte Tomaten','passierte_tomaten','tomaten',400), Z('3 Stück','Gewürzgurken','gewuerzgurken','gurken',90), Z('1 EL','Senf','senf','senf',15),
          Z('250 g','Skyr','skyr','skyr',250), Z('4 Scheiben','Cheddar light','cheddar_light','kaesescheiben',100)],
 ex=['1 EL Tomatenmark', '1 TL Paprikapulver', 'Salz, Pfeffer'],
 intro='Cheeseburger als Lasagne: Hack mit Zwiebeln, Gewürzgurken, Senf und geschmolzener Cheddar, alles, was einen Burger ausmacht, in Schichten. Die Kinder lieben sie, und sie macht richtig satt: {k} kcal und {p} g Eiweiß pro Portion statt 900 für Cheeseburger mit Pommes!',
 schritte=['Zwiebel fein würfeln und mit dem Hack in einer beschichteten Pfanne krümelig anbraten, Tomatenmark kurz mitrösten, passierte Tomaten und Paprikapulver dazu, salzen, pfeffern und 10 Minuten köcheln.',
           'Skyr mit Senf glatt rühren, Gewürzgurken in Scheiben schneiden. In einer Auflaufform (20 × 30 cm) dreimal schichten: Hacksoße, Lasagneplatten, Senf-Skyr, ein paar Gurkenscheiben. Mit Hacksoße abschließen und mit Cheddar belegen.',
           'Bei 180 °C Ober-/Unterhitze 35–40 Minuten backen, 10 Minuten ruhen lassen und mit den restlichen Gurkenscheiben servieren.'],
 frage='Cheeseburger: mit Gurke oder ohne?', tags='#cheeseburger #lasagne #auflauf #fitmitkev',
 prompt='A white ceramic rectangular baking dish with a cheeseburger lasagna: golden orange melted cheddar cheese on top with round green pickle slices, one square portion lifted out onto a white plate in front showing layers of pasta sheets, browned minced beef in tomato sauce and white cream from the side, a few green pickle slices on top, a fork beside.'),
# 15 · 19:45 · süß · Kuchen am Abend (12.10. ×12,7, 18.10. 93 k; seitdem nicht gelaufen)
dict(key='TiramisuSkyrKuchen', suess=True, hook='Tiramisu als Kuchen:', titel=['TIRAMISU-','SKYR-KUCHEN'], portion='pro Stück', anzahl=8, vs=400,
 zutaten=[Z('8 Stück','Löffelbiskuits','loeffelbiskuit','loeffelbiskuit',st=8), Z('60 ml','Espresso','espresso','espresso',60), Z('750 g','Skyr','skyr','skyr',750),
          Z('3 Stück','Eier','eier','ei',st=3), Z('1 Päckchen','Vanillepudding-Pulver','vanillepudding_pulver','puddingpulver',37), Z('60 g','Erythrit','erythrit','erythrit',60),
          Z('10 g','Backkakao','backkakao','kakao',10)],
 ex=[],
 intro='Tiramisu als gebackener Skyr-Kuchen: unten in Espresso getränkte Löffelbiskuits, darauf eine cremige Vanille-Skyr-Schicht, obendrauf dick Kakao. Ohne Mascarpone und ohne rohe Eier: {k} kcal und {p} g Eiweiß pro Stück statt 400 für die Tiramisu-Torte vom Konditor!',
 schritte=['Springform (20 cm) mit Backpapier auslegen. Löffelbiskuits kurz in den Espresso tunken und als Boden auslegen.',
           'Skyr, Eier, Puddingpulver und Erythrit glatt rühren, auf den Boden füllen und bei 170 °C Ober-/Unterhitze 50 Minuten backen.',
           'Im ausgeschalteten Ofen 30 Minuten abkühlen lassen, mindestens 3 Stunden kalt stellen und vor dem Servieren dick mit Kakao bestäuben.'],
 frage='Tiramisu: als Kuchen oder klassisch aus der Form?', tags='#tiramisu #fitmitkev',
 prompt='A round pale cheesecake about 5 cm tall on a white cake stand seen from the side, the top thickly dusted with dark brown cocoa powder, one slice cut and placed on a small white plate in front showing from the side a thin base of coffee-soaked ladyfinger sponge biscuits and a thick creamy white filling with a dark cocoa top, two ladyfinger biscuits and a small white cup of espresso beside, a fork beside.'),
# 16 · 20:45 · herzhaft · Wiederholung des Treffers vom 31.10., 20:45 Uhr (117 k)
dict(key='Kaesespaetzle', suess=False, hook='Wie auf der Hütte:', titel=['KÄSE-','SPÄTZLE'], portion='pro Portion', anzahl=4, vs=900,
 zutaten=[Z('500 g','Spätzle oder Knöpfle','spaetzle','spaetzle',500), Z('2 Stück','Zwiebeln','zwiebeln','zwiebel',st=2), Z('150 g','Reibekäse light','reibekaese_light','reibekaese',150),
          Z('150 g','Skyr','skyr','skyr',150), Z('100 ml','Milch (1,5 %)','milch','milch',100), Z('150 g','Hüttenkäse','huettenkaese','huettenkaese',150),
          Z('1 EL','Öl','oel','oel',10), Z('2 EL','Schnittlauch','schnittlauch','schnittlauch',0)],
 ex=['Salz, Pfeffer, Muskat'],
 intro='Käsespätzle wie auf der Hütte, nur mit halb so viel Fett: Käse light, Hüttenkäse und Skyr statt Bergkäse und Sahne, dazu Röstzwiebeln aus dem Ofen. Mit Spätzle oder Knöpfle aus dem Kühlregal in 30 Minuten fertig: {k} kcal und {p} g Eiweiß pro Portion statt 900 für Käsespätzle von der Hütte!',
 schritte=['Zwiebeln in Ringe schneiden, mit Öl und Salz mischen und bei 200 °C Ober-/Unterhitze 15 Minuten im Ofen rösten.',
           'Spätzle oder Knöpfle nach Packung erhitzen. Skyr, Milch, Hüttenkäse und die Hälfte vom Käse verrühren, unter die heißen Spätzle heben und mit Salz, Pfeffer und Muskat würzen.',
           'In eine Auflaufform (20 × 30 cm) geben, restlichen Käse darüber streuen, 10 Minuten überbacken und mit Röstzwiebeln und Schnittlauch servieren.'],
 frage='Käsespätzle: mit Röstzwiebeln oder mit Salat dazu?', tags='#käsespätzle #fitmitkev',
 prompt='A white ceramic rectangular baking dish with German cheese spaetzle (Käsespätzle): small soft irregular egg noodles in melted stretchy golden cheese, topped with golden brown roasted onion rings and chopped green chives, one portion served on a white plate in front with melted cheese strings, a fork beside.'),
]

# Extras (Tomatenmark …) in kcal/Eiweiß/KH/Fett pro Rezept gesamt
EXN={'CheeseburgerLasagne':(13,0.6,2,0)}
for r in R: r['exnut']=[EXN[r['key']]] if r['key'] in EXN else []

# Hashtag-Test (Kev 10.11.), Gruppen gegenüber Mittwoch GETAUSCHT: Beiträge 1,2,5,6,9,10,13,14 = Gruppe B (4–5), 3,4,7,8,11,12,15,16 = Gruppe A (2–3).
# Je Gruppe 4 süße + 4 herzhafte. #fitmitkev immer zuletzt.
HASHTAG_SOLL={1:5,2:5,3:3,4:3,5:4,6:4,7:2,8:2,9:5,10:5,11:3,12:3,13:4,14:4,15:2,16:2}

if __name__=='__main__':
    assert len(R)==16
    for i,r in enumerate(R,1):
        k,p,c,f=macros4(r); nt=len(r['tags'].split())
        assert nt==HASHTAG_SOLL[i], (i,r['key'],nt)
        assert r['tags'].split()[-1]=='#fitmitkev'
        assert r['suess']==(i%2==1), ('süß/herzhaft-Wechsel',i)
        assert r['vs']>k and len(r['zutaten'])<=8 and len(r['schritte'])==3, r['key']
        assert r['suess'] or r['portion']!='pro Portion' or k<=500, ('Hauptgericht über 500 kcal',r['key'],k)
        print(f"{i:2d} {r['key']:22s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P {c:3d}C {f:3d}F  {r['portion']:15s} vs {r['vs']}  {len(r['zutaten'])} Kacheln  {nt} #")
