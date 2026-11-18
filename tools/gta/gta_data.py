# -*- coding: utf-8 -*-
# GTA VI erscheint am Do 19.11.2026 – Kev 18.11., 22:03: „Erstell mir 2-3 GTA VI Facebook Rezepte, ich möchte die Reichweite des Themas mitnehmen“.
# 3 Themen-Rezepte (GTA 6 spielt in Leonida = Florida-Vorbild, Vice City = Miami): Key-Lime-Pie-Bowl (süß), Cuban Sandwich (herzhaft), Ofen-Nachos (Zocker-Snack).
# Keine Logos, keine Figuren, keine Spielszenen im Bild – „GTA 6“ nur im Schriftzug/Text. Hook-Test: 3 verschiedene GTA-Hooks.
import sys, os
_D=os.path.dirname(os.path.abspath(__file__))
for g in ('g87','g88','g89','g90'): sys.path.insert(0, os.path.join(_D, '..', g))
from g90_data import NUT, PIECE, nut, Z, macros4
NUT.update({'butterkekse':(435,7,73,12), 'tortilla':(300,9,50,7)})
R=[
 dict(key='KeyLimeBowl', suess=True, hook='Zum GTA-6-Start:', titel=['KEY-LIME-PIE-','BOWL'], portion='die ganze Bowl', anzahl=1, vs=800,
  zutaten=[Z('4 Stück','Butterkekse','butterkekse','butterkekse',33), Z('250 g','Skyr','skyr','skyr',250), Z('1 Stück','Ei','ei','ei',st=1),
           Z('15 g','Vanillepudding-Pulver','vanillepudding_pulver','puddingpulver',15), Z('20 g','Erythrit','erythrit','erythrit',20),
           Z('1 Stück','Limette (Saft und Abrieb)','limette','zitrone',30)],
  ex=[],
  intro='Key Lime Pie ist der Kuchen aus Florida, dem Vorbild für die Welt von GTA 6: frisch, cremig und ein bisschen sauer. Bei mir als Bowl nur für dich, mit Skyr statt gezuckerter Kondensmilch: {k} kcal und {p} g Eiweiß die ganze Bowl statt 800 für zwei Stücke Key Lime Pie!',
  schritte=['Die Butterkekse fein zerbröseln und in eine kleine gefettete Glasform (15 × 10 cm) drücken.',
            '200 g Skyr, Ei, Puddingpulver, Erythrit, den Limettensaft und die Hälfte vom Abrieb glatt rühren, auf den Keksboden füllen und bei 170 °C Ober-/Unterhitze 22 Minuten backen.',
            'Abkühlen lassen, 1 Stunde kalt stellen, die restlichen 50 g Skyr als Haube daraufgeben und mit dem restlichen Limettenabrieb bestreuen.'],
  frage='Spielt bei euch heute jemand GTA 6?', tags='#gta6 #keylimepie #fitmitkev'),
 dict(key='Cubano', suess=False, hook='Für den GTA-Abend:', titel=['KUBANISCHES','SANDWICH'], portion='pro Stück', anzahl=2, vs=650,
  zutaten=[Z('2 Stück','Ciabatta-Brötchen','broetchen','broetchen',160), Z('60 g','Kochschinken','kochschinken','kochschinken',60),
           Z('60 g','Putenschinken','putenschinken','putenschinken',60), Z('2 Scheiben','Käse light','kaese_light','kaesescheiben',40),
           Z('2 Stück','Gewürzgurken','gewuerzgurken','gurken',60), Z('2 TL','Senf','senf','senf',10), Z('1 TL','Öl','oel','oel',5)],
  ex=[],
  intro='Das Cuban Sandwich kommt aus Miami, der Stadt, die in GTA 6 als Vice City zu sehen ist: Schinken, Käse, Gewürzgurken und Senf in einem knusprig gepressten Brötchen. Ich nehme Kochschinken und Putenschinken statt fettem Schweinebraten und drücke es in der Pfanne mit einem Topf flach: {k} kcal und {p} g Eiweiß pro Sandwich statt 650 für das Sandwich aus dem Diner!',
  schritte=['Die Brötchen aufschneiden und innen dünn mit Senf bestreichen. Die Gewürzgurken in dünne Scheiben schneiden.',
            'Die Unterseiten mit Kochschinken, Putenschinken, Gurkenscheiben und Käse belegen und die Deckel daraufsetzen.',
            'Eine Pfanne mit dem Öl erhitzen, die Sandwiches hineinlegen und mit einem schweren Topf flach drücken. Von jeder Seite 3–4 Minuten goldbraun rösten, bis der Käse schmilzt, und diagonal halbieren.'],
  frage='Zocken oder lieber Serie: Was läuft bei euch heute Abend?', tags='#gta6 #sandwich #miami #abendessen #fitmitkev'),
 dict(key='OfenNachos', suess=False, hook='Wenn heute alle GTA zocken:', titel=['OFEN-','NACHOS'], portion='pro Portion', anzahl=4, vs=700,
  zutaten=[Z('4 Stück','Vollkorn-Tortillas','tortilla','tortilla',240), Z('300 g','Rinderhack (mager)','rinderhack','hack',300),
           Z('1 Stück','Rote Paprika','rote_paprika','paprika_st',st=1), Z('140 g','Mais (Dose)','mais','mais',140),
           Z('80 g','Reibekäse light','reibekaese_light','reibekaese',80), Z('200 g','Passierte Tomaten','passierte_tomaten','tomaten',200),
           Z('200 g','Skyr','skyr','skyr',200)],
  ex=['Salz, Pfeffer, 1 TL Paprikapulver, ½ TL Kreuzkümmel, Schnittlauch'],
  intro='Heute erscheint GTA 6, und bei vielen wird bis spät in die Nacht gezockt. Statt Chipstüte gibt es Nachos vom Blech: Tortilla-Ecken knusprig gebacken, darauf Hack, Paprika, Mais und Käse, dazu Salsa und ein Skyr-Dip. {k} kcal und {p} g Eiweiß pro Portion statt 700 für Nachos mit Käsesoße!',
  schritte=['Die Tortillas in je 8 Dreiecke schneiden, auf einem Backblech mit Backpapier verteilen und bei 200 °C Ober-/Unterhitze 6–8 Minuten knusprig backen.',
            'Das Hack in einer beschichteten Pfanne krümelig braten, Paprikawürfel und Mais 3 Minuten mitbraten und mit Salz, Pfeffer, Paprikapulver und Kreuzkümmel würzen.',
            'Die Hack-Mischung über die Chips verteilen, mit Käse bestreuen und 5 Minuten überbacken. Passierte Tomaten mit Salz und Pfeffer als Salsa und Skyr mit Salz, Pfeffer und Schnittlauch als Dip dazu reichen.'],
  frage='Nachos: mit Salsa oder mit Dip?', tags='#gta6 #nachos #fitmitkev'),
]
for _r in R: _r['kurz']=['–','–','–']; _r['exnut']=[]
NAME={'KeyLimeBowl':'Key-Lime-Pie-Bowl nur für dich','Cubano':'Kubanisches Sandwich wie in Miami','OfenNachos':'Ofen-Nachos für den Zocker-Abend'}
FORM={'KeyLimeBowl':'1 Portion, Glasform 15 × 10 cm','Cubano':'2 Sandwiches','OfenNachos':'4 Portionen, Backblech'}
if __name__=='__main__':
    for r in R:
        k,p,c,f=macros4(r); assert r['vs']>k and len(r['zutaten'])<=8
        txt=(r['intro']+' '.join(r['schritte'])).lower(); assert 'abnehm' not in txt and 'esn' not in txt
        print(r['key'],k,'kcal',p,'P',c,'KH',f,'F', r['portion'])
