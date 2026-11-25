# G103 – Donnerstag 26.11.2026: Tagesplan aus 6 neuen Rezepten (out/donnerstag_neu_posts.json) und 13 Wiederholern (14-Tage-Regel, Kev 24.11.).
# WIEDERHOLER-TEST Tag 2: Feld `bild` je Wiederholer – 'neu' = neues Foto + neue Schreibschrift-Zeile + anderes Emoji (Board G103-…),
#   'alt' = Board vom letzten Lauf unverändert. 1. Kommentar wie beim letzten Lauf. Hashtags wie beim letzten Lauf, nur ohne #lecker/#food/#zuckerfrei
#   und mit #fitmitkev am Ende; drei Läufe vom 9./10.11. hatten noch den Höflich-Titel – der fällt weg (Regel), der Titel wird „kcal … Rezept im 1. Kommentar“.
# Schreibt out/donnerstag_posts.json, out/posting-plan-donnerstag.txt, out/texte-donnerstag.txt.
import json, os
D=os.path.dirname(os.path.abspath(__file__)); REPO=os.environ.get('REPO','/home/claude/fitmitkev-bilder')
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/{}.jpg"
NEU={p['key']:p for p in json.load(open(f"{D}/out/donnerstag_neu_posts.json"))}
def lade(f): return {p['key']:p for p in json.load(open(f"{REPO}/tools/{f}"))}
Q={'g87':lade('g87/montag_posts.json'),'g88':lade('g88/dienstag_posts.json'),'g89':lade('g89/mittwoch_posts.json'),'g90':lade('g90/donnerstag_posts.json')}
# (Uhrzeit, Schlüssel, Quelle, Board, Titel jetzt, Hashtags jetzt, zuletzt gelaufen: Datum Uhrzeit · Reichweite · × Tagesmedian, bild)
PLAN=[('06:50','Fruehstuecksbroetchen','g90','G103-Fruehstuecksbroetchen-ohneBox','165 kcal pro Stück 🤤 Rezept im 1. Kommentar ⤵️','#brötchen #frühstück #ohnehefe #backen #fitmitkev','12.11. 07:10 · 17.498 · 0,6-fach','neu'),
      ('07:35','NusseckenOats','g89','G89-NusseckenOats',None,'#overnightoats #nussecken #fitmitkev','11.11. 06:10 · 9.139 · 0,6-fach','alt'),
      ('08:20','LaugenBrezeln','g88','G88-LaugenBrezeln',None,'#brezeln #laugengebäck #backen #ohnehefe #fitmitkev','10.11. 08:15 · 5.545 · 0,5-fach','alt'),
      ('09:00','Apfeltaschen','g88','G103-Apfeltaschen-ohneBox','190 kcal pro Stück 🥰 Rezept im 1. Kommentar ⤵️','#apfeltaschen #apfel #backen #fitmitkev','10.11. 09:03 · 4.949 · 0,4-fach','neu'),
      ('09:40','StrammerMax','g90','G90-StrammerMax',None,'#strammermax #spiegelei #fitmitkev','12.11. 09:05 · 7.915 · 0,3-fach','alt'),
      ('10:20','ZimtschneckenPancakes','g87','G87-ZimtschneckenPancakes','330 kcal pro Portion 🤗 Rezept im 1. Kommentar ⤵️','#pancakes #zimtschnecken #frühstück #fitmitkev','9.11. 08:02 · 9.699 · 0,3-fach (Höflich-Titel)','alt'),
      ('11:00','LasagneSuppe','g87','G103-LasagneSuppe-ohneBox','480 kcal pro Teller 😍 Rezept im 1. Kommentar ⤵️','#lasagne #suppe #fitmitkev','9.11. 11:03 · 10.345 · 0,3-fach (Höflich-Titel)','neu'),
      ('11:40','Engelsaugen','g90','G90-Engelsaugen',None,'#engelsaugen #plätzchen #fitmitkev','12.11. 08:05 · 15.086 · 0,5-fach','alt'),
      ('12:20','KlossHirsch',None,None,None,None,'neu',None),          # Kloßteig-Reihe, Idee 2
      ('13:40','CordonBleu','g90','G103-CordonBleu-ohneBox','455 kcal pro Portion 🤤 Rezept im 1. Kommentar ⤵️','#cordonbleu #fitmitkev','12.11. 13:03 · 10.830 · 0,4-fach','neu'),
      ('14:20','BratapfelSkyrKuchen','g87','G103-BratapfelSkyrKuchen-ohneBox','145 kcal pro Stück 😋 Rezept im 1. Kommentar ⤵️','#bratapfel #skyrkuchen #backen #fitmitkev','9.11. 14:04 · 18.752 · 0,6-fach (Höflich-Titel)','neu'),
      ('15:00','KlossPilz',None,None,None,None,'neu',None),            # Kloßteig-Reihe, Idee 13
      ('15:40','MandarinenSchmand','g88','G103-MandarinenSchmand-ohneBox','175 kcal pro Stück 😍 Rezept im 1. Kommentar ⤵️','#schmandkuchen #mandarinen #blechkuchen #fitmitkev','10.11. 13:31 · 8.716 · 0,8-fach (Höflich-Titel)','neu'),
      ('16:20','GnocchiAuflauf','g90','G103-GnocchiAuflauf-ohneBox','455 kcal pro Portion 🥰 Rezept im 1. Kommentar ⤵️','#gnocchi #auflauf #fitmitkev','12.11. 16:50 · 15.531 · 0,5-fach','neu'),
      ('17:00','Schneewittchen',None,None,None,None,'neu',None),
      ('17:45','KlossFrikadellen',None,None,None,None,'neu',None),     # Kloßteig-Reihe, Idee 10
      ('18:30','ToastHawaii',None,None,None,None,'neu',None),
      ('19:15','GyrosAuflauf','g89','G89-GyrosAuflauf',None,'#gyros #auflauf #fitmitkev','11.11. 19:16 · 8.087 · 0,6-fach','alt'),
      ('20:45','JapanKaesekuchen',None,None,None,None,'neu',None)]
FEST={'06:10':'ESN-Rezept Schoko-Mousse, 260 kcal (schon eingeplant, Id 434673372)','13:00':'ESN-Rezept Tiramisu-Bowl, 240 kcal (schon eingeplant, Id 434673472)','20:15':'Buch-Beitrag B7 „5 Klassiker unter 500 kcal“ aus der Wohlfühlküche'}
SW=[False,True,False,True,False,True,False,True,False, False,True,False,True,False,True,False,False,False,True]   # zwischen Platz 9 und 10 liegt das feste süße ESN-Rezept um 13:00
posts=[]
for n,(zeit,key,src,bild,titel,tags,zuletzt,test) in enumerate(PLAN,1):
    if src is None:
        q=NEU[key]; text,fc,media,alt,kcal,suess=q['text'],q['fc'],q['media'],q['alt'],q['kcal'],q['suess']; bild=media.split('/')[-1][:-4]; test=None; zuletzt=None
    else:
        q=Q[src][key]; alt_titel=q['text'].partition('\n\n')[0]; fc=q['fc']; assert test in ('neu','alt'), key
        assert f"{q['kcal']} kcal" in alt_titel, key
        if titel is None: titel=alt_titel
        if test=='neu':
            assert bild==f'G103-{key}-ohneBox' and titel!=alt_titel, key
            e_alt=[c for c in '😍🤤🥰🤗😋' if c in alt_titel]; e_neu=[c for c in '😍🤤🥰🤗😋' if c in titel]; assert len(e_alt)==1 and len(e_neu)==1 and e_alt!=e_neu, key
        else:
            assert q['media'].endswith('/'+bild+'.jpg'), ('ALT muss das Board vom letzten Lauf behalten',key)
            assert titel==alt_titel or 'Höfliche' in alt_titel, key
        text=titel+'\n\n'+tags
        media,alt,kcal,suess=URL.format(bild),q['alt'],q['kcal'],q['suess']
        assert '#' not in fc and '📖' not in fc, key
    assert os.path.exists(f"{REPO}/boards/{bild}.jpg"), ('Board fehlt',bild)
    tg=[w for w in text.split() if w.startswith('#')]; nt=len(tg)
    assert tg[-1]=='#fitmitkev' and 2<=nt<=5, (n,key,nt)
    assert bool(suess)==SW[n-1], ('süß/herzhaft',n,key)
    low=(text+fc).lower()
    for w in ('esn','abnehm','höflich','rezeptbuch','http','melly','gta','food','#lecker','#zuckerfrei','📖'): assert w not in low,(key,w)
    assert zeit not in FEST and 'Rezept im 1. Kommentar' in text, key
    posts.append(dict(n=n,key=key,date=f'2026-11-26T{zeit}:00',text=text,fc=fc,media=media,alt=alt,bild=test,board=bild,box=False,kcal=kcal,suess=bool(suess),hashtags=nt,
                      gruppe='A (2–3)' if nt<=3 else 'B (4–5)',neu=src is None,buch=False,zuletzt=zuletzt))
assert len(posts)==19 and len({p['date'] for p in posts})==19 and len({p['key'] for p in posts})==19
assert sum(p['gruppe'][0]=='A' for p in posts)==9 and sum(p['suess'] for p in posts)==8
assert sum(p['bild']=='neu' for p in posts)==7 and sum(p['bild']=='alt' for p in posts)==6 and sum(p['neu'] for p in posts)==6
assert all(p['kcal']<=500 for p in posts)
json.dump(posts,open(f"{D}/out/donnerstag_posts.json","w"),ensure_ascii=False,indent=1)
def art(p): return 'NEU' if p['neu'] else ('TEST neues Foto' if p['bild']=='neu' else 'TEST altes Bild')+' · zuletzt '+p['zuletzt']
alle=[(p['date'][11:16],f"{p['n']:02d} · {'süß ' if p['suess'] else 'herz'} · {p['alt']} · {p['kcal']} kcal · {p['hashtags']} Hashtags · {art(p)}") for p in posts]
alle+=[(t,f"–– · fest · {x}") for t,x in FEST.items()]
with open(f"{D}/out/posting-plan-donnerstag.txt","w") as fh:
    fh.write("Posting-Plan Donnerstag 26.11.2026 – 22 Beiträge: 19 Rezepte + 2 feste ESN-Rezepte (schon eingeplant) + Buch-Beitrag 20:15.\n")
    fh.write("Neue Regel: kein Rezept, das in den letzten 14 Tagen lief. Alle 13 Wiederholer liefen zuletzt am 9.–12.11.\n")
    fh.write("6 neue Rezepte: 3 aus der Kloßteig-Reihe (12:20 Hirschgulasch mit Preiselbeeren, 15:00 Pilzrahmsoße, 17:45 Frikadellen in Zwiebelsoße), Schneewittchenkuchen, Toast Hawaii, Japanischer Käsekuchen.\n")
    fh.write("WIEDERHOLER-TEST Tag 2: 7 Wiederholer mit NEUEM Foto und neuer Schreibschrift-Zeile, 6 mit altem Bild. Rezept, Kalorien und 1. Kommentar wie beim letzten Lauf.\n")
    fh.write("Alle Boards ohne Box. Ein Werbe-Beitrag (Buch, 20:15), keine Buch-Zeile.\nHinter jedem Wiederholer: letzter Lauf · Reichweite · Vielfaches des Tagesmittels.\n\n")
    for t,x in sorted(alle): fh.write(f"{t} · {x}\n")
with open(f"{D}/out/texte-donnerstag.txt","w") as fh:
    for p in posts:
        fh.write(f"===== {p['n']:02d} · {p['date'][11:16]} · {p['alt']}{'  ·  NEU' if p['neu'] else ('  ·  TEST neues Foto' if p['bild']=='neu' else '  ·  TEST altes Bild')}\n\nBEITRAG:\n{p['text']}\n\n1. KOMMENTAR:\n{p['fc']}\n\nBILD: {p['media']}\n\n\n")
print(open(f"{D}/out/posting-plan-donnerstag.txt").read())
