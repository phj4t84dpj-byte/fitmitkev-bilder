# -*- coding: utf-8 -*-
# ESN Black Week 2026 – 14 Rezepte ohne Backen mit Proteinpulver (Kev 16.11. per Dialog: „Ja, so bauen“), jedes läuft zweimal (7 Tage später),
# täglich 6:10 + 13:00 vom Do 19.11. bis Mi 2.12. Board markenfrei („Proteinpulver Schoko/Vanille/…“), ESN nur im 1. Kommentar (Zeile je Datum).
# Do–Sa 19.–21.11. (vor dem Start): Vanilla Milk / Milk Chocolate, Zeile ohne Black Week. Ab 22.11. neue Sorten.
# Alle Boards ohne Box (Kev 16.11.). Bowl-/Glas-Prompts: genau EIN schlichter Löffel (Kev 16.11. „Achte in Zukunft besser drauf“).
import sys, os
_D=os.path.dirname(os.path.abspath(__file__))
for g in ('g87','g88','g89','g90','g91','g92','g93','g93n','g94','g95','g96'): sys.path.insert(0, os.path.join(_D, '..', g))
from g90_data import NUT, PIECE, nut, Z, macros4
import g91_data, g92_data, g93_data, g94_data, g95_data
NUT.update({'pflaumen':(47,0.6,10,0.2), 'griess':(330,11,69,1)})
SPOON=" Exactly one small plain smooth stainless steel teaspoon with a straight simple handle; there is no other spoon, fork or cutlery anywhere in the picture."
BOWL1=("A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, "
       "both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner. Exactly one small plain smooth stainless steel "
       "teaspoon with a straight simple handle rests inside the dish in the eaten corner, empty and clean. There is no other spoon, fork or cutlery anywhere in the picture. Inside: ")
SPEK="thin flat rectangular Dutch speculaas spiced biscuit with an embossed windmill relief and slightly scalloped edges, light golden brown"
NOROUND=" Every biscuit in the picture is rectangular with a windmill relief; there are no round cookies anywhere."
R=[
# ---- A: Do–Sa 19.–21.11. (und 26.–28.11.) – Vanilla Milk / Milk Chocolate
dict(key='SchokoMousseESN', suess=True, sorte='Milk Chocolate', hook='Mit 5 Zutaten:', titel=['SCHOKO-','MOUSSE'], portion='pro Glas', anzahl=2, vs=380,
 zutaten=[Z('400 g','Skyr','skyr','skyr',400), Z('30 g','Proteinpulver Schoko','proteinpulver','proteinpulver',30), Z('15 g','Backkakao','backkakao','kakao',15),
          Z('20 g','Erythrit','erythrit','erythrit',20), Z('20 g','Zartbitterschokolade','zartbitterschokolade','schokolade',20)], ex=[],
 intro='Schokomousse ohne Sahne und ohne Eier, in 5 Minuten aufgeschlagen: Skyr, Kakao und Proteinpulver mit Schokogeschmack, obendrauf Zartbitter-Raspel. Cremig wie im Restaurant: {k} kcal und {p} g Eiweiß pro Glas statt 380 für die Mousse au Chocolat mit Sahne!',
 schritte=['Skyr, Proteinpulver, Kakao und Erythrit mit dem Schneebesen 2 Minuten cremig aufschlagen.',
           'In 2 Gläser füllen und mindestens 30 Minuten kalt stellen.',
           'Zartbitterschokolade grob raspeln und darüber streuen.'],
 frage='Schokomousse: mit Schokoraspeln oder mit Beeren obendrauf?', tags='#schokomousse #dessert #fitmitkev',
 prompt='Two clear straight dessert glasses seen from the side at eye level, filled with smooth airy dark chocolate mousse, topped with dark chocolate shavings, one teaspoon lying beside the glasses, a few pieces of dark chocolate on the table.'+SPOON),
dict(key='TiramisuBowlESN', suess=True, sorte='Vanilla Milk', hook='Nur für dich:', titel=['TIRAMISU-','BOWL'], portion='die ganze Bowl', anzahl=1, vs=600,
 zutaten=[Z('4 Stück','Löffelbiskuits','loeffelbiskuit','loeffelbiskuit',st=4), Z('150 g','Skyr','skyr','skyr',150), Z('15 g','Proteinpulver Vanille','proteinpulver','proteinpulver',15),
          Z('50 ml','Espresso','espresso','espresso',50), Z('10 g','Erythrit','erythrit','erythrit',10), Z('3 g','Backkakao','backkakao','kakao',3)], ex=[],
 intro='Tiramisu nur für dich, ohne Mascarpone und ohne rohe Eier: Löffelbiskuits in Espresso getunkt, darauf eine Vanille-Skyr-Creme, Kakao drüber, fertig. Ohne Backen in 10 Minuten geschichtet: {k} kcal und {p} g Eiweiß die ganze Bowl statt 600 für eine Portion Tiramisu!',
 schritte=['Löffelbiskuits kurz in den abgekühlten Espresso tunken und in eine kleine Glasform (15 × 10 cm) legen.',
           'Skyr, Proteinpulver und Erythrit cremig rühren und auf die Biskuits streichen.',
           'Mindestens 1 Stunde kalt stellen und vor dem Essen dick mit Kakao bestäuben.'],
 frage='Tiramisu: mit Espresso oder lieber ohne Kaffee?', tags='#tiramisu #bowl #ohnebacken #proteindessert #fitmitkev',
 prompt=BOWL1+'two layers of espresso-soaked pale ladyfinger biscuits and thick smooth white cream, the top thickly dusted with dark cocoa powder, two ladyfinger biscuits lying beside the dish.'),
dict(key='BratapfelQuarkESN', suess=True, sorte='Vanilla Milk', hook='Wie Bratapfel:', titel=['BRATAPFEL-','DESSERT'], portion='pro Glas', anzahl=2, vs=420,
 zutaten=[Z('2 Stück','Äpfel','apfel','apfel',st=2), Z('250 g','Magerquark','magerquark','quark',250), Z('150 g','Skyr','skyr','skyr',150),
          Z('30 g','Proteinpulver Vanille','proteinpulver','proteinpulver',30), Z('15 g','Erythrit','erythrit','erythrit',15), Z('1 TL','Zimt','zimt','zimt',0),
          Z('20 g','Rosinen','rosinen','rosinen',20), Z('20 g','Mandelblättchen','mandelblaettchen','mandelblaettchen',20)], ex=[],
 intro='Schmeckt wie Bratapfel mit Vanillesoße, nur ohne Ofen: warme Zimtäpfel mit Rosinen, dazwischen eine Vanille-Quark-Creme, obendrauf geröstete Mandeln. In 10 Minuten fertig: {k} kcal und {p} g Eiweiß pro Glas statt 420 für Bratapfel mit Vanillesoße!',
 schritte=['Äpfel würfeln und mit Zimt, Rosinen und 3 EL Wasser 5 Minuten in der Pfanne weich dünsten. Mandelblättchen ohne Fett kurz goldbraun rösten.',
           'Quark, Skyr, Proteinpulver und Erythrit cremig rühren.',
           'Creme und warme Zimtäpfel abwechselnd in 2 Gläser schichten und mit den Mandelblättchen bestreuen.'],
 frage='Bratapfel: warm aus dem Ofen oder so im Glas?', tags='#bratapfel #dessertimglas #fitmitkev',
 prompt='Two clear straight dessert glasses seen from the side at eye level, layers of warm diced cinnamon apples with raisins and thick white vanilla quark cream, topped with golden toasted flaked almonds and a dusting of cinnamon, one red apple and a cinnamon stick beside, one teaspoon beside the glasses.'+SPOON),
dict(key='SchwarzwaelderGlasESN', suess=True, sorte='Milk Chocolate', hook='Wie Torte:', titel=['SCHWARZWÄLDER','IM GLAS'], portion='pro Glas', anzahl=2, vs=450,
 zutaten=[Z('300 g','Skyr','skyr','skyr',300), Z('100 g','Magerquark','magerquark','quark',100), Z('30 g','Proteinpulver Schoko','proteinpulver','proteinpulver',30),
          Z('10 g','Backkakao','backkakao','kakao',10), Z('200 g','Sauerkirschen (Glas)','sauerkirschen','sauerkirschen_glas',200),
          Z('4 Stück','Löffelbiskuits','loeffelbiskuit','loeffelbiskuit',st=4), Z('15 g','Erythrit','erythrit','erythrit',15), Z('10 g','Zartbitterschokolade','zartbitterschokolade','schokolade',10)], ex=[],
 intro='Schwarzwälder Kirschtorte zum Löffeln, ohne Sahne und ohne Backen: Biskuit-Brösel, Schokocreme, Sauerkirschen und eine weiße Quarkhaube mit Schokoraspel. In 10 Minuten geschichtet: {k} kcal und {p} g Eiweiß pro Glas statt 450 für ein Stück Schwarzwälder Kirsch!',
 schritte=['200 g Skyr mit Proteinpulver, Kakao und der Hälfte vom Erythrit zu einer Schokocreme rühren.',
           '100 g Skyr mit Quark und dem restlichen Erythrit zu einer weißen Creme rühren.',
           'In 2 Gläser schichten: zerbröselte Löffelbiskuits, Schokocreme, Kirschen, weiße Creme. Mit Schokoraspel und je einer Kirsche garnieren.'],
 frage='Schwarzwälder Kirsch: Lieblingstorte oder eher nicht?', tags='#schwarzwälderkirsch #dessertimglas #ohnebacken #proteindessert #fitmitkev',
 prompt='Two clear straight dessert glasses seen from the side at eye level with visible layers: crumbled pale sponge biscuits at the bottom, dark chocolate cream, dark red sour cherries, thick white cream on top, sprinkled with dark chocolate shavings and one cherry on each glass, a few cherries on the table, one teaspoon beside the glasses.'+SPOON),
dict(key='VanillepuddingPflaumenESN', suess=True, sorte='Vanilla Milk', hook='Wie bei Oma:', titel=['VANILLEPUDDING','MIT ZIMTPFLAUMEN'], portion='pro Glas', anzahl=2, vs=400,
 zutaten=[Z('400 ml','Milch (1,5 %)','milch','milch',400), Z('1 Päckchen','Vanillepudding-Pulver','vanillepudding_pulver','puddingpulver',37),
          Z('30 g','Proteinpulver Vanille','proteinpulver','proteinpulver',30), Z('20 g','Erythrit','erythrit','erythrit',20),
          Z('200 g','Pflaumen (TK)','pflaumen','pflaumen',200), Z('1 TL','Zimt','zimt','zimt',0)], ex=[],
 intro='Vanillepudding wie bei Oma, nur mit doppelt so viel Eiweiß: cremig gekocht, das Proteinpulver kommt erst am Ende rein, obendrauf warme Zimtpflaumen. In 15 Minuten fertig: {k} kcal und {p} g Eiweiß pro Glas statt 400 für Pudding mit Sahne und Zwetschgenkompott!',
 schritte=['Pflaumen mit Zimt und 2 EL Wasser 5 Minuten in einem kleinen Topf weich köcheln.',
           'Puddingpulver mit Erythrit und 6 EL Milch glatt rühren. Restliche Milch aufkochen, das Pulver einrühren und unter Rühren 1 Minute köcheln.',
           'Vom Herd nehmen, 2 Minuten abkühlen lassen, Proteinpulver einrühren, in 2 Gläser füllen und die Zimtpflaumen darauf geben.'],
 frage='Pudding: warm oder kalt?', tags='#vanillepudding #pflaumen #fitmitkev',
 prompt='Two clear straight dessert glasses seen from the side at eye level, filled with smooth creamy pale yellow vanilla pudding, topped with warm dark purple stewed plum halves in glossy cinnamon syrup, a cinnamon stick and two fresh plums beside, one teaspoon beside the glasses.'+SPOON),
dict(key='SchokoKugelnESN', suess=True, sorte='Milk Chocolate', hook='Ohne Backen:', titel=['SCHOKO-','KUGELN'], portion='pro Kugel', anzahl=12, vs=140,
 zutaten=[Z('100 g','Zarte Haferflocken','zarte_haferflocken','haferflocken',100), Z('60 g','Proteinpulver Schoko','proteinpulver','proteinpulver',60),
          Z('60 g','Erdnussmus','erdnussmus','erdnussmus',60), Z('100 g','Magerquark','magerquark','quark',100), Z('15 g','Backkakao','backkakao','kakao',15),
          Z('20 g','Honig','honig','honig',20), Z('10 g','Kokosraspel','kokosraspel','kokosraspel',10)], ex=[],
 intro='Schoko-Kugeln für zwischendurch, ohne Backen und ohne Zucker im Teig: Haferflocken, Erdnussmus, Quark und Proteinpulver mit Schokogeschmack verkneten, Kugeln rollen, fertig. 12 Stück in 15 Minuten: {k} kcal und {p} g Eiweiß pro Kugel statt 140 für eine Schokopraline!',
 schritte=['Haferflocken, Proteinpulver und Kakao mischen.',
           'Erdnussmus, Quark und Honig dazugeben und zu einem festen Teig kneten (ist er zu trocken, 1–2 EL Milch dazu).',
           '12 Kugeln formen, in Kokosraspel wälzen und 30 Minuten kalt stellen.'],
 frage='Schoko-Kugeln: für die Brotdose oder fürs Sofa?', tags='#energyballs #snack #ohnebacken #schokolade #fitmitkev',
 prompt='A small white plate piled with about twelve round dark chocolate energy balls, some rolled in white desiccated coconut, one ball cut in half in front showing the dense chocolate oat inside, a few rolled oats and two balls lying on the table.'),
# ---- B: ab So 22.11. (und 29.11.–2.12.) – neue Sorten
dict(key='SpekulatiusMousseESN', suess=True, sorte='Vanilla Speculoos', hook='In 5 Minuten:', titel=['SPEKULATIUS-','MOUSSE'], portion='pro Glas', anzahl=2, vs=420,
 zutaten=[Z('400 g','Skyr','skyr','skyr',400), Z('30 g','Proteinpulver Spekulatius','proteinpulver','proteinpulver',30), Z('6 Stück','Spekulatius','spekulatius','spekulatius',st=6),
          Z('15 g','Erythrit','erythrit','erythrit',15), Z('1 TL','Spekulatiusgewürz','spekulatiusgewuerz','zimt',0)], ex=[],
 intro='Spekulatius-Mousse in 5 Minuten: Skyr mit Proteinpulver in Spekulatius-Geschmack luftig aufgeschlagen, dazwischen Spekulatius-Brösel, obendrauf ein ganzer Keks. Ohne Sahne, ohne Backen: {k} kcal und {p} g Eiweiß pro Glas statt 420 für die Spekulatius-Creme mit Sahne!',
 schritte=['Skyr, Proteinpulver, Erythrit und Spekulatiusgewürz 2 Minuten cremig aufschlagen.',
           '4 Spekulatius fein zerbröseln und abwechselnd mit der Creme in 2 Gläser schichten.',
           'Mit je einem ganzen Spekulatius garnieren und 20 Minuten kalt stellen.'],
 frage='Spekulatius: Plätzchen oder Dessert?', tags='#spekulatius #mousse #fitmitkev',
 prompt='Two clear straight dessert glasses seen from the side at eye level with visible layers of fluffy light beige spiced cream and brown biscuit crumbs, topped with crumbs and one whole '+SPEK+' standing upright in each glass, two more rectangular speculaas lying flat on the table, one teaspoon beside the glasses.'+NOROUND+SPOON),
dict(key='ErdbeerBowlESN', suess=True, sorte='Strawberry Cream', hook='Nur für dich:', titel=['ERDBEER-','QUARK-BOWL'], portion='die ganze Bowl', anzahl=1, vs=450,
 zutaten=[Z('150 g','Skyr','skyr','skyr',150), Z('100 g','Magerquark','magerquark','quark',100), Z('20 g','Proteinpulver Erdbeere','proteinpulver','proteinpulver',20),
          Z('150 g','Erdbeeren (TK)','erdbeeren','erdbeeren',150), Z('2 Stück','Butterkekse','butterkekse','butterkeks',st=2), Z('10 g','Erythrit','erythrit','erythrit',10)], ex=[],
 intro='Erdbeer-Bowl nur für dich, auch im Winter: Butterkeks-Boden, darauf eine rosa Erdbeer-Quark-Creme, obendrauf aufgetaute Erdbeeren. Ohne Backen in 5 Minuten: {k} kcal und {p} g Eiweiß die ganze Bowl statt 450 für einen Erdbeerbecher mit Sahne!',
 schritte=['Erdbeeren auftauen lassen und die Hälfte mit einer Gabel zerdrücken.',
           'Skyr, Quark, Proteinpulver, Erythrit und die zerdrückten Erdbeeren cremig rühren.',
           'Butterkekse in eine kleine Glasform (15 × 10 cm) bröseln, die Creme darauf streichen und mit den restlichen Erdbeeren belegen.'],
 frage='Erdbeeren: Hast du auch immer welche im Tiefkühler?', tags='#erdbeeren #bowl #ohnebacken #proteindessert #fitmitkev',
 prompt=BOWL1+'a thin golden butter biscuit crumb base at the bottom, a thick layer of smooth pale pink strawberry cream, topped with glossy halved red strawberries, two strawberries and one rectangular butter biscuit beside the dish.'),
dict(key='ZimtschneckenOatsESN', suess=True, sorte='Cinnamon Cereal', hook='Zimtschnecke im Glas:', titel=['ZIMTSCHNECKEN-','OVERNIGHT OATS'], portion='pro Glas', anzahl=2, vs=450, bild='../g90/hero/ZimtschneckenOats.jpg',
 zutaten=[Z('100 g','Zarte Haferflocken','zarte_haferflocken','haferflocken',100), Z('300 g','Skyr','skyr','skyr',300), Z('200 ml','Milch (1,5 %)','milch','milch',200),
          Z('30 g','Proteinpulver Zimt','proteinpulver','proteinpulver',30), Z('2 TL','Zimt','zimt','zimt',0), Z('10 g','Erythrit','erythrit','erythrit',10),
          Z('60 g','Frischkäse light','frischkaese_light','frischkaese',60)], ex=[],
 intro='Schmeckt wie eine Zimtschnecke mit Frosting, ist aber ein Frühstück, das bis mittags satt macht: Haferflocken, Skyr, Zimt und Proteinpulver über Nacht im Glas, morgens ein Frischkäse-Swirl obendrauf. Abends in 5 Minuten gerührt: {k} kcal und {p} g Eiweiß pro Glas statt 450 für die Zimtschnecke mit Glasur!',
 schritte=['Haferflocken, 240 g Skyr, Milch, Proteinpulver, Zimt und Erythrit verrühren und auf 2 Gläser verteilen.',
           'Über Nacht (mindestens 4 Stunden) in den Kühlschrank stellen.',
           'Morgens 60 g Skyr mit dem Frischkäse glatt rühren, als Frosting-Swirl auf die Oats geben und mit etwas Zimt bestäuben.'],
 frage='Zimtschnecke: lieber im Glas zum Löffeln oder frisch vom Bäcker?', tags='#overnightoats #zimtschnecken #fitmitkev', prompt=''),
dict(key='DarkSchokoPuddingESN', suess=True, sorte='Ultra Dark Chocolate', hook='Selbst gekocht:', titel=['DUNKLER','SCHOKOPUDDING'], portion='pro Glas', anzahl=2, vs=350,
 zutaten=[Z('400 ml','Milch (1,5 %)','milch','milch',400), Z('30 g','Speisestärke','speisestaerke','speisestaerke',30), Z('20 g','Backkakao','backkakao','kakao',20),
          Z('30 g','Proteinpulver Schoko','proteinpulver','proteinpulver',30), Z('25 g','Erythrit','erythrit','erythrit',25), Z('80 g','Himbeeren (TK)','himbeeren','himbeeren',80)], ex=[],
 intro='Dunkler Schokopudding, selbst gekocht in 10 Minuten: Milch, Kakao und Stärke, am Ende Proteinpulver mit Zartbittergeschmack, obendrauf ein paar Himbeeren. Schön schokoladig: {k} kcal und {p} g Eiweiß pro Glas statt 350 für zwei Becher Schokopudding mit Sahnehaube!',
 schritte=['Stärke, Kakao und Erythrit mit 6 EL Milch glatt rühren.',
           'Restliche Milch aufkochen, die Mischung einrühren und unter Rühren 1 Minute köcheln, dann vom Herd nehmen.',
           '2 Minuten abkühlen lassen, Proteinpulver einrühren, in 2 Gläser füllen, kalt stellen und mit Himbeeren servieren.'],
 frage='Schokopudding: mit Haut oder ohne?', tags='#schokopudding #pudding #dessert #proteindessert #fitmitkev',
 prompt='Two clear straight dessert glasses seen from the side at eye level, filled with glossy smooth very dark chocolate pudding, topped with a few fresh red raspberries, a few raspberries on the table, one teaspoon beside the glasses.'+SPOON),
dict(key='SpekulatiusTiramisuESN', suess=True, sorte='Vanilla Speculoos', hook='Wie Tiramisu:', titel=['SPEKULATIUS-','TIRAMISU'], portion='pro Glas', anzahl=2, vs=500,
 zutaten=[Z('6 Stück','Spekulatius','spekulatius','spekulatius',st=6), Z('100 ml','Espresso','espresso','espresso',100), Z('250 g','Skyr','skyr','skyr',250),
          Z('150 g','Magerquark','magerquark','quark',150), Z('30 g','Proteinpulver Spekulatius','proteinpulver','proteinpulver',30), Z('15 g','Erythrit','erythrit','erythrit',15),
          Z('5 g','Backkakao','backkakao','kakao',5)], ex=[],
 intro='Tiramisu mit Spekulatius statt Löffelbiskuits: die Kekse in Espresso getunkt, dazwischen eine Creme aus Skyr, Quark und Proteinpulver in Spekulatius-Geschmack, Kakao obendrauf. Ohne Mascarpone, ohne Backen: {k} kcal und {p} g Eiweiß pro Glas statt 500 für eine Portion Tiramisu!',
 schritte=['Skyr, Quark, Proteinpulver und Erythrit cremig rühren.',
           '4 Spekulatius kurz in den abgekühlten Espresso tunken und abwechselnd mit der Creme in 2 Gläser schichten.',
           'Mindestens 1 Stunde kalt stellen, mit Kakao bestäuben und mit je einem Spekulatius garnieren.'],
 frage='Tiramisu: klassisch oder mit Spekulatius?', tags='#tiramisu #spekulatius #fitmitkev',
 prompt='Two clear straight dessert glasses seen from the side at eye level with visible layers of espresso-soaked brown speculaas biscuits and thick white cream, the top dusted with dark cocoa powder, one whole '+SPEK+' standing upright in each glass, one teaspoon beside the glasses.'+NOROUND+SPOON),
dict(key='ErdbeerCheesecakeGlasESN', suess=True, sorte='Strawberry Cream', hook='Ohne Backen:', titel=['ERDBEER-CHEESECAKE','IM GLAS'], portion='pro Glas', anzahl=2, vs=480,
 zutaten=[Z('4 Stück','Butterkekse','butterkekse','butterkeks',st=4), Z('200 g','Skyr','skyr','skyr',200), Z('100 g','Frischkäse light','frischkaese_light','frischkaese',100),
          Z('30 g','Proteinpulver Erdbeere','proteinpulver','proteinpulver',30), Z('15 g','Erythrit','erythrit','erythrit',15), Z('200 g','Erdbeeren (TK)','erdbeeren','erdbeeren',200),
          Z('1 TL','Vanilleextrakt','vanilleextrakt','vanille',0)], ex=[],
 intro='Erdbeer-Cheesecake ohne Backen und ohne Sahne: Keksboden, darauf eine Frischkäse-Skyr-Creme mit Erdbeer-Proteinpulver, obendrauf Erdbeeren. In 10 Minuten geschichtet: {k} kcal und {p} g Eiweiß pro Glas statt 480 für ein Stück Erdbeer-Cheesecake!',
 schritte=['Butterkekse zerbröseln und auf 2 Gläser verteilen.',
           'Skyr, Frischkäse, Proteinpulver, Erythrit und Vanille glatt rühren und auf die Brösel geben.',
           'Erdbeeren auftauen lassen, die Hälfte zerdrücken, als Soße auf die Creme geben und mit den restlichen Erdbeeren belegen.'],
 frage='Cheesecake: mit Erdbeeren oder mit Himbeeren?', tags='#cheesecake #erdbeeren #ohnebacken #dessertimglas #fitmitkev',
 prompt='Two clear straight dessert glasses seen from the side at eye level with visible layers: golden butter biscuit crumbs at the bottom, thick smooth white cheesecake cream, glossy red strawberry sauce, topped with halved red strawberries, two strawberries on the table, one teaspoon beside the glasses.'+SPOON),
dict(key='ZimtGriessbreiESN', suess=True, sorte='Cinnamon Cereal', hook='Wie bei Oma:', titel=['ZIMT-','GRIESSBREI'], portion='pro Portion', anzahl=2, vs=450,
 zutaten=[Z('500 ml','Milch (1,5 %)','milch','milch',500), Z('60 g','Weichweizengrieß','griess','griess',60), Z('30 g','Proteinpulver Zimt','proteinpulver','proteinpulver',30),
          Z('15 g','Erythrit','erythrit','erythrit',15), Z('1 TL','Zimt','zimt','zimt',0), Z('1 Stück','Apfel','apfel','apfel',st=1)], ex=[],
 intro='Grießbrei wie bei Oma, nur mit viel mehr Eiweiß: cremig gekocht, Proteinpulver mit Zimtgeschmack zum Schluss rein, obendrauf frische Apfelwürfel und Zimt. In 10 Minuten fertig: {k} kcal und {p} g Eiweiß pro Portion statt 450 für Grießbrei mit Zimtzucker und Butter!',
 schritte=['Milch mit Erythrit aufkochen, Grieß einrühren und unter Rühren 3 Minuten quellen lassen.',
           'Vom Herd nehmen, 2 Minuten abkühlen lassen und das Proteinpulver einrühren.',
           'In 2 Schalen füllen, mit Apfelwürfeln belegen und mit Zimt bestäuben.'],
 frage='Grießbrei: mit Zimt und Zucker oder mit Kirschen?', tags='#grießbrei #omasrezepte #fitmitkev',
 prompt='Two white ceramic bowls of thick creamy semolina pudding seen from a slight angle, topped with fresh diced red apple and a generous dusting of cinnamon, a cinnamon stick and half an apple beside, one spoon lying beside one bowl.'+SPOON),
dict(key='SchokoEisESN', suess=True, sorte='Ultra Dark Chocolate', hook='Ohne Eismaschine:', titel=['SCHOKO-EIS AUS','HÜTTENKÄSE'], portion='pro Portion', anzahl=4, vs=300,
 zutaten=[Z('500 g','Hüttenkäse','huettenkaese','huettenkaese',500), Z('30 g','Proteinpulver Schoko','proteinpulver','proteinpulver',30), Z('20 g','Backkakao','backkakao','kakao',20),
          Z('30 g','Erythrit','erythrit','erythrit',30), Z('20 g','Zartbitterschokolade','zartbitterschokolade','schokolade',20), Z('50 ml','Milch (1,5 %)','milch','milch',50)], ex=[],
 intro='Schoko-Eis aus Hüttenkäse, ganz ohne Eismaschine: alles im Mixer pürieren, gehackte Zartbitterschokolade rein, einfrieren. Cremig und richtig schokoladig: {k} kcal und {p} g Eiweiß pro Portion statt 300 für drei Kugeln Schokoeis aus der Eisdiele!',
 schritte=['Hüttenkäse, Milch, Proteinpulver, Kakao und Erythrit im Mixer ganz glatt pürieren.',
           'In eine flache Form füllen, gehackte Schokolade unterrühren und 3–4 Stunden einfrieren, dabei jede Stunde einmal durchrühren.',
           '10 Minuten antauen lassen und Kugeln abstechen.'],
 frage='Eis im Winter: ja oder nein?', tags='#schokoeis #eis #hüttenkäse #proteineis #fitmitkev',
 prompt='A white ceramic bowl with three round scoops of creamy dark chocolate ice cream with small chocolate chunks, a metal loaf tin with more chocolate ice cream and an ice cream scoop blurred behind, one spoon lying beside the bowl.'+SPOON),
]
TILES={'pflaumen':'Several dark purple plums, two whole and two halved showing the yellow flesh, lying together, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no text.',
       'griess':'A small white bowl filled with fine pale yellow durum wheat semolina, a little semolina spilled beside it, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no text.'}
# Plan: (Datum, 06:10-Key, 13:00-Key)
TAGE=['2026-11-19','2026-11-20','2026-11-21','2026-11-22','2026-11-23','2026-11-24','2026-11-25','2026-11-26','2026-11-27','2026-11-28','2026-11-29','2026-11-30','2026-12-01','2026-12-02']
KEYS=[r['key'] for r in R]
PLAN=[(TAGE[i], KEYS[2*(i%7)], KEYS[2*(i%7)+1]) for i in range(14)]
for _r in R: _r.setdefault('kurz',['–','–','–'])
OHNE_BOX=set(range(1,15)); GRUPPE_A={i+1 for i,r in enumerate(R) if len(r['tags'].split())<=3}; HASHTAG_SOLL={i+1:len(r['tags'].split()) for i,r in enumerate(R)}; ZEITEN=['06:10','13:00']*7
if __name__=='__main__':
    assert len(R)==14 and len(set(KEYS))==14
    for i,r in enumerate(R,1):
        k,p,c,f=macros4(r)
        assert r['vs']>k and len(r['zutaten'])<=8 and len(r['schritte'])==3 and r['tags'].split()[-1]=='#fitmitkev'
        assert 'abnehm' not in (r['intro']+' '.join(r['schritte'])).lower() and 'esn' not in (r['intro']+r['frage']).lower()
        print(f"{i:2d} {r['key']:26s} {r['sorte']:20s} {k:4d} kcal {p:3d}P {c:3d}C {f:3d}F {r['portion']:14s} vs {r['vs']} {len(r['tags'].split())}#")
    for d,a,b in PLAN: print(d,a,b)
