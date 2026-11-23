# G101 – Dienstag 24.11.2026: Tagesplan aus 4 neuen Rezepten (out/dienstag_neu_posts.json), dem fertigen Kloß-Board vom 22.11. (Tomate-Mozzarella) und 14 Wiederholern (7-Tage-Regel).
# Schreibt out/dienstag_posts.json, out/posting-plan-dienstag.txt, out/texte-dienstag.txt.
import json, os
D=os.path.dirname(os.path.abspath(__file__)); REPO=os.environ.get('REPO','/home/claude/fitmitkev-bilder')
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/{}.jpg"
NEU={p['key']:p for p in json.load(open(f"{D}/out/dienstag_neu_posts.json"))}
def lade(f): return {p['key']:p for p in json.load(open(f"{REPO}/tools/{f}"))}
Q={'g95':lade('g95/dienstag_neu_posts.json'),'g94':lade('g94/montag_posts.json'),'g93n':lade('g93n/sonntag_neu_posts.json'),'g91':lade('g91/freitag_posts.json'),
   'g90':lade('g90/donnerstag_posts.json'),'g100':lade('g100/montag_neu_posts.json')}
# (Uhrzeit, Schlüssel, Quelle, Board, Hashtags, zuletzt gelaufen: Datum · Reichweite · × Tagesmedian) – Läufe mit lauf.py gegen Metricool geprüft (FBPO03)
PLAN=[('06:50','Laugenbroetchen','g95','G95-Laugenbroetchen-ohneBox','#laugenbrötchen #laugengebäck #brötchen #frühstück #fitmitkev','17.11. · 14.650 · 1,2-fach'),
      ('07:35','KipferlOats','g94','G94-KipferlOats-ohneBox','#overnightoats #vanillekipferl #frühstück #fitmitkev','16.11. · 35.435 · 2,3-fach'),
      ('08:20','BigMacSalat','g93n','G93N-BigMacSalat-ohneBox','#bigmac #salatimglas #fitmitkev','15.11. · 14.287 · 1,0-fach'),
      ('09:00','Quarkbaellchen','g94','G94-Quarkbaellchen-ohneBox','#quarkbällchen #kirmes #ohnefritteuse #backen #fitmitkev','16.11. · 148.467 · 9,7-fach'),
      ('09:40','Doener','g94','G94-Doener-ohneBox','#döner #fladenbrot #fitmitkev','16.11. · 17.288 · 1,1-fach'),
      ('10:20','EierlikoerWoelkchen',None,None,None,'neu'),      # Mitbewerber-Check 23.11.: Winterwölkchen 10,8-fach, Eierlikör-Wölkchen im Anlauf
      ('11:00','Buletten',None,None,None,'neu'),                 # Mitbewerber-Check 22./23.11.: Buletten mit Speck-Kartoffelsalat 5,3-fach
      ('11:40','BrownieBowl','g94','G94-BrownieBowl-ohneBox','#brownie #bowl #schokolade #fitmitkev','17.11. · 38.717 · 3,2-fach'),
      ('12:20','KlossJaeger',None,None,None,'neu'),              # Kloßteig-Reihe, Idee 9
      ('13:40','CordonBleuAuflauf','g94','G94-CordonBleuAuflauf-ohneBox','#cordonbleu #auflauf #fitmitkev','17.11. · 42.473 · 3,5-fach'),
      ('14:20','BenjaminBowl','g95','G95-BenjaminBowl-ohneBox','#erdbeeren #fitmitkev','17.11. · 282.372 · 23,3-fach'),   # gleicher Text wie beim Treffer (2 Hashtags) → Platz 11 (Gruppe A)
      ('15:00','KlossTomMozz','g100','G100-KlossTomMozz-ohneBox','#klöße #tomatemozzarella #überbacken #auflauf #fitmitkev','neu (Board von Kev am 22.11. freigegeben)'),   # Kloßteig-Reihe, Kevs dritter Vorschlag
      ('15:40','SchokoMousse','g90','G90-SchokoMousse','#schokomousse #dessert #schokolade #skyr #fitmitkev','12.11. · 63.806 · 2,2-fach'),
      ('16:20','Nuggets','g95','G95-Nuggets-ohneBox','#chickennuggets #hähnchen #fitmitkev','17.11. · 18.758 · 1,5-fach'),
      ('17:00','Poffertjes','g91','G91-Poffertjes-ohneBox','#poffertjes #weihnachtsmarkt #fitmitkev','13.11. · 15.537 · 1,7-fach'),
      ('17:45','KlossSauerbraten',None,None,None,'neu'),         # Kloßteig-Reihe, Idee 1
      ('18:30','Elisenlebkuchen','g95','G95-Elisenlebkuchen-ohneBox','#lebkuchen #elisenlebkuchen #weihnachtsbäckerei #fitmitkev','17.11. · 16.203 · 1,3-fach'),
      ('19:15','SalamiPizza','g95','G95-SalamiPizza-ohneBox','#pizza #salamipizza #pizzaabend #fitmitkev','17.11. · 19.319 · 1,6-fach'),
      ('20:45','Haferplaetzchen','g94','G94-Haferplaetzchen-ohneBox','#plätzchen #haferflocken #fitmitkev','17.11. · 15.206 · 1,3-fach')]
FEST={'06:10':'ESN-Rezept Tiramisu im Glas, 310 kcal (ohne ESN-Zeile)','13:00':'ESN-Rezept Cheesecake im Glas, 275 kcal (ohne ESN-Zeile)','20:15':'Buch-Beitrag „5 Aufläufe unter 500 kcal“'}
GRUPPE_A={3,5,6,7,10,11,14,15,16,19}      # 2–3 Hashtags; übrige 4–5 (Gegenstück zu Montag: dort {1,2,4,8,9,12,13,17,18})
BUCH={'Elisenlebkuchen':'📖 Diese Elisenlebkuchen findest du auch in meinem Rezeptbuch „Weihnachtsbäckerei in leicht“, zusammen mit 35 weiteren Rezepten: https://fitmitkev.de/rezeptbuecher'}
# ESN-Zeile der Overnight-Oats entfällt: im selben Text steht „macht bis mittags satt“ (keine Sättigungs-Aussage neben ESN-Werbung); Zutat bleibt neutral „Proteinpulver Vanille“.
STREICH={'KipferlOats':'Werbung: Als Proteinpulver nehme ich das Designer Protein von ESN in Vanille.\n\n'}
SW=[False,True,False,True,False,True,False,True,False, False,True,False,True,False,True,False,True,False,True]   # zwischen Platz 9 und 10 liegt das feste süße ESN-Rezept um 13:00
posts=[]
for n,(zeit,key,src,bild,tags,zuletzt) in enumerate(PLAN,1):
    if key is None: assert zeit in FEST; continue      # fester Platz (zählt in der Nummerierung mit, damit Hashtag-Gruppen und süß/herzhaft der übrigen Plätze gleich bleiben)
    if src is None:
        q=NEU[key]; text,fc,media,alt,kcal,suess=q['text'],q['fc'],q['media'],q['alt'],q['kcal'],q['suess']; bild=media.split('/')[-1][:-4]
    else:
        q=Q[src][key]; titel=q['text'].partition('\n\n')[0]; text=titel+'\n\n'+tags; fc=q['fc']
        media,alt,kcal,suess=URL.format(bild),q['alt'],q['kcal'],q['suess']
        if key in STREICH: assert STREICH[key] in fc, key; fc=fc.replace(STREICH[key],'')
        if key in BUCH: fc=fc.replace('\n\n'+BUCH[key],'')      # Buch-Zeile stand schon im Text vom 17.11. – wird unten wieder angehängt
        assert '#' not in fc and '📖' not in fc, key
        if key in BUCH: fc=fc+'\n\n'+BUCH[key]
    tg=[w for w in text.split() if w.startswith('#')]; nt=len(tg)
    assert tg[-1]=='#fitmitkev' and 2<=nt<=5 and (nt<=3)==(n in GRUPPE_A), (n,key,nt)
    assert bool(suess)==SW[n-1], ('süß/herzhaft',n,key)
    low=(text+fc.replace(BUCH.get(key,''),'')).lower()
    for w in ('esn','abnehm','höflich','rezeptbuch','http','melly','gta','16.11','box „','food','#lecker'): assert w not in low,(key,w)
    assert zeit not in FEST and 'Rezept im 1. Kommentar' in text, key
    posts.append(dict(n=n,key=key,date=f'2026-11-24T{zeit}:00',text=text,fc=fc,media=media,alt=alt,bild=bild,box=False,kcal=kcal,suess=bool(suess),hashtags=nt,
                      gruppe='A (2–3)' if nt<=3 else 'B (4–5)',neu=src is None,buch=key in BUCH,zuletzt=zuletzt))
assert len(posts)==19 and len({p['date'] for p in posts})==19 and len({p['key'] for p in posts})==19
assert sum(p['gruppe'][0]=='A' for p in posts)==10 and sum(p['suess'] for p in posts)==9 and sum(p['buch'] for p in posts)==1
assert all(p['kcal']<=500 for p in posts)
json.dump(posts,open(f"{D}/out/dienstag_posts.json","w"),ensure_ascii=False,indent=1)
alle=[(p['date'][11:16],f"{p['n']:02d} · {'süß ' if p['suess'] else 'herz'} · {p['alt']} · {p['kcal']} kcal · {p['hashtags']} Hashtags · {'NEU' if p['neu'] else 'zuletzt '+p['zuletzt']}{' · BUCH-ZEILE' if p['buch'] else ''}") for p in posts]
alle+=[(t,f"–– · fest · {x}") for t,x in FEST.items()]
with open(f"{D}/out/posting-plan-dienstag.txt","w") as fh:
    fh.write("Posting-Plan Dienstag 24.11.2026 – 22 Beiträge: 19 Rezepte + 2 feste ESN-Rezepte (ohne ESN-Zeile) + Buch-Beitrag 20:15.\n")
    fh.write("5 neue Rezepte (3 davon aus der Kloßteig-Reihe: 12:20 Jägerschnitzel, 15:00 Tomate-Mozzarella, 17:45 Sauerbraten), 14 bewährte (7-Tage-Regel). Alle Boards ohne Box. Ein Werbe-Beitrag (Buch, 20:15), eine Buch-Zeile (18:30 Elisenlebkuchen).\nHinter jedem Wiederholer: letzter Lauf · Reichweite · Vielfaches des Tagesmittels.\n\n")
    for t,x in sorted(alle): fh.write(f"{t} · {x}\n")
with open(f"{D}/out/texte-dienstag.txt","w") as fh:
    for p in posts:
        fh.write(f"===== {p['n']:02d} · {p['date'][11:16]} · {p['alt']}{'  ·  NEU' if p['neu'] else ''}\n\nBEITRAG:\n{p['text']}\n\n1. KOMMENTAR:\n{p['fc']}\n\nBILD: {p['media']}\n\n\n")
print(open(f"{D}/out/posting-plan-dienstag.txt").read())
