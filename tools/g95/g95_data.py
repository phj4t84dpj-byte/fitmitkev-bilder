# -*- coding: utf-8 -*-
# G95 – Dienstag 17.11.2026, 20 Rezept-Plätze 6:10–20:45 (Kev 15.11. per Dialog: Box „Halb/halb wie bisher“, Mehrwert „Eiweiß im Frühstück“ 17:30).
# 6 Plätze sind schon belegt (am 14.11. von Montag verschoben, gleiche Uhrzeit): 9 Brownie-Bowl · 10 Cordon-Bleu-Auflauf · 11 Spekulatius-Eis ·
#   15 Haferflocken-Plätzchen · 17 Apfel-Streusel-Skyr-Kuchen · 19 Rote Grütze. Neu gebaut werden nur 1–8, 12, 13, 14, 16, 18, 20.
# Platz 18 läuft um 21:30 (19:15 = Buch-Beitrag „Eure Fragen zu den Büchern“). Keine ESN-Zeile (ESN erst ab Do 19.11.), kein Höflich-Titel.
# Buch-Zeile unter 2 Rezepten, die im Buch stehen: 3 Elisenlebkuchen (Weihnachtsbäckerei) · 8 Hähnchen-Nudelauflauf (Wohlfühlküche).
# Zugpferde (5-Tage-Plan): Laugenbrötchen aus Skyr-Teig (28.10. 271 k) 6:55 · Kirsch-Streusel-Bowl (10.11. 84 k) 10:45.
# Neu aus Kevs Vorlagen: Schichtsalat im Glas, Benjamin-Blümchen-Bowl (Kev 14.11.: Erdbeer-Schoko, TK-Erdbeeren, keine Figur im Bild).
# Hashtag-Gruppen wie Sonntag: 1,2,5,6,9,10,13,14,17,18 = A (2–3) · 3,4,7,8,11,12,15,16,19,20 = B (4–5)
#   -> die 6 verschobenen Beiträge brauchen dafür eine neue Hashtag-Zahl (nur nach Kevs Freigabe ändern, siehe NEU_TAGS).
# Box-Test: OHNE Box 1,3,4,6,7,10,13,15,16,18 (10 und 15 sind schon so angelegt) · MIT Box 2,5,8,9,11,12,14,17,19,20.
import sys, os, copy
_D=os.path.dirname(os.path.abspath(__file__))
for g in ('g87','g88','g89','g90','g91','g92','g93','g93n','g94'): sys.path.insert(0, os.path.join(_D, '..', g))
from g90_data import NUT, PIECE, nut, Z, macros4
import g91_data, g92_data, g93_data, g93n_data, g94_data, g88_data
NUT.update({
 'aubergine':(24,1,3.6,0.2), 'erdbeeren':(32,0.7,5.5,0.4), 'zuckerstreusel':(400,0,95,2), 'oblaten':(380,10,80,1),
 'orange':(0,0,0,0), 'lebkuchengewuerz':(0,0,0,0), 'paprikapulver':(0,0,0,0), 'apfelsaft':(45,0.1,10,0.1),
})
_R88={r['key']:r for r in g88_data.R}
_R94={r['key']:r for r in g94_data.R}
def alt(src, key, **kw):
    r=copy.deepcopy(src[key]); r.update(kw); r.pop('fb',None); r.pop('hinweis',None); return r

BUCH_W='📖 Diese Elisenlebkuchen findest du auch in meinem Rezeptbuch „Weihnachtsbäckerei in leicht“, zusammen mit 35 weiteren Rezepten: https://fitmitkev.de/rezeptbuecher'
BUCH_K='📖 Diesen Nudelauflauf findest du auch in meinem Rezeptbuch „Wohlfühlküche in leicht“, zusammen mit 35 weiteren Rezepten: https://fitmitkev.de/rezeptbuecher'
GLAS='A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: '

R = [
# 1 · 06:10 · süß · Bratapfel-Porridge (G88; 10.11. 6:00 31 k) · ohne Box · 3 #
alt(_R88,'BratapfelPorridge',
 kurz=['Apfel würfeln, mit Zimt, Rosinen und 2 EL Wasser 5 Min. weich dünsten.',
       'Haferflocken mit Milch, Erythrit, Vanille und Salz 5 Min. cremig köcheln.',
       'Auf 2 Schalen verteilen, Bratapfel, je 50 g Skyr und Mandelblättchen darauf.'],
 tags='#porridge #bratapfel #fitmitkev',
 prompt='A white ceramic bowl of creamy warm oatmeal porridge seen from the side slightly elevated, topped with a generous heap of soft golden cinnamon-stewed apple cubes with raisins, a dollop of thick white skyr and toasted golden flaked almonds, a light dusting of cinnamon, steam rising, a second bowl blurred behind, half a red apple and a cinnamon stick beside the bowl, a spoon beside.'),
# 2 · 06:55 · herzhaft · Zugpferd Laugenbrötchen aus Skyr-Teig (G80; 28.10. 271 k) · mit Box · 2 #
dict(key='Laugenbroetchen', suess=False, hook='Wie vom Bäcker:', titel=['LAUGENBRÖTCHEN','AUS SKYR-TEIG'], portion='pro Stück', anzahl=6, vs=280,
 zutaten=[Z('300 g','Dinkelmehl','dinkelmehl','dinkelmehl',300), Z('300 g','Skyr','skyr','skyr',300), Z('2 TL','Backpulver','backpulver','backpulver',0),
          Z('3 EL','Natron (für die Lauge)','natron','natron',0), Z('1 TL','Salz + grobes Salz','salz_grobes_salz','salz',0)],
 ex=['1 l Wasser für die Lauge'],
 intro='Laugenbrötchen wie vom Bäcker, aber ohne Hefe und ohne Gehzeit: Skyr-Teig, kurz in Natronlauge gebadet, dann goldbraun gebacken. Außen die typische Laugenkruste, innen weich: {k} kcal und {p} g Eiweiß pro Brötchen statt 280 beim Bäcker!',
 schritte=['Mehl, Skyr, Backpulver und 1 TL Salz zu einem glatten Teig kneten (bei Bedarf 1–2 EL Wasser dazu) und 6 runde Brötchen formen.',
           '1 Liter Wasser aufkochen und das Natron vorsichtig einrühren (schäumt kurz auf). Die Brötchen einzeln 30 Sekunden darin baden und mit einer Schaumkelle auf ein Blech mit Backpapier heben.',
           'Oben kreuzweise einschneiden, mit grobem Salz bestreuen und bei 200 °C Ober-/Unterhitze 18–20 Minuten goldbraun backen.'],
 kurz=['Mehl, Skyr, Backpulver und 1 TL Salz verkneten und 6 Brötchen formen.',
       '1 l Wasser aufkochen, Natron einrühren, Brötchen je 30 Sek. darin baden.',
       'Einschneiden, grobes Salz drauf, bei 200 °C 18–20 Min. goldbraun backen.'],
 frage='Laugenbrötchen: mit Butter oder mit Frischkäse?', tags='#laugenbrötchen #fitmitkev',
 prompt='Six round German pretzel rolls (Laugenbrötchen) with a glossy golden chestnut-brown pretzel crust, warm bakery color, not dark, a cross cut on top showing the pale soft inside, sprinkled with coarse white salt crystals, on a wooden board, one roll cut in half in front showing the soft fluffy white crumb with a little butter, a small bowl of coarse salt beside.'),
# 3 · 07:40 · süß · Elisenlebkuchen ohne Mehl (G79; 1.11. 7:20 40 k) · Buch-Zeile Weihnachtsbäckerei · ohne Box · 4 #
dict(key='Elisenlebkuchen', suess=True, hook='Wie aus Nürnberg:', titel=['ELISEN-','LEBKUCHEN'], portion='pro Stück', anzahl=20, vs=220,
 zutaten=[Z('200 g','Gemahlene Mandeln','gemahlene_mandeln','mandeln',200), Z('100 g','Gemahlene Haselnüsse','gemahlene_haselnuesse','haselnuesse',100),
          Z('3 Stück','Eiweiß','eiweiss','eiweiss',99), Z('100 g','Erythrit','erythrit','erythrit',100), Z('2 TL','Lebkuchengewürz','lebkuchengewuerz','lebkuchengewuerz',0),
          Z('1 Stück','Orange (Schalenabrieb)','orange','orange',0), Z('50 g','Zartbitterschokolade','zartbitterschokolade','schokolade',50)],
 ex=['20 Back-Oblaten (7 cm)'],
 intro='Elisenlebkuchen wie aus Nürnberg: ohne Mehl, nur Nüsse, Eiweiß und Gewürze auf Oblaten, mit Zartbitterguss. Das Original hat Zucker und Orangeat, meine haben Erythrit und frischen Orangenabrieb: {k} kcal und {p} g Eiweiß pro Lebkuchen statt 220 vom Weihnachtsmarkt!',
 schritte=['Das Eiweiß steif schlagen und das Erythrit einrieseln lassen. Mandeln, Haselnüsse, Lebkuchengewürz und Orangenabrieb vorsichtig unterheben.',
           'Die Masse mit einem Löffel kuppelförmig auf 20 Oblaten streichen und auf ein Backblech mit Backpapier setzen.',
           'Bei 160 °C Ober-/Unterhitze 20–22 Minuten backen, abkühlen lassen und mit der geschmolzenen Schokolade bestreichen.'],
 kurz=['Eiweiß steif schlagen, Erythrit einrieseln, Nüsse, Gewürz und Orangenabrieb unterheben.',
       'Masse kuppelförmig auf 20 Oblaten streichen, aufs Blech mit Backpapier setzen.',
       'Bei 160 °C 20–22 Min. backen, abkühlen lassen, mit Schokolade bestreichen.'],
 hinweis=BUCH_W,
 frage='Lebkuchen: mit Schokoguss oder mit Zuckerguss?', tags='#lebkuchen #elisenlebkuchen #weihnachtsbäckerei #fitmitkev',
 prompt='Several round German Elisen gingerbread cookies (Elisenlebkuchen) on a white plate and on the wooden table, each a thick domed round nut gingerbread about 7 cm wide on a thin white wafer base, the top coated with glossy dark chocolate, one cookie broken in half in front showing the moist light brown nutty inside, a few whole almonds, an orange and a cinnamon stick beside.'),
# 4 · 08:30 · herzhaft · Käse-Schinken-Waffeln (G88; 10.11. 34 k) · ohne Box · 5 #
alt(_R88,'KaeseSchinkenWaffeln',
 kurz=['Mehl, Skyr, Eier, Milch, Backpulver und Gewürze glatt rühren.',
       'Käse, Schinkenwürfel und Schnittlauch unterheben.',
       'Im leicht geölten Waffeleisen je 2 EL Teig 4 Min. goldbraun backen (8 Stück).'],
 tags='#waffeln #herzhaft #frühstück #mealprep #fitmitkev',
 prompt='A stack of four golden brown savory heart-shaped waffles on a white plate, small pink ham cubes and melted golden cheese visible in the waffle surface, sprinkled with fresh chopped green chives, one waffle broken in front showing the fluffy inside with ham and cheese, a small bowl of white herb cream cheese dip beside.'),
# 5 · 09:15 · süß · neu: Apfelstrudel-Tiramisu im Glas (Kevs Vorlage) · mit Box · 2 #
dict(key='ApfelstrudelTiramisu', suess=True, hook='Ohne Mascarpone:', titel=['APFELSTRUDEL-','TIRAMISU'], portion='pro Glas', anzahl=4, vs=420,
 zutaten=[Z('12 Stück','Löffelbiskuits','loeffelbiskuit','loeffelbiskuit',st=12), Z('400 g','Skyr','skyr','skyr',400), Z('250 g','Magerquark','magerquark','quark',250),
          Z('2 Stück','Äpfel','apfel','apfel',st=2), Z('40 g','Erythrit','erythrit','erythrit',40), Z('20 g','Rosinen','rosinen','rosinen',20),
          Z('20 g','Mandelblättchen','mandelblaettchen','mandelblaettchen',20), Z('1 TL','Zimt','zimt','zimt',0)],
 ex=['100 ml Apfelsaft', '1 TL Vanilleextrakt'],
 intro='Apfelstrudel trifft Tiramisu: Löffelbiskuits in Apfelsaft getränkt, dazu warme Zimtäpfel mit Rosinen und eine Vanillecreme aus Skyr und Quark statt Mascarpone, obendrauf geröstete Mandelblättchen. Im Glas geschichtet, ohne Backen: {k} kcal und {p} g Eiweiß pro Glas statt 420 für Tiramisu mit Mascarpone!',
 schritte=['Die Äpfel schälen, würfeln und mit Zimt, Rosinen, 10 g Erythrit und 2 EL Wasser 5 Minuten weich dünsten, abkühlen lassen. Die Mandelblättchen ohne Fett goldbraun rösten.',
           'Skyr, Quark, 30 g Erythrit und Vanille glatt rühren. Die Löffelbiskuits halbieren und kurz in den Apfelsaft tauchen.',
           'In 4 Gläser schichten: Biskuits, Creme, Zimtäpfel, dann noch einmal Biskuits und Creme. Mit Zimtäpfeln und Mandelblättchen abschließen und 2 Stunden kalt stellen.'],
 kurz=['Äpfel würfeln, mit Zimt, Rosinen, 10 g Erythrit 5 Min. dünsten. Mandeln rösten.',
       'Skyr, Quark, 30 g Erythrit und Vanille verrühren, Biskuits in Apfelsaft tauchen.',
       'In 4 Gläser schichten, mit Äpfeln und Mandeln abschließen, 2 Std. kalt stellen.'],
 frage='Tiramisu: klassisch mit Kaffee oder mit Apfel und Zimt?', tags='#tiramisu #fitmitkev',
 prompt='Four small clear dessert glasses seen from the side at eye level, layered dessert clearly visible through the glass: pale golden soaked sponge finger biscuits, thick white vanilla cream layers and golden cinnamon apple cubes with raisins, topped with more cinnamon apple cubes, toasted golden flaked almonds and a dusting of cinnamon, one glass standing in front with a teaspoon beside it, a red apple and a cinnamon stick on the table.'),
# 6 · 10:00 · herzhaft · Moussaka in leicht (G53; 25.10. 40 k) · ohne Box · 3 #
dict(key='Moussaka', suess=False, hook='Wie beim Griechen:', titel=['MOUSSAKA','IN LEICHT'], portion='pro Portion', anzahl=4, vs=800,
 zutaten=[Z('2 Stück','Auberginen','aubergine','aubergine',600), Z('400 g','Kartoffeln','kartoffeln','kartoffeln',400), Z('500 g','Rinderhack (mager)','rinderhack','hack',500),
          Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1), Z('400 g','Passierte Tomaten','passierte_tomaten','tomaten',400), Z('250 g','Skyr','skyr','skyr',250),
          Z('1 Stück','Ei','ei','ei',st=1), Z('60 g','Reibekäse light','reibekaese_light','reibekaese',60)],
 ex=['1 EL Öl', 'Salz, Pfeffer, Muskat, ½ TL Zimt, 1 TL Oregano'],
 intro='Moussaka wie beim Griechen: Auberginen, Kartoffeln, würziges Hack in Tomatensoße und eine goldbraune Haube. Die Auberginen kommen in den Ofen statt in die Pfanne voller Öl, die Béchamel ist aus Skyr: {k} kcal und {p} g Eiweiß pro Portion statt 800 im Restaurant!',
 schritte=['Auberginen und Kartoffeln in 5 mm dicke Scheiben schneiden, auf zwei Blechen mit 1 EL Öl und Salz bei 200 °C Ober-/Unterhitze 15 Minuten vorbacken.',
           'Zwiebel würfeln und mit dem Hack krümelig braten. Passierte Tomaten, Zimt, Oregano, Salz und Pfeffer dazu und 10 Minuten köcheln. In einer Auflaufform (20 × 30 cm) schichten: Kartoffeln, Hälfte Hack, Auberginen, Rest Hack, Rest Auberginen.',
           'Skyr mit Ei, Salz und Muskat verrühren, darüber streichen, mit Käse bestreuen und bei 180 °C Ober-/Unterhitze 35 Minuten backen.'],
 kurz=['Auberginen und Kartoffeln in Scheiben mit 1 EL Öl bei 200 °C 15 Min. vorbacken.',
       'Hack mit Zwiebel braten, Tomaten und Gewürze dazu, alles in die Form schichten.',
       'Skyr mit Ei verrühren, drüber, Käse drauf, bei 180 °C 35 Min. backen.'],
 frage='Moussaka: mit oder ohne Kartoffeln?', tags='#moussaka #auflauf #fitmitkev',
 prompt='A rectangular white ceramic baking dish with Greek moussaka with a thick golden brown baked creamy topping, one square portion served on a white plate in front clearly showing the layers from the side: soft dark purple-skinned eggplant slices, potato slices and browned minced beef in red tomato sauce under the thick creamy white topping, a little fresh oregano on top, a fork beside.'),
# 7 · 10:45 · süß · Zugpferd Kirsch-Streusel-Bowl (G88; 10.11. 10:30 84 k) · ohne Box · 4 #
alt(_R88,'KirschStreuselBowl',
 zutaten=[Z('35 g','Zarte Haferflocken','zarte_haferflocken','haferflocken',35), Z('120 g','Skyr','skyr','skyr',120), Z('1 Stück','Ei','ei','ei',st=1),
          Z('100 g','Sauerkirschen (Glas)','sauerkirschen','kirschen',100), Z('20 g','Erythrit','erythrit','erythrit',20), Z('15 g','Dinkelmehl','dinkelmehl','dinkelmehl',15),
          Z('6 g','Butter','butter','butter',6), Z('8 g','Vanillepudding-Pulver','vanillepudding_pulver','puddingpulver',8)],
 kurz=['Haferflocken, 100 g Skyr, Ei, 10 g Erythrit und Backpulver in die Glasform geben.',
       'Kirschen mit 20 g Skyr und Puddingpulver verrühren und darauf verteilen.',
       'Mehl, Butter, 10 g Erythrit, Zimt zu Streuseln, drüber, bei 180 °C 22 Min. backen.'],
 tags='#streuselkuchen #kirschen #bowl #fitmitkev',
 prompt=GLAS+'a soft golden oat base, a thick layer of glossy dark red sour cherries in creamy pale yellow pudding, topped with golden crumble streusel, a few dark red cherries beside the dish.'),
# 8 · 11:30 · herzhaft · Cremiger Hähnchen-Nudelauflauf (G80; Wohlfühlküche) · Buch-Zeile · mit Box · 5 #
dict(key='HaehnchenNudelauflauf', suess=False, hook='Für die ganze Familie:', titel=['HÄHNCHEN-','NUDELAUFLAUF'], portion='pro Portion', anzahl=4, vs=780,
 zutaten=[Z('200 g','Nudeln (roh)','penne','nudeln',200), Z('400 g','Hähnchenbrust','haehnchenbrust','haehnchen',400), Z('300 g','Brokkoli (TK)','brokkoli','brokkoli',300),
          Z('250 g','Skyr','skyr','skyr',250), Z('150 ml','Milch (1,5 %)','milch','milch',150), Z('100 g','Frischkäse light','frischkaese_light','frischkaese',100),
          Z('100 g','Reibekäse light','reibekaese_light','reibekaese',100), Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1)],
 ex=['1 TL Öl', 'Salz, Pfeffer, Paprikapulver, Knoblauch'],
 intro='Nudelauflauf mit Hähnchen und Brokkoli in einer cremigen Soße aus Skyr, Milch und Frischkäse, obendrauf eine goldbraune Käsekruste. Das Essen, bei dem alle am Tisch sitzen: {k} kcal und {p} g Eiweiß pro Portion statt 780 für den Nudelauflauf mit Sahne!',
 schritte=['Die Nudeln 2 Minuten kürzer als auf der Packung angegeben kochen, den Brokkoli die letzten 3 Minuten mitkochen und abgießen.',
           'Das Hähnchen würfeln und mit der gewürfelten Zwiebel im Öl anbraten, mit Salz, Pfeffer, Paprikapulver und Knoblauch würzen. Skyr, Milch und Frischkäse verrühren und salzen.',
           'Alles mischen, in eine Auflaufform (20 × 30 cm) geben, den Käse darüber streuen und bei 200 °C Ober-/Unterhitze 20 Minuten überbacken.'],
 kurz=['Nudeln 2 Min. kürzer kochen, Brokkoli die letzten 3 Min. mitkochen.',
       'Hähnchen mit Zwiebel anbraten, würzen. Skyr, Milch und Frischkäse verrühren.',
       'Alles mischen, in die Form, Käse drauf, bei 200 °C 20 Min. überbacken.'],
 hinweis=BUCH_K,
 frage='Nudelauflauf: mit Brokkoli oder lieber mit Erbsen?', tags='#nudelauflauf #hähnchen #familienessen #auflauf #fitmitkev',
 prompt='A rectangular white ceramic baking dish with a creamy pasta bake of penne, tender chicken pieces and bright green broccoli florets in a creamy white sauce under a golden brown bubbly melted cheese crust, one portion served on a white plate in front showing the creamy penne, chicken and broccoli, a fork beside.'),
# 9 · 12:20 · süß · Brownie-Bowl – schon angelegt (am 14.11. von Montag verschoben)
alt(_R94,'BrownieBowl', tags='#brownie #bowl #fitmitkev', vorhanden=428377083),
# 10 · 13:05 · herzhaft · Cordon-Bleu-Auflauf – schon angelegt
alt(_R94,'CordonBleuAuflauf', tags='#cordonbleu #auflauf #fitmitkev', vorhanden=428377156),
# 11 · 13:50 · süß · Spekulatius-Eis aus Hüttenkäse – schon angelegt (ESN-Zeile am 14.11. entfernt)
alt(_R94,'HuettenEis', tags='#eis #spekulatius #dessert #fitmitkev', vorhanden=428377221),
# 12 · 14:35 · herzhaft · neu: Schichtsalat im Glas (Kevs Vorlage) · mit Box · 4 #
dict(key='Schichtsalat', suess=False, hook='Party-Klassiker im Glas:', titel=['SCHICHTSALAT','IM GLAS'], portion='pro Glas', anzahl=4, vs=550,
 zutaten=[Z('200 g','Eisbergsalat','eisbergsalat','eisbergsalat',200), Z('150 g','Erbsen (TK)','erbsen','erbsen',150), Z('140 g','Mais (Dose)','mais','mais',140),
          Z('4 Stück','Eier','eier','ei',st=4), Z('150 g','Kochschinken','kochschinken','kochschinken',150), Z('80 g','Reibekäse light','reibekaese_light','reibekaese',80),
          Z('250 g','Skyr','skyr','skyr',250), Z('½ Bund','Schnittlauch','schnittlauch','schnittlauch',0)],
 ex=['1 TL Senf, 1 TL Zitronensaft', 'Salz, Pfeffer'],
 intro='Der Schichtsalat von jeder Familienfeier, nur im Glas und ohne Mayonnaise: Eisbergsalat, Erbsen, Mais, Eier, Schinken und Käse in Schichten, dazwischen ein Senf-Dressing aus Skyr. Hält sich abgedeckt 2 Tage im Kühlschrank: {k} kcal und {p} g Eiweiß pro Glas statt 550 für Schichtsalat mit Mayo!',
 schritte=['Die Eier 9 Minuten hart kochen, pellen und würfeln. Die Erbsen 2 Minuten in kochendem Wasser garen und kalt abschrecken. Salat in Streifen und Schinken in Würfel schneiden.',
           'Skyr mit Senf, Zitronensaft, der Hälfte vom Schnittlauch, Salz und Pfeffer zu einem Dressing verrühren.',
           'In 4 Gläser schichten: Salat, Erbsen, Mais, Eier, Schinken, dazwischen und obendrauf je 1 Löffel Dressing. Mit Käse und restlichem Schnittlauch bestreuen.'],
 kurz=['Eier 9 Min. kochen und würfeln, Erbsen 2 Min. garen, Salat und Schinken schneiden.',
       'Skyr mit Senf, Zitronensaft, halbem Schnittlauch, Salz und Pfeffer verrühren.',
       'In 4 Gläser schichten, Dressing dazwischen, Käse und Schnittlauch obendrauf.'],
 frage='Schichtsalat: mit Erbsen oder ohne?', tags='#schichtsalat #salat #partyrezepte #fitmitkev',
 prompt='Four tall clear glass jars filled with a German layered salad (Schichtsalat) seen from the side at eye level, distinct colorful horizontal layers clearly visible through the glass: shredded pale green iceberg lettuce, bright green peas, yellow corn kernels, chopped hard-boiled egg, pink diced ham and thin white creamy dressing layers, topped with grated cheese and fresh chopped chives, one jar in front with a fork beside it.'),
# 13 · 15:25 · süß · neu: Benjamin-Blümchen-Bowl (Kev 14.11.: Erdbeer-Schoko, TK-Erdbeeren, keine Figur) · ohne Box · 2 #
dict(key='BenjaminBowl', suess=True, hook='Nur für dich:', titel=['BENJAMIN-BLÜMCHEN-','BOWL'], portion='die ganze Bowl', anzahl=1, vs=550,
 zutaten=[Z('1 Stück','Ei','ei','ei',st=1), Z('20 g','Dinkelmehl','dinkelmehl','dinkelmehl',20), Z('15 g','Backkakao','backkakao','kakao',15),
          Z('25 g','Erythrit','erythrit','erythrit',25), Z('200 g','Skyr','skyr','skyr',200), Z('100 g','Erdbeeren (TK)','erdbeeren','erdbeeren',100),
          Z('½ TL','Backpulver','backpulver','backpulver',0), Z('3 g','Bunte Zuckerstreusel','zuckerstreusel','zuckerstreusel',3)],
 ex=[],
 intro='Die Erdbeer-Schoko-Torte aus der Kindheit als Bowl nur für dich: unten ein saftiger Schoko-Biskuit, darauf eine rosa Erdbeercreme aus Skyr, ein Klecks Schokocreme und bunte Streusel. Mit TK-Erdbeeren, die gibt es auch im Winter: {k} kcal und {p} g Eiweiß die ganze Bowl statt 550 für zwei Stücke Torte!',
 schritte=['Ei, Mehl, 10 g Kakao, 15 g Erythrit, 50 g Skyr und Backpulver glatt rühren, in eine gefettete Glasform (15 × 10 cm) geben und bei 180 °C Ober-/Unterhitze 12 Minuten backen. Abkühlen lassen.',
           'Die Erdbeeren auftauen lassen, pürieren und mit 100 g Skyr und 10 g Erythrit verrühren. 50 g Skyr mit 5 g Kakao zu einer Schokocreme rühren.',
           'Die Erdbeercreme auf den Biskuit streichen, die Schokocreme in Tupfen darauf setzen und mit den bunten Streuseln bestreuen.'],
 kurz=['Ei, Mehl, 10 g Kakao, 15 g Erythrit, 50 g Skyr, Backpulver: 12 Min. bei 180 °C.',
       'Erdbeeren auftauen, pürieren, mit 100 g Skyr verrühren. 50 g Skyr mit 5 g Kakao.',
       'Erdbeercreme auf den Biskuit, Schokotupfen drauf, bunte Streusel drüber.'],
 frage='Erdbeer-Schoko-Torte: Wer kennt sie noch vom Kindergeburtstag?', tags='#erdbeeren #fitmitkev',
 prompt=GLAS+'a dark brown chocolate sponge cake layer at the bottom, a thick layer of smooth pastel pink strawberry cream on top, several small piped dollops of light brown chocolate cream on the pink cream and colorful rainbow sugar sprinkles scattered on top, two halved red strawberries beside the dish.'),
# 14 · 16:10 · herzhaft · Currywurst-Auflauf (G88; 10.11. 17:15 15 k) · mit Box · 3 #
alt(_R88,'CurrywurstAuflauf',
 kurz=['Kartoffeln in Scheiben 8 Min. vorkochen und in die Form (20 × 30 cm) schichten.',
       'Zwiebel anbraten, Tomatenmark und Curry mitrösten, Tomaten und Honig dazu.',
       'Würstchen drauf, Soße drüber, Käse drauf, bei 200 °C 20 Min. überbacken.'],
 tags='#currywurst #auflauf #fitmitkev'),
# 15 · 16:55 · süß · Haferflocken-Plätzchen – schon angelegt
alt(_R94,'Haferplaetzchen', tags='#plätzchen #haferflocken #backen #fitmitkev', vorhanden=428377276),
# 16 · 17:40 · herzhaft · Chicken Nuggets aus dem Ofen (G37; Wohlfühlküche) · ohne Box · 5 #
dict(key='Nuggets', suess=False, hook='Knusprig ohne Fritteuse:', titel=['CHICKEN NUGGETS','AUS DEM OFEN'], portion='pro Portion', anzahl=4, vs=550,
 zutaten=[Z('600 g','Hähnchenbrust','haehnchenbrust','haehnchen',600), Z('2 Stück','Eier','eier','ei',st=2), Z('80 g','Cornflakes (ungesüßt)','cornflakes','cornflakes',80),
          Z('40 g','Dinkelmehl','dinkelmehl','dinkelmehl',40), Z('1 TL','Paprikapulver','paprikapulver','paprikapulver',0), Z('150 g','Skyr','skyr','skyr',150),
          Z('1 TL','Senf','senf','senf',5)],
 ex=['1 TL Honig, Salz, Pfeffer', 'etwas Öl zum Besprühen'],
 intro='Chicken Nuggets wie vom Schnellrestaurant, nur aus dem Ofen statt aus der Fritteuse: knusprige Cornflakes-Panade, innen saftiges Hähnchen, dazu ein Honig-Senf-Dip aus Skyr. Die Kinder merken keinen Unterschied: {k} kcal und {p} g Eiweiß pro Portion statt 550 für Nuggets mit Dip!',
 schritte=['Das Hähnchen in mundgerechte Stücke schneiden und mit Salz, Pfeffer und Paprikapulver würzen. Die Cornflakes in einem Gefrierbeutel fein zerdrücken.',
           'Jedes Stück nacheinander durch Mehl, verquirlte Eier und Cornflakes ziehen, auf ein Blech mit Backpapier legen, leicht mit Öl besprühen und bei 200 °C Umluft 15–18 Minuten backen, einmal wenden.',
           'Für den Dip Skyr mit Senf, Honig und einer Prise Salz verrühren.'],
 kurz=['Hähnchen in Stücke schneiden und würzen, Cornflakes im Beutel zerdrücken.',
       'Durch Mehl, Ei und Cornflakes ziehen, bei 200 °C Umluft 15–18 Min. backen.',
       'Skyr mit Senf, Honig und einer Prise Salz zum Dip verrühren.'],
 frage='Nuggets: mit Ketchup oder mit Honig-Senf?', tags='#chickennuggets #hähnchen #familienessen #kinderessen #fitmitkev',
 prompt='Many crispy golden brown oven-baked chicken nuggets with a crunchy cornflake crust piled on a white plate, one nugget broken open in front showing the juicy white chicken inside, a small bowl of creamy pale yellow honey mustard dip and a small bowl of ketchup beside the plate.'),
# 17 · 18:25 · süß · Apfel-Streusel-Skyr-Kuchen – schon angelegt
alt(_R94,'ApfelStreusel', tags='#apfelkuchen #streuselkuchen #fitmitkev', vorhanden=428377365),
# 18 · 21:30 · herzhaft · Gefüllte Paprika (G88; 10.11. 12 k) · ohne Box · 2 #
alt(_R88,'GefuelltePaprika',
 kurz=['Reis 10 Min. vorkochen, mit Hack, Zwiebel, Knoblauch, Tomatenmark und Gewürzen mischen.',
       'Paprika halbieren, füllen, in die Form mit gewürzten passierten Tomaten setzen.',
       'Mit Käse bestreuen und bei 190 °C Ober-/Unterhitze 40 Min. garen.'],
 tags='#gefülltepaprika #fitmitkev',
 prompt='A white ceramic baking dish with halved red bell peppers generously stuffed with minced beef and rice, baked in a red tomato sauce, topped with melted golden brown cheese and a little fresh parsley, one stuffed pepper half served on a white plate in front with tomato sauce, a fork beside.'),
# 19 · 20:00 · süß · Rote Grütze – schon angelegt
alt(_R94,'RoteGruetze', tags='#rotegrütze #dessert #omasrezepte #fitmitkev', vorhanden=428377422),
# 20 · 20:45 · herzhaft · Salami-Pizza aus Skyr-Teig (G79; 22.10. 29 k) · mit Box · 4 #
dict(key='SalamiPizza', suess=False, hook='Wie vom Lieferdienst:', titel=['SALAMI-PIZZA','AUS SKYR-TEIG'], portion='pro Pizza', anzahl=2, vs=900,
 zutaten=[Z('150 g','Dinkelmehl','dinkelmehl','dinkelmehl',150), Z('170 g','Skyr','skyr','skyr',170), Z('1 TL','Backpulver','backpulver','backpulver',0),
          Z('150 g','Passierte Tomaten','passierte_tomaten','tomaten',150), Z('80 g','Reibekäse light','reibekaese_light','reibekaese',80), Z('40 g','Salami','salami','salami',40),
          Z('1 Stück','Paprika','paprika','paprika_st',st=1)],
 ex=['Salz, Oregano, 1 Zehe Knoblauch'],
 intro='Eine ganze Salami-Pizza für dich allein: Teig aus Dinkelmehl und Skyr ohne Hefe, dünn ausgerollt und knusprig gebacken, mit Käse, Salami und Paprika. Beim Lieferdienst hat die gleiche Pizza über 900 kcal, hier sind es {k} kcal und {p} g Eiweiß pro Pizza!',
 schritte=['Mehl, Skyr, Backpulver und ½ TL Salz zu einem glatten Teig kneten, halbieren und auf Backpapier zu zwei dünnen Fladen (ca. 22 cm) ausrollen. Bei 200 °C Ober-/Unterhitze 6 Minuten vorbacken.',
           'Passierte Tomaten mit Salz, Oregano und gepresstem Knoblauch würzen und auf die Fladen streichen.',
           'Mit Käse, Salami und Paprikastreifen belegen und weitere 12–14 Minuten backen, bis der Käse goldbraun ist.'],
 kurz=['Teig kneten, zu 2 dünnen Fladen (22 cm) ausrollen, bei 200 °C 6 Min. vorbacken.',
       'Passierte Tomaten mit Salz, Oregano und Knoblauch würzen und draufstreichen.',
       'Käse, Salami und Paprika drauf und weitere 12–14 Min. goldbraun backen.'],
 frage='Pizza: Salami oder lieber vegetarisch?', tags='#pizza #salamipizza #pizzaabend #fitmitkev',
 prompt='A whole round thin-crust homemade salami pizza about 22 cm on a wooden board, golden brown crispy edge, melted golden cheese, slightly crispy round salami slices and red and green bell pepper strips, a little oregano on top, one slice cut and pulled slightly out with stretchy melted cheese, a pizza cutter beside.'),
]

# Extras (Öl, Honig, Oblaten …) in kcal/Eiweiß/KH/Fett pro Rezept gesamt
EXN={'Moussaka':(90,0,0,10), 'HaehnchenNudelauflauf':(45,0,0,5), 'Nuggets':(65,0,6,4.5), 'Elisenlebkuchen':(80,2,16,0.2),
     'ApfelstrudelTiramisu':(45,0,10,0), 'Schichtsalat':(5,0,0,0)}
EXN.update({k:v for k,v in g88_data.EXN.items() if k in ('KaeseSchinkenWaffeln','CurrywurstAuflauf','GefuelltePaprika')})
for r in R:
    if r['key'] in EXN: r['exnut']=[EXN[r['key']]]
    elif 'exnut' not in r: r['exnut']=[]

ZEITEN=['06:10','06:55','07:40','08:30','09:15','10:00','10:45','11:30','12:20','13:05','13:50','14:35','15:25','16:10','16:55','17:40','18:25','21:30','20:00','20:45']
HASHTAG_SOLL={1:3,2:2,3:4,4:5,5:2,6:3,7:4,8:5,9:3,10:3,11:4,12:4,13:2,14:3,15:4,16:5,17:3,18:2,19:4,20:4}
GRUPPE_A={1,2,5,6,9,10,13,14,17,18}
OHNE_BOX={1,3,4,6,7,10,13,15,16,18}
VORHANDEN={9,10,11,15,17,19}

if __name__=='__main__':
    assert len(R)==20 and len({r['key'] for r in R})==20
    for i,r in enumerate(R,1):
        k,p,c,f=macros4(r); nt=len(r['tags'].split())
        assert nt==HASHTAG_SOLL[i], (i,r['key'],nt)
        assert (nt<=3)==(i in GRUPPE_A), (i,'Gruppe')
        assert r['tags'].split()[-1]=='#fitmitkev'
        assert r['suess']==(i%2==1), ('süß/herzhaft-Wechsel',i)
        assert bool(r.get('vorhanden'))==(i in VORHANDEN), i
        assert r['vs']>k and len(r['zutaten'])<=8 and len(r['schritte'])==3 and len(r['kurz'])==3, r['key']
        assert all(len(s)<=100 for s in r['kurz']), (r['key'],[len(s) for s in r['kurz']])
        assert r['suess'] or r['portion']!='pro Portion' or k<=500, ('Hauptgericht über 500 kcal',r['key'],k)
        assert 'abnehm' not in (r['intro']+' '.join(r['schritte'])+' '.join(r['kurz'])+r.get('hinweis','')).lower()
        assert 'esn' not in r.get('hinweis','').lower()
        print(f"{i:2d} {ZEITEN[i-1]} {r['key']:22s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P {c:3d}C {f:3d}F  {r['portion']:15s} vs {r['vs']}  {len(r['zutaten'])} Kacheln  {nt} #  kurz {max(len(s) for s in r['kurz'])}  {'ohne Box' if i in OHNE_BOX else 'mit Box '} {'(schon angelegt)' if r.get('vorhanden') else ''} {'BUCH' if r.get('hinweis') else ''}")
    ob=[i for i in OHNE_BOX]; assert len(ob)==10 and sum(R[i-1]['suess'] for i in ob)==5 and sum(i in GRUPPE_A for i in ob)==5
    assert sum(1 for r in R if r.get('hinweis'))==2
    import json
    TL=os.path.join(_D,'..','tilex','tiles_orig'); MAP=json.load(open(TL+'/_map_g87.json'))
    fehlt=sorted({z['tile'] for r in R for z in r['zutaten'] if not os.path.exists(f"{TL}/{MAP.get(z['tile'],z['tile'])}.png")}); print('Kacheln fehlen:',fehlt)
