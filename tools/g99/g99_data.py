# -*- coding: utf-8 -*-
# G99 – Sonntag 22.11.2026 (in Arbeit). Stand 20.11.: nur die 3 neuen Rezepte nach dem Muster der Mitbewerberin „Mellys Köstlichkeiten“
#   (Kev 20.11. per Dialog: „Ja, alle 4“ und „Ja, bei 2 testen“ = Rezept direkt im Beitrag bei den 2 Gläsern).
#   Auswertung Melly 6.–20.11.: beste Beiträge = Klassiker zum Löffeln im Glas mit 3–5 Zutaten (Spekulatius-Kirsch 1.071 Reaktionen, Nutella-Banane 657),
#   seit 10.11. umgebautes Fast Food (Döner-Kuchen 147 Reaktionen / 102 geteilt, Pizza-Kartoffeln 75 / 63). Siehe Projekt-Dokument `claude/mitbewerber-analyse.md`.
#   Das vierte „Melly-Rezept“ ist unser Spekulatius-Kirsch-Glas vom So 15.11. (G93N, 5,0 × Tagesmedian) – genau 7 Tage später, gleiches Bild.
#   „Schwarzwälder Kirsch im Glas“ entfällt: am Fr 20.11. 13:00 lief das ESN-Rezept „Schwarzwälder im Glas“, und mehr als 2 Gläser am Tag nutzen das Format ab.
# Nachtrag 20.11., 16 Uhr: Kev hat vier weitere Mitbewerber-Seiten hinzugefügt (Unsere Weihnachtsbäckerei, Leicht & Lecker Zuhause, Lecker Zuhause, Leckeria).
#   Dort vorn: weiche Plätzchen/„Wölkchen“, „1 Teig – viele Sorten“, Sonntagsbraten mit Rotkohl und Klößen, Blumenkohlsuppe. Kev per Dialog: „Alle 4 am Sonntag“.
#   → 4 weitere neue Rezepte: EinTeig (Grundteig = Butterplätzchen aus dem Buch, G79/G35), QuarkWoelkchen, Sonntagsbraten, Blumenkohlsuppe. Damit 7 neue + SpekKirsch fest, 8 Plätze offen.
# Der Rest des Sonntags (8 ausgeruhte Treffer, Zeiten, Hashtag-Gruppen) wird am Sa 21.11. früh mit Kev und den Freitagszahlen festgelegt.
# Feste Beiträge am Sonntag: 06:10 ESN-Rezept Spekulatius-Mousse · 06:50 ESN K2 · 11:00 ESN P1 · 12:00 ESN P0 · 13:00 ESN-Rezept Erdbeer-Bowl · 20:15 Buch-Beitrag.
import sys, os, copy
_D=os.path.dirname(os.path.abspath(__file__))
for g in ('g87','g88','g89','g90','g91','g92','g93','g93n'): sys.path.insert(0, os.path.join(_D, '..', g))
from g90_data import NUT, PIECE, nut, Z, macros4
import g93n_data
_A={}
for m in (g93n_data,):
    for r in m.R: _A[r['key']]=r
def alt(key, tags, **kw):
    r=copy.deepcopy(_A[key]); r['tags']=tags; r['kurz']=r.get('kurz') or ['–','–','–']
    for x in ('fb','hinweis','n','buch','vorhanden'): r.pop(x,None)
    r.update(kw); return r
for _k,_v in {'eisbergsalat':(14,1,2,0.2), 'nussnougatcreme':(540,6,57,31), 'blumenkohl':(25,2,2.5,0.3), 'kloesse':(105,2,22.5,0.5)}.items(): NUT.setdefault(_k,_v)   # bestehende Werte nicht überschreiben

NEU=dict(
 NutellaBanane=dict(key='NutellaBanane', suess=True, hook='Nur 3 Zutaten:', titel=['NUTELLA-BANANE','IM GLAS'], portion='pro Glas', anzahl=1, vs=550,
  zutaten=[Z('200 g','Skyr','skyr','skyr',200), Z('15 g','Nuss-Nougat-Creme','nuss_nougat_creme','nussnougatcreme',15), Z('1 Stück','Banane','banane','banane',st=1)],
  ex=[],
  intro='Nutella und Banane gehen immer. Hier als Dessert im Glas aus nur 3 Zutaten: cremiger Skyr mit einem Löffel Nuss-Nougat-Creme verrührt, dazwischen Bananenscheiben. Ohne Backen und in 5 Minuten fertig: {k} kcal und {p} g Eiweiß das ganze Glas statt 550 für einen Crêpe mit Nutella und Banane!',
  schritte=['Den Skyr mit der Nuss-Nougat-Creme glatt rühren, dabei einen kleinen Klecks Creme für oben zurückbehalten.',
            'Die Banane in Scheiben schneiden und abwechselnd mit der Creme in ein Glas (ca. 350 ml) schichten.',
            'Mit ein paar Bananenscheiben und dem Klecks Nuss-Nougat-Creme abschließen. Sofort löffeln oder 30 Minuten kalt stellen.'],
  frage='Team Nutella-Banane oder Team Spekulatius-Kirsch?', tags='#nutellabanane #dessertimglas #fitmitkev',
  prompt='One tall clear dessert glass filled with layers of smooth pale brown chocolate hazelnut yogurt cream and fresh banana slices, several round banana slices pressed flat against the inside of the glass wall, on top a fan of banana slices and a small glossy swirl of dark brown chocolate hazelnut spread, one plain straight teaspoon lying beside the glass, one whole yellow banana and a few banana slices beside the glass.'),
 DoenerKuchen=dict(key='DoenerKuchen', suess=False, hook='Döner mal anders:', titel=['DÖNER-','KUCHEN'], portion='pro Stück', anzahl=4, vs=900,
  zutaten=[Z('200 g','Dinkelmehl','dinkelmehl','dinkelmehl',200), Z('350 g','Skyr','skyr','skyr',350), Z('500 g','Hähnchenbrust','haehnchenbrust','haehnchen',500),
           Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1), Z('80 g','Reibekäse light','reibekaese_light','reibekaese',80), Z('1 Zehe','Knoblauch','knoblauch','knoblauch',3),
           Z('100 g','Eisbergsalat','eisbergsalat','eisbergsalat',100), Z('½ Stück','Salatgurke','salatgurke','gurke',100)],
  ex=['1 Päckchen Backpulver, 2 Tomaten, 1 TL Öl', '2 TL Paprikapulver, 1 TL Oregano, ½ TL Kreuzkümmel', 'Salz, Pfeffer, etwas Zitronensaft'],
  intro='Döner als Kuchen: ein knuspriger Boden aus Skyr-Teig, darauf würziges Hähnchen und geschmolzener Käse, obendrauf frischer Salat, Tomate, Gurke und Knoblauchsoße. Anschneiden wie eine Torte, und alle greifen zu. Ein Viertel vom Kuchen: {k} kcal und {p} g Eiweiß statt 900 für den Döner vom Imbiss!',
  schritte=['Mehl, 200 g Skyr, Backpulver und ½ TL Salz zu einem glatten Teig kneten. Eine Springform (24 cm) mit Backpapier auslegen, den Teig hineindrücken und dabei einen 4 cm hohen Rand formen. Den Boden mehrfach einstechen und bei 200 °C Ober-/Unterhitze 8 Minuten vorbacken.',
            'Hähnchen in dünne Streifen und Zwiebel in Ringe schneiden, mit Öl, Paprikapulver, Oregano, Kreuzkümmel, Salz und Pfeffer mischen und in einer heißen Pfanne 5–6 Minuten kräftig braten. Die Hälfte des Käses auf den Boden streuen, das Hähnchen darauf verteilen, den restlichen Käse darüber geben und 15–20 Minuten goldbraun backen.',
            '150 g Skyr mit gepresstem Knoblauch, etwas Zitronensaft, Salz und Pfeffer verrühren. Salat, Tomaten und Gurke klein schneiden. Den Kuchen 5 Minuten ruhen lassen, in 4 Stücke schneiden und mit Salat und Knoblauchsoße servieren.'],
  frage='Döner: mit Knoblauchsoße oder lieber scharf?', tags='#dönerkuchen #döner #hähnchen #abendessen #fitmitkev',
  prompt='A round savory pie standing on a wooden board, baked in a springform and the ring removed: a golden brown bread dough crust with a four centimeter high rim, filled with browned spiced chicken strips and golden melted cheese, the top covered with fresh shredded green iceberg lettuce, diced red tomato, diced cucumber, thin red onion rings and drizzled stripes of white garlic yogurt sauce, one quarter slice cut out and served on a white plate in front showing the chicken filling inside the crust, a small white bowl of white garlic sauce beside.'),
 PizzaKartoffeln=dict(key='PizzaKartoffeln', suess=False, hook='Pizza trifft Ofenkartoffel:', titel=['PIZZA-','KARTOFFELN'], portion='pro Portion', anzahl=4, vs=850,
  zutaten=[Z('1 kg','Kartoffeln','kartoffeln','kartoffeln',1000), Z('300 g','Passierte Tomaten','passierte_tomaten','tomaten',300),
           Z('200 g','Körniger Frischkäse','huettenkaese','huettenkaese',200), Z('100 g','Reibekäse light','reibekaese_light','reibekaese',100),
           Z('60 g','Salami','salami','salami',60), Z('1 Stück','Rote Paprika','rote_paprika','paprika_st',st=1),
           Z('1 EL','Öl','oel','oel',10), Z('2 TL','Pizza-Kräuter','pizza_kraeuter','vanille',0)],
  ex=['Salz, Pfeffer, 1 TL Paprikapulver'],
  intro='Knusprige Ofenkartoffeln, belegt wie eine Pizza: Tomatensoße, Salami, Paprika und goldbraun geschmolzener Käse. Der Trick steckt in der Soße: körniger Frischkäse, glatt püriert, macht sie cremig und bringt Eiweiß. Alles aus einer Form: {k} kcal und {p} g Eiweiß pro Portion statt 850 für die Salami-Pizza vom Lieferdienst!',
  schritte=['Die Kartoffeln in 2 cm große Würfel schneiden, mit Öl, Salz und Paprikapulver mischen und auf einem Backblech mit Backpapier bei 220 °C Ober-/Unterhitze 25 Minuten goldbraun backen, nach der Hälfte wenden.',
            'Passierte Tomaten mit dem körnigen Frischkäse, den Pizza-Kräutern, Salz und Pfeffer glatt pürieren. Die Paprika klein würfeln.',
            'Die Kartoffeln in eine Auflaufform (20 × 30 cm) geben, Soße und Paprika in der Mitte verteilen, mit Käse und Salami belegen und 10–12 Minuten überbacken. Am Rand ein paar Kartoffeln ohne Soße lassen, die bleiben knusprig.'],
  frage='Pizza-Kartoffeln: mit Salami oder mit Schinken?', tags='#pizzakartoffeln #kartoffeln #ofengericht #familienessen #fitmitkev',
  prompt='Close view of a rectangular white ceramic baking dish filled to the top with many small golden brown crispy roasted potato cubes, the middle of the dish covered with a blanket of golden browned bubbling melted mozzarella cheese, round slices of red salami lying on top of the cheese, a little red tomato sauce showing under the cheese, small red bell pepper cubes, crispy bare potato cubes clearly visible all around the edge of the dish, sprinkled with dried oregano. In front a white plate with one portion of crispy potato cubes with stretchy melted cheese and two salami slices, a fork beside the plate.'),
 EinTeig=dict(key='EinTeig', suess=True, hook='Nur 1 Teig:', titel=['5 SORTEN','PLÄTZCHEN'], portion='pro Stück', anzahl=50, vs=70,
  zutaten=[Z('300 g','Dinkelmehl','dinkelmehl','dinkelmehl',300), Z('100 g','Butter (kalt)','butter','butter',100), Z('100 g','Skyr','skyr','skyr',100),
           Z('100 g','Erythrit','erythrit','erythrit',100), Z('1 Stück','Ei','ei','ei',st=1), Z('1 EL','Backkakao','backkakao','kakao',10),
           Z('15 g','Kokosraspel','kokosraspel','kokosraspel',15), Z('40 g','Fruchtaufstrich','fruchtaufstrich','fruchtaufstrich',40)],
  ex=['1 TL Vanilleextrakt, 1 TL Zimt, 1 Prise Salz'],
  intro='Ein Teig, fünf Sorten: Butter-Sterne, Sterne mit Zimt, Schoko-Sterne, Engelsaugen im Kokosmantel und Schoko-Engelsaugen. Du knetest nur einmal, teilst den Teig durch fünf, und der Plätzchenteller ist voll. Der Teig mit Skyr braucht nur 100 g Butter und bleibt trotzdem mürbe. 50 Plätzchen: {k} kcal pro Stück statt 70 für ein klassisches Butterplätzchen!',
  schritte=['Mehl, Butter in Stücken, Skyr, 80 g Erythrit, Ei, Vanille und Salz rasch zu einem glatten Teig kneten und in 5 gleich große Portionen teilen. Unter zwei Portionen den Backkakao mit 2 TL Wasser kneten. Alles in Folie wickeln und 30 Minuten kalt stellen.',
            'Sorte 1 bis 3: Zwei helle Portionen und eine Schoko-Portion 4 mm dick ausrollen und Sterne ausstechen. 1 TL Zimt mit dem restlichen Erythrit mischen und die Hälfte der hellen Sterne vor dem Backen damit bestreuen.',
            'Sorte 4 und 5: Aus der letzten hellen und der zweiten Schoko-Portion je 10 Kugeln formen. Die hellen Kugeln in den Kokosraspeln wälzen. In jede Kugel mit einem Kochlöffelstiel eine Mulde drücken und mit Fruchtaufstrich füllen. Wer mag, setzt auch auf ein paar Sterne einen kleinen Tupfen.',
            'Alle Plätzchen auf Blechen mit Backpapier bei 175 °C Ober-/Unterhitze 10–12 Minuten hell backen und auf dem Blech abkühlen lassen.'],
  frage='Welche der 5 Sorten wäre bei euch zuerst weg?', tags='#plätzchen #weihnachtsbäckerei #backen #weihnachten #fitmitkev',
  prompt='A large round white plate piled with five different kinds of small homemade Christmas cookies arranged in five neat groups: pale golden star-shaped butter cookies, star-shaped cookies sprinkled with brown cinnamon, dark brown chocolate heart-shaped cut-out cookies, round cookies coated in white shredded coconut, and round thumbprint cookies with a glossy red jam center. A few cookies lying on the table in front of the plate, a small star-shaped metal cookie cutter beside.'),
 QuarkWoelkchen=dict(key='QuarkWoelkchen', suess=True, hook='Zergehen auf der Zunge:', titel=['QUARK-','WÖLKCHEN'], portion='pro Stück', anzahl=40, vs=70,
  zutaten=[Z('150 g','Dinkelmehl','dinkelmehl','dinkelmehl',150), Z('100 g','Speisestärke','speisestaerke','speisestaerke',100), Z('150 g','Magerquark','magerquark','quark',150),
           Z('70 g','Butter (weich)','butter','butter',70), Z('80 g','Erythrit','erythrit','erythrit',80), Z('1 Stück','Eigelb','eigelb','eigelb',st=1),
           Z('1 TL','Vanilleextrakt','vanilleextrakt','vanille',0)],
  ex=['1 TL Backpulver, 1 Prise Salz'],
  intro='Wölkchen sind die Plätzchen, die auf der Zunge zergehen: weich, zart und weiß bestäubt wie frisch gefallener Schnee. Das Geheimnis ist die Speisestärke im Teig. Bei mir kommt Magerquark dazu, dafür reichen 70 g Butter. Kugeln formen, mit der Gabel andrücken, fertig, ganz ohne Ausstechen. 40 Stück vom Blech: {k} kcal pro Wölkchen statt 70 für die Sorte mit viel Butter!',
  schritte=['Butter, 60 g Erythrit, Eigelb und Vanille cremig rühren, dann den Quark unterrühren. Mehl, Speisestärke, Backpulver und Salz mischen und kurz unterkneten, bis ein weicher Teig entsteht. 30 Minuten kalt stellen.',
            'Mit bemehlten Händen 40 kleine Kugeln formen, mit Abstand auf zwei Bleche mit Backpapier setzen und mit einer Gabel leicht flach drücken.',
            'Bei 170 °C Ober-/Unterhitze 12–14 Minuten backen. Die Wölkchen sollen hell bleiben. Das restliche Erythrit im Mixer zu Puder mahlen und die abgekühlten Wölkchen damit bestäuben.'],
  frage='Wölkchen: pur oder mit einem Klecks Marmelade in der Mitte?', tags='#wölkchen #plätzchen #weihnachtsbäckerei #fitmitkev',
  prompt='A white plate piled high with many small round pale cream-colored soft melt-in-the-mouth cookies, each cookie a slightly flattened ball with fork tine marks pressed on top, thickly dusted with white powdered sugar like snow, a few cookies lying on the table in front of the plate, one cookie broken in half showing the soft tender pale crumb inside, a small metal sieve with powdered sugar beside.'),
 Sonntagsbraten=dict(key='Sonntagsbraten', suess=False, hook='Wie früher bei Oma:', titel=['SONNTAGSBRATEN','MIT ROTKOHL'], portion='pro Portion', anzahl=4, vs=900,
  zutaten=[Z('600 g','Rinderbraten','rinderbraten','rind',600), Z('600 g','Rotkohl (Glas)','rotkohl','rotkohl',600), Z('500 g','Kloßteig (Kühlregal)','kartoffelkloesse','kloesse',500),
           Z('2 Stück','Zwiebeln','zwiebeln','zwiebel',st=2), Z('2 Stück','Karotten','karotten','karotten',150), Z('2 EL','Tomatenmark','tomatenmark','tomatenmark',30),
           Z('500 ml','Rinderbrühe','rinderbruehe','bruehe',0), Z('1 EL','Speisestärke','speisestaerke','speisestaerke',10)],
  ex=['1 EL Öl, 2 Lorbeerblätter, 1 TL Senf', 'Salz, Pfeffer'],
  intro='Sonntags gab es bei Oma Braten, und das ganze Haus hat danach gerochen. So mache ich ihn heute: mageres Rindfleisch, zwei Stunden im Ofen geschmort, bis es fast von allein zerfällt. Die dunkle Soße wird mit dem Schmorgemüse püriert und braucht weder Sahne noch Butter. Dazu Rotkohl und zwei Klöße: {k} kcal und {p} g Eiweiß pro Teller statt 900 im Gasthaus!',
  schritte=['Einen mageren Rinderbraten nehmen, zum Beispiel aus der Keule. Rundum salzen und pfeffern und in einem Bräter im heißen Öl von allen Seiten kräftig anbraten, dann herausnehmen. Zwiebeln und Karotten grob würfeln und im Bräter 3 Minuten anrösten. Das Tomatenmark 1 Minute mitrösten, mit der Brühe ablöschen, Lorbeer und Senf zugeben.',
            'Den Braten wieder einlegen und zugedeckt bei 160 °C Ober-/Unterhitze 2 bis 2,5 Stunden im Ofen schmoren, bis er weich ist. Nach der Hälfte der Zeit wenden.',
            'Aus dem Kloßteig 8 kleine Klöße formen und nach Packungsangabe in siedendem Salzwasser gar ziehen lassen (ca. 20 Minuten). Den Rotkohl erwärmen.',
            'Den Braten herausnehmen und 10 Minuten ruhen lassen. Den Lorbeer entfernen und die Soße mit dem Gemüse fein pürieren. Die Speisestärke in 2 EL kaltem Wasser anrühren, einrühren und kurz aufkochen. Den Braten in Scheiben schneiden und mit Soße, Rotkohl und Klößen servieren.'],
  frage='Sonntagsbraten: mit Klößen oder mit Salzkartoffeln?', tags='#sonntagsbraten #rinderbraten #rotkohl #omasrezepte #fitmitkev',
  prompt='A white dinner plate with three thick slices of tender braised beef roast covered with glossy dark brown gravy, beside the meat a portion of shiny purple braised red cabbage and two round pale yellow German potato dumplings with a little chopped parsley on top. Behind the plate a small white gravy boat filled with dark brown gravy.'),
 Blumenkohlsuppe=dict(key='Blumenkohlsuppe', suess=False, hook='Cremig wie bei Oma:', titel=['BLUMENKOHL-','SUPPE'], portion='pro Portion', anzahl=4, vs=480,
  zutaten=[Z('1 Kopf','Blumenkohl','blumenkohl','blumenkohl',800), Z('300 g','Kartoffeln','kartoffeln','kartoffeln',300), Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1),
           Z('1 l','Gemüsebrühe','gemuesebruehe','bruehe',0), Z('100 ml','Kochsahne (15 %)','kochsahne','kochsahne',100), Z('4 Stück','Geflügelwürstchen','gefluegel_wiener','wiener',200),
           Z('10 g','Butter','butter','butter',10), Z('½ Bund','Petersilie','petersilie','petersilie',0)],
  ex=['Salz, Pfeffer, Muskat'],
  intro='Blumenkohlsuppe wie bei Oma: cremig, mild und mit Würstchen drin, damit alle am Tisch zufrieden sind. Die Kartoffeln machen sie sämig, darum reicht ein Schuss Kochsahne. In 30 Minuten steht der Topf auf dem Tisch: {k} kcal und {p} g Eiweiß pro Teller statt 480 für die Suppe mit viel Sahne und Mettwurst!',
  schritte=['Die Zwiebel fein würfeln und in der Butter glasig dünsten. Den Blumenkohl (ca. 800 g) in Röschen teilen, die Kartoffeln schälen und würfeln. Beides zugeben, mit der Brühe aufgießen und zugedeckt 15–20 Minuten weich kochen.',
            'Eine Kelle Röschen herausnehmen und beiseitestellen. Die Suppe fein pürieren, die Kochsahne einrühren und mit Salz, Pfeffer und Muskat abschmecken.',
            'Die Würstchen in Scheiben schneiden und mit den Röschen in der Suppe 5 Minuten heiß werden lassen. Mit gehackter Petersilie bestreuen.'],
  frage='Blumenkohlsuppe: mit Würstchen oder ganz ohne?', tags='#blumenkohlsuppe #suppe #omasrezepte #abendessen #fitmitkev',
  prompt='A deep white soup bowl standing on a flat white plate, filled with creamy pale ivory cauliflower soup, in the soup several small white cauliflower florets and many round slices of pink sausage, sprinkled with fresh chopped green parsley and a little black pepper, a spoon lying on the plate beside the bowl. On the right side behind the bowl one small whole white cauliflower. The left side of the table is empty.'),
)
for _k,_r in NEU.items(): _r['kurz']=['–','–','–']; _r['exnut']=[]
NEU['DoenerKuchen']['exnut']=[(72,1,5,5)]   # 1 TL Öl + 2 Tomaten
NEU['Sonntagsbraten']['exnut']=[(95,0.5,0.5,10)]   # 1 EL Öl + 1 TL Senf
GLAS=alt('SpekKirschGlas','#spekulatius #kirschen #dessertimglas #weihnachten #fitmitkev', frage='Team Spekulatius-Kirsch oder Team Nutella-Banane?')
R=[NEU['NutellaBanane'], NEU['DoenerKuchen'], NEU['PizzaKartoffeln'], GLAS,     # die 4 „Melly-Rezepte“
   NEU['EinTeig'], NEU['QuarkWoelkchen'], NEU['Sonntagsbraten'], NEU['Blumenkohlsuppe']]   # 4 weitere nach Auswertung der neuen Seiten (Reihenfolge vorläufig)
REZEPT_IM_BEITRAG={'NutellaBanane','SpekKirschGlas'}   # Test: Rezept im Beitragstext statt im 1. Kommentar

if __name__=='__main__':
    for r in R:
        k,p,c,f=macros4(r); assert r['vs']>k and len(r['zutaten'])<=8 and k<=500, r['key']
        txt=r['intro']+' '.join(r['schritte'])+r['frage']
        for w in ('abnehm','esn ','melly','gta','ohne zucker','satt'): assert w not in txt.lower(), (r['key'],w)
        print(f"{r['key']:16s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P {c:3d}K {f:2d}F {r['portion']} × {r['anzahl']} vs {r['vs']}")
    print('ok')
