# -*- coding: utf-8 -*-
# G98 – Samstag 21.11.2026. Kev 20.11. per Dialog: „Heller Look, 4 Fast-Food-Klassiker“ und „22 wie bisher“.
# 22 Beiträge am Tag = 16 Rezepte (diese Datei) + feste Beiträge, die schon eingeplant sind:
#   06:10 ESN-Rezept Vanillepudding mit Zimtpflaumen · 09:00 ESN „So schmecken die Designer Bars“ Teil 1 · 11:00 ESN K1 ·
#   13:00 ESN-Rezept Schoko-Kugeln · 18:30 ESN Designer Bars Teil 2 · 20:15 Buch-Beitrag „5 Plätzchen unter 75 kcal“.
# Auswahl (Reichweite ÷ Tagesmedian, Stand 16.11.):
#   7-Tage-Regel Samstag 14.11. (G92): Rotweinkuchen 23,1 · Vanillekipferl 3,3 · Pizza Hawaii 3,0 · Rumkugeln 2,4 · Curry 1,7 · Schinken-Käse-Nudeln 1,4 ·
#     Reispfanne 1,1 · Süß-sauer 0,9 · Cevapcici 0,8.  Raus: Pastitsio, Hörnchen, Zwiebelkuchen, Lava-Cookies (0,4–0,5), Kartoffelsalat 0,7.
#   Ausgeruht seit Freitag 13.11. (G91, 8 Tage): Marmorkuchen-Bowl 5,4 · Milchreis 3,7 · Reibekuchen 1,1.
#   4 Fast-Food-Klassiker neu im hellen Look (GTA-Tag 19.11.: süßes Fast Food lief am besten – Donuts 54,6k, Erdbeer-Milchshake 48,6k):
#     Schoko-Milchshake, Churros aus dem Ofen, Crispy-Chicken-Burger, Ofen-Tacos. Nichts, was seit 14.11. schon lief
#     (Currywurst-Auflauf und Nuggets liefen Di 17.11., Cheeseburger/Hot Dog/Nachos/Döner/Donuts/Erdbeer-Shake Do 19.11.).
# 7 süß / 9 herzhaft: mit den zwei süßen ESN-Rezepten sind es am Tag 9 : 9, nie zwei süße Rezepte hintereinander.
# Alle ohne Box (Kev 16.11.). Keine Buch-Zeile (die zwei Werbe-Zeilen des Tages stehen unter den ESN-Rezepten), keine ESN-Zeile in diesen 16.
# Hashtag-Gruppen: A (2–3) = 3,4,7,8,12,13,15,16 · B (4–5) = 1,2,5,6,9,10,11,14. Die drei Besten vom 14.11. behalten ihre Hashtags (Rotweinkuchen 4, Vanillekipferl 2, Pizza Hawaii 2).
import sys, os, copy
_D=os.path.dirname(os.path.abspath(__file__))
for g in ('g87','g88','g89','g90','g91','g92'): sys.path.insert(0, os.path.join(_D, '..', g))
from g90_data import NUT, PIECE, nut, Z, macros4
import g91_data, g92_data
_A={}
for m in (g91_data, g92_data):
    for r in m.R: _A[r['key']]=r
def alt(key, tags, **kw):
    r=copy.deepcopy(_A[key]); r['tags']=tags; r['kurz']=r.get('kurz') or ['–','–','–']
    for x in ('fb','hinweis','n','buch','vorhanden'): r.pop(x,None)
    r.update(kw); return r
for _k,_v in {'eisbergsalat':(14,1,2,0.2), 'tortilla':(300,9,50,7)}.items(): NUT.setdefault(_k,_v)   # bestehende Werte nicht überschreiben

NEU=dict(
 CrispyBurger=dict(key='CrispyBurger', suess=False, hook='Wie vom Drive-in:', titel=['CRISPY-CHICKEN-','BURGER'], portion='pro Burger', anzahl=4, vs=650,
  zutaten=[Z('4 Stück','Burger-Brötchen','broetchen','broetchen',240), Z('400 g','Hähnchenbrust','haehnchenbrust','haehnchen',400),
           Z('60 g','Cornflakes (ungesüßt)','cornflakes','cornflakes',60), Z('1 Stück','Ei','ei','ei',st=1),
           Z('80 g','Skyr','skyr','skyr',80), Z('2 EL','Ketchup','ketchup','ketchup',30), Z('2 TL','Senf','senf','senf',10),
           Z('80 g','Eisbergsalat','eisbergsalat','eisbergsalat',80)],
  ex=['1 Tomate, Salz, Pfeffer, 1 TL Paprikapulver'],
  intro='Der Crispy-Chicken-Burger vom Drive-in, nur aus dem Ofen statt aus der Fritteuse: Hähnchenbrust in knuspriger Cornflakes-Panade, dazu Salat, Tomate und eine Burgersoße aus Skyr, Ketchup und Senf im getoasteten Brötchen. In 30 Minuten fertig: {k} kcal und {p} g Eiweiß pro Burger statt 650 für den vom Drive-in!',
  schritte=['Die Hähnchenbrust waagerecht in 4 flache Schnitzel schneiden und mit Salz, Pfeffer und Paprikapulver würzen. Die Cornflakes in einem Gefrierbeutel fein zerdrücken.',
            'Die Schnitzel erst im verquirlten Ei, dann in den Cornflakes wenden und auf ein Backblech mit Backpapier legen. Bei 200 °C Ober-/Unterhitze 18–20 Minuten knusprig backen und nach der Hälfte wenden.',
            'Skyr mit Ketchup und Senf verrühren. Die Brötchen aufschneiden, kurz toasten und mit Soße, Salat, Tomatenscheiben und Hähnchen belegen.'],
  frage='Burger: lieber mit Hähnchen oder mit Rind?', tags='#crispychicken #burger #hähnchen #fitmitkev',
  prompt='Two homemade crispy chicken burgers on a wooden board: toasted sesame burger buns, in each a thick golden brown crunchy cornflake-crusted chicken breast fillet, crisp green iceberg lettuce, a red tomato slice and creamy pale pink burger sauce, one burger cut in half and turned to the camera showing the juicy white chicken inside the crunchy golden crust, a small white bowl of pale pink sauce beside.'),
 OfenTacos=dict(key='OfenTacos', suess=False, hook='Einfach in die Mitte stellen:', titel=['OFEN-TACOS','MIT HACK'], portion='pro Portion', anzahl=4, vs=700,
  zutaten=[Z('8 Stück','Mini-Tortillas','tortilla','tortilla',240), Z('400 g','Rinderhack (mager)','rinderhack','hack',400), Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1),
           Z('200 g','Passierte Tomaten','passierte_tomaten','tomaten',200), Z('140 g','Mais (Dose)','mais','mais',140),
           Z('80 g','Reibekäse light','reibekaese_light','reibekaese',80), Z('150 g','Skyr','skyr','skyr',150), Z('80 g','Eisbergsalat','eisbergsalat','eisbergsalat',80)],
  ex=['Salz, Pfeffer, 1 TL Paprikapulver, ½ TL Kreuzkümmel'],
  intro='Tacos aus dem Ofen: weiche Tortillas, gefüllt mit würzigem Hack, Mais und Käse, alle zusammen in einer Form gebacken, bis die Ränder knusprig sind. Obendrauf Salat und ein Klecks Skyr. Einfach in die Mitte stellen und alle greifen zu: {k} kcal und {p} g Eiweiß für 2 Tacos statt 700 für die Tacos vom Mexikaner!',
  schritte=['Die Zwiebel fein würfeln und mit dem Hack in einer beschichteten Pfanne krümelig braten. Passierte Tomaten und Mais zugeben, mit Salz, Pfeffer, Paprikapulver und Kreuzkümmel würzen und 5 Minuten einkochen.',
            'Die Tortillas (je ca. 15 cm) in der Mitte falten, aufrecht nebeneinander in eine Auflaufform (20 × 30 cm) stellen, mit der Hackmasse füllen und mit dem Käse bestreuen.',
            'Bei 200 °C Ober-/Unterhitze 10–12 Minuten backen, bis die Ränder knusprig sind. Mit Salatstreifen und je einem Klecks Skyr servieren.'],
  frage='Tacos: mit Hack oder mit Hähnchen?', tags='#tacos #hackfleisch #familienessen #fitmitkev',
  prompt='A rectangular white ceramic baking dish with eight small soft flour tortillas folded into taco shape, standing upright side by side in a row, baked until the edges are golden and crispy, each taco filled with browned ground beef in a little tomato sauce, yellow sweet corn and golden melted cheese, topped with shredded green iceberg lettuce and a small spoonful of white yogurt cream, two tacos served on a white plate in front.'),
 SchokoShake=dict(key='SchokoShake', suess=True, hook='Wie im Diner:', titel=['SCHOKO-','MILCHSHAKE'], portion='pro Glas', anzahl=2, vs=500,
  zutaten=[Z('1 Stück','Banane (gefroren)','banane','banane',st=1), Z('300 g','Skyr','skyr','skyr',300), Z('300 ml','Milch (1,5 %)','milch','milch',300),
           Z('20 g','Backkakao','backkakao','kakao',20), Z('20 g','Erythrit','erythrit','erythrit',20),
           Z('10 g','Zartbitterschokolade','zartbitterschokolade','schokolade',10), Z('1 TL','Vanilleextrakt','vanilleextrakt','vanille',0)],
  ex=[],
  intro='Ein dicker Schoko-Milchshake wie im amerikanischen Diner, nur ohne Eis und ohne Sahne: Die gefrorene Banane macht ihn so cremig, dass du beides nicht vermisst. Alles in den Mixer, 1 Minute, fertig: {k} kcal und {p} g Eiweiß pro Glas statt 500 für den Schoko-Shake mit Eis und Sahne!',
  schritte=['Die Banane schälen, in Scheiben schneiden und mindestens 2 Stunden einfrieren (am besten schon am Vortag).',
            'Gefrorene Banane, Skyr, Milch, Backkakao, Erythrit und Vanille im Mixer 1 Minute dick und cremig pürieren.',
            'In 2 große Gläser füllen, die Schokolade darüber raspeln und sofort servieren.'],
  frage='Milchshake: Schoko, Vanille oder Erdbeere?', tags='#milchshake #schoko #fitmitkev',
  prompt='Two tall classic milkshake glasses filled to the top with thick creamy chocolate brown milkshake with a light foamy surface, sprinkled with fine dark chocolate shavings and a little cocoa powder, a paper straw in each glass, a few pieces of dark chocolate and one whole banana lying beside the glasses.'),
 Churros=dict(key='Churros', suess=True, hook='Wie von der Kirmes:', titel=['CHURROS','AUS DEM OFEN'], portion='pro Portion', anzahl=4, vs=500,
  zutaten=[Z('120 g','Dinkelmehl','dinkelmehl','dinkelmehl',120), Z('200 ml','Milch (1,5 %)','milch','milch',200), Z('40 g','Butter','butter','butter',40),
           Z('2 Stück','Eier','eier','ei',st=2), Z('20 g','Erythrit','erythrit','erythrit',20), Z('1 TL','Zimt','zimt','zimt',0),
           Z('40 g','Zartbitterschokolade','zartbitterschokolade','schokolade',40)],
  ex=['100 ml Wasser, 1 Prise Salz'],
  intro='Churros wie von der Kirmes, nur aus dem Ofen statt aus dem heißen Fett: außen knusprig, innen weich, in Zimt gewälzt und in warme Schokosoße getunkt. Der Teig kommt ganz ohne Zucker aus und ist in 10 Minuten gerührt. 5 Churros mit Soße: {k} kcal und {p} g Eiweiß pro Portion statt 500 für die Tüte von der Kirmes!',
  schritte=['150 ml Milch, 100 ml Wasser, 30 g Butter und eine Prise Salz aufkochen. Das Mehl auf einmal zugeben und kräftig rühren, bis sich der Teig als Kloß vom Topfboden löst. 5 Minuten abkühlen lassen, dann die Eier einzeln unterrühren.',
            'Den Teig in einen Spritzbeutel mit Sterntülle füllen, 20 Stangen (je 10 cm) auf ein Backblech mit Backpapier spritzen und bei 200 °C Ober-/Unterhitze 20–22 Minuten goldbraun backen.',
            'Die heißen Churros dünn mit 10 g geschmolzener Butter bepinseln und in Erythrit und Zimt wälzen. Die Schokolade mit 50 ml Milch schmelzen und als Soße dazu reichen.'],
  frage='Churros: mit Schokosoße oder nur mit Zimt?', tags='#churros #kirmes #backen #fitmitkev',
  prompt='A pile of homemade golden brown baked churros on brown baking paper on a wooden board: straight pastry sticks about ten centimeters long, piped through a star nozzle, each with deep parallel ridges running along its whole length, coated in fine cinnamon sugar, a small white bowl of glossy dark chocolate dipping sauce beside, one churro standing in the bowl dipped halfway into the chocolate sauce.'),
)
for _k,_r in NEU.items(): _r['kurz']=['–','–','–']; _r['exnut']=[]

R=[
 alt('Reibekuchen','#reibekuchen #kartoffelpuffer #weihnachtsmarkt #fitmitkev'),              # 1 B herz  06:50
 alt('Milchreis','#milchreis #wieoma #frühstück #fitmitkev'),                                 # 2 B süß   07:35
 alt('Reispfanne','#reispfanne #fitmitkev'),                                                  # 3 A herz  08:20
 alt('Vanillekipferl','#vanillekipferl #fitmitkev'),                                          # 4 A süß   09:40  (wie 14.11.)
 NEU['CrispyBurger'],                                                                         # 5 B herz  10:20  Fast Food
 alt('MarmorBowl','#marmorkuchen #bowl #wieoma #fitmitkev'),                                  # 6 B süß   11:40
 alt('PizzaHawaii','#pizzahawaii #fitmitkev'),                                                # 7 A herz  12:20  (wie 14.11.)
 alt('Curry','#hähnchencurry #curry #fitmitkev'),                                             # 8 A herz  13:40
 NEU['Churros'],                                                                              # 9 B süß   14:20  Fast Food
 NEU['OfenTacos'],                                                                            # 10 B herz 15:00  Fast Food
 alt('Rotweinkuchen','#rotweinkuchen #kastenkuchen #backen #fitmitkev'),                      # 11 B süß  15:40  (wie 14.11.: 15:25, 4 Hashtags)
 alt('KaeseNudeln','#schinkenkäsenudeln #onepot #fitmitkev'),                                 # 12 A herz 16:20
 NEU['SchokoShake'],                                                                          # 13 A süß  17:00  Fast Food
 alt('SuessSauer','#süßsauer #hähnchen #asiatisch #fitmitkev'),                               # 14 B herz 17:45
 alt('Cevapcici','#cevapcici #balkan #fitmitkev'),                                            # 15 A herz 19:15
 alt('Rumkugeln','#rumkugeln #weihnachten #fitmitkev'),                                       # 16 A süß  20:45
]
ZEITEN=['06:50','07:35','08:20','09:40','10:20','11:40','12:20','13:40','14:20','15:00','15:40','16:20','17:00','17:45','19:15','20:45']
FEST={'06:10':'ESN-Rezept Vanillepudding mit Zimtpflaumen','09:00':'ESN Designer Bars Teil 1','11:00':'ESN K1','13:00':'ESN-Rezept Schoko-Kugeln',
      '18:30':'ESN Designer Bars Teil 2','20:15':'Buch-Beitrag „5 Plätzchen unter 75 kcal“'}
GRUPPE_A={3,4,7,8,12,13,15,16}
HASHTAG_SOLL={i+1:len(r['tags'].split()) for i,r in enumerate(R)}
OHNE_BOX=set(range(1,17))
FASTFOOD={'CrispyBurger','OfenTacos','SchokoShake','Churros'}

if __name__=='__main__':
    assert len(R)==16 and len({r['key'] for r in R})==16 and len(ZEITEN)==16 and not set(ZEITEN)&set(FEST)
    SW=[False,True,False,True,False,True,False,False,True,False,True,False,True,False,False,True]
    for i,r in enumerate(R,1):
        k,p,c,f=macros4(r); nt=len(r['tags'].split())
        assert (nt<=3)==(i in GRUPPE_A) and (2<=nt<=5), (i,r['key'],nt)
        assert r['tags'].split()[-1]=='#fitmitkev'
        assert r['suess']==SW[i-1], ('süß/herzhaft',i,r['key'])
        assert r['vs']>k and len(r['zutaten'])<=8 and k<=500, r['key']
        txt=r['intro']+' '.join(r['schritte'])+r.get('hinweis','')+r['frage']
        for w in ('abnehm','martin','euer wunsch','community','14.11','13.11','samstag','freitag','esn','gta','box'): assert w not in txt.lower(), (r['key'],w)
        print(f"{i:2d} {ZEITEN[i-1]} {r['key']:15s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P {c:3d}K {f:2d}F {r['portion']:14s} vs {r['vs']} {nt}# {'A' if i in GRUPPE_A else 'B'}{'  FAST FOOD' if r['key'] in FASTFOOD else ''}")
    print('ok')
