# -*- coding: utf-8 -*-
# Instagram fitmitkevclips 21.11.2026: Captions und Metricool-Payloads für die Top 3 vom Fr 20.11. Aufruf: python3 ig_plan.py <commit-hash>
import json, sys
REPO='/home/claude/fitmitkev-bilder'; H=sys.argv[1]
FB={p['key']:p for p in json.load(open(f'{REPO}/tools/g97/donnerstag_posts.json'))}
PLAN=[('12:00','ChowMein','cm','Gebratene Nudeln mit Hähnchen','Na, Hunger? Gebratene Nudeln wie vom Asia-Imbiss. Eine Pfanne, 390 kcal.','#gebratenenudeln #asiatischkochen #hähnchen #abendessen #kalorienarm #proteinreich #rezeptideen #fitmitkev'),
      ('16:00','KFFladen','kw','Wrap aus körnigem Frischkäse','Na, Hunger? Wrap ohne Mehl. Nur körniger Frischkäse und Eier, 290 kcal.','#körnigerfrischkäse #hüttenkäse #wrap #ohnemehl #lowcarb #proteinreich #rezeptideen #fitmitkev'),
      ('19:00','Kokosmakronen','km','Kokosmakronen aus 3 Zutaten','Na, Hunger? Kokosmakronen aus 3 Zutaten. 55 kcal pro Stück.','#kokosmakronen #plätzchen #weihnachtsbäckerei #backen #kalorienarm #ohnemehl #rezeptideen #fitmitkev')]
import os
PLAN=[p for p in PLAN if not os.environ.get('ONLY') or p[2] in os.environ['ONLY'].split(',')]
out=[]
for zeit,key,pre,name,hook,tags in PLAN:
    slug=json.load(open(f'{pre}.json'))['slug']
    fc=FB[key]['fc']; body=fc.split('\n\n',1)[1]
    body='\n'.join(l for l in body.split('\n') if not l.startswith('Schmeckt nach Sünde') and not l.startswith('📖')).strip()
    while '\n\n\n' in body: body=body.replace('\n\n\n','\n\n')
    text=f"{hook}\n\n{body}\n\n{tags}"
    low=text.lower()
    for w in ('http','rezeptbuch','abnehm','esn','#abnehmen','1. kommentar'): assert w not in low,(key,w)
    assert len(tags.split())==8 and tags.split()[-1]=='#fitmitkev' and len(text)<2200,(key,len(text))
    media=[f'https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/{H}/instagram/karussell/{slug}-{i}.jpg' for i in range(1,7)]
    import os
    for i in range(1,7): assert os.path.exists(f'{REPO}/instagram/karussell/{slug}-{i}.jpg'),(slug,i)
    dt=f'2026-11-21T{zeit}:00'
    info={"autoPublish":True,"draft":False,"firstCommentText":"","hasNotReadNotes":False,"media":media,"mediaAltText":[name]*6,"providers":[{"network":"instagram"}],
          "publicationDate":{"dateTime":dt,"timezone":"Europe/Berlin"},"shortener":False,"smartLinkData":{"ids":[]},"text":text,"instagramData":{"type":"POST","isAiGenerated":True}}
    out.append(dict(key=key,date=dt,info=info))
if not os.environ.get('ONLY'): json.dump(out,open(f'{REPO}/tools/instagram/ig_2026-11-21.json','w'),ensure_ascii=False,indent=1)
for o in out: print('#####',o['date']+'+01:00'); print(json.dumps(o['info'],ensure_ascii=False))
