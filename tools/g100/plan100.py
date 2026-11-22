# -*- coding: utf-8 -*-
# G100 – Montag 23.11.2026: Tagesplan aus 4 neuen Rezepten (out/montag_neu_posts.json) und 16 Wiederholern (7-Tage-Regel).
# Schreibt out/montag_posts.json, out/posting-plan-montag.txt, out/texte-montag.txt.
import json, os
D=os.path.dirname(os.path.abspath(__file__)); REPO=os.environ.get('REPO','/home/claude/fitmitkev-bilder')
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/{}.jpg"
NEU={p['key']:p for p in json.load(open(f"{D}/out/montag_neu_posts.json"))}
def lade(f): return {p['key']:p for p in json.load(open(f"{REPO}/tools/{f}"))}
Q={'g94':lade('g94/montag_posts.json'),'g93':lade('g93/sonntag_posts.json'),'g91':lade('g91/freitag_posts.json'),'g88':lade('g88/dienstag_posts.json'),
   'g92':lade('g92/samstag_posts.json'),'g89':lade('g89/mittwoch_posts.json')}
# (Uhrzeit, Schlüssel, Quelle, Board, Hashtags, zuletzt gelaufen: Datum · Reichweite · × Tagesmedian)
PLAN=[('06:50','Quarkbroetchen','g94','G94-Quarkbroetchen-ohneBox','#quarkbrötchen #ohnehefe #fitmitkev','16.11. · 24.390 · 1,6-fach'),
      ('07:35','Nussecken','g94','G94-Nussecken-ohneBox','#nussecken #backen #fitmitkev','16.11. · 23.717 · 1,6-fach'),
      ('08:20','Schichtsalat',None,None,None,'neu'),
      ('09:00','Zitronenkuchen','g94','G94-Zitronenkuchen-ohneBox','#zitronenkuchen #fitmitkev','16.11. · 109.058 · 7,3-fach'),
      ('09:40','CheeseburgerAuflauf','g94','G94-CheeseburgerAuflauf-ohneBox','#cheeseburger #auflauf #familienessen #fitmitkev','16.11. · 13.762 · 0,9-fach (9.11. 2,5-fach)'),
      ('10:20','KokosWoelkchen',None,None,None,'neu'),
      ('11:00','HackNudeln',None,None,None,'neu'),
      ('11:40','ZimtBowl','g93','G93-ZimtBowl-ohneBox','#zimtschnecken #bowl #fitmitkev','16.11. · 17.801 · 1,2-fach (15.11. 2,8-fach)'),
      ('12:20','Frikassee',None,None,None,'neu'),   # Kev 22.11., 15:49: „Rinder Rouladen bitte raus – dafür Knödel mit Hühnerfrikassee rein“
      ('13:40','PizzaWrap',None,None,None,'neu'),
      ('14:20','MandarinenBowl','g94','G94-MandarinenBowl-ohneBox-neu','#käsekuchen #mandarinen #bowl #omasrezepte #fitmitkev','16.11. · 44.817 · 3,0-fach'),
      ('15:00','KlossPaprika',None,None,None,'neu'),   # Kloßteig-Reihe (Kev 22.11., 16:06); vorher Champignons mit Knoblauchsoße (13.11. · 7.331 · 0,8-fach)   # statt Käse-Lauch-Suppe: deren altes Board (G88) hat eine trübe Schüssel unter der Zutatenspalte und Brot im Bild
      ('15:40','Rumkugeln','g92','G92-Rumkugeln-ohneBox','#rumkugeln #weihnachten #fitmitkev','14.11. · 34.136 · 3,1-fach'),
      ('16:20','Souvlaki','g91','G91-Souvlaki-ohneBox','#souvlaki #griechisch #hähnchen #tzatziki #fitmitkev','13.11. · 7.962 · 0,9-fach'),
      ('17:00','Waffeln','g93','G93-Waffeln-ohneBox','#waffeln #wiebeioma #backen #fitmitkev','16.11. · 18.865 · 1,3-fach'),
      ('17:45','KlossGulasch',None,None,None,'neu'),   # Kloßteig-Reihe; vorher Rindergulasch mit Kartoffeln (13.11. · 9.129 · 1,0-fach) – sonst zwei Gulasch am selben Tag
      ('18:30','Spritzgebaeck','g93','G93-Spritzgebaeck-ohneBox','#spritzgebäck #plätzchen #fitmitkev','16.11. · 15.968 · 1,1-fach'),
      ('19:15','KlossTomMozz',None,None,None,'neu'),   # Kloßteig-Reihe; vorher Senfeier (10.11. · 10.434 · 0,9-fach)
      ('20:45','Plaetzchen','g91','G91-Plaetzchen-ohneBox','#plätzchen #weihnachtsbäckerei #backen #fitmitkev','13.11. · 16.758 · 1,8-fach')]
# Kev 22.11., 10:20 per Dialog: „Ja go“ und „Buch-Beitrag täglich weiter“ → 20:15 gehört dem Buch-Beitrag, Flammkuchen (0,7-fach) entfällt, Ausstech-Plätzchen rücken auf 20:45.
FEST={'06:10':'ESN-Rezept Zimtschnecken-Overnight-Oats (ohne ESN-Zeile)','13:00':'ESN-Rezept Schokopudding (ohne ESN-Zeile)','20:15':'Buch-Beitrag (neu, wird Kev vorher gezeigt)'}
GRUPPE_A={1,2,4,8,9,12,13,17,18}          # 2–3 Hashtags; übrige 4–5
BUCH={'Plaetzchen':'📖 Diese Plätzchen findest du auch in meinem Rezeptbuch „Weihnachtsbäckerei in leicht“, zusammen mit 35 weiteren Rezepten: https://fitmitkev.de/rezeptbuecher'}
SW=[False,True,False,True,False,True,False,True,False, False,True,False,True,False,True,False,True,False,True]   # zwischen Platz 9 und 10 liegt das feste süße ESN-Rezept um 13:00
posts=[]
for n,(zeit,key,src,bild,tags,zuletzt) in enumerate(PLAN,1):
    if src is None:
        q=NEU[key]; text,fc,media,alt,kcal,suess=q['text'],q['fc'],q['media'],q['alt'],q['kcal'],q['suess']; bild=media.split('/')[-1][:-4]
    else:
        q=Q[src][key]; titel=q['text'].partition('\n\n')[0]; text=titel+'\n\n'+tags; fc=q['fc']
        media,alt,kcal,suess=URL.format(bild),q['alt'],q['kcal'],q['suess']
        assert '#' not in fc and '📖' not in fc, key
        if key in BUCH: fc=fc+'\n\n'+BUCH[key]
    tg=[w for w in text.split() if w.startswith('#')]; nt=len(tg)
    assert tg[-1]=='#fitmitkev' and 2<=nt<=5 and (nt<=3)==(n in GRUPPE_A), (n,key,nt)
    assert bool(suess)==SW[n-1], ('süß/herzhaft',n,key)
    low=(text+fc.replace(BUCH.get(key,''),'')).lower()
    for w in ('esn','abnehm','höflich','rezeptbuch','http','melly','gta','16.11','box „','food','#lecker'): assert w not in low,(key,w)
    assert zeit not in FEST and 'Rezept im 1. Kommentar' in text, key
    posts.append(dict(n=n,key=key,date=f'2026-11-23T{zeit}:00',text=text,fc=fc,media=media,alt=alt,bild=bild,box=False,kcal=kcal,suess=bool(suess),hashtags=nt,
                      gruppe='A (2–3)' if nt<=3 else 'B (4–5)',neu=src is None,buch=key in BUCH,zuletzt=zuletzt))
assert len(posts)==19 and len({p['date'] for p in posts})==19 and len({p['key'] for p in posts})==19
assert sum(p['gruppe'][0]=='A' for p in posts)==9 and sum(p['suess'] for p in posts)==9 and sum(p['buch'] for p in posts)==1
assert all(p['kcal']<=500 for p in posts)
json.dump(posts,open(f"{D}/out/montag_posts.json","w"),ensure_ascii=False,indent=1)
alle=[(p['date'][11:16],f"{p['n']:02d} · {'süß ' if p['suess'] else 'herz'} · {p['alt']} · {p['kcal']} kcal · {p['hashtags']} Hashtags · {'NEU' if p['neu'] else 'zuletzt '+p['zuletzt']}{' · BUCH-ZEILE' if p['buch'] else ''}") for p in posts]
alle+=[(t,f"–– · fest · {x}") for t,x in FEST.items()]
with open(f"{D}/out/posting-plan-montag.txt","w") as fh:
    fh.write("Posting-Plan Montag 23.11.2026 – 22 Beiträge: 19 Rezepte + 2 feste ESN-Rezepte (schon eingeplant, ohne ESN-Zeile) + Buch-Beitrag 20:15.\n")
    fh.write("8 neue Rezepte (4 davon aus der Kloßteig-Reihe: 12:20, 15:00, 17:45, 19:15), 11 bewährte (7-Tage-Regel). Alle Boards ohne Box. Ein Werbe-Beitrag (Buch, 20:15), eine Buch-Zeile (20:45 Ausstech-Plätzchen).\nHinter jedem Wiederholer: letzter Lauf · Reichweite · Vielfaches des Tagesmittels.\n\n")
    for t,x in sorted(alle): fh.write(f"{t} · {x}\n")
with open(f"{D}/out/texte-montag.txt","w") as fh:
    for p in posts:
        fh.write(f"===== {p['n']:02d} · {p['date'][11:16]} · {p['alt']}{'  ·  NEU' if p['neu'] else ''}\n\nBEITRAG:\n{p['text']}\n\n1. KOMMENTAR:\n{p['fc']}\n\nBILD: {p['media']}\n\n\n")
print(open(f"{D}/out/posting-plan-montag.txt").read())
