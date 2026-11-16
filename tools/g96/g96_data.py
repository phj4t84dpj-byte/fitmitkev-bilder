# -*- coding: utf-8 -*-
# G96 – Mittwoch 18.11.2026, 21 Rezepte 6:10–20:45 + Mehrwert MW7 „Proteinpulver ist Chemie?“ 17:30 = 22 Beiträge (Stufenplan Kev 16.11.).
# Kev 16.11. per Dialog: Box-Regel „süß ohne Box, herzhaft mit Box“ · Hashtag-Test weiter (A 2–3 / B 4–5) ·
#   statt Werbepause 1 Buch-Zeile unter einem passenden Rezept (Zimtsterne → Weihnachtsbäckerei), kein Buch-Beitrag, kein ESN.
# Auswahl nach der 7-Tage-Regel: der Mittwoch 11.11. (G89, bester Tag der Vorwoche) genau 7 Tage später + ausgeruhte Treffer vom 9./10.11.
#   (Zitronenkuchen-Bowl 190 k, Gewürzkuchen 159 k, Blitz-Käsekuchen 118 k, Zimtsterne 107 k, Mutzen 70 k, Weckmann 69 k …);
#   neu: Milchschnitte-Bowl (G93N, gebaut für 15.11., lief nie – Platz ging an den Langos-YouTube-Beitrag). Gleiche Rohbilder wie beim ersten Lauf.
# Hashtag-Gruppen gegenüber Dienstag getauscht: A (2–3) = 3,4,7,8,11,12,15,16,19,20 · B (4–5) = 1,2,5,6,9,10,13,14,17,18,21.
import sys, os, copy
_D=os.path.dirname(os.path.abspath(__file__))
for g in ('g87','g88','g89','g90','g91','g92','g93','g93n','g94','g95'): sys.path.insert(0, os.path.join(_D, '..', g))
from g90_data import NUT, PIECE, nut, Z, macros4
import g91_data, g92_data, g93_data, g93n_data, g94_data, g95_data, g87_data, g88_data, g89_data
_A={}
for m in (g87_data, g88_data, g89_data, g93n_data):
    for r in m.R: _A[r['key']]=r
def alt(key, tags, kurz=None, **kw):
    r=copy.deepcopy(_A[key]); r['tags']=tags; r['kurz']=kurz or r.get('kurz') or ['–','–','–']
    r.pop('fb',None); r.pop('hinweis',None); r.pop('n',None); r.pop('buch',None); r.update(kw); return r

BUCH_W='📖 Diese Zimtsterne findest du auch in meinem Rezeptbuch „Weihnachtsbäckerei in leicht“, zusammen mit 35 weiteren Rezepten: https://fitmitkev.de/rezeptbuecher'
_w=_A['Weckmann']['intro']; _s=_w.index('!')+1
R=[
 alt('Weckmann','#weckmann #stutenkerl #backen #ohnehefe #fitmitkev', hook='Wie vom Bäcker:', intro=('Weckmann wie vom Bäcker, im Advent ein Muss!'+_w[_s:]).replace(' fertig für den Laternenumzug',' fertig')),
 alt('KoernerBroetchen','#körnerbrötchen #brötchen #ohnehefe #fitmitkev',
     ['Mehl, Skyr, Ei, Backpulver, Salz, Honig, Leinsamen und halbe Kürbiskerne verkneten.',
      '8 Brötchen formen, mit Wasser bestreichen, in Haferflocken, Sesam und Kernen wälzen.',
      'Aufs Blech mit Backpapier setzen und bei 200 °C 22 Min. goldbraun backen.']),
 alt('Zimtsterne','#zimtsterne #plätzchen #fitmitkev', hinweis=BUCH_W),
 alt('Bauernfruehstueck','#bauernfrühstück #fitmitkev',
     ['Kartoffeln in Scheiben schneiden und im Öl in der Pfanne goldbraun braten.',
      'Zwiebel und Schinken würfeln und 3 Min. mitbraten.',
      'Eier darauf schlagen, würzen und mit Deckel 4–5 Min. stocken lassen.']),
 alt('Gewuerzkuchen','#gewürzkuchen #blechkuchen #backen #fitmitkev'),
 alt('LaugenKnoten','#laugenknoten #laugengebäck #ohnehefe #snack #fitmitkev',
     ['Teig kneten, 8 Stränge (40 cm) rollen, mit Käse füllen, zu Knoten schlingen.',
      '1 l Wasser mit Natron aufkochen, Knoten je 30 Sek. baden, Salz und Sesam drauf.',
      'Bei 200 °C 20 Min. backen, bis die Kruste glänzend braun ist.']),
 alt('BlitzKaesekuchen','#käsekuchen #fitmitkev'),
 alt('PizzaMuffins','#pizzamuffins #snack #fitmitkev',
     ['Skyr, Eier, Oregano, Salz und Pfeffer verrühren, Mehl und Backpulver unterheben.',
      'Salami und Paprika würfeln und mit Mais und halbem Käse unterheben.',
      'In 12 Muffinmulden füllen, Käse drauf, bei 180 °C 22–25 Min. backen.']),
 alt('Mutzen','#mutzen #kirmes #ohnefritteuse #fitmitkev', intro=_A['Mutzen']['intro'].replace(', pünktlich zum 11.11.:',':')),
 alt('GebratenerReis','#gebratenerreis #asiatisch #hähnchen #mealprep #fitmitkev',
     ['Reis kochen und abkühlen lassen. Hähnchen würfeln, scharf anbraten, herausnehmen.',
      'Zwiebel, Knoblauch, Karotten 4 Min. braten, Erbsen und Reis 3 Min. mitbraten.',
      'Eier in der Pfanne stocken lassen, Hähnchen zurück, mit Sojasauce abschmecken.']),
 alt('ZitronenBowl','#zitronenkuchen #bowl #fitmitkev'),
 alt('Schinkennudeln','#schinkennudeln #fitmitkev',
     ['Nudeln bissfest kochen. Zwiebel und Schinken 3 Min. anbraten, Nudeln dazu.',
      'Eier, Milch, Skyr und Gewürze verquirlen, drübergießen, mit Deckel 5 Min. stocken.',
      'Käse drüberstreuen, 2 Min. schmelzen lassen, mit Petersilie bestreuen.']),
 alt('KokosMandelTiramisu','#tiramisu #kokos #dessert #fitmitkev'),
 alt('GyrosBowl','#gyros #bowl #proteinbowl #mealprep #fitmitkev',
     ['Reis kochen und in eine gefettete Glasform (15 × 10 cm) geben.',
      'Hähnchen mit Gyrosgewürz anbraten, Paprika und Zwiebel 4 Min. mitbraten.',
      'Skyr-Tzatziki drüber, Käse drauf und bei 200 °C 12 Min. überbacken.']),
 alt('MilchschnitteBowl','#milchschnitte #bowl #fitmitkev'),
 alt('Hackbraten','#hackbraten #omasrezepte #fitmitkev',
     ['Hack mit Brötchen, Ei, Zwiebel, Senf und Gewürzen verkneten, Laib formen.',
      'Anbraten, Brühe dazu, bei 180 °C 40 Min. garen, Soße mit Stärke binden.',
      'Kartoffeln kochen, mit heißer Milch zu Püree stampfen und dazu servieren.']),
 alt('Zupfkuchen','#zupfkuchen #käsekuchen #backen #fitmitkev'),
 alt('ZuercherGeschnetzeltes','#geschnetzeltes #hähnchen #familienessen #fitmitkev',
     ['Hähnchen in Streifen schneiden, würzen, scharf anbraten und herausnehmen.',
      'Zwiebel und Champignons anbraten, Brühe dazu, binden, Schmand einrühren.',
      'Hähnchen zurück in die Soße, mit Zitrone abschmecken, mit Reis anrichten.']),
 alt('BrownieKaesekuchen','#browniekäsekuchen #fitmitkev'),
 alt('HaehnchenJaegersosse','#jägersoße #hähnchen #fitmitkev',
     ['Hähnchen in Scheiben schneiden, würzen und je Seite 3 Min. anbraten.',
      'Zwiebel, Champignons und Tomatenmark anbraten, Brühe dazu, Schmand einrühren.',
      'Hähnchen zurück in die Soße und mit Nudeln anrichten.']),
 alt('ZimtschneckenSkyrKuchen','#zimtschnecken #skyrkuchen #käsekuchen #backen #fitmitkev'),
]
ZEITEN=['06:10','06:50','07:30','08:10','08:50','09:30','10:10','10:50','11:30','12:15','13:00','13:45','14:30','15:15','16:00','16:45','18:05','18:45','19:25','20:05','20:45']
GRUPPE_A={3,4,7,8,11,12,15,16,19,20}
HASHTAG_SOLL={i+1:len(r['tags'].split()) for i,r in enumerate(R)}
OHNE_BOX=set(range(1,22))   # Kev 16.11., 11:5x: „Lass die Boxen bitte ganz weg“ (vorher: süß ohne, herzhaft mit)
VORHANDEN=set()

if __name__=='__main__':
    assert len(R)==21 and len({r['key'] for r in R})==21 and len(ZEITEN)==21
    for i,r in enumerate(R,1):
        k,p,c,f=macros4(r); nt=len(r['tags'].split())
        assert (nt<=3)==(i in GRUPPE_A) and (2<=nt<=5), (i,r['key'],nt)
        assert r['tags'].split()[-1]=='#fitmitkev'
        assert r['suess']==(i%2==1), ('süß/herzhaft-Wechsel',i)
        assert r['vs']>k and len(r['zutaten'])<=8 and len(r['schritte'])==3 and len(r['kurz'])==3, r['key']
        if not r['suess']: assert all(len(s)<=100 for s in r['kurz']) and '–' not in r['kurz'], (r['key'],[len(s) for s in r['kurz']])
        assert 'abnehm' not in (r['intro']+' '.join(r['schritte'])+' '.join(r['kurz'])+r.get('hinweis','')).lower()
        assert 'martin' not in r['intro'].lower() and 'esn' not in r.get('hinweis','').lower()
        print(f"{i:2d} {ZEITEN[i-1]} {r['key']:24s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P  {r['portion']:15s} vs {r['vs']}  {nt} #  {'ohne Box' if i in OHNE_BOX else 'MIT Box'}{'  BUCH' if r.get('hinweis') else ''}")
    assert sum(1 for r in R if r.get('hinweis'))==1
