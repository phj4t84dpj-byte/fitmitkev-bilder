# -*- coding: utf-8 -*-
# Instagram fitmitkevclips ab 22.11.2026: nur noch Captions bauen (Kev postet selbst, nichts wird in Metricool eingeplant).
# Aufruf: python3 ig_caption.py  -> out/<slug>-Caption.txt je Karussell
import json, os
REPO='/home/claude/fitmitkev-bilder'
FB={p['key']:p for p in json.load(open(f'{REPO}/tools/g99/sonntag_posts.json'))}
PLAN=[('PizzaKartoffeln','pk','Na, Hunger? Pizza-Kartoffeln aus dem Ofen, belegt wie eine Pizza. 390 kcal pro Portion.','#pizzakartoffeln #ofenkartoffeln #ofengericht #familienessen #körnigerfrischkäse #kalorienarm #rezeptideen #fitmitkev'),
      ('EinTeig','tp','Na, Hunger? 1 Teig, 5 Sorten Plätzchen. 40 kcal pro Stück.','#plätzchen #weihnachtsbäckerei #plätzchenbacken #advent #backen #kalorienarm #rezeptideen #fitmitkev'),
      ('DoenerKuchen','dk','Na, Hunger? Döner als Kuchen aus Skyr-Teig. 440 kcal und 51 g Eiweiß pro Stück.','#dönerkuchen #döner #skyrteig #hähnchen #proteinreich #kalorienarm #rezeptideen #fitmitkev')]
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
