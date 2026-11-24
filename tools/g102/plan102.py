# G102 – Mittwoch 25.11.2026: Tagesplan aus 6 neuen Rezepten (out/mittwoch_neu_posts.json) und 13 Wiederholern (7-Tage-Regel vom Mi 18.11.).
# WIEDERHOLER-TEST Tag 1 (Kev 23.11.): Feld `bild` je Wiederholer – 'neu' = neues Foto + neue Schreibschrift-Zeile + anderes Emoji (Board G102-…),
#   'alt' = Board und Text unverändert wie beim letzten Lauf. 1. Kommentar und Hashtags bleiben in beiden Gruppen wie beim letzten Lauf.
# Schreibt out/mittwoch_posts.json, out/posting-plan-mittwoch.txt, out/texte-mittwoch.txt.
import json, os
D=os.path.dirname(os.path.abspath(__file__)); REPO=os.environ.get('REPO','/home/claude/fitmitkev-bilder')
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/{}.jpg"
NEU={p['key']:p for p in json.load(open(f"{D}/out/mittwoch_neu_posts.json"))}
def lade(f): return {p['key']:p for p in json.load(open(f"{REPO}/tools/{f}"))}
Q={'g96':lade('g96/mittwoch_posts.json'),'g88':lade('g88/dienstag_posts.json')}
# (Uhrzeit, Schlüssel, Quelle, Board, Hashtags, zuletzt gelaufen: Datum Uhrzeit · Reichweite · × Tagesmedian, bild) – Läufe mit lauf.py gegen Metricool geprüft (FBPO03)
PLAN=[('06:50','KoernerBroetchen','g96','G96-KoernerBroetchen-ohneBox','#körnerbrötchen #brötchen #ohnehefe #fitmitkev','18.11. 06:50 · 6.545 · 0,7-fach','alt'),
      ('07:35','Zimtsterne','g96','G96-Zimtsterne-ohneBox','#zimtsterne #plätzchen #fitmitkev','18.11. 07:30 · 145.602 · 14,7-fach','alt'),
      ('08:20','NudelsalatNacht',None,None,None,'neu',None),      # Verwandter vom Schichtsalat über Nacht (Mo 23.11., 8:20 Uhr, 7,0-fach)
      ('09:00','Gewuerzkuchen','g96','G102-Gewuerzkuchen-ohneBox','#gewürzkuchen #blechkuchen #backen #fitmitkev','18.11. 08:50 · 95.863 · 9,7-fach','neu'),
      ('09:40','DoenerKartoffeln',None,None,None,'neu',None),     # Verwandter der Pizza-Kartoffeln (So 22.11., 4,1-fach) und des Döner-Kuchens (2,1-fach)
      ('10:20','WinterWoelkchen',None,None,None,'neu',None),      # Mitbewerber-Check 24.11.: Winterwölkchen 14,1-fach; gleicher Platz wie Kokos- (Mo) und Eierlikör-Wölkchen (Di)
      ('11:00','KaeseLauchSuppe','g88','G102-KaeseLauchSuppe-ohneBox','#käselauchsuppe #suppe #hackfleisch #fitmitkev','10.11. 11:15 · 10.937 · 1,0-fach','neu'),   # alte Hashtags ohne #food #lecker
      ('11:40','Mutzen','g96','G96-Mutzen-ohneBox','#mutzen #kirmes #ohnefritteuse #fitmitkev','18.11. 11:30 · 146.324 · 14,7-fach','alt'),
      ('12:20','KlossKasseler',None,None,None,'neu',None),        # Kloßteig-Reihe, Idee 5
      ('13:40','GebratenerReis','g96','G96-GebratenerReis-ohneBox','#gebratenerreis #asiatisch #hähnchen #mealprep #fitmitkev','18.11. 12:15 · 9.928 · 1,0-fach','alt'),
      ('14:20','KokosMandelTiramisu','g96','G96-KokosMandelTiramisu-ohneBox','#tiramisu #kokos #dessert #fitmitkev','18.11. 14:30 · 22.568 · 2,3-fach','alt'),
      ('15:00','KlossScheiben',None,None,None,'neu',None),        # Kloßteig-Reihe, Idee 19
      ('15:40','MilchschnitteBowl','g96','G102-MilchschnitteBowl-ohneBox','#milchschnitte #bowl #fitmitkev','18.11. 16:07 · 256.827 · 25,9-fach','neu'),
      ('16:20','GyrosBowl','g96','G102-GyrosBowl-ohneBox','#gyros #bowl #proteinbowl #mealprep #fitmitkev','18.11. 15:15 · 30.225 · 3,0-fach','neu'),
      ('17:00','BlitzKaesekuchen','g96','G102-BlitzKaesekuchen-ohneBox','#käsekuchen #fitmitkev','18.11. 10:10 · 32.131 · 3,2-fach','neu'),   # einziger Wiederholer mit deutlich anderer Uhrzeit (10:20 gehört den Wölkchen)
      ('17:45','KlossLauch',None,None,None,'neu',None),           # Kloßteig-Reihe, Idee 16
      ('18:30','Zupfkuchen','g96','G102-Zupfkuchen-ohneBox','#zupfkuchen #käsekuchen #backen #fitmitkev','18.11. 18:13 · 12.765 · 1,3-fach','neu'),
      ('19:15','Hackbraten','g96','G96-Hackbraten-ohneBox','#hackbraten #omasrezepte #fitmitkev','18.11. 16:45 · 8.800 · 0,9-fach','alt'),
      ('20:45','ZimtschneckenSkyrKuchen','g96','G96-ZimtschneckenSkyrKuchen-ohneBox','#zimtschnecken #skyrkuchen #käsekuchen #backen #fitmitkev','18.11. 20:45 · 28.585 · 2,9-fach','alt')]
FEST={'06:10':'ESN-Rezept Zimt-Grießbrei wie bei Oma, 315 kcal (ohne ESN-Zeile)','13:00':'ESN-Rezept Schoko-Eis aus Hüttenkäse, 195 kcal (ohne ESN-Zeile)','20:15':'Buch-Beitrag „5 Weihnachtsmarkt-Klassiker ohne Fritteuse“'}
# Hashtag-Gruppen: Die Test-Wiederholer behalten die Hashtags ihres letzten Laufs (sonst mischen sich zwei Tests); die freien Plätze füllen auf 9 × A (2–3) / 10 × B (4–5) auf.
GRUPPE_A={2,3,5,6,9,12,13,15,18}
BUCH={'Zimtsterne':'📖 Diese Zimtsterne findest du auch in meinem Rezeptbuch „Weihnachtsbäckerei in leicht“, zusammen mit 35 weiteren Rezepten: https://fitmitkev.de/rezeptbuecher'}
EMO_NEU={'Gewuerzkuchen':('🤗','🥰'),'KaeseLauchSuppe':('😋','🤤'),'MilchschnitteBowl':('🤗','😍'),'GyrosBowl':('🥰','🤗'),'BlitzKaesekuchen':('😍','🤤'),'Zupfkuchen':('😍','😋')}   # (Emoji beim letzten Lauf, Emoji jetzt)
SW=[False,True,False,True,False,True,False,True,False, False,True,False,True,False,True,False,True,False,True]   # zwischen Platz 9 und 10 liegt das feste süße ESN-Rezept um 13:00
posts=[]
for n,(zeit,key,src,bild,tags,zuletzt,test) in enumerate(PLAN,1):
    if src is None:
        q=NEU[key]; text,fc,media,alt,kcal,suess=q['text'],q['fc'],q['media'],q['alt'],q['kcal'],q['suess']; bild=media.split('/')[-1][:-4]; assert test is None
    else:
        q=Q[src][key]; titel=q['text'].partition('\n\n')[0]; fc=q['fc']; assert test in ('neu','alt'), key
        if test=='neu':
            a,b=EMO_NEU[key]; assert titel.count(a)==1 and a!=b, key; titel=titel.replace(a,b); assert bild==f'G102-{key}-ohneBox', key
        else:
            assert q['media'].endswith('/'+bild+'.jpg') and q['text']==titel+'\n\n'+tags, ('ALT muss Board und Text vom letzten Lauf behalten',key)
        text=titel+'\n\n'+tags
        media,alt,kcal,suess=URL.format(bild),q['alt'],q['kcal'],q['suess']
        if key in BUCH: assert fc.endswith('\n\n'+BUCH[key]), key; fc=fc[:-len('\n\n'+BUCH[key])]
        assert '#' not in fc and '📖' not in fc, key
        if key in BUCH: fc=fc+'\n\n'+BUCH[key]
        if test=='alt': assert fc==q['fc'], key
    assert os.path.exists(f"{REPO}/boards/{bild}.jpg"), ('Board fehlt',bild)
    tg=[w for w in text.split() if w.startswith('#')]; nt=len(tg)
    assert tg[-1]=='#fitmitkev' and 2<=nt<=5 and (nt<=3)==(n in GRUPPE_A), (n,key,nt)
    assert bool(suess)==SW[n-1], ('süß/herzhaft',n,key)
    low=(text+fc.replace(BUCH.get(key,''),'')).lower()
    for w in ('esn','abnehm','höflich','rezeptbuch','http','melly','gta','11.11','box „','food','#lecker'): assert w not in low,(key,w)
    assert zeit not in FEST and 'Rezept im 1. Kommentar' in text, key
    posts.append(dict(n=n,key=key,date=f'2026-11-25T{zeit}:00',text=text,fc=fc,media=media,alt=alt,bild=test,board=bild,box=False,kcal=kcal,suess=bool(suess),hashtags=nt,
                      gruppe='A (2–3)' if nt<=3 else 'B (4–5)',neu=src is None,buch=key in BUCH,zuletzt=zuletzt))
assert len(posts)==19 and len({p['date'] for p in posts})==19 and len({p['key'] for p in posts})==19
assert sum(p['gruppe'][0]=='A' for p in posts)==9 and sum(p['suess'] for p in posts)==9 and sum(p['buch'] for p in posts)==1
assert sum(p['bild']=='neu' for p in posts)==6 and sum(p['bild']=='alt' for p in posts)==7 and sum(p['neu'] for p in posts)==6
assert all(p['kcal']<=500 for p in posts)
json.dump(posts,open(f"{D}/out/mittwoch_posts.json","w"),ensure_ascii=False,indent=1)
def art(p): return 'NEU' if p['neu'] else ('TEST neues Foto' if p['bild']=='neu' else 'TEST altes Bild')+' · zuletzt '+p['zuletzt']
alle=[(p['date'][11:16],f"{p['n']:02d} · {'süß ' if p['suess'] else 'herz'} · {p['alt']} · {p['kcal']} kcal · {p['hashtags']} Hashtags · {art(p)}{' · BUCH-ZEILE' if p['buch'] else ''}") for p in posts]
alle+=[(t,f"–– · fest · {x}") for t,x in FEST.items()]
with open(f"{D}/out/posting-plan-mittwoch.txt","w") as fh:
    fh.write("Posting-Plan Mittwoch 25.11.2026 – 22 Beiträge: 19 Rezepte + 2 feste ESN-Rezepte (ohne ESN-Zeile) + Buch-Beitrag 20:15.\n")
    fh.write("6 neue Rezepte (3 davon aus der Kloßteig-Reihe: 12:20 Kasseler mit Sauerkraut, 15:00 gebratene Kloßscheiben, 17:45 Schinken und Lauch überbacken), 13 bewährte (7-Tage-Regel).\n")
    fh.write("WIEDERHOLER-TEST Tag 1: 6 bewährte Rezepte mit NEUEM Foto und neuer Schreibschrift-Zeile, 7 unverändert mit altem Bild. Rezept, Kalorien, 1. Kommentar und Hashtags sind in beiden Gruppen wie beim letzten Lauf.\n")
    fh.write("Alle Boards ohne Box. Ein Werbe-Beitrag (Buch, 20:15), eine Buch-Zeile (07:35 Zimtsterne, wie am 18.11.).\nHinter jedem Wiederholer: letzter Lauf · Reichweite · Vielfaches des Tagesmittels.\n\n")
    for t,x in sorted(alle): fh.write(f"{t} · {x}\n")
with open(f"{D}/out/texte-mittwoch.txt","w") as fh:
    for p in posts:
        fh.write(f"===== {p['n']:02d} · {p['date'][11:16]} · {p['alt']}{'  ·  NEU' if p['neu'] else ('  ·  TEST neues Foto' if p['bild']=='neu' else '  ·  TEST altes Bild')}\n\nBEITRAG:\n{p['text']}\n\n1. KOMMENTAR:\n{p['fc']}\n\nBILD: {p['media']}\n\n\n")
print(open(f"{D}/out/posting-plan-mittwoch.txt").read())
