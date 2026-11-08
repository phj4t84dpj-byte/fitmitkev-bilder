# -*- coding: utf-8 -*-
# G87 – Montag 09.11.2026, 15 Beiträge stündlich 6:00–20:00, Reset-Tag (keine Werbung)
# Nährwerte pro 100 g bzw. pro Stück: (kcal, Eiweiß, KH, Fett)
NUT = {
 'skyr':(63,11,4,0.2), 'dinkelmehl':(340,12,70,2), 'haferflocken':(370,13,59,7),
 'milch':(47,3.4,4.9,1.5), 'puddingpulver':(350,0,86,0), 'haehnchen':(105,23,0,1.5),
 'hack':(130,21,0,5), 'reibekaese':(260,30,0,15), 'frischkaese':(150,10,4,10),
 'tomaten':(30,1.5,4,0.5), 'lasagneplatten':(350,12,70,2), 'kartoffeln':(75,2,16,0.1),
 'putenschinken':(105,20,1,2), 'mandeln':(600,21,5,53), 'haselnuesse':(650,15,7,62),
 'kirschen':(50,1,10,0.3), 'kakao':(350,22,10,20), 'schokolade':(530,6,45,33),
 'gurken':(15,0.5,2,0), 'reis':(350,7,78,1), 'nudeln':(355,12,72,1.5), 'honig':(310,0,80,0),
 'butter':(740,0.7,0.6,82), 'quark':(70,12,4,0.3), 'tomatenmark':(85,4,14,0.5),
 'mozzarella':(165,20,1,9), 'salami':(230,25,1,14), 'mandelblaettchen':(600,21,5,53),
 'champignons':(20,3,0.5,0.3), 'mais':(90,3,16,1.2), 'apfelmus':(50,0.3,12,0.2),
 'rosinen':(300,2,70,0.5), 'kochschinken':(110,19,1,3), 'erythrit':(0,0,0,0), 'zimt':(0,0,0,0),
 'backpulver':(0,0,0,0), 'natron':(0,0,0,0), 'gyrosgewuerz':(0,0,0,0), 'vanille':(0,0,0,0),
 'oel':(900,0,0,100), 'kaesescheiben':(250,25,0,17), 'brokkoli':(30,3,3,0.3), 'gurke':(12,0.6,2,0.1),
 'tomate':(18,1,3,0.2), 'zwiebeln':(30,1,6,0.1), 'paprika':(25,1,5,0.3), 'ketchup':(100,1,24,0.2),
 'senf':(90,6,6,4), 'eiweiss':(50,11,0.5,0),
}
# Stück-Angaben (Gramm pro Stück)
PIECE = {'ei':(60,(90,7.5,0.5,6.5)), 'spekulatius':(8,(38,0.5,6,1.4)), 'apfel':(150,(80,0.4,17,0.3)),
         'zwiebel':(80,(30,1,6,0.1)), 'paprika_st':(150,(40,1.5,7,0.5)), 'loeffelbiskuit':(5,(19,0.5,4,0.2))}

def nut(item, grams=None, pieces=None):
    if item in PIECE:
        g,(k,p,c,f)=PIECE[item]; n=pieces if pieces is not None else grams/g
        return k*n,p*n,c*n,f*n
    k,p,c,f=NUT[item]; return k*grams/100,p*grams/100,c*grams/100,f*grams/100

# Zutaten: (Anzeige-Menge, Anzeige-Name, tile, nut_item, grams_or_None, pieces_or_None)
def Z(menge,name,tile,item,g=None,st=None): return dict(menge=menge,name=name,tile=tile,item=item,g=g,st=st)

R = [
# 1 · 06:00 · süß · Oats
dict(key='SpekOats', suess=True, hook='Frühstück wie Weihnachten:', titel=['SPEKULATIUS-','OVERNIGHT OATS'], portion='pro Glas', anzahl=2, vs=520,
 zutaten=[Z('80 g','Haferflocken','haferflocken','haferflocken',80), Z('250 g','Skyr','skyr','skyr',250), Z('200 ml','Milch (1,5 %)','milch','milch',200),
          Z('6 Stück','Spekulatius','spekulatius','spekulatius',st=6), Z('1 TL','Zimt','zimt','zimt',0), Z('1 TL','Lebkuchengewürz','lebkuchengewuerz','zimt',0),
          Z('20 g','Erythrit','erythrit','erythrit',20), Z('1 Stück','Apfel','apfel','apfel',st=1)],
 ex=[],
 intro='Overnight Oats, die nach Spekulatius schmecken: Haferflocken, Skyr und Milch mit Zimt und Lebkuchengewürz über Nacht quellen lassen, morgens geriebener Apfel und zerbröselte Spekulatius obendrauf. Kein Zucker, in 5 Minuten vorbereitet: {k} kcal und {p} g Eiweiß pro Glas statt 520 für Müsli mit Milch und Croissant!',
 schritte=['Haferflocken, Skyr, Milch, Zimt, Lebkuchengewürz und Erythrit in einer Schüssel verrühren und auf 2 Gläser verteilen.',
           'Über Nacht (mindestens 4 Stunden) in den Kühlschrank stellen.',
           'Morgens den Apfel grob reiben, auf die Oats geben und die Spekulatius zerbröselt darüber streuen.'],
 frage='Overnight Oats: Spekulatius oder Zimtschnecke?', tags='#overnightoats #spekulatius #fitmitkev',
 fb='Spekulatius-Overnight-Oats mit Apfel, abends gerührt, morgens fertig: {k} kcal und {p} g Eiweiß pro Glas statt 520 🎄',
 prompt='Two glass jars with overnight oats seen from the side at eye level, creamy oats with skyr, topped with grated apple, cinnamon and crumbled speculoos cookies, a whole speculoos cookie leaning against the glass, a spoon beside.'),
# 2 · 07:00 · herzhaft · Brötchen
dict(key='Quarkbroetchen', suess=False, hook='Wie vom Bäcker:', titel=['QUARK-','BRÖTCHEN'], portion='pro Stück', anzahl=8, vs=280,
 zutaten=[Z('350 g','Dinkelmehl','dinkelmehl','dinkelmehl',350), Z('250 g','Magerquark','quark','quark',250), Z('1 Stück','Ei','ei','ei',st=1),
          Z('1 Päckchen','Backpulver','backpulver','backpulver',0), Z('2 EL','Milch (1,5 %)','milch','milch',30), Z('1 EL','Haferflocken','haferflocken','haferflocken',10), Z('1 TL','Honig','honig','honig',7)],
 ex=['1 TL Salz'],
 intro='Quarkbrötchen wie vom Bäcker, nur ohne Hefe und ohne Gehzeit: Dinkelmehl, Magerquark, Ei und Backpulver kneten, formen, backen. In 35 Minuten stehen 8 Brötchen auf dem Tisch, außen knusprig, innen weich. {k} kcal und {p} g Eiweiß pro Brötchen statt 280 für das Körnerbrötchen vom Bäcker!',
 schritte=['Mehl, Quark, Ei, Backpulver, Salz, Honig und Milch zu einem glatten Teig kneten (klebt er, etwas Mehl dazu).',
           '8 Brötchen formen, oben kreuzweise einschneiden, mit Wasser bestreichen und mit Haferflocken bestreuen.',
           'Bei 200 °C Ober-/Unterhitze 22 Minuten goldbraun backen.'],
 frage='Brötchen: mit Käse oder mit Marmelade?', tags='#quarkbrötchen #ohnehefe #fitmitkev',
 fb='Körnerbrötchen vom Bäcker: 280 kcal. Meine Quarkbrötchen ohne Hefe, in 35 Minuten fertig: {k} kcal und {p} g Eiweiß 🥖',
 prompt='Homemade round quark bread rolls on baking paper on a light wooden board, golden brown crust with a cross cut on top sprinkled with oat flakes, one roll in front cut open showing a soft white fluffy crumb, a small dish of butter beside.'),
# 3 · 08:00 · süß · Pancakes
dict(key='ZimtschneckenPancakes', suess=True, hook='Zimtschnecke zum Frühstück:', titel=['ZIMTSCHNECKEN-','PANCAKES'], portion='pro Portion (4 Stück)', anzahl=3, vs=650,
 zutaten=[Z('150 g','Dinkelmehl','dinkelmehl','dinkelmehl',150), Z('250 g','Skyr','skyr','skyr',250), Z('2 Stück','Eier','ei','ei',st=2),
          Z('100 ml','Milch (1,5 %)','milch','milch',100), Z('1 TL','Backpulver','backpulver','backpulver',0), Z('2 TL','Zimt','zimt','zimt',0),
          Z('30 g','Erythrit','erythrit','erythrit',30), Z('60 g','Frischkäse light','frischkaese','frischkaese',60)],
 ex=['1 TL Vanilleextrakt', '1 EL Milch für den Guss'],
 intro='Pancakes, die nach Zimtschnecke schmecken: Skyr-Teig mit Zimt, in der Pfanne gebacken, und obendrauf der typische Frischkäse-Guss. 12 Pancakes für 3 Personen, ohne Zucker und ohne Butter: {k} kcal und {p} g Eiweiß pro Portion mit 4 Stück statt 650 für Pancakes mit Sirup!',
 schritte=['Mehl, Skyr, Eier, Milch, Backpulver, Zimt, 20 g Erythrit und Vanille zu einem glatten Teig rühren.',
           'In einer beschichteten Pfanne ohne Fett je 2 EL Teig pro Pancake von beiden Seiten goldbraun backen (12 Stück).',
           'Frischkäse mit 10 g Erythrit und 1 EL Milch glatt rühren und als Guss über die Pancakes geben, mit Zimt bestäuben.'],
 frage='Pancakes: mit Zimt oder mit Blaubeeren?', tags='#pancakes #zimtschnecken #fitmitkev',
 fb='Zimtschnecken-Pancakes mit Frischkäse-Guss, 4 Stück pro Person ohne Zucker: {k} kcal und {p} g Eiweiß statt 650 🥞',
 prompt='A white plate with a stack of four golden fluffy pancakes with a cinnamon swirl pattern on top, drizzled with white cream cheese glaze, dusted with cinnamon, a cinnamon stick beside, a fork beside.'),
# 4 · 09:00 · herzhaft · Pizzabrötchen
dict(key='Pizzabroetchen', suess=False, hook='Wie vom Lieferdienst:', titel=['PIZZA-','BRÖTCHEN'], portion='pro Stück', anzahl=10, vs=280,
 zutaten=[Z('300 g','Dinkelmehl','dinkelmehl','dinkelmehl',300), Z('300 g','Skyr','skyr','skyr',300), Z('1 Päckchen','Backpulver','backpulver','backpulver',0),
          Z('100 g','Reibekäse light','reibekaese','reibekaese',100), Z('80 g','Geflügelsalami','salami','salami',80), Z('80 g','Frischkäse light','frischkaese','frischkaese',80),
          Z('1 Stück','Paprika','paprika','paprika_st',st=1)],
 ex=['1 TL Oregano', '1 TL Salz', 'Knoblauch'],
 intro='Pizzabrötchen wie vom Lieferdienst, aus Skyr-Teig ohne Hefe: Teigkugeln mit Frischkäse, Salami, Paprika und Käse überbacken, in 30 Minuten fertig. 10 Stück: {k} kcal und {p} g Eiweiß pro Brötchen statt 280 für das Pizzabrötchen mit Kräuterbutter vom Lieferdienst!',
 schritte=['Mehl, Skyr, Backpulver und Salz zu einem Teig kneten, 10 flache Kugeln formen und auf ein Blech mit Backpapier setzen.',
           'Frischkäse mit Knoblauch und Oregano verrühren und auf die Brötchen streichen, Salami und Paprikawürfel darauf verteilen, Käse darüber.',
           'Bei 200 °C Ober-/Unterhitze 20 Minuten backen.'],
 frage='Pizzabrötchen: mit oder ohne Kräuterbutter-Dip?', tags='#pizzabrötchen #skyrteig #fitmitkev',
 fb='Pizzabrötchen vom Lieferdienst: 280 kcal. Meine aus Skyr-Teig mit Salami und Käse, 10 Stück: {k} kcal und {p} g Eiweiß',
 prompt='Homemade pizza rolls on baking paper on a light wooden board: small round bread rolls topped with melted golden cheese, slices of poultry salami and diced red pepper, one in front torn open showing a soft crumb and melted cheese, a small bowl of herb dip beside.'),
# 5 · 10:00 · süß · Quarkbällchen
dict(key='ApfelQuarkbaellchen', suess=True, hook='Wie von der Kirmes:', titel=['APFEL-','QUARKBÄLLCHEN'], portion='pro Stück', anzahl=16, vs=130,
 zutaten=[Z('250 g','Magerquark','quark','quark',250), Z('200 g','Dinkelmehl','dinkelmehl','dinkelmehl',200), Z('1 Stück','Ei','ei','ei',st=1),
          Z('1 Stück','Apfel','apfel','apfel',st=1), Z('50 g','Erythrit','erythrit','erythrit',50), Z('2 TL','Backpulver','backpulver','backpulver',0),
          Z('2 TL','Zimt','zimt','zimt',0)],
 ex=['1 TL Vanilleextrakt', '1 EL Erythrit + 1 TL Zimt zum Wälzen'],
 intro='Quarkbällchen wie von der Kirmes, mit kleinen Apfelstückchen und Zimt im Teig, aus dem Ofen statt aus dem Fett. 16 Stück ohne Zucker: {k} kcal und {p} g Eiweiß pro Bällchen statt 130 für das frittierte!',
 schritte=['Quark, Mehl, Ei, Erythrit, Backpulver, Zimt und Vanille zu einem Teig verkneten, Apfelwürfel unterkneten.',
           'Mit feuchten Händen 16 Kugeln formen und auf ein Blech mit Backpapier setzen.',
           'Bei 180 °C Ober-/Unterhitze 18 Minuten backen und noch warm in Zimt-Erythrit wälzen.'],
 frage='Quarkbällchen: pur, mit Apfel oder gefüllt?', tags='#quarkbällchen #ohnefritteuse #fitmitkev',
 fb='Quarkbällchen von der Kirmes: 130 kcal. Meine mit Apfel und Zimt aus dem Ofen statt aus dem Fett: {k} kcal pro Stück 🍎',
 prompt='Homemade golden-brown baked quark balls rolled in cinnamon on a white plate, one in front broken in half showing small soft apple pieces inside the fluffy dough, half an apple and a cinnamon stick beside.'),
# 6 · 11:00 · herzhaft · Lasagne-Suppe
dict(key='LasagneSuppe', suess=False, hook='Lasagne aus dem Topf:', titel=['LASAGNE-','SUPPE'], portion='pro Teller', anzahl=4, vs=750,
 zutaten=[Z('500 g','Rinderhack (mager)','hack','hack',500), Z('150 g','Lasagneplatten','lasagneplatten','lasagneplatten',150), Z('700 g','Passierte Tomaten','tomaten','tomaten',700),
          Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1), Z('2 EL','Tomatenmark','tomatenmark','tomatenmark',30), Z('800 ml','Rinderbrühe','bruehe','erythrit',0),
          Z('150 g','Frischkäse light','frischkaese','frischkaese',150), Z('60 g','Reibekäse light','reibekaese','reibekaese',60)],
 ex=['Knoblauch, Oregano, Basilikum, Salz, Pfeffer', '1 EL Öl'],
 intro='Lasagne als Suppe aus einem Topf: Hack anbraten, Tomaten und Brühe dazu, zerbrochene Lasagneplatten direkt im Topf garen, zum Schluss Frischkäse einrühren und Käse obendrauf. Schmeckt wie Lasagne, braucht aber nur 30 Minuten und keinen Ofen: {k} kcal und {p} g Eiweiß pro Teller statt 750 für die Lasagne beim Italiener!',
 schritte=['Hack mit gewürfelter Zwiebel und Knoblauch im Öl krümelig anbraten, Tomatenmark kurz mitrösten.',
           'Passierte Tomaten, Brühe, Oregano und Basilikum zugeben, aufkochen, Lasagneplatten in Stücke brechen und 12 Minuten mitköcheln.',
           'Frischkäse einrühren, salzen und pfeffern, auf Teller verteilen und mit Reibekäse bestreuen.'],
 frage='Lasagne: klassisch aus dem Ofen oder als Suppe?', tags='#lasagnesuppe #onepot #fitmitkev',
 fb='Lasagne beim Italiener: 750 kcal. Meine Lasagne-Suppe aus einem Topf in 30 Minuten: {k} kcal und {p} g Eiweiß 🍝',
 prompt='A white bowl of lasagna soup: rich red tomato and minced beef soup with broken lasagna pasta sheets, a dollop of white cream cheese melting in the middle, grated cheese and fresh basil leaves on top, a spoon beside, a pot blurred in the background.'),
# 7 · 12:00 · süß · Bowl
dict(key='NusseckenBowl', suess=True, hook='Nur für dich:', titel=['NUSSECKEN-','BOWL'], portion='die ganze Bowl', anzahl=1, vs=560,
 zutaten=[Z('35 g','Haferflocken','haferflocken','haferflocken',35), Z('120 g','Skyr','skyr','skyr',120), Z('1 Stück','Ei','ei','ei',st=1),
          Z('10 g','Gemahlene Haselnüsse','haselnuesse','haselnuesse',10), Z('8 g','Mandelblättchen','mandelblaettchen','mandelblaettchen',8), Z('20 g','Erythrit','erythrit','erythrit',20),
          Z('1 TL','Backpulver','backpulver','backpulver',0), Z('8 g','Zartbitterschokolade','schokolade','schokolade',8)],
 ex=['1 TL Honig', '1 EL Aprikosenmarmelade ohne Zucker (optional)', 'Prise Salz'],
 intro='Nussecken als Bowl nur für dich: unten ein weicher Haferflocken-Skyr-Boden, darauf eine knusprige Schicht aus Haselnüssen, Mandeln und Honig, die Ecken in Schokolade getunkt – hier als Schoko-Drizzle. Aus der Glasform, warm gegessen: {k} kcal und {p} g Eiweiß die ganze Bowl statt 560 für zwei Nussecken vom Bäcker!',
 schritte=['Haferflocken, 80 g Skyr, Ei, 10 g Erythrit, Backpulver und Salz verrühren und in eine kleine gefettete Glasform (15 × 10 cm) geben.',
           'Haselnüsse, Mandelblättchen, 10 g Erythrit und Honig mit 40 g Skyr mischen und auf dem Teig verteilen.',
           'Bei 180 °C Ober-/Unterhitze 22 Minuten backen, Schokolade schmelzen und darüber träufeln.'],
 frage='Nussecken: die Ecke mit Schokolade zuerst oder zuletzt?', tags='#nussecken #bowl #fitmitkev',
 fb='Nussecken nur für dich, warm aus der Glasform mit Schoko: {k} kcal und {p} g Eiweiß die ganze Bowl statt 560 🥜',
 prompt='A single portion baked in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, empty counter behind. No whipped cream, nothing on the spoon. Inside: a soft golden oat base topped with a crunchy baked hazelnut and almond flake layer, drizzled with dark chocolate, a few hazelnuts beside the dish.'),
# 8 · 13:00 · herzhaft · Auflauf
dict(key='CordonBleuAuflauf', suess=False, hook='Cordon bleu aus der Form:', titel=['CORDON-BLEU-','AUFLAUF'], portion='pro Portion', anzahl=4, vs=850,
 zutaten=[Z('500 g','Hähnchenbrust','haehnchen','haehnchen',500), Z('600 g','Kartoffeln','kartoffeln','kartoffeln',600), Z('120 g','Kochschinken','kochschinken','kochschinken',120),
          Z('150 g','Frischkäse light','frischkaese','frischkaese',150), Z('150 ml','Milch (1,5 %)','milch','milch',150), Z('80 g','Reibekäse light','reibekaese','reibekaese',80),
          Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1), Z('1 TL','Senf','senf','senf',5)],
 ex=['Knoblauch, Muskat, Paprikapulver, Salz, Pfeffer', '1 EL Öl'],
 intro='Cordon bleu ohne Panade und ohne Fritteuse: Hähnchen und Kochschinken auf Kartoffelscheiben, darüber eine Frischkäse-Senf-Soße und eine Käsekruste aus dem Ofen. Alles aus einer Form: {k} kcal und {p} g Eiweiß pro Portion statt 850 für Cordon bleu mit Pommes!',
 schritte=['Kartoffeln in dünne Scheiben schneiden, 8 Minuten vorkochen und in eine Auflaufform schichten.',
           'Hähnchenwürfel mit Zwiebel im Öl anbraten, würzen, mit Schinkenstreifen auf den Kartoffeln verteilen. Frischkäse, Milch, Senf, Knoblauch und Muskat verrühren und darüber gießen.',
           'Käse darüber streuen und bei 200 °C Ober-/Unterhitze 25 Minuten goldbraun überbacken.'],
 frage='Cordon bleu: mit Pommes oder mit Kartoffeln aus der Form?', tags='#cordonbleu #auflauf #fitmitkev',
 fb='Cordon bleu mit Pommes: 850 kcal. Mein Cordon-Bleu-Auflauf mit Kartoffeln, ohne Panade: {k} kcal und {p} g Eiweiß 🧀',
 prompt='A white ceramic rectangular baking dish with a casserole of sliced potatoes, chicken pieces and strips of ham in a creamy pale sauce, covered with a golden bubbly melted cheese crust, one portion already served on a white plate in front showing the layers from the side, nothing above the dish.'),
# 9 · 14:00 · süß · Skyr-Kuchen
dict(key='BratapfelSkyrKuchen', suess=True, hook='Mein Bestseller, neu:', titel=['BRATAPFEL-','SKYR-KUCHEN'], portion='pro Stück', anzahl=12, vs=400,
 zutaten=[Z('1000 g','Skyr','skyr','skyr',1000), Z('3 Stück','Eier','ei','ei',st=3), Z('1 Päckchen','Vanillepudding-Pulver','puddingpulver','puddingpulver',37),
          Z('80 g','Erythrit','erythrit','erythrit',80), Z('3 Stück','Äpfel','apfel','apfel',st=3), Z('2 TL','Zimt','zimt','zimt',0),
          Z('30 g','Rosinen','rosinen','rosinen',30), Z('20 g','Mandelblättchen','mandelblaettchen','mandelblaettchen',20)],
 ex=['8 Butterkekse + 2 EL Milch (dünner Boden)', '1 TL Vanilleextrakt'],
 intro='Mein Skyr-Kuchen in der Bratapfel-Version: dünner Keksboden, cremige Skyr-Füllung, darin Apfelwürfel mit Zimt und Rosinen, obendrauf geröstete Mandelblättchen. Kein Zucker, 12 Stücke: {k} kcal und {p} g Eiweiß pro Stück statt 400 für den Apfel-Käsekuchen vom Bäcker!',
 schritte=['Butterkekse fein zerbröseln, mit der Milch mischen und in eine Springform (26 cm) mit Backpapier drücken. Äpfel schälen, würfeln und mit Zimt und Rosinen mischen.',
           'Skyr, Eier, Puddingpulver, Erythrit und Vanille glatt rühren, Apfelmischung unterheben, auf den Boden gießen und Mandelblättchen darüber streuen.',
           'Bei 160 °C Ober-/Unterhitze 55 Minuten backen, im Ofen abkühlen lassen und über Nacht kalt stellen.'],
 frage='Skyr-Kuchen: Spekulatius oder Bratapfel?', tags='#skyrkuchen #bratapfel #fitmitkev',
 fb='Mein beliebtester Kuchen als Bratapfel-Version mit Zimt und Rosinen: {k} kcal und {p} g Eiweiß pro Stück statt 400 🍎',
 prompt='A round cheesecake on a white cake stand seen from the side, one slice cut and placed on a small white plate in front showing the creamy pale filling from the side, a crustless cheesecake with soft apple pieces, raisins and cinnamon baked into the creamy filling and toasted almond flakes on top, half an apple and a cinnamon stick beside the plate.'),
# 10 · 15:00 · herzhaft · Bowl
dict(key='GyrosBowl', suess=False, hook='Nur für dich:', titel=['GYROS-','BOWL'], portion='die ganze Bowl', anzahl=1, vs=800,
 zutaten=[Z('125 g','Hähnchenbrust','haehnchen','haehnchen',125), Z('40 g','Reis (roh)','reis','reis',40), Z('1 EL','Gyrosgewürz','gyrosgewuerz','gyrosgewuerz',0),
          Z('½ Stück','Paprika','paprika','paprika_st',st=0.5), Z('½ Stück','Zwiebel','zwiebel','zwiebel',st=0.5), Z('100 g','Skyr','skyr','skyr',100),
          Z('¼ Stück','Gurke','gurke','gurke',80), Z('15 g','Reibekäse light','reibekaese','reibekaese',15)],
 ex=['Knoblauch, 1 TL Öl, Salz, Pfeffer'],
 intro='Gyros als Bowl nur für dich, aus dem Ofen: Reis unten, darauf Hähnchen-Gyros mit Paprika und Zwiebel, obendrauf eine Haube aus Skyr-Tzatziki und etwas Käse überbacken. {k} kcal und {p} g Eiweiß die ganze Bowl statt 800 für den Gyros-Teller beim Griechen!',
 schritte=['Reis kochen und in eine kleine gefettete Glasform (15 × 10 cm) geben.',
           'Hähnchenstreifen mit Gyrosgewürz im Öl scharf anbraten, Paprika- und Zwiebelstreifen 4 Minuten mitbraten und auf den Reis geben.',
           'Skyr mit geriebener, ausgedrückter Gurke, Knoblauch, Salz und Pfeffer verrühren, darüber streichen, Käse darauf und bei 200 °C Ober-/Unterhitze 12 Minuten überbacken.'],
 frage='Gyros: mit Tzatziki oder mit Knoblauchsoße?', tags='#gyros #bowl #fitmitkev',
 fb='Gyros nur für dich, überbacken mit Tzatziki-Haube: {k} kcal und {p} g Eiweiß die ganze Bowl statt 800 beim Griechen 🇬🇷',
 prompt='A single portion baked in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, empty counter behind. No whipped cream, nothing on the spoon. Inside: rice at the bottom, seared spiced chicken gyros strips with red pepper and onion, topped with a baked white tzatziki-skyr layer with lightly browned cheese, a few cucumber slices beside the dish.'),
# 11 · 16:00 · süß · Bowl
dict(key='BienenstichBowl', suess=True, hook='Nur für dich:', titel=['BIENENSTICH-','BOWL'], portion='die ganze Bowl', anzahl=1, vs=550,
 zutaten=[Z('25 g','Dinkelmehl','dinkelmehl','dinkelmehl',25), Z('150 g','Skyr','skyr','skyr',150), Z('1 Stück','Ei','ei','ei',st=1),
          Z('½ Päckchen','Vanillepudding-Pulver','puddingpulver','puddingpulver',12), Z('100 ml','Milch (1,5 %)','milch','milch',100), Z('12 g','Mandelblättchen','mandelblaettchen','mandelblaettchen',12),
          Z('1 TL','Honig','honig','honig',7), Z('25 g','Erythrit','erythrit','erythrit',25)],
 ex=['1 TL Backpulver', '1 TL Vanilleextrakt'],
 intro='Bienenstich als Bowl nur für dich: fluffiger Skyr-Boden, darauf eine dicke Schicht Vanillepudding-Creme und obendrauf die knusprige Honig-Mandel-Kruste. Ohne Zucker, ohne Sahne: {k} kcal und {p} g Eiweiß die ganze Bowl statt 550 für ein Stück Bienenstich vom Bäcker!',
 schritte=['Mehl, 100 g Skyr, Ei, 10 g Erythrit, Backpulver und Vanille verrühren, in eine kleine gefettete Glasform (15 × 10 cm) geben. Mandelblättchen mit Honig mischen und darauf verteilen.',
           'Bei 180 °C Ober-/Unterhitze 20 Minuten backen, bis die Mandeln goldbraun sind, auskühlen lassen.',
           'Puddingpulver mit Milch und 15 g Erythrit kochen, kurz abkühlen, 50 g Skyr unterrühren. Boden waagerecht halbieren, Creme dazwischen und obendrauf, Mandeldeckel wieder aufsetzen.'],
 frage='Bienenstich: die Mandelkruste oder die Creme – was isst du zuerst?', tags='#bienenstich #bowl #fitmitkev',
 fb='Bienenstich nur für dich mit Honig-Mandel-Kruste und Puddingcreme: {k} kcal und {p} g Eiweiß die ganze Bowl statt 550 🍯',
 prompt='A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, layers visible through the glass: a golden cake base, a thick pale yellow vanilla pudding cream layer and a crunchy caramelized honey almond flake topping; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, empty counter behind. No whipped cream, nothing on the spoon.'),
# 12 · 17:00 · herzhaft · Auflauf
dict(key='CheeseburgerAuflauf', suess=False, hook='Für die ganze Familie:', titel=['CHEESEBURGER-','AUFLAUF'], portion='pro Portion', anzahl=4, vs=900,
 zutaten=[Z('450 g','Rinderhack (mager)','hack','hack',450), Z('220 g','Nudeln (roh)','nudeln','nudeln',220), Z('400 g','Passierte Tomaten','tomaten','tomaten',400),
          Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1), Z('80 g','Reibekäse light','reibekaese','reibekaese',80), Z('4 Stück','Gewürzgurken','gurken','gurken',120),
          Z('100 g','Skyr','skyr','skyr',100)],
 ex=['1 EL Ketchup', '1 EL Senf', 'Paprikapulver, Salz, Pfeffer', '1 EL Öl'],
 intro='Cheeseburger als Auflauf für die ganze Familie: Nudeln, krümeliges Hack in Tomatensoße, Käsekruste aus dem Ofen und obendrauf Gewürzgurken und Burgersoße aus Skyr, Ketchup und Senf. {k} kcal und {p} g Eiweiß pro Portion statt 900 für Doppel-Cheeseburger mit Pommes!',
 schritte=['Nudeln bissfest kochen. Hack mit gewürfelter Zwiebel im Öl krümelig braten, mit Paprikapulver, Salz und Pfeffer würzen, passierte Tomaten zugeben.',
           'Nudeln und Hacksoße in einer Auflaufform mischen, Käse darüber und bei 200 °C Ober-/Unterhitze 15 Minuten überbacken.',
           'Skyr mit Ketchup und Senf zur Burgersoße verrühren, Auflauf mit Gurkenscheiben belegen und mit der Soße beträufeln.'],
 frage='Cheeseburger: mit oder ohne Gewürzgurke?', tags='#cheeseburger #nudelauflauf #fitmitkev',
 fb='Cheeseburger-Auflauf für die ganze Familie mit Nudeln und Käsekruste: {k} kcal und {p} g Eiweiß pro Portion statt 900 🍔',
 prompt='A white ceramic rectangular baking dish with a cheeseburger pasta bake: pasta and crumbled browned minced beef in tomato sauce under a golden melted cheese crust, topped with pickle slices and a drizzle of pale burger sauce, one portion already served on a white plate in front, nothing above the dish.'),
# 13 · 18:00 · süß · Konditorei
dict(key='SchwarzwaelderSkyr', suess=True, hook='Wie aus der Konditorei:', titel=['SCHWARZWÄLDER','SKYR-KUCHEN'], portion='pro Stück', anzahl=12, vs=450,
 zutaten=[Z('750 g','Skyr','skyr','skyr',750), Z('3 Stück','Eier','ei','ei',st=3), Z('1 Päckchen','Schokopudding-Pulver','puddingpulver','puddingpulver',37),
          Z('30 g','Backkakao','kakao','kakao',30), Z('80 g','Erythrit','erythrit','erythrit',80), Z('350 g','Sauerkirschen','kirschen','kirschen',350),
          Z('200 g','Frischkäse light','frischkaese','frischkaese',200), Z('20 g','Zartbitterschokolade','schokolade','schokolade',20)],
 ex=['1 TL Vanilleextrakt', '2 EL Kirschsaft'],
 intro='Schwarzwälder Kirsch als Skyr-Kuchen: ein saftiger Schoko-Skyr-Boden ohne Mehl, einmal durchgeschnitten, dazwischen und obendrauf eine helle Creme aus Frischkäse und Skyr statt Sahne mit Sauerkirschen, zum Schluss Schokoraspel. 12 Stücke ohne Zucker: {k} kcal und {p} g Eiweiß pro Stück statt 450 für die Torte aus der Konditorei!',
 schritte=['500 g Skyr, Eier, Puddingpulver, Kakao und 60 g Erythrit glatt rühren, in eine Springform (26 cm) mit Backpapier gießen und bei 160 °C Ober-/Unterhitze 45 Minuten backen, auskühlen lassen.',
           'Boden waagerecht halbieren und die untere Hälfte mit 2 EL Kirschsaft beträufeln. Frischkäse, 250 g Skyr, 20 g Erythrit und Vanille cremig rühren.',
           'Die Hälfte der Creme mit den Kirschen auf den unteren Boden geben, zweiten Boden aufsetzen, restliche Creme darauf verstreichen, Schokoraspel darüber und 3 Stunden kalt stellen.'],
 frage='Schwarzwälder Kirsch: mit oder ohne Kirschwasser?', tags='#schwarzwälderkirsch #skyrkuchen #fitmitkev',
 fb='Schwarzwälder Kirsch vom Konditor: 450 kcal. Meine als Skyr-Kuchen ohne Sahne: {k} kcal und {p} g Eiweiß pro Stück 🍒',
 prompt='A round cake on a white cake stand seen from the side, one slice cut and placed on a small white plate in front showing the layers from the side: a dark chocolate base, dark red sour cherries, a thick white creamy layer and dark chocolate shavings on top, a few cherries beside the plate.'),
# 14 · 19:00 · herzhaft · Laugen
dict(key='LaugenKnoten', suess=False, hook='Wie vom Bäcker:', titel=['LAUGEN-KNOTEN','MIT KÄSE'], portion='pro Stück', anzahl=8, vs=320,
 zutaten=[Z('350 g','Dinkelmehl','dinkelmehl','dinkelmehl',350), Z('300 g','Skyr','skyr','skyr',300), Z('1 Päckchen','Backpulver','backpulver','backpulver',0),
          Z('3 EL','Natron','natron','natron',0), Z('100 g','Reibekäse light','reibekaese','reibekaese',100), Z('1 EL','Sesam','sesam','mandelblaettchen',10)],
 ex=['1 TL Salz + grobes Salz', '1 l Wasser für die Lauge'],
 intro='Laugenknoten mit Käsefüllung wie vom Bäcker, aus Skyr-Teig ohne Hefe: Stränge rollen, Käse einwickeln, verknoten, kurz in Natronlauge baden und backen. In 35 Minuten fertig, außen glänzend braun, innen weich mit geschmolzenem Käse: {k} kcal und {p} g Eiweiß pro Knoten statt 320 für den Käse-Laugenknoten vom Bäcker!',
 schritte=['Mehl, Skyr, Backpulver und Salz zu einem glatten Teig kneten, in 8 Stücke teilen und zu 40 cm langen Strängen rollen. Jeden Strang flach drücken, Käse in die Mitte, zuklappen, gut verschließen und zu Knoten schlingen.',
           '1 l Wasser mit Natron aufkochen, jeden Knoten 30 Sekunden darin baden, abtropfen lassen, mit grobem Salz und Sesam bestreuen.',
           'Bei 200 °C Ober-/Unterhitze 20 Minuten backen, bis die Kruste glänzend braun ist.'],
 frage='Laugengebäck: Brezel, Brötchen oder Knoten?', tags='#laugenknoten #ohnehefe #fitmitkev',
 fb='Käse-Laugenknoten vom Bäcker: 320 kcal. Meine mit Käsefüllung aus Skyr-Teig ohne Hefe: {k} kcal und {p} g Eiweiß 🥨',
 prompt='Homemade pretzel knots (Laugenknoten) on baking paper on a light wooden board: knotted soft rolls with a glossy chestnut-brown lye crust, coarse salt, sesame and a golden baked melted cheese crust on top, one in front torn open showing a soft white crumb, warm bakery color, not black.'),
# 15 · 20:00 · süß · Käsekuchen
dict(key='BrownieKaesekuchen', suess=True, hook='Zwei Kuchen in einem:', titel=['BROWNIE-','KÄSEKUCHEN'], portion='pro Stück', anzahl=12, vs=420,
 zutaten=[Z('750 g','Skyr','skyr','skyr',750), Z('3 Stück','Eier','ei','ei',st=3), Z('1 Päckchen','Vanillepudding-Pulver','puddingpulver','puddingpulver',37),
          Z('80 g','Erythrit','erythrit','erythrit',80), Z('40 g','Backkakao','kakao','kakao',40), Z('60 g','Dinkelmehl','dinkelmehl','dinkelmehl',60),
          Z('60 g','Zartbitterschokolade','schokolade','schokolade',60), Z('100 ml','Milch (1,5 %)','milch','milch',100)],
 ex=['1 TL Backpulver', '1 TL Vanilleextrakt', 'Prise Salz'],
 intro='Brownie und Käsekuchen in einem: unten ein saftiger Schoko-Brownie-Boden aus Kakao und geschmolzener Zartbitterschokolade, oben die cremige Skyr-Schicht, beides zusammen gebacken und marmoriert. 12 Stücke ohne Butter und ohne Zucker: {k} kcal und {p} g Eiweiß pro Stück statt 420 für den Brownie-Cheesecake aus dem Café!',
 schritte=['Schokolade mit Milch schmelzen, mit 250 g Skyr, 1 Ei, Kakao, Mehl, 30 g Erythrit, Backpulver und Salz zu einem Brownie-Teig rühren und in eine Springform (26 cm) mit Backpapier streichen.',
           '500 g Skyr, 2 Eier, Puddingpulver, 50 g Erythrit und Vanille glatt rühren und auf den Brownie-Teig gießen, mit einer Gabel leicht marmorieren.',
           'Bei 160 °C Ober-/Unterhitze 50 Minuten backen, im Ofen abkühlen lassen und über Nacht kalt stellen.'],
 frage='Brownie oder Käsekuchen – oder beides?', tags='#browniekäsekuchen #skyrkuchen #fitmitkev',
 fb='Brownie-Käsekuchen, zwei Kuchen in einem, ohne Butter und Zucker: {k} kcal und {p} g Eiweiß pro Stück statt 420 🍫',
 prompt='A round brownie cheesecake on a white cake stand seen from the side, one slice cut and placed on a small white plate in front showing the layers from the side: a dark fudgy chocolate brownie base and a creamy pale cheesecake top with chocolate marbling, a few dark chocolate pieces beside the plate.'),
]

def macros4(r):
    K=P=C=F=0.0
    for z in r['zutaten']:
        k,p,c,f=nut(z['item'],z['g'],z['st']); K+=k;P+=p;C+=c;F+=f
    for ex in r.get('exnut',[]):
        K+=ex[0];P+=ex[1];C+=ex[2];F+=ex[3]
    n=r['anzahl']
    return int(round(K/n/5)*5), int(round(P/n)), int(round(C/n)), int(round(F/n))

# kleine Extras (Öl, Honig, Marmelade …) in kcal pro Rezept gesamt
EXN={'LasagneSuppe':(90,0,0,10),'CordonBleuAuflauf':(90,0,0,10),'GyrosBowl':(45,0,0,5),'CheeseburgerAuflauf':(105,0,4,10),
     'NusseckenBowl':(30,0,8,0),'ZimtschneckenPancakes':(10,0,2,0),'BratapfelSkyrKuchen':(250,3,40,8)}
for r in R: r['exnut']=[EXN[r['key']]] if r['key'] in EXN else []

if __name__=='__main__':
    for i,r in enumerate(R,1):
        k,p,c,f=macros4(r); print(i, r['key'], 'süß' if r['suess'] else 'herz', k,p,c,f, r['portion'], len(r['zutaten']))
