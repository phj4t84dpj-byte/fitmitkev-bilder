# -*- coding: utf-8 -*-
# G97 – Donnerstag 19.11.2026 (ESN-Start), Stufenplan 23 Beiträge: 20 Rezepte + 2 ESN-Rezepte (6:10, 13:00, schon eingeplant) + 17:30 persönlicher Beitrag (offen).
# Auswahl nach der 7-Tage-Regel: Donnerstag 12.11. (G90) genau 7 Tage später (ohne Schokomousse/Tiramisu-Skyr-Kuchen – am selben Tag laufen
#   ESN-Schoko-Mousse und ESN-Tiramisu-Bowl) + ausgeruhte Treffer vom 9./10.11. (Nussecken-Bowl 152k, Schwarzwälder, Bienenstich, Bratapfel-Skyr, Senfeier, Käse-Lauch-Suppe).
# Alle ohne Box (Kev 16.11.). 1 Buch-Zeile (Kokosmakronen → Weihnachtsbäckerei), keine ESN-Zeile in diesen 20.
# Hashtag-Gruppen gegenüber Mittwoch getauscht: A (2–3) = 1,2,5,6,9,11,14,15,17,18 · B (4–5) = übrige (je 5 süß / 5 herzhaft).
import sys, os, copy
_D=os.path.dirname(os.path.abspath(__file__))
for g in ('g87','g88','g89','g90','g91','g92','g93','g93n','g94','g95'): sys.path.insert(0, os.path.join(_D, '..', g))
from g90_data import NUT, PIECE, nut, Z, macros4
import g87_data, g88_data, g90_data
_A={}
for m in (g87_data, g88_data, g90_data):
    for r in m.R: _A[r['key']]=r
def alt(key, tags, **kw):
    r=copy.deepcopy(_A[key]); r['tags']=tags; r['kurz']=r.get('kurz') or ['–','–','–']
    for x in ('fb','hinweis','n','buch'): r.pop(x,None)
    r.update(kw); return r
BUCH='📖 Diese Kokosmakronen findest du auch in meinem Rezeptbuch „Weihnachtsbäckerei in leicht“, zusammen mit 35 weiteren Rezepten: https://fitmitkev.de/rezeptbuecher'
_mw=_A['MaulwurfBowl']['intro'].replace('Euer Wunsch aus den Kommentaren: Maulwurfkuchen','Maulwurfkuchen')
R=[
 alt('Fruehstuecksbroetchen','#brötchen #ohnehefe #fitmitkev'),                       # 1 A herz
 alt('ZimtschneckenOats','#overnightoats #zimtschnecken #fitmitkev'),                 # 2 A süß
 alt('StrammerMax','#strammermax #spiegelei #brotzeit #fitmitkev'),                   # 3 B herz
 alt('NusseckenBowl','#nussecken #bowl #backen #lecker #fitmitkev'),                  # 4 B süß
 alt('Senfeier','#senfeier #fitmitkev'),                                              # 5 A herz
 alt('Engelsaugen','#engelsaugen #plätzchen #fitmitkev'),                             # 6 A süß
 alt('KaeseLauchSuppe','#käselauchsuppe #suppe #omasrezepte #fitmitkev'),             # 7 B herz
 alt('SpekKaeseBowl','#spekulatius #käsekuchen #bowl #fitmitkev'),                    # 8 B süß
 alt('Lasagne','#lasagne #auflauf #fitmitkev'),                                       # 9 A herz
 alt('CordonBleu','#cordonbleu #hähnchen #ausdemofen #fitmitkev'),                    # 10 B herz
 alt('Kokosmakronen','#kokosmakronen #plätzchen #fitmitkev', hinweis=BUCH),           # 11 A süß
 alt('SchinkenLauchQuiche','#quiche #herzhaftbacken #schinken #lauch #fitmitkev'),    # 12 B herz
 alt('ZimtstreuselSkyr','#skyrkuchen #zimtstreusel #backen #fitmitkev'),              # 13 B süß
 alt('GnocchiAuflauf','#gnocchi #auflauf #fitmitkev'),                                # 14 A herz
 alt('SchwarzwaelderSkyr','#schwarzwälderkirsch #fitmitkev'),                         # 15 A süß
 alt('MaulwurfBowl','#maulwurfkuchen #bowl #backen #fitmitkev', hook='Nur für dich:', intro=_mw),   # 16 B süß
 alt('CheeseburgerLasagne','#cheeseburger #lasagne #fitmitkev'),                      # 17 A herz
 alt('MohnStreuselkuchen','#mohnkuchen #streuselkuchen #fitmitkev'),                  # 18 A süß (statt Bienenstich-Bowl: verzierter Löffel im Bild)
 alt('Kaesespaetzle','#käsespätzle #hütte #omasrezepte #fitmitkev'),                  # 19 B herz
 alt('BratapfelSkyrKuchen','#skyrkuchen #bratapfel #backen #lecker #fitmitkev'),      # 20 B süß
]
ZEITEN=['06:50','07:30','08:15','08:55','09:35','10:15','10:55','11:40','12:20',
        '13:40','14:15','14:55','15:35','16:15','16:50',
        '18:10','18:50','19:25','20:05','20:45']
FEST={'06:10':'ESN Schoko-Mousse (eingeplant)','13:00':'ESN Tiramisu-Bowl (eingeplant)','17:30':'persönlicher Beitrag „Was ich an einem Tag esse“ (offen)'}
GRUPPE_A={1,2,5,6,9,11,14,15,17,18}
HASHTAG_SOLL={i+1:len(r['tags'].split()) for i,r in enumerate(R)}
OHNE_BOX=set(range(1,21))
VORHANDEN=set()
if __name__=='__main__':
    assert len(R)==20 and len({r['key'] for r in R})==20 and len(ZEITEN)==20
    SW=[False,True,False,True,False,True,False,True,False,False,True,False,True,False,True,True,False,True,False,True]
    for i,r in enumerate(R,1):
        k,p,c,f=macros4(r); nt=len(r['tags'].split())
        assert (nt<=3)==(i in GRUPPE_A) and (2<=nt<=5), (i,r['key'],nt)
        assert r['tags'].split()[-1]=='#fitmitkev'
        assert r['suess']==SW[i-1], ('süß/herzhaft',i,r['key'])
        assert r['vs']>k and len(r['zutaten'])<=8, r['key']
        txt=r['intro']+' '.join(r['schritte'])+r.get('hinweis','')
        for w in ('abnehm','martin','wunsch','11.11','donnerstag','esn'): assert w not in txt.lower(), (r['key'],w)
        print(f"{i:2d} {ZEITEN[i-1]} {r['key']:22s} {'süß ' if r['suess'] else 'herz'} {k:4d} kcal {p:3d}P {r['portion']:14s} vs {r['vs']} {nt}#{'  BUCH' if r.get('hinweis') else ''}")
    ga=[r for i,r in enumerate(R,1) if i in GRUPPE_A]; assert sum(r['suess'] for r in ga)==5
    print('ok')
