# -*- coding: utf-8 -*-
# G94 – Montag 16.11.2026, 20 Beiträge 6:10–20:45 (Kev 14.11. per Dialog: „20 Beiträge“, Box „Halb/halb wie am Wochenende“)
# Keine Werbung für die Black Week, kein Höflich-Titel. Erster Tag der Aufwärmwoche: 2 Rezepte mit Proteinpulver als echter Zutat
#   (Vanillekipferl-Oats 6:10, Spekulatius-Eis 13:50) – Board markenfrei („Proteinpulver Vanille“), ESN nur als gekennzeichnete Zeile im 1. Kommentar.
# Box-Test, dritter Tag, neues Muster (hängt weder an der Uhrzeit noch an der Hashtag-Gruppe):
#   OHNE Box „So geht's“: 1, 4, 5, 7, 10, 12, 13, 15, 18, 20 · MIT Box: 2, 3, 6, 8, 9, 11, 14, 16, 17, 19 (OHNE_BOX unten).
# Hashtag-Test 2–3 gegen 4–5, Gruppen gegenüber Sonntag getauscht: 1,2,5,6,9,10,13,14,17,18 = 4–5 · 3,4,7,8,11,12,15,16,19,20 = 2–3.
# Auswahl nach der 7-Tage-Regel (letzter Lauf spätestens 9.11., nichts von Di–So):
#   Zugpferde: Quarkbällchen ohne Fritteuse (G80; 30.10. 68 k, ×11) 9:15 · Brownie-Bowl (G54; 25.10. 152 k, ×6,9) 12:20;
#   ausgeruhte Treffer: Nussecken (G80; 30.10. 344 k), Zitronenkuchen ohne Mehl & Butter (G9; 15.10. 126 k), Spekulatius-Eis aus Hüttenkäse
#   (G60; 26.10. 119 k), Gyros-Lasagne (G62; 26.10. 126 k), Bratkartoffeln mit Spiegelei (6.11. ×8), Vanillekipferl-Oats (7.11. ×7,6),
#   Mac and Cheese (G77; 3.11. ×3,4), Döner im Skyr-Fladenbrot (G67; 28.10. ×3,5);
#   vom Montag 9.11. (genau 7 Tage Pause, ausgereift): Cheeseburger-Auflauf 92 k, Cordon-Bleu-Auflauf 88 k, Quarkbrötchen 42 k, Pizzabrötchen 34 k;
#   aus dem Archiv, länger nicht gelaufen: Mandarinen-Käsekuchen-Bowl (G65), Haferflocken-Plätzchen (G39), Apfel-Streusel-Skyr-Kuchen (G29),
#   Rote Grütze (G79), Kartoffelgratin (G80); neu: Maultaschen-Auflauf.
import sys, os, copy
_D=os.path.dirname(os.path.abspath(__file__))
for g in ('g87','g88','g89','g90','g91','g92','g93'): sys.path.insert(0, os.path.join(_D, '..', g))
from g90_data import NUT, PIECE, nut, Z, macros4
from g89_data import BOWL
import g91_data, g92_data, g93_data   # NUT-Ergänzungen von Freitag bis Sonntag
import g87_data
NUT.update({
 # ESN Designer Protein Extra Creamy: laut esn.com 112–116 kcal und 22–24 g Eiweiß je 30 g (je nach Sorte) -> 113 kcal / 23 g; KH/Fett typische Werte
 'proteinpulver':(377,77,7,5),
 'beeren':(45,1,8,0.5), 'maultaschen':(200,9,22,8), 'huettenkaese':(95,12,2.5,4.3),
})
_R87={r['key']:r for r in g87_data.R}
def alt(key, kurz, tags, **kw):
    r=copy.deepcopy(_R87[key]); r['kurz']=kurz; r['tags']=tags; r.update(kw); r.pop('fb',None); return r
ESN_ZEILE='Werbung: Als Proteinpulver nehme ich das Designer Protein von ESN in Vanille.'

R = [
# 1 · 06:10 · süß · Vanillekipferl-Oats mit Proteinpulver (7.11. ×7,6) · ohne Box · 4 #
dict(key='KipferlOats', suess=True, hook='Abends vorbereiten:', titel=['VANILLEKIPFERL-','OVERNIGHT OATS'], portion='pro Glas', anzahl=2, vs=520,
 zutaten=[Z('80 g','Zarte Haferflocken','zarte_haferflocken','haferflocken',80), Z('250 g','Skyr','skyr','skyr',250), Z('250 ml','Milch (1,5 %)','milch','milch',250),
          Z('30 g','Proteinpulver Vanille','proteinpulver','proteinpulver',30), Z('30 g','Gemahlene Mandeln','gemahlene_mandeln','mandeln',30),
          Z('1 TL','Vanilleextrakt','vanilleextrakt','vanille',0), Z('10 g','Mandelblättchen','mandelblaettchen','mandelblaettchen',10)],
 ex=[],
 intro='Vanillekipferl zum Frühstück: Haferflocken, Skyr, gemahlene Mandeln und Vanille über Nacht im Glas, morgens geröstete Mandelblättchen obendrauf. Abends in 5 Minuten gerührt, macht bis mittags satt: {k} kcal und {p} g Eiweiß pro Glas statt 520 für Müsli mit Joghurt und Honig!',
 schritte=['Das Proteinpulver mit der Milch glatt rühren. Haferflocken, Skyr, gemahlene Mandeln und Vanille unterrühren und auf 2 Gläser verteilen.',
           'Über Nacht (mindestens 4 Stunden) in den Kühlschrank stellen.',
           'Die Mandelblättchen in einer Pfanne ohne Fett 2 Minuten goldbraun rösten und morgens auf die Oats streuen.'],
 kurz=['Proteinpulver in der Milch glatt rühren, Haferflocken, Skyr, Mandeln und Vanille unterrühren.',
       'Auf 2 Gläser verteilen und über Nacht (mindestens 4 Std.) kalt stellen.',
       'Mandelblättchen ohne Fett 2 Min. goldbraun rösten und morgens obendrauf streuen.'],
 hinweis=ESN_ZEILE,
 frage='Overnight Oats: lieber mit Vanille oder mit Zimt?', tags='#overnightoats #vanillekipferl #frühstück #fitmitkev',
 prompt='Two glass jars with overnight oats seen from the side at eye level, creamy pale vanilla oats visible through the glass, each topped with a thick layer of toasted golden flaked almonds and a light dusting of white powdered sugar, two small crescent-shaped vanilla cookies (Vanillekipferl) and a vanilla pod lying beside the jars, a spoon beside.'),
# 2 · 06:55 · herzhaft · Bratkartoffeln mit Spiegelei (6.11. 6 Uhr ×8) · mit Box · 4 #
dict(key='Bratkartoffeln', suess=False, hook='Wie bei Oma:', titel=['BRATKARTOFFELN','MIT SPIEGELEI'], portion='pro Portion', anzahl=2, vs=750,
 zutaten=[Z('500 g','Kartoffeln (gekocht)','kartoffeln','kartoffeln',500), Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1), Z('60 g','Kochschinken','kochschinken','kochschinken',60),
          Z('4 Stück','Eier','eier','ei',st=4), Z('1 EL','Öl','oel','oel',10), Z('2 Stück','Gewürzgurken','gewuerzgurken','gurken',60),
          Z('½ Bund','Schnittlauch','schnittlauch','schnittlauch',0)],
 ex=['Salz, Pfeffer, 1 TL Paprikapulver'],
 intro='Bratkartoffeln mit Spiegelei wie bei Oma: knusprig, mit Zwiebeln und Schinkenwürfeln, dazu zwei Spiegeleier und eine Gewürzgurke. Mit nur einem Löffel Öl aus der beschichteten Pfanne: {k} kcal und {p} g Eiweiß pro Portion statt 750 für die Bratkartoffeln mit Speck aus dem Gasthaus!',
 schritte=['Die gekochten Kartoffeln vom Vortag in Scheiben schneiden und im heißen Öl in einer großen beschichteten Pfanne 10 Minuten knusprig braten, dabei nur selten wenden.',
           'Zwiebel und Schinken würfeln, dazugeben und 5 Minuten mitbraten. Mit Salz, Pfeffer und Paprikapulver würzen.',
           'Die Eier in einer zweiten beschichteten Pfanne zu Spiegeleiern braten, auf die Bratkartoffeln setzen und mit Schnittlauch und Gewürzgurken servieren.'],
 kurz=['Kartoffeln vom Vortag in Scheiben schneiden und im Öl 10 Min. knusprig braten.',
       'Zwiebel und Schinken würfeln, 5 Min. mitbraten, mit Salz, Pfeffer und Paprika würzen.',
       '4 Spiegeleier braten, obendrauf setzen, mit Schnittlauch und Gewürzgurken servieren.'],
 frage='Bratkartoffeln: mit Spiegelei oder mit Sülze?', tags='#bratkartoffeln #spiegelei #omasrezepte #fitmitkev',
 prompt='A black cast iron pan filled with crispy golden brown fried potato slices with browned onions and small pink ham cubes, two fried eggs sunny side up with bright orange yolks lying on top, sprinkled with fresh chopped green chives, two pickled gherkins on a small plate beside, a fork beside.'),
# 3 · 07:40 · süß · Nussecken (G80; 30.10. 344 k) · mit Box · 3 #
dict(key='Nussecken', suess=True, hook='Wie vom Bäcker:', titel=['NUSSECKEN','IN LEICHT'], portion='pro Stück', anzahl=16, vs=300,
 zutaten=[Z('150 g','Dinkelmehl','dinkelmehl','dinkelmehl',150), Z('100 g','Skyr','skyr','skyr',100), Z('30 g','Butter','butter','butter',30),
          Z('1 Stück','Ei','ei','ei',st=1), Z('80 g','Erythrit','erythrit','erythrit',80), Z('60 g','Aprikosen-Fruchtaufstrich','aprikosen_fruchtaufstrich','fruchtaufstrich',60),
          Z('120 g','Haselnüsse (gehackt)','haselnuesse','haselnuesse',120), Z('40 g','Zartbitterschokolade','zartbitterschokolade','schokolade',40)],
 ex=[],
 intro='Nussecken wie vom Bäcker: Mürbeteig, Aprikosen-Fruchtaufstrich, knusprige Haselnusskruste und Schokospitzen. Skyr ersetzt den größten Teil der Butter, gesüßt wird ohne Zucker: {k} kcal und {p} g Eiweiß pro Nussecke statt 300 für die vom Bäcker!',
 schritte=['Mehl, 60 g Skyr, Butter, Ei und 30 g Erythrit zu einem Teig kneten, auf einem Backblech mit Backpapier ca. 25 × 25 cm groß ausrollen und mit dem Fruchtaufstrich bestreichen.',
           'Haselnüsse, 40 g Skyr und 50 g Erythrit mischen, auf dem Teig verteilen und bei 180 °C Ober-/Unterhitze 20–25 Minuten backen.',
           'Noch warm in 8 Quadrate und diese diagonal in 16 Dreiecke schneiden. Die Schokolade schmelzen und die Spitzen hineintauchen.'],
 kurz=['Mehl, 60 g Skyr, Butter, Ei und 30 g Erythrit verkneten, 25 × 25 cm ausrollen, bestreichen.',
       'Nüsse, 40 g Skyr und 50 g Erythrit mischen, verteilen, bei 180 °C 20–25 Min. backen.',
       'Warm in 16 Dreiecke schneiden und die Spitzen in geschmolzene Schokolade tauchen.'],
 frage='Nussecken: die Spitzen in Schokolade oder ganz ohne?', tags='#nussecken #backen #fitmitkev',
 prompt='Several triangular German nut corner pastries (Nussecken) stacked on a wooden board: a thin shortcrust base, a thin layer of apricot jam and a thick golden brown caramelized chopped hazelnut topping, two corners of each triangle dipped in glossy dark chocolate, one triangle leaning in front showing the layers from the side, a few whole hazelnuts beside.'),
# 4 · 08:30 · herzhaft · Quarkbrötchen (9.11. 42 k) · ohne Box · 3 #
alt('Quarkbroetchen',
 kurz=['Mehl, Quark, Ei, Backpulver, Salz, Honig und Milch zu einem glatten Teig kneten.',
       '8 Brötchen formen, kreuzweise einschneiden, mit Wasser bestreichen, Haferflocken drauf.',
       'Auf dem Backblech bei 200 °C Ober-/Unterhitze 22 Min. goldbraun backen.'],
 tags='#quarkbrötchen #ohnehefe #fitmitkev'),
# 5 · 09:15 · süß · Zugpferd Quarkbällchen (G80; 30.10. 68 k, ×11) · ohne Box · 5 #
dict(key='Quarkbaellchen', suess=True, hook='Wie von der Kirmes:', titel=['QUARKBÄLLCHEN','OHNE FRITTEUSE'], portion='pro Stück', anzahl=12, vs=150,
 zutaten=[Z('250 g','Magerquark','quark','quark',250), Z('1 Stück','Ei','ei','ei',st=1), Z('150 g','Dinkelmehl','dinkelmehl','dinkelmehl',150),
          Z('60 g','Erythrit','erythrit','erythrit',60), Z('2 TL','Backpulver','backpulver','backpulver',0), Z('1 TL','Zimt','zimt','zimt',0)],
 ex=[],
 intro='Quarkbällchen wie von der Kirmes, nur aus dem Ofen statt aus dem Fett: innen fluffig, außen in Zimt gewälzt. Sechs Zutaten, eine Schüssel, in 25 Minuten fertig: {k} kcal und {p} g Eiweiß pro Bällchen statt 150 für eins von der Kirmes. Da darf es auch die ganze Tüte sein!',
 schritte=['Quark, Ei, Mehl, 40 g Erythrit und Backpulver zu einem weichen Teig verrühren.',
           'Mit zwei Löffeln 12 Bällchen formen, auf ein Backblech mit Backpapier setzen und bei 180 °C Ober-/Unterhitze 15–18 Minuten goldbraun backen (Airfryer: 170 °C, 12 Minuten).',
           'Noch warm in Zimt und 20 g gemahlenem Erythrit wälzen.'],
 kurz=['Quark, Ei, Mehl, 40 g Erythrit und Backpulver zu einem weichen Teig verrühren.',
       '12 Bällchen aufs Blech setzen, bei 180 °C Ober-/Unterhitze 15–18 Min. goldbraun backen.',
       'Noch warm in Zimt und 20 g gemahlenem Erythrit wälzen.'],
 frage='Quarkbällchen: in Zimt gewälzt oder pur?', tags='#quarkbällchen #kirmes #ohnefritteuse #backen #fitmitkev',
 prompt='A white paper bag lying on its side on the table with many round golden brown German quark doughnut balls (Quarkbällchen) rolled in cinnamon sugar spilling out onto a wooden board, one ball in front broken open showing the fluffy pale yellow crumb inside, a small bowl of cinnamon sugar beside.'),
# 6 · 10:00 · herzhaft · neu: Maultaschen-Auflauf · mit Box · 5 #
dict(key='Maultaschen', suess=False, hook='Schwäbisch & überbacken:', titel=['MAULTASCHEN-','AUFLAUF'], portion='pro Portion', anzahl=4, vs=700,
 zutaten=[Z('600 g','Maultaschen (Kühlregal)','maultaschen','maultaschen',600), Z('2 Stück','Zwiebeln','zwiebeln','zwiebel',st=2), Z('3 Stück','Eier','eier','ei',st=3),
          Z('150 ml','Milch (1,5 %)','milch','milch',150), Z('80 g','Reibekäse light','reibekaese_light','reibekaese',80), Z('½ Bund','Schnittlauch','schnittlauch','schnittlauch',0)],
 ex=['1 TL Öl','Salz, Pfeffer, Muskat'],
 intro='Maultaschen-Auflauf wie aus dem Schwabenland: Maultaschen in Scheiben, goldbraune Zwiebeln, ein Guss aus Ei und Milch und obendrauf eine Käsekruste. Fünf Minuten Arbeit, den Rest macht der Ofen: {k} kcal und {p} g Eiweiß pro Portion statt 700 für geschmälzte Maultaschen mit Butter und Käse!',
 schritte=['Die Zwiebeln in Ringe schneiden und im Öl 5 Minuten goldbraun braten. Die Maultaschen in fingerdicke Scheiben schneiden und mit den Zwiebeln in eine Auflaufform (20 × 30 cm) schichten.',
           'Eier und Milch verquirlen, mit Salz, Pfeffer und Muskat würzen und darüber gießen.',
           'Den Käse darüber streuen, bei 200 °C Ober-/Unterhitze 25 Minuten goldbraun überbacken und mit Schnittlauch bestreuen.'],
 kurz=['Zwiebelringe im Öl goldbraun braten, Maultaschen in Scheiben schneiden, in die Form (20 × 30 cm).',
       'Eier und Milch verquirlen, mit Salz, Pfeffer und Muskat würzen und darüber gießen.',
       'Käse drauf, bei 200 °C Ober-/Unterhitze 25 Min. überbacken, Schnittlauch drüber.'],
 frage='Maultaschen: aus der Brühe, geschmälzt oder überbacken?', tags='#maultaschen #auflauf #schwäbisch #überbacken #fitmitkev',
 prompt='A rectangular white ceramic baking dish with a casserole of thick slices of Swabian filled pasta squares (Maultaschen, pale pasta dough with a green-speckled meat and spinach filling visible on the cut sides) baked in a set egg custard with golden brown fried onion rings and a golden melted cheese crust, sprinkled with fresh chopped chives, one portion served on a white plate in front, a fork beside.'),
# 7 · 10:45 · süß · Zitronenkuchen ohne Mehl & Butter (G9; 15.10. 126 k) · ohne Box · 2 #
dict(key='Zitronenkuchen', suess=True, hook='Saftig & frisch:', titel=['ZITRONENKUCHEN','OHNE MEHL & BUTTER'], portion='pro Stück', anzahl=8, vs=320,
 zutaten=[Z('150 g','Gemahlene Mandeln','gemahlene_mandeln','mandeln',150), Z('3 Stück','Eier','eier','ei',st=3), Z('200 g','Skyr','skyr','skyr',200),
          Z('70 g','Erythrit','erythrit','erythrit',70), Z('1 Stück','Bio-Zitrone','zitrone','zitrone',0), Z('1 TL','Backpulver','backpulver','backpulver',0)],
 ex=[],
 intro='Saftiger Zitronenkuchen mit Zitronenguss, in dem kein Gramm Mehl und keine Butter steckt: gemahlene Mandeln, Eier, Skyr und eine ganze Zitrone. Sechs Zutaten, eine Schüssel: {k} kcal und {p} g Eiweiß pro Stück statt 320 für das Stück Zitronenkuchen vom Bäcker!',
 schritte=['Die Zitronenschale abreiben, den Saft auspressen. Eier und 60 g Erythrit schaumig schlagen, Skyr, Zitronenschale und die Hälfte vom Saft unterrühren.',
           'Gemahlene Mandeln und Backpulver unterheben, in eine Springform (20 cm) mit Backpapier füllen und bei 170 °C Ober-/Unterhitze 35–40 Minuten goldbraun backen.',
           'Den restlichen Saft mit 10 g gemahlenem Erythrit verrühren und über den abgekühlten Kuchen streichen.'],
 kurz=['Eier und 60 g Erythrit schaumig schlagen, Skyr, Zitronenschale und halben Saft unterrühren.',
       'Mandeln und Backpulver unterheben, in der Springform (20 cm) bei 170 °C 35–40 Min. backen.',
       'Restlichen Saft mit 10 g gemahlenem Erythrit verrühren, auf den kalten Kuchen streichen.'],
 frage='Zitronenkuchen: mit dickem Guss oder nur mit Puder bestäubt?', tags='#zitronenkuchen #fitmitkev',
 prompt='A round golden yellow lemon almond cake about 5 cm tall on a white cake stand seen from the side, the top covered with a white lemon icing glaze dripping slightly over the edge and decorated with three thin lemon slices and fine yellow lemon zest, one slice cut and placed on a small white plate in front showing the moist golden crumb from the side, half a lemon beside, a fork beside.'),
# 8 · 11:30 · herzhaft · Gyros-Lasagne (G62; 26.10. 126 k) · mit Box · 2 #
dict(key='GyrosLasagne', suess=False, hook='Gyros trifft Lasagne:', titel=['GYROS-LASAGNE','IN LEICHT'], portion='pro Portion', anzahl=4, vs=850,
 zutaten=[Z('9 Stück','Lasagneplatten (180 g)','lasagneplatten','lasagneplatten',180), Z('500 g','Hähnchenbrust','haehnchenbrust','haehnchen',500), Z('2 Stück','Zwiebeln','zwiebeln','zwiebel',st=2),
          Z('500 g','Passierte Tomaten','passierte_tomaten','tomaten',500), Z('400 g','Skyr','skyr','skyr',400), Z('2 Zehen','Knoblauch','knoblauch','knoblauch',0),
          Z('125 g','Mozzarella light','mozzarella_light','mozzarella',125), Z('2 EL','Gyrosgewürz','gyrosgewuerz','gyrosgewuerz',0)],
 ex=['1 TL Öl','Salz, Pfeffer'],
 intro='Gyros trifft Lasagne: würziges Hähnchen-Gyros mit Zwiebeln in Tomatensoße, dazwischen eine Tzatziki-Creme aus Skyr und Knoblauch, obendrauf Käse. Mit Hähnchen statt Schwein und Skyr statt Béchamel: {k} kcal und {p} g Eiweiß pro Portion statt 850 für die klassische Lasagne!',
 schritte=['Das Hähnchen in dünne Streifen schneiden, mit Gyrosgewürz würzen und mit den Zwiebelringen im Öl scharf anbraten. Passierte Tomaten dazugeben und 5 Minuten köcheln.',
           'Skyr mit gepresstem Knoblauch, Salz und Pfeffer verrühren. In einer Auflaufform (20 × 30 cm) dreimal schichten: Gyros-Soße, Lasagneplatten, Skyr-Creme.',
           'Den Mozzarella darauf verteilen und bei 190 °C Ober-/Unterhitze 35 Minuten backen. 10 Minuten ruhen lassen.'],
 kurz=['Hähnchenstreifen mit Gyrosgewürz und Zwiebeln anbraten, passierte Tomaten dazu, 5 Min. köcheln.',
       'Skyr mit Knoblauch würzen. In der Form (20 × 30 cm) 3× schichten: Soße, Platten, Creme.',
       'Mozzarella drauf, bei 190 °C Ober-/Unterhitze 35 Min. backen, 10 Min. ruhen lassen.'],
 frage='Gyros oder Lasagne – oder einfach beides?', tags='#lasagne #fitmitkev',
 prompt='A rectangular white ceramic baking dish with a lasagne with a golden brown melted cheese crust, one square portion served on a white plate in front clearly showing the layers from the side: pasta sheets, strips of browned gyros-seasoned chicken with onions in red tomato sauce and layers of thick white yogurt cream, a few red onion rings and a little oregano on top, a fork beside.'),
# 9 · 12:20 · süß · Zugpferd Brownie-Bowl (G54; 25.10. 152 k) · mit Box · 4 #
dict(key='BrownieBowl', suess=True, hook='Nur für dich:', titel=['BROWNIE-','BOWL'], portion='die ganze Bowl', anzahl=1, vs=550,
 zutaten=[Z('150 g','Skyr','skyr','skyr',150), Z('1 Stück','Ei','ei','ei',st=1), Z('10 g','Backkakao','backkakao','kakao',10),
          Z('15 g','Erythrit','erythrit','erythrit',15), Z('20 g','Dinkelmehl','dinkelmehl','dinkelmehl',20), Z('15 g','Zartbitterschokolade','zartbitterschokolade','schokolade',15)],
 ex=['1 Prise Salz'],
 intro='Ein Brownie nur für dich, warm aus dem Ofen und direkt aus der Glasform gelöffelt: außen fest, innen noch feucht, mit geschmolzenen Schokostückchen. Aus Skyr statt Butter, in 25 Minuten fertig: {k} kcal und {p} g Eiweiß die ganze Bowl statt 550 für den Brownie aus dem Café!',
 schritte=['Skyr, Ei, Kakao, Erythrit, Mehl und eine Prise Salz glatt rühren.',
           'Die Schokolade grob hacken, die Hälfte unterrühren, den Teig in eine gefettete Glasform (15 × 10 cm) füllen und die restliche Schokolade darauf verteilen.',
           'Bei 180 °C Ober-/Unterhitze 20–22 Minuten backen, die Mitte darf noch leicht weich sein. 5 Minuten abkühlen lassen und warm löffeln.'],
 kurz=['Skyr, Ei, Kakao, Erythrit, Mehl und eine Prise Salz glatt rühren.',
       'Schokolade hacken, die Hälfte unterrühren, in die Glasform (15 × 10 cm), Rest obendrauf.',
       'Bei 180 °C Ober-/Unterhitze 20–22 Min. backen, 5 Min. abkühlen lassen, warm löffeln.'],
 frage='Brownie: innen weich oder durchgebacken?', tags='#brownie #bowl #schokolade #fitmitkev',
 prompt=BOWL+'Inside: a baked dark chocolate brownie with a shiny crackled dark brown top and melted dark chocolate chunks, the moist fudgy dark crumb visible through the glass and where it was eaten, two small pieces of dark chocolate beside the dish.'),
# 10 · 13:05 · herzhaft · Cordon-Bleu-Auflauf (9.11. 88 k, gleiche Uhrzeit) · ohne Box · 4 #
alt('CordonBleuAuflauf',
 kurz=['Kartoffeln in dünne Scheiben schneiden, 8 Min. vorkochen und in die Form (20 × 30 cm) schichten.',
       'Hähnchen und Zwiebel anbraten, mit Schinken darauf verteilen, Frischkäse-Senf-Soße darüber.',
       'Käse drüberstreuen und bei 200 °C Ober-/Unterhitze 25 Min. goldbraun überbacken.'],
 tags='#cordonbleu #auflauf #familienessen #fitmitkev'),
# 11 · 13:50 · süß · Spekulatius-Eis aus Hüttenkäse mit Proteinpulver (G60; 26.10. 119 k) · mit Box · 3 #
dict(key='HuettenEis', suess=True, hook='Ohne Eismaschine:', titel=['SPEKULATIUS-EIS','AUS HÜTTENKÄSE'], portion='pro Portion', anzahl=4, vs=320,
 zutaten=[Z('500 g','Hüttenkäse','huettenkaese','huettenkaese',500), Z('30 g','Proteinpulver Vanille','proteinpulver','proteinpulver',30), Z('30 g','Erythrit','erythrit','erythrit',30),
          Z('50 ml','Milch (1,5 %)','milch','milch',50), Z('6 Stück','Spekulatius','spekulatius','spekulatius',st=6), Z('1 TL','Zimt','zimt','zimt',0)],
 ex=[],
 intro='Eis aus Hüttenkäse klingt verrückt, wird aber cremig wie vom Eiscafé: pürieren, einfrieren, fertig. Mit Vanille, Zimt und Spekulatius-Stückchen schmeckt es nach Advent, ganz ohne Eismaschine und ohne Sahne: {k} kcal und {p} g Eiweiß pro Portion statt 320 für drei Kugeln aus der Eisdiele!',
 schritte=['Hüttenkäse, Proteinpulver, Erythrit, Milch und Zimt im Mixer 1–2 Minuten pürieren, bis die Masse komplett glatt ist.',
           '4 Spekulatius grob zerbröseln und unterheben. In eine Kastenform (25 cm) füllen und 3–4 Stunden einfrieren, dabei nach 1 und nach 2 Stunden kräftig durchrühren.',
           '10 Minuten antauen lassen, Kugeln abstechen und mit den restlichen zerbröselten Spekulatius bestreuen.'],
 kurz=['Hüttenkäse, Proteinpulver, Erythrit, Milch und Zimt 1–2 Min. komplett glatt pürieren.',
       '4 Spekulatius zerbröseln, unterheben, in der Kastenform (25 cm) 3–4 Std. einfrieren.',
       '10 Min. antauen lassen, Kugeln abstechen, restliche Spekulatius drüberbröseln.'],
 hinweis=ESN_ZEILE,
 frage='Hüttenkäse als Eis: Würdest du es probieren?', tags='#eis #spekulatius #fitmitkev',
 prompt='A white ceramic bowl with three round scoops of creamy pale beige cinnamon ice cream sprinkled with brown spiced biscuit crumbs, two thin flat rectangular brown spiced biscuits (German Spekulatius) with an embossed windmill pattern stuck into the ice cream, a metal loaf tin with more ice cream and an ice cream scoop blurred behind, a cinnamon stick and a spoon beside.'),
# 12 · 14:35 · herzhaft · Döner im Skyr-Fladenbrot (G67; 28.10. ×3,5) · ohne Box · 3 #
dict(key='Doener', suess=False, hook='Wie vom Dönermann:', titel=['DÖNER IM','SKYR-FLADENBROT'], portion='pro Stück', anzahl=4, vs=900,
 zutaten=[Z('300 g','Dinkelmehl','dinkelmehl','dinkelmehl',300), Z('450 g','Skyr','skyr','skyr',450), Z('2 TL','Backpulver','backpulver','backpulver',0),
          Z('500 g','Hähnchenbrust','haehnchenbrust','haehnchen',500), Z('2 TL','Dönergewürz','gyrosgewuerz','gyrosgewuerz',0), Z('½ Stück','Salatgurke','salatgurke','gurke',150),
          Z('1 Stück','Rote Zwiebel','rote_zwiebel','zwiebel',st=1), Z('1 Zehe','Knoblauch','knoblauch','knoblauch',0)],
 ex=['2 Tomaten, ½ Eisbergsalat','1 TL Öl','Salz'],
 intro='Döner wie vom Dönermann, nur selbst gemacht: knuspriges Hähnchen, frischer Salat und Knoblauchsoße im warmen Fladenbrot aus Skyr-Teig, das ohne Hefe in 15 Minuten gebacken ist. {k} kcal und {p} g Eiweiß pro Döner statt 900 für den vom Imbiss!',
 schritte=['300 g Skyr, Mehl, Backpulver und 1 TL Salz zu einem Teig kneten, 4 ovale Fladen (ca. 1,5 cm dick) formen und auf einem Backblech mit Backpapier bei 220 °C Ober-/Unterhitze 12–15 Minuten backen.',
           'Das Hähnchen in dünne Streifen schneiden, mit Dönergewürz und Öl mischen und in einer heißen Pfanne 6–8 Minuten knusprig braten. 150 g Skyr mit gepresstem Knoblauch und Salz verrühren.',
           'Salat in Streifen, Tomaten und Gurke in Scheiben, Zwiebel in Ringe schneiden. Die Fladenbrote seitlich aufschneiden und mit Salat, Hähnchen, Gemüse und Soße füllen.'],
 kurz=['300 g Skyr, Mehl, Backpulver und Salz kneten, 4 Fladen formen, bei 220 °C 12–15 Min. backen.',
       'Hähnchenstreifen mit Dönergewürz knusprig braten, 150 g Skyr mit Knoblauch verrühren.',
       'Fladen aufschneiden, mit Salat, Tomate, Gurke, Zwiebel, Hähnchen und Soße füllen.'],
 frage='Döner: mit alles und scharf? 🌶️', tags='#döner #fladenbrot #fitmitkev',
 prompt='Two homemade doner kebabs in golden brown oval flatbread pockets standing upright on a wooden board, generously filled with crispy browned strips of chicken, shredded green iceberg lettuce, tomato slices, cucumber slices and red onion rings, with white garlic yogurt sauce drizzled on top, a small bowl of white yogurt sauce beside.'),
# 13 · 15:25 · süß · Mandarinen-Käsekuchen-Bowl (G65) · ohne Box · 5 #
dict(key='MandarinenBowl', suess=True, hook='Nur für dich:', titel=['MANDARINEN-','KÄSEKUCHEN-BOWL'], portion='die ganze Bowl', anzahl=1, vs=450,
 zutaten=[Z('150 g','Skyr','skyr','skyr',150), Z('1 Stück','Ei','ei','ei',st=1), Z('10 g','Vanillepudding-Pulver','vanillepudding_pulver','puddingpulver',10),
          Z('15 g','Erythrit','erythrit','erythrit',15), Z('80 g','Mandarinen (Dose, abgetropft)','mandarinen','mandarinen',80), Z('1 Stück','Butterkeks','butterkekse','butterkeks',st=1)],
 ex=[],
 intro='Wie der Mandarinen-Schmand-Kuchen von Oma, nur als Bowl für dich allein: unten Keksboden, darüber cremiger Käsekuchen aus Skyr, obendrauf Mandarinen. Fünf Minuten rühren, 20 Minuten backen: {k} kcal und {p} g Eiweiß die ganze Bowl statt 450 für ein Stück Schmandkuchen vom Blech!',
 schritte=['Den Butterkeks zerbröseln und in eine gefettete Glasform (15 × 10 cm) drücken.',
           'Skyr, Ei, Puddingpulver und Erythrit glatt rühren, auf den Boden geben und bei 180 °C Ober-/Unterhitze 20–22 Minuten backen.',
           '10 Minuten abkühlen lassen und mit den gut abgetropften Mandarinen belegen. Lauwarm oder kalt löffeln.'],
 kurz=['Butterkeks zerbröseln und in eine gefettete Glasform (15 × 10 cm) drücken.',
       'Skyr, Ei, Puddingpulver und Erythrit glatt rühren, einfüllen, bei 180 °C 20–22 Min. backen.',
       '10 Min. abkühlen lassen, mit abgetropften Mandarinen belegen, lauwarm oder kalt löffeln.'],
 frage='Mandarinen-Kuchen: Kennst du den noch von Oma?', tags='#käsekuchen #mandarinen #bowl #omasrezepte #fitmitkev',
 prompt=BOWL+'Inside: a baked creamy pale yellow cheesecake with a thin golden biscuit crumb base at the bottom visible through the glass, the top completely covered with bright orange mandarin segments, a few mandarin segments and one rectangular butter biscuit beside the dish.'),
# 14 · 16:10 · herzhaft · Kartoffelgratin (G80) · mit Box · 5 #
dict(key='Kartoffelgratin', suess=False, hook='Cremig ohne Sahne-Berg:', titel=['KARTOFFELGRATIN','IN LEICHT'], portion='pro Portion', anzahl=4, vs=550,
 zutaten=[Z('1 kg','Kartoffeln','kartoffeln','kartoffeln',1000), Z('300 ml','Milch (1,5 %)','milch','milch',300), Z('200 g','Skyr','skyr','skyr',200),
          Z('100 ml','Kochsahne (15 %)','kochsahne','kochsahne',100), Z('100 g','Reibekäse light','reibekaese_light','reibekaese',100), Z('2 Zehen','Knoblauch','knoblauch','knoblauch',0),
          Z('1 Stück','Ei','ei','ei',st=1)],
 ex=['Salz, Pfeffer, Muskat, Thymian'],
 intro='Kartoffelgratin wie bei Oma, nur ohne 400 ml Sahne: Milch, Skyr, etwas Kochsahne und ein Ei werden im Ofen genauso cremig, obendrauf eine goldbraune Käsekruste. Als Hauptgericht oder als Beilage zum Sonntagsbraten: {k} kcal und {p} g Eiweiß pro Portion statt 550!',
 schritte=['Die Kartoffeln (am besten festkochende) schälen und in dünne Scheiben hobeln. Eine Auflaufform (20 × 30 cm) mit einer halbierten Knoblauchzehe ausreiben.',
           'Milch, Skyr, Kochsahne, Ei und den gepressten restlichen Knoblauch verrühren und kräftig mit Salz, Pfeffer, Muskat und Thymian würzen.',
           'Die Kartoffelscheiben in die Form schichten, den Guss darüber gießen, den Käse darüber streuen und bei 180 °C Ober-/Unterhitze 50–55 Minuten goldbraun backen.'],
 kurz=['Kartoffeln schälen, in dünne Scheiben hobeln und in die Auflaufform (20 × 30 cm) schichten.',
       'Milch, Skyr, Kochsahne, Ei und Knoblauch verrühren, kräftig würzen und darüber gießen.',
       'Käse drüberstreuen und bei 180 °C Ober-/Unterhitze 50–55 Min. goldbraun backen.'],
 frage='Kartoffelgratin: als Beilage oder als Hauptgericht?', tags='#kartoffelgratin #kartoffeln #auflauf #omasrezepte #fitmitkev',
 prompt='A rectangular white ceramic baking dish with a creamy potato gratin made of thin overlapping potato slices with a golden brown bubbly cheese crust, one portion lifted out and served on a white plate in front clearly showing the thin creamy potato layers from the side, a sprig of fresh thyme on top, a fork beside.'),
# 15 · 16:55 · süß · Haferflocken-Plätzchen (G39) · ohne Box · 2 #
dict(key='Haferplaetzchen', suess=True, hook='Außen knusprig, innen weich:', titel=['HAFERFLOCKEN-','PLÄTZCHEN'], portion='pro Stück', anzahl=24, vs=110,
 zutaten=[Z('150 g','Zarte Haferflocken','zarte_haferflocken','haferflocken',150), Z('50 g','Butter','butter','butter',50), Z('1 Stück','Ei','ei','ei',st=1),
          Z('70 g','Erythrit','erythrit','erythrit',70), Z('50 g','Dinkelmehl','dinkelmehl','dinkelmehl',50), Z('50 g','Skyr','skyr','skyr',50),
          Z('1 TL','Zimt','zimt','zimt',0), Z('1 TL','Backpulver','backpulver','backpulver',0)],
 ex=['1 Prise Salz'],
 intro='Haferflocken-Plätzchen wie bei Oma: die Haferflocken erst in Butter geröstet, dann mit Zimt gebacken, außen knusprig und innen weich. Mit halb so viel Butter und ohne Zucker: {k} kcal und {p} g Eiweiß pro Plätzchen statt 110. Schnell gemacht, ohne Ausrollen und ohne Ausstechen!',
 schritte=['Die Haferflocken in der Butter in einer Pfanne 3 Minuten anrösten, bis sie duften, und abkühlen lassen.',
           'Ei, Erythrit, Skyr und Zimt verrühren, dann Haferflocken, Mehl, Backpulver und eine Prise Salz unterrühren.',
           'Mit zwei Teelöffeln 24 Häufchen auf ein Backblech mit Backpapier setzen, leicht flach drücken und bei 180 °C Ober-/Unterhitze 12–14 Minuten goldbraun backen.'],
 kurz=['Haferflocken in der Butter 3 Min. anrösten, bis sie duften, und abkühlen lassen.',
       'Ei, Erythrit, Skyr und Zimt verrühren, Haferflocken, Mehl und Backpulver unterrühren.',
       '24 Häufchen aufs Blech setzen, flach drücken, bei 180 °C 12–14 Min. goldbraun backen.'],
 frage='Wer hat die früher auch immer mit Oma gebacken?', tags='#plätzchen #fitmitkev',
 prompt='Many small round rustic golden brown oatmeal cookies with a rough textured surface of visible oat flakes on a white plate, a stack of five cookies in front and one cookie broken in half showing the soft inside, a few cookies lying on the light wooden table, a small bowl of rolled oats and a cinnamon stick beside.'),
# 16 · 17:40 · herzhaft · Cheeseburger-Auflauf (9.11. 92 k, gleiche Uhrzeit) · mit Box · 2 #
alt('CheeseburgerAuflauf',
 kurz=['Nudeln kochen. Hack mit Zwiebel krümelig braten, würzen, passierte Tomaten dazugeben.',
       'Beides in der Auflaufform (20 × 30 cm) mischen, Käse drauf, bei 200 °C 15 Min. überbacken.',
       'Skyr, Ketchup und Senf verrühren, mit Gurkenscheiben auf dem Auflauf verteilen.'],
 tags='#cheeseburger #fitmitkev'),
# 17 · 18:25 · süß · Apfel-Streusel-Skyr-Kuchen (G29) · mit Box · 4 #
dict(key='ApfelStreusel', suess=True, hook='Drei Kuchen in einem:', titel=['APFEL-STREUSEL-','SKYR-KUCHEN'], portion='pro Stück', anzahl=15, vs=320,
 zutaten=[Z('200 g','Dinkelmehl','dinkelmehl','dinkelmehl',200), Z('60 g','Butter','butter','butter',60), Z('750 g','Skyr','skyr','skyr',750),
          Z('3 Stück','Eier','eier','ei',st=3), Z('1 Päckchen','Vanillepudding-Pulver','vanillepudding_pulver','puddingpulver',37), Z('110 g','Erythrit','erythrit','erythrit',110),
          Z('3 Stück','Äpfel','aepfel','apfel',st=3), Z('1 TL','Zimt','zimt','zimt',0)],
 ex=['1 Prise Salz'],
 intro='Drei Kuchen in einem: knuspriger Streuselboden, cremige Käsekuchen-Schicht aus Skyr und obendrauf Zimtäpfel mit noch mehr Streuseln. Vom Blech für die ganze Kaffeetafel, mit wenig Butter und ohne Zucker: {k} kcal und {p} g Eiweiß pro Stück statt 320 für den Apfel-Streusel vom Bäcker!',
 schritte=['Mehl, Butter in Stückchen, 50 g Erythrit, 1 Ei und eine Prise Salz zu Streuseln verkneten. Zwei Drittel als Boden in eine Form (20 × 30 cm) mit Backpapier drücken.',
           'Skyr, 2 Eier, Puddingpulver und 60 g Erythrit glatt rühren und auf den Boden streichen. Die Äpfel schälen, in dünne Spalten schneiden, mit Zimt mischen und darauf verteilen.',
           'Die restlichen Streusel darüber zupfen, bei 175 °C Ober-/Unterhitze 45 Minuten backen und mindestens 2 Stunden kalt stellen.'],
 kurz=['Mehl, Butter, 50 g Erythrit und 1 Ei zu Streuseln kneten, ⅔ in die Form (20 × 30 cm) drücken.',
       'Skyr, 2 Eier, Pudding und 60 g Erythrit glatt rühren, daraufstreichen, Zimtäpfel darauf.',
       'Rest-Streusel drüber, bei 175 °C Ober-/Unterhitze 45 Min. backen, 2 Std. kalt stellen.'],
 frage='Apfelkuchen: mit Streuseln oder gedeckt?', tags='#apfelkuchen #streuselkuchen #skyrkuchen #fitmitkev',
 prompt='Square pieces of German apple crumble cheesecake on a wooden board: a thin golden crumb base, a thick creamy white cheesecake layer, thin soft apple slices with cinnamon and golden crumble streusel on top, one piece in front on a small white plate clearly showing the three layers from the side, the rest of the cake blurred behind, a red apple and a fork beside.'),
# 18 · 19:15 · herzhaft · Pizzabrötchen (9.11. 34 k) · ohne Box · 4 #
alt('Pizzabroetchen',
 kurz=['Mehl, Skyr, Backpulver und Salz kneten, 10 flache Kugeln formen und aufs Backblech setzen.',
       'Frischkäse mit Knoblauch und Oregano verrühren, aufstreichen, Salami, Paprika und Käse drauf.',
       'Bei 200 °C Ober-/Unterhitze 20 Min. goldbraun backen.'],
 tags='#pizzabrötchen #skyrteig #abendessen #fitmitkev'),
# 19 · 20:00 · süß · Rote Grütze mit Vanillesoße (G79) · mit Box · 3 #
dict(key='RoteGruetze', suess=True, hook='Wie bei Oma:', titel=['ROTE GRÜTZE','MIT VANILLESOSSE'], portion='pro Glas', anzahl=4, vs=250,
 zutaten=[Z('500 g','Beerenmischung (TK)','beerenmischung','beeren',500), Z('150 g','Sauerkirschen (Glas)','sauerkirschen','kirschen',150), Z('20 g','Speisestärke','speisestaerke','speisestaerke',20),
          Z('40 g','Erythrit','erythrit','erythrit',40), Z('200 g','Skyr','skyr','skyr',200), Z('50 ml','Milch (1,5 %)','milch','milch',50),
          Z('1 TL','Vanilleextrakt','vanilleextrakt','vanille',0)],
 ex=[],
 intro='Rote Grütze wie bei Oma, fruchtig und ohne Zucker gekocht. Statt Vanillesoße aus Sahne gibt es eine kühle Vanillesoße aus Skyr dazu, die auch noch Eiweiß mitbringt. In 10 Minuten gekocht: {k} kcal und {p} g Eiweiß pro Glas statt 250 für die Rote Grütze mit Sahnesoße!',
 schritte=['Beeren und Kirschen mit etwas Saft aufkochen. Die Stärke mit 3 EL Wasser anrühren, einrühren, 1 Minute köcheln, 30 g Erythrit zugeben und abkühlen lassen.',
           'Skyr, Milch, Vanille und 10 g Erythrit zu einer glatten Soße rühren.',
           'Die Grütze auf 4 Gläser verteilen und die Vanillesoße darüber geben. Warm oder kalt servieren.'],
 kurz=['Beeren und Kirschen aufkochen, angerührte Stärke einrühren, 1 Min. köcheln, 30 g Erythrit dazu.',
       'Skyr, Milch, Vanille und 10 g Erythrit zu einer glatten Soße rühren.',
       'Grütze auf 4 Gläser verteilen, Vanillesoße darüber geben, warm oder kalt servieren.'],
 frage='Rote Grütze: warm oder kalt?', tags='#rotegrütze #dessert #fitmitkev',
 prompt='Four small clear dessert glasses filled with dark red berry compote (German Rote Grütze) with whole cherries, raspberries and red currants visible through the glass, each topped with a thick layer of creamy pale yellow vanilla sauce running down into the red fruit, one glass standing in front with a teaspoon beside it, a few fresh raspberries and red currants on the table.'),
# 20 · 20:45 · herzhaft · Mac and Cheese (G77; 3.11. ×3,4) · ohne Box · 3 #
dict(key='MacCheese', suess=False, hook='Cremig & überbacken:', titel=['MAC AND CHEESE','IN LEICHT'], portion='pro Portion', anzahl=4, vs=800,
 zutaten=[Z('250 g','Makkaroni (roh)','nudeln','nudeln',250), Z('300 g','Hähnchenbrust','haehnchenbrust','haehnchen',300), Z('100 g','Reibekäse light','reibekaese_light','reibekaese',100),
          Z('200 g','Skyr','skyr','skyr',200), Z('200 ml','Milch (1,5 %)','milch','milch',200), Z('1 TL','Senf','senf','senf',5),
          Z('1 EL','Speisestärke','speisestaerke','speisestaerke',10)],
 ex=['1 TL Paprikapulver','Muskat, Salz, Pfeffer'],
 intro='Mac and Cheese richtig cremig, aber mit Skyr und Käse light statt Sahne und Butter, dazu Hähnchen für ordentlich Eiweiß. Aus dem Ofen mit goldbrauner Käsekruste, perfekt für den Abend auf dem Sofa: {k} kcal und {p} g Eiweiß pro Portion statt 800 für die Käsenudeln aus dem Diner!',
 schritte=['Die Makkaroni bissfest kochen. Das Hähnchen würfeln, mit Paprikapulver, Salz und Pfeffer würzen und in einer beschichteten Pfanne goldbraun braten.',
           'Die Milch mit der Stärke verrühren, aufkochen und 1 Minute köcheln. Vom Herd nehmen, 80 g Käse, Skyr und Senf einrühren und mit Muskat, Salz und Pfeffer abschmecken.',
           'Nudeln und Hähnchen unter die Soße mischen, in eine Auflaufform (20 × 30 cm) geben, den restlichen Käse darüber streuen und bei 200 °C Ober-/Unterhitze 10 Minuten überbacken.'],
 kurz=['Makkaroni bissfest kochen. Hähnchen würfeln, würzen und in der Pfanne goldbraun braten.',
       'Milch mit Stärke aufkochen, vom Herd nehmen, 80 g Käse, Skyr und Senf einrühren.',
       'Alles mischen, in die Form (20 × 30 cm), Rest-Käse drauf, bei 200 °C 10 Min. überbacken.'],
 frage='Käsenudeln: aus dem Ofen oder direkt aus dem Topf?', tags='#macandcheese #käsenudeln #fitmitkev',
 prompt='A round white ceramic baking dish with creamy macaroni and cheese with small browned chicken pieces under a golden brown bubbly melted cheese crust, one portion served on a white plate in front with stretchy melted cheese and creamy elbow macaroni clearly visible, a fork beside.'),
]

# Extras (Öl, Ketchup …) in kcal/Eiweiß/KH/Fett pro Rezept gesamt
EXN={'CordonBleuAuflauf':(90,0,0,10), 'CheeseburgerAuflauf':(105,0,4,10), 'Maultaschen':(45,0,0,5), 'GyrosLasagne':(45,0,0,5),
     'Doener':(95,3,10,5.5)}   # Döner: 1 TL Öl + 2 Tomaten (240 g) + ½ Eisbergsalat (100 g)
for r in R: r['exnut']=[EXN[r['key']]] if r['key'] in EXN else []

# Hashtag-Test, Gruppen gegenüber Sonntag getauscht: 1,2,5,6,9,10,13,14,17,18 = B (4–5) · 3,4,7,8,11,12,15,16,19,20 = A (2–3).
HASHTAG_SOLL={1:4,2:4,3:3,4:3,5:5,6:5,7:2,8:2,9:4,10:4,11:3,12:3,13:5,14:5,15:2,16:2,17:4,18:4,19:3,20:3}
# Box-Test, dritter Tag: diese Plätze laufen OHNE Box „So geht's“ (neues Muster, weder an Uhrzeit noch an Hashtag-Gruppe gekoppelt).
OHNE_BOX={1,4,5,7,10,12,13,15,18,20}

if __name__=='__main__':
    assert len(R)==20 and len({r['key'] for r in R})==20
    for i,r in enumerate(R,1):
        k,p,c,f=macros4(r); nt=len(r['tags'].split())
        assert nt==HASHTAG_SOLL[i], (i,r['key'],nt)
        assert r['tags'].split()[-1]=='#fitmitkev'
        assert r['suess']==(i%2==1), ('süß/herzhaft-Wechsel',i)
        assert r['vs']>k and len(r['zutaten'])<=8 and len(r['schritte'])==3 and len(r['kurz'])==3, r['key']
        assert all(len(s)<=100 for s in r['kurz']), (r['key'],[len(s) for s in r['kurz']])
        assert r['suess'] or r['portion']!='pro Portion' or k<=500, ('Hauptgericht über 500 kcal',r['key'],k)
        assert 'abnehm' not in (r['intro']+' '.join(r['schritte'])+' '.join(r['kurz'])).lower()
        print(f"{i:2d} {r['key']:20s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P {c:3d}C {f:3d}F  {r['portion']:15s} vs {r['vs']}  {len(r['zutaten'])} Kacheln  {nt} #  kurz {max(len(s) for s in r['kurz'])}  {'ohne Box' if i in OHNE_BOX else 'mit Box'}")
    ob=[r for i,r in enumerate(R,1) if i in OHNE_BOX]; assert len(ob)==10 and sum(r['suess'] for r in ob)==5
    assert sum(HASHTAG_SOLL[i]<=3 for i in OHNE_BOX)==5
    import os
    TL=os.path.join(_D,'..','tilex','tiles_orig'); import json; MAP=json.load(open(TL+'/_map_g87.json'))
    fehlt=sorted({z['tile'] for r in R for z in r['zutaten'] if not os.path.exists(f"{TL}/{MAP.get(z['tile'],z['tile'])}.png")}); print('Kacheln fehlen:',fehlt)
