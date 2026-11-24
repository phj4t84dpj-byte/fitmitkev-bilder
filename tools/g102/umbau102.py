# G102-Umbau (Kev 24.11., 20:05: „keine doppelten Rezepte, also wiederholen innerhalb von 14 Tagen“ → per Dialog: Mittwoch heute Abend umbauen,
# Wiederholer-Test mit 14 Tagen Pause weiter, Varianten zählen als neues Rezept). Die 12 Wiederholer vom 18.11. werden durch Rezepte ersetzt,
# deren letzter Lauf am 11.11. oder früher war (geprüft gegen alle Läufe 10.–24.11. per Schlüssel, Name und Stichwort). Alte Boards, Bild 'alt'.
import json, os
D=os.path.dirname(os.path.abspath(__file__)); REPO='/home/claude/fitmitkev-bilder'
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/{}.jpg"
V1={p['n']:p for p in json.load(open(f'{D}/out/mittwoch_posts_v1_vor_14tage.json'))}
def lade(f): return {p['key']:p for p in json.load(open(f'{REPO}/tools/{f}'))}
Q={'g87':lade('g87/montag_posts.json'),'g88':lade('g88/dienstag_posts.json'),'g89':lade('g89/mittwoch_posts.json')}
# n: (Quelle, Schlüssel, Hashtags, zuletzt)
ERS={1:('g89','Kaesebroetchen','#käsebrötchen #brötchen #fitmitkev','11.11. 06:55 · 0,4-fach'),
     2:('g87','SpekOats','#overnightoats #spekulatius #fitmitkev','9.11. 06:01 · 0,8-fach'),
     4:('g88','MohnStreuselkuchen','#mohnkuchen #streuselkuchen #blechkuchen #fitmitkev','10.11. 18:11 · 1,1-fach'),
     8:('g89','Zimtschnecken','#zimtschnecken #ohnehefe #backen #fitmitkev','11.11. 10:45 · 0,7-fach'),
     10:('g89','KoenigsbergerKlopse','#königsbergerklopse #omasrezepte #kartoffeln #fitmitkev','11.11. 11:31 · 0,6-fach'),
     11:('g88','KokosMandelBowl','#kokos #bowl #fitmitkev','10.11. 12:05 · 0,9-fach'),
     13:('g89','SchokoKaesekuchen','#käsekuchen #schokokuchen #skyrkuchen #backen #fitmitkev','11.11. 20:06 · 1,0-fach'),
     14:('g89','Flammkuchen','#flammkuchen #skyrteig #ohnehefe #fitmitkev','11.11. 20:46 · 0,7-fach'),
     15:('g87','BienenstichBowl','#bienenstich #bowl #fitmitkev','9.11. 16:08 · 0,9-fach'),
     17:('g88','EierlikoerSkyrKuchen','#eierlikör #skyrkuchen #käsekuchen #backen #fitmitkev','10.11. 15:04 · 0,9-fach'),
     18:('g88','Senfeier','#senfeier #kartoffelpüree #omasrezepte #fitmitkev','10.11. 20:16 · 0,9-fach'),
     19:('g88','Kaiserschmarrn','#kaiserschmarrn #ofen #skyr #zuckerfrei #fitmitkev','10.11. 07:30 · 0,6-fach')}
GRUPPE_A={1,2,3,5,6,9,11,12,15}
posts=[]
for n in range(1,20):
    p=dict(V1[n])
    if n in ERS:
        src,key,tags,zul=ERS[n]; q=Q[src][key]
        titel=q['text'].partition('\n\n')[0]; board=q['media'].split('/')[-1][:-4]
        assert os.path.exists(f'{REPO}/boards/{board}.jpg') and 'Rezept im 1. Kommentar' in titel
        p.update(key=key,text=titel+'\n\n'+tags,fc=q['fc'],media=URL.format(board),alt=q['alt'],bild='alt',board=board,kcal=q['kcal'],suess=bool(q['suess']),
                 hashtags=len(tags.split()),gruppe='A (2–3)' if len(tags.split())<=3 else 'B (4–5)',neu=False,buch=False,zuletzt=zul)
    else:
        assert p['neu'] or p['key']=='KaeseLauchSuppe', p['key']
    tg=p['text'].split('\n\n')[-1].split(); assert tg[-1]=='#fitmitkev' and 2<=len(tg)<=5 and (len(tg)<=3)==(n in GRUPPE_A),(n,p['key'],tg)
    low=(p['text']+p['fc']).lower()
    for w in ('esn','abnehm','höflich','rezeptbuch','http','youtube','#food','#lecker','📖'): assert w not in low,(p['key'],w)
    posts.append(p)
SW=[False,True,False,True,False,True,False,True,False, False,True,False,True,False,True,False,True,False,True]
assert [p['suess'] for p in posts]==SW and len({p['key'] for p in posts})==19 and sum(p['gruppe'][0]=='A' for p in posts)==9 and all(p['kcal']<=500 for p in posts)
json.dump(posts,open(f'{D}/out/mittwoch_posts.json','w'),ensure_ascii=False,indent=1)
FEST={'06:10':'ESN-Rezept Zimt-Grießbrei wie bei Oma, 315 kcal (ohne ESN-Zeile)','13:00':'ESN-Rezept Schoko-Eis aus Hüttenkäse, 195 kcal (ohne ESN-Zeile)','20:15':'Buch-Beitrag „5 Weihnachtsmarkt-Klassiker ohne Fritteuse“'}
def art(p): return 'NEU' if p['neu'] else ('TEST neues Foto · zuletzt '+p['zuletzt'] if p['bild']=='neu' else 'wiederholt (altes Bild) · zuletzt '+p['zuletzt'])
alle=[(p['date'][11:16],f"{p['n']:02d} · {'süß ' if p['suess'] else 'herz'} · {p['alt']} · {p['kcal']} kcal · {p['hashtags']} Hashtags · {art(p)}") for p in posts]+[(t,'–– · fest · '+x) for t,x in FEST.items()]
with open(f'{D}/out/posting-plan-mittwoch.txt','w') as fh:
    fh.write("Posting-Plan Mittwoch 25.11.2026 – NEUE FASSUNG nach der 14-Tage-Regel (Kev 24.11., 20:05).\n22 Beiträge: 19 Rezepte + 2 feste ESN-Rezepte (ohne ESN-Zeile) + Buch-Beitrag 20:15.\n")
    fh.write("Geblieben: 6 neue Rezepte (3 aus der Kloßteig-Reihe) und die Käse-Lauch-Suppe mit neuem Foto (letzter Lauf 10.11.).\nErsetzt: die 12 Rezepte vom 18.11. durch Rezepte, die zuletzt am 9.–11.11. liefen (alle mindestens 14 Tage Pause), mit ihrem alten Bild.\nHinter jedem Wiederholer: letzter Lauf · Vielfaches des Tagesmittels damals.\n\n")
    for t,x in sorted(alle): fh.write(f'{t} · {x}\n')
with open(f'{D}/out/texte-mittwoch.txt','w') as fh:
    for p in posts: fh.write(f"===== {p['n']:02d} · {p['date'][11:16]} · {p['alt']}\n\nBEITRAG:\n{p['text']}\n\n1. KOMMENTAR:\n{p['fc']}\n\nBILD: {p['media']}\n\n\n")
print(open(f'{D}/out/posting-plan-mittwoch.txt').read())
