# -*- coding: utf-8 -*-
# G99 – Sonntag 22.11.2026 (in Arbeit). Stand 20.11.: nur die 3 neuen Rezepte nach dem Muster der Mitbewerberin „Mellys Köstlichkeiten“
#   (Kev 20.11. per Dialog: „Ja, alle 4“ und „Ja, bei 2 testen“ = Rezept direkt im Beitrag bei den 2 Gläsern).
#   Auswertung Melly 6.–20.11.: beste Beiträge = Klassiker zum Löffeln im Glas mit 3–5 Zutaten (Spekulatius-Kirsch 1.071 Reaktionen, Nutella-Banane 657),
#   seit 10.11. umgebautes Fast Food (Döner-Kuchen 147 Reaktionen / 102 geteilt, Pizza-Kartoffeln 75 / 63). Siehe Projekt-Dokument `claude/mitbewerber-analyse.md`.
#   Das vierte „Melly-Rezept“ ist unser Spekulatius-Kirsch-Glas vom So 15.11. (G93N, 5,0 × Tagesmedian) – genau 7 Tage später, gleiches Bild.
#   „Schwarzwälder Kirsch im Glas“ entfällt: am Fr 20.11. 13:00 lief das ESN-Rezept „Schwarzwälder im Glas“, und mehr als 2 Gläser am Tag nutzen das Format ab.
# Der Rest des Sonntags (12 ausgeruhte Treffer, Zeiten, Hashtag-Gruppen) wird am Sa 21.11. früh mit Kev und den Freitagszahlen festgelegt.
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
for _k,_v in {'eisbergsalat':(14,1,2,0.2), 'nussnougatcreme':(540,6,57,31)}.items(): NUT.setdefault(_k,_v)   # bestehende Werte nicht überschreiben

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
  prompt='A rectangular white ceramic baking dish filled with golden brown crispy roasted potato cubes, topped like a pizza: red tomato sauce in the middle, golden browned bubbling melted cheese, round slices of red salami and small red bell pepper cubes, crispy potato cubes without sauce visible around the edge, sprinkled with dried oregano, one portion served on a white plate in front, a fork beside.'),
)
for _k,_r in NEU.items(): _r['kurz']=['–','–','–']; _r['exnut']=[]
NEU['DoenerKuchen']['exnut']=[(72,1,5,5)]   # 1 TL Öl + 2 Tomaten
GLAS=alt('SpekKirschGlas','#spekulatius #kirschen #dessertimglas #weihnachten #fitmitkev', frage='Team Spekulatius-Kirsch oder Team Nutella-Banane?')
R=[NEU['NutellaBanane'], NEU['DoenerKuchen'], NEU['PizzaKartoffeln'], GLAS]     # vorläufig: nur die 4 „Melly-Rezepte“
REZEPT_IM_BEITRAG={'NutellaBanane','SpekKirschGlas'}   # Test: Rezept im Beitragstext statt im 1. Kommentar

if __name__=='__main__':
    for r in R:
        k,p,c,f=macros4(r); assert r['vs']>k and len(r['zutaten'])<=8 and k<=500, r['key']
        txt=r['intro']+' '.join(r['schritte'])+r['frage']
        for w in ('abnehm','esn','melly','gta'): assert w not in txt.lower(), (r['key'],w)
        print(f"{r['key']:16s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P {c:3d}K {f:2d}F {r['portion']} × {r['anzahl']} vs {r['vs']}")
    print('ok')
