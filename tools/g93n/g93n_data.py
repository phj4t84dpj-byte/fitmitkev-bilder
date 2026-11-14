# -*- coding: utf-8 -*-
# G93N – Sonntag 15.11.2026: 6 neue Rezepte ersetzen 6 Plätze von G93 (Kev 14.11., 21:54 + Dialog: „Die Rezepte von morgen soweit es geht
#   austauschen und die Rezepte von morgen dann auf Montag packen“; Markennamen: „Marke im Titel“ – Kev über das Abmahn-Risiko informiert).
# Vorbild: Kevs Screenshots einer anderen Seite (Dessert im Glas, Big-Mac-Salat im Glas) + Süßigkeiten-Bowls Hanuta, Lotus Biscoff, Milchschnitte.
# Eigene Rezepte im Fitmitkev-Look, keine Kopien. Plätze (Sonntags-Raster): 9 12:20 · 10 13:05 · 11 13:50 · 15 16:55 · 17 18:25 · 19 20:00.
# Box-Test wie im G93-Muster für diese Plätze: OHNE Box 9, 11, 17 · MIT Box 10, 15, 19 -> Sonntag bleibt 10/10.
# Hashtags nach G93-HASHTAG_SOLL für dieselben Plätze.
import sys, os
_D=os.path.dirname(os.path.abspath(__file__))
for g in ('g87','g88','g89','g90','g91','g92','g93','g94'): sys.path.insert(0, os.path.join(_D, '..', g))
from g90_data import NUT, PIECE, nut, Z, macros4
from g89_data import BOWL
import g91_data, g92_data, g93_data, g94_data
NUT.update({
 'haselnussmus':(650,15,8,62),
 'haselnusswaffeln':(520,6,62,27),          # Haselnuss-Waffelschnitten aus dem Supermarkt, typische Werte je 100 g
 'karamellkekscreme':(584,2.9,57,38),       # Karamellkeks-Creme (Biscoff-Aufstrich), Packungswerte je 100 g
 'eisbergsalat':(14,1,2,0.2),
 'sauerkirschen_glas':(70,0.7,16,0.3),      # Sauerkirschen im Glas, abgetropft (leicht gezuckert)
})
PIECE.update({'karamellkeks':(7.8,(38,0.4,5.7,1.5))})   # 1 Lotus-Karamellkeks = 7,8 g

GLAS_HINWEIS=''
R = [
# 9 · 12:20 · süß · Hanuta-Bowl · ohne Box · 3 #
dict(n=9, key='HanutaBowl', suess=True, hook='Nur für dich:', titel=['HANUTA-','BOWL'], portion='die ganze Bowl', anzahl=1, vs=600,
 zutaten=[Z('150 g','Skyr','skyr','skyr',150), Z('1 Stück','Ei','ei','ei',st=1), Z('15 g','Haselnussmus','haselnussmus','haselnussmus',15),
          Z('8 g','Backkakao','backkakao','kakao',8), Z('15 g','Erythrit','erythrit','erythrit',15), Z('15 g','Dinkelmehl','dinkelmehl','dinkelmehl',15),
          Z('15 g','Haselnuss-Waffeln','haselnusswaffeln','haselnusswaffeln',15)],
 ex=['1 Prise Salz'],
 intro='Schmeckt wie Hanuta, nur als warme Bowl für dich allein: saftiger Schoko-Haselnuss-Kuchen aus Skyr, obendrauf knusprige Haselnuss-Waffeln. Fünf Minuten rühren, 20 Minuten backen: {k} kcal und {p} g Eiweiß die ganze Bowl statt 600 für fünf Hanuta!',
 schritte=['Skyr, Ei, Haselnussmus, Kakao, Erythrit, Mehl und eine Prise Salz glatt rühren und in eine gefettete Glasform (15 × 10 cm) füllen.',
           'Bei 180 °C Ober-/Unterhitze 20 Minuten backen, die Mitte darf noch leicht weich sein. 5 Minuten abkühlen lassen.',
           'Die Haselnuss-Waffeln grob zerbröseln und obendrauf streuen. Warm oder kalt löffeln.'],
 kurz=['Skyr, Ei, Haselnussmus, Kakao, Erythrit und Mehl glatt rühren.',
       'In die Glasform (15 × 10 cm) füllen und bei 180 °C 20 Min. backen.',
       '5 Min. abkühlen lassen, Haselnuss-Waffeln zerbröseln und obendrauf streuen.'],
 frage='Hanuta: Was war deine liebste Süßigkeit in der Schulpause?', tags='#hanuta #bowl #fitmitkev',
 prompt=BOWL+'Inside: a baked moist dark chocolate hazelnut cake with a smooth dark brown top, generously covered with coarsely crumbled thin crispy golden wafer pieces with light brown hazelnut cream between the thin wafer layers, the moist dark chocolate crumb visible through the glass and where it was eaten, two small rectangular golden hazelnut wafer bars and a few whole hazelnuts lying beside the dish.'),
# 10 · 13:05 · herzhaft · Big-Mac-Salat im Glas · mit Box · 3 #
dict(n=10, key='BigMacSalat', suess=False, hook='Zum Mitnehmen:', titel=['BIG-MAC-SALAT','IM GLAS'], portion='pro Glas', anzahl=2, vs=500,
 zutaten=[Z('250 g','Rinderhack (5 %)','rinderhack','hack',250), Z('150 g','Eisbergsalat','eisbergsalat','eisbergsalat',150), Z('3 Stück','Gewürzgurken','gewuerzgurken','gurken',90),
          Z('1 Stück','Zwiebel','zwiebel','zwiebel',st=1), Z('40 g','Cheddar light','cheddar_light','reibekaese',40), Z('100 g','Skyr','skyr','skyr',100),
          Z('1 EL','Ketchup','ketchup','ketchup',15), Z('1 TL','Senf','senf','senf',5)],
 ex=['1 TL Öl','2 EL Gurkenwasser','Salz, Pfeffer, Paprikapulver, Knoblauchpulver'],
 intro='Alles, was einen Big Mac ausmacht, geschichtet im Glas: würziges Hack, Gurken, Zwiebeln, Cheddar, knackiger Eisbergsalat und die typische Burgersoße, hier aus Skyr. Hält sich im Kühlschrank bis zum nächsten Mittag: {k} kcal und {p} g Eiweiß pro Glas statt über 500 für einen Big Mac!',
 schritte=['Das Hack im heißen Öl krümelig braten, mit Salz, Pfeffer und Paprikapulver würzen und abkühlen lassen. Die Zwiebel fein würfeln, 2 Gewürzgurken in Scheiben schneiden, den Salat in feine Streifen.',
           'Für die Soße Skyr, Ketchup, Senf, Gurkenwasser, Knoblauchpulver und die dritte, fein gehackte Gewürzgurke verrühren.',
           'In 2 Gläser schichten: die Hälfte der Soße, Hack, Zwiebeln und Gurkenscheiben, Cheddar, Eisbergsalat, obendrauf die restliche Soße und ein paar Gurkenscheiben.'],
 kurz=['Hack im Öl krümelig braten, würzen und abkühlen lassen.',
       'Soße: Skyr, Ketchup, Senf, Gurkenwasser und 1 gehackte Gewürzgurke verrühren.',
       'In 2 Gläser schichten: Soße, Hack, Zwiebeln, Gurken, Cheddar, Salat, Soße.'],
 frage='Big Mac: mit oder ohne Gurke?', tags='#bigmac #salatimglas #fitmitkev',
 prompt='Two tall clear drinking glasses seen from the side at eye level, one in front and one behind, each filled with neat clearly visible horizontal layers from bottom to top: pale pink creamy burger sauce, browned crumbly minced beef, finely diced white onions and green pickle slices, shredded orange cheddar cheese, shredded crisp light green iceberg lettuce, topped with a dollop of pale pink burger sauce and two green pickle slices, a fork beside, a small glass bowl with pickle slices beside.'),
# 11 · 13:50 · süß · Spekulatius-Kirsch im Glas · ohne Box · 5 #
dict(n=11, key='SpekKirschGlas', suess=True, hook='Dessert im Glas:', titel=['SPEKULATIUS-','KIRSCH'], portion='pro Glas', anzahl=2, vs=450,
 zutaten=[Z('400 g','Skyr','skyr','skyr',400), Z('250 g','Sauerkirschen (Glas)','sauerkirschen','sauerkirschen_glas',250), Z('6 Stück','Spekulatius','spekulatius','spekulatius',st=6),
          Z('20 g','Erythrit','erythrit','erythrit',20), Z('5 g','Speisestärke','speisestaerke','speisestaerke',5), Z('1 TL','Vanilleextrakt','vanilleextrakt','vanille',0),
          Z('1 Prise','Zimt','zimt','zimt',0)],
 ex=[],
 intro='Spekulatius trifft Sauerkirsche, geschichtet im Glas: unten Spekulatius-Brösel, dazwischen Vanille-Skyr und warme Kirschen, obendrauf ein ganzer Spekulatius. Ohne Backen in 15 Minuten fertig: {k} kcal und {p} g Eiweiß pro Glas statt 450 für einen Kirschbecher mit Sahne!',
 schritte=['Die Kirschen abtropfen lassen, 50 ml Saft auffangen und mit der Stärke verrühren. Mit den Kirschen kurz aufkochen, bis die Soße andickt, und abkühlen lassen.',
           'Skyr, Erythrit, Vanille und eine Prise Zimt glatt rühren. 4 Spekulatius fein zerbröseln.',
           'In 2 Gläser schichten: Spekulatius-Brösel, Skyr-Creme, Kirschen, wieder Creme und Kirschen. Mit je einem Spekulatius garnieren.'],
 kurz=['Kirschen mit 50 ml Saft und Stärke kurz aufkochen und abkühlen lassen.',
       'Skyr, Erythrit, Vanille und Zimt glatt rühren, 4 Spekulatius zerbröseln.',
       'In 2 Gläser schichten: Brösel, Creme, Kirschen, Creme, Kirschen, je 1 Spekulatius.'],
 frage='Spekulatius: lieber mit Kirschen oder mit Apfel?', tags='#spekulatius #kirschen #dessertimglas #weihnachten #fitmitkev',
 prompt='Two clear glass tumblers seen from the side at eye level, one in front and one behind, each with a thin layer of brown spiced biscuit crumbs at the bottom, above it thick white vanilla cream with dark red sour cherries and glossy deep red cherry sauce swirled through it, clearly visible through the glass, topped with whole dark red sour cherries in glossy sauce, one thin flat rectangular brown spiced biscuit with an embossed windmill pattern (German Spekulatius) stuck upright into the top of each glass, a spoon beside, a few cherries on the table.'),
# 15 · 16:55 · süß · Lotus-Biscoff-Bowl · mit Box · 4 #
dict(n=15, key='BiscoffBowl', suess=True, hook='Nur für dich:', titel=['LOTUS-BISCOFF-','BOWL'], portion='die ganze Bowl', anzahl=1, vs=600,
 zutaten=[Z('150 g','Skyr','skyr','skyr',150), Z('1 Stück','Ei','ei','ei',st=1), Z('15 g','Erythrit','erythrit','erythrit',15),
          Z('20 g','Dinkelmehl','dinkelmehl','dinkelmehl',20), Z('½ TL','Zimt','zimt','zimt',0), Z('2 Stück','Karamellkekse','karamellkekse','karamellkeks',st=2),
          Z('15 g','Karamellkeks-Creme','spekulatiuscreme','karamellkekscreme',15)],
 ex=[],
 intro='Schmeckt wie Lotus Biscoff, nur als warme Bowl für dich allein: cremiger Skyr-Kuchen mit Zimt, obendrauf geschmolzene Karamellkeks-Creme und Keksbrösel. Fünf Minuten rühren, 20 Minuten backen: {k} kcal und {p} g Eiweiß die ganze Bowl statt 600 für ein Stück Biscoff-Cheesecake im Café!',
 schritte=['Skyr, Ei, Erythrit, Mehl und Zimt glatt rühren, einen Karamellkeks hineinbröseln und alles in eine gefettete Glasform (15 × 10 cm) füllen.',
           'Bei 180 °C Ober-/Unterhitze 20 Minuten backen und 5 Minuten abkühlen lassen.',
           'Die Karamellkeks-Creme 10 Sekunden in der Mikrowelle flüssig machen, über die Bowl ziehen und den zweiten Keks darüberbröseln.'],
 kurz=['Skyr, Ei, Erythrit, Mehl und Zimt glatt rühren, 1 Karamellkeks hineinbröseln.',
       'In die Glasform (15 × 10 cm) füllen und bei 180 °C 20 Min. backen.',
       'Keks-Creme kurz erwärmen, darüberziehen, zweiten Keks darüberbröseln.'],
 frage='Karamellkekse: zum Kaffee oder pur?', tags='#lotus #biscoff #bowl #fitmitkev',
 prompt=BOWL+'Inside: a baked creamy pale golden skyr cake, the top covered with a glossy smooth layer of light caramel brown spiced cookie butter spread, sprinkled with crumbled caramelized biscuit crumbs, the creamy pale crumb visible through the glass and where it was eaten, two plain smooth rectangular caramel brown caramelized biscuits with wavy edges lying beside the dish.'),
# 17 · 18:25 · süß · Bratapfel-Spekulatius im Glas (Grundrezept aus „Weihnachtsbäckerei in leicht“, dort mit Mandeln) · ohne Box · 3 #
dict(n=17, key='BratapfelSpekGlas', suess=True, hook='Dessert im Glas:', titel=['BRATAPFEL-','SPEKULATIUS'], portion='pro Glas', anzahl=4, vs=380,
 zutaten=[Z('3 Stück','Äpfel','aepfel','apfel',st=3), Z('30 g','Rosinen','rosinen','rosinen',30), Z('1 TL','Zimt','zimt','zimt',0),
          Z('400 g','Skyr','skyr','skyr',400), Z('20 g','Vanillepudding-Pulver','vanillepudding_pulver','puddingpulver',20), Z('30 g','Erythrit','erythrit','erythrit',30),
          Z('8 Stück','Spekulatius','spekulatius','spekulatius',st=8)],
 ex=['3 EL Wasser'],
 intro='Bratapfel aus dem Topf mit Zimt und Rosinen, dazu Vanille-Skyr-Creme und Spekulatius, geschichtet im Glas. Schmeckt wie Weihnachten und ist ohne Backofen in 20 Minuten fertig: {k} kcal und {p} g Eiweiß pro Glas statt 380 für einen Bratapfel mit Vanillesoße!',
 schritte=['Die Äpfel schälen, würfeln und mit Rosinen, Zimt und 3 EL Wasser 8 Minuten weich dünsten. Abkühlen lassen.',
           'Skyr, Puddingpulver und Erythrit glatt rühren. 4 Spekulatius fein zerbröseln.',
           'In 4 Gläser schichten: Spekulatius-Brösel, Creme, Bratapfel, wieder Creme und Bratapfel. Mit je einem Spekulatius garnieren.'],
 kurz=['Äpfel würfeln, mit Rosinen, Zimt und 3 EL Wasser 8 Min. dünsten, abkühlen lassen.',
       'Skyr, Puddingpulver und Erythrit glatt rühren, 4 Spekulatius zerbröseln.',
       'In 4 Gläser schichten: Brösel, Creme, Apfel, Creme, Apfel, je 1 Spekulatius.'],
 frage='Bratapfel: mit oder ohne Rosinen?', tags='#bratapfel #dessertimglas #fitmitkev',
 buch='📖 Die Grundversion mit gerösteten Mandeln findest du in meinem Rezeptbuch „Weihnachtsbäckerei in leicht“, zusammen mit 35 weiteren Rezepten: https://fitmitkev.de/rezeptbuecher',
 prompt='Four clear glass tumblers seen from the side at eye level, one in front and three behind, each with a thin layer of brown spiced biscuit crumbs at the bottom, above it thick white vanilla cream layered with soft golden cinnamon apple cubes and a few raisins, the layers clearly visible through the glass, topped with soft golden cinnamon dusted apple cubes and raisins, one thin flat rectangular brown spiced biscuit with an embossed windmill pattern (German Spekulatius) stuck upright into the top of each glass, a red apple and a cinnamon stick beside, a spoon beside.'),
# 19 · 20:00 · süß · Milchschnitte-Bowl · mit Box · 5 #
dict(n=19, key='MilchschnitteBowl', suess=True, hook='Nur für dich:', titel=['MILCHSCHNITTE-','BOWL'], portion='die ganze Bowl', anzahl=1, vs=470,
 zutaten=[Z('1 Stück','Ei','ei','ei',st=1), Z('10 g','Backkakao','backkakao','kakao',10), Z('15 g','Dinkelmehl','dinkelmehl','dinkelmehl',15),
          Z('10 g','Erythrit','erythrit','erythrit',10), Z('130 g','Skyr','skyr','skyr',130), Z('30 g','Frischkäse light','frischkaese_light','frischkaese',30),
          Z('10 g','Honig','honig','honig',10)],
 ex=['½ TL Backpulver','etwas Vanille'],
 intro='Schmeckt wie Milchschnitte, nur als Bowl für dich allein: unten saftiger Schoko-Biskuit, oben kühle Milchcreme mit einem Hauch Honig. 12 Minuten backen, kurz kalt stellen, fertig: {k} kcal und {p} g Eiweiß die ganze Bowl statt 470 für vier Milchschnitten!',
 schritte=['Ei, Kakao, Mehl, Erythrit, 30 g Skyr und das Backpulver glatt rühren, in eine gefettete Glasform (15 × 10 cm) füllen und bei 180 °C Ober-/Unterhitze 12 Minuten backen.',
           'Den Schoko-Biskuit vollständig abkühlen lassen.',
           'Die restlichen 100 g Skyr mit Frischkäse, Honig und Vanille cremig rühren, auf den Biskuit streichen, mit etwas Kakao bestäuben und 30 Minuten kalt stellen.'],
 kurz=['Ei, Kakao, Mehl, Erythrit, 30 g Skyr und Backpulver glatt rühren.',
       'In die Glasform (15 × 10 cm), bei 180 °C 12 Min. backen, abkühlen lassen.',
       '100 g Skyr, Frischkäse und Honig cremig rühren, draufstreichen, 30 Min. kalt stellen.'],
 frage='Milchschnitte: Kennst du sie noch aus der Brotdose?', tags='#milchschnitte #bowl #dessert #schokolade #fitmitkev',
 prompt=BOWL+'Inside: a thin layer of moist dark chocolate sponge cake at the bottom and a thick layer of smooth white milk cream on top, the top lightly dusted with cocoa powder, the dark brown sponge and the white cream layer clearly visible through the glass and where it was eaten, a small glass jar of golden honey beside the dish.'),
]
EXN={'BigMacSalat':(45,0,0,5)}   # 1 TL Öl
for r in R: r['exnut']=[EXN[r['key']]] if r['key'] in EXN else []
HASHTAG_SOLL=g93_data.HASHTAG_SOLL
OHNE_BOX={9,11,17}

if __name__=='__main__':
    for r in R:
        i=r['n']; k,p,c,f=macros4(r); nt=len(r['tags'].split())
        assert nt==HASHTAG_SOLL[i], (i,r['key'],nt)
        assert r['tags'].split()[-1]=='#fitmitkev'
        assert r['suess']==(i%2==1), ('süß/herzhaft-Wechsel',i)
        assert r['vs']>k and len(r['zutaten'])<=8 and len(r['schritte'])==3 and len(r['kurz'])==3, r['key']
        assert all(len(s)<=100 for s in r['kurz']), (r['key'],[len(s) for s in r['kurz']])
        assert r['suess'] or k<=500
        assert 'abnehm' not in (r['intro']+' '.join(r['schritte'])+' '.join(r['kurz'])).lower()
        print(f"{i:2d} {r['key']:20s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P {c:3d}C {f:3d}F  {r['portion']:15s} vs {r['vs']}  {len(r['zutaten'])} Kacheln  {nt} #  kurz {max(len(s) for s in r['kurz'])}  {'ohne Box' if i in OHNE_BOX else 'mit Box'}")
    import json
    TL=os.path.join(_D,'..','tilex','tiles_orig'); MAP=json.load(open(TL+'/_map_g87.json'))
    fehlt=sorted({z['tile'] for r in R for z in r['zutaten'] if not os.path.exists(f"{TL}/{MAP.get(z['tile'],z['tile'])}.png")}); print('Kacheln fehlen:',fehlt)
