# -*- coding: utf-8 -*-
# Instagram fitmitkevclips ab 22.11.2026: nur noch Captions bauen (Kev postet selbst, nichts wird in Metricool eingeplant).
# Aufruf: python3 ig_caption.py  -> out/<slug>-Caption.txt je Karussell
import json, os
REPO='/home/claude/fitmitkev-bilder'
FB={p['key']:p for p in json.load(open(f'{REPO}/tools/g98/samstag_posts.json'))}
PLAN=[('Rotweinkuchen','rw','Na, Hunger? Rotweinkuchen wie früher bei Oma. 140 kcal pro Stück.','#rotweinkuchen #kastenkuchen #kuchenliebe #backen #omasrezepte #kalorienarm #rezeptideen #fitmitkev'),
      ('MarmorBowl','mk','Na, Hunger? Marmorkuchen als Bowl nur für dich. 330 kcal und 25 g Eiweiß.','#marmorkuchen #bowl #haferflocken #skyr #proteinreich #kalorienarm #rezeptideen #fitmitkev'),
      ('Churros','ch','Na, Hunger? Churros wie von der Kirmes, nur aus dem Ofen. 300 kcal pro Portion.','#churros #kirmes #ofenrezept #backen #zimt #kalorienarm #rezeptideen #fitmitkev')]
for key,pre,hook,tags in PLAN:
    slug=json.load(open(f'{pre}.json'))['slug']
    fc=FB[key]['fc']; body=fc.split('\n\n',1)[1]
    body='\n'.join(l for l in body.split('\n') if not l.startswith('Schmeckt nach Sünde') and not l.startswith('📖')).strip()
    while '\n\n\n' in body: body=body.replace('\n\n\n','\n\n')
    text=f"{hook}\n\n{body}\n\n{tags}"
    low=text.lower()
    for w in ('http','rezeptbuch','abnehm','esn','1. kommentar'): assert w not in low,(key,w)
    assert len(tags.split())==8 and tags.split()[-1]=='#fitmitkev' and len(text)<2200,(key,len(text))
    open(f'out/{slug}-Caption.txt','w').write(text+'\n')
    print('#####',slug,len(text)); print(text); print()
