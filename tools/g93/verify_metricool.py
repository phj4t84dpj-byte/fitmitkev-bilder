# Prüft die Sonntags-Beiträge in Metricool (Antwort von getScheduledPosts als Datei) Feld für Feld gegen out/sonntag_posts.json
import json,sys,collections
raw=json.load(open(sys.argv[1],encoding='utf-8')); data=raw['data'] if isinstance(raw,dict) else raw
fb=[p for p in data if [x['network'] for x in p['providers']]==['facebook']]
pins=[p for p in data if any(x['network']=='pinterest' for x in p['providers'])]
soll=json.load(open('out/sonntag_posts.json',encoding='utf-8'))
by=collections.defaultdict(list)
for p in fb: by[p['publicationDate']['dateTime'][:19]].append(p)
ids=[]; ok=True
for s in soll:
    L=by.get(s['date'][:19],[])
    rez=[p for p in L if p['text']==s['text']]
    if len(rez)!=1: ok=False; print(s['n'],s['date'][11:16],s['key'],'ANZAHL',len(rez)); continue
    p=rez[0]
    chk=dict(fc=p['firstCommentText']==s['fc'], alt=p['mediaAltText']==[s['alt']], status=p['providers'][0]['status']=='PENDING',
             auto=p['autoPublish'] is True and p['draft'] is False, media=len(p['media'])==1 and p['media'][0].startswith('https://static.metricool.com/'),
             typ=p['facebookData']['type']=='POST')
    bad=[k for k,v in chk.items() if not v]; ok&=not bad
    print(f"{s['n']:>2} {s['date'][11:16]} {s['key']:<16} id={p['id']} {'OK' if not bad else 'FEHLER '+str(bad)}")
    ids.append(dict(n=s['n'],key=s['key'],date=s['date'],id=p['id'],uuid=p['uuid'],media=p['media'][0],box=s.get('box',True),hashtags=s['hashtags'],gruppe=s['gruppe'],kcal=s['kcal'],suess=s['suess']))
rest=[p for p in fb if p['text'] not in {s['text'] for s in soll}]
print('Facebook gesamt',len(fb),'· Rezepte',len(ids),'· sonstige FB:',[(p['publicationDate']['dateTime'][11:16],p['id'],p['text'][:30]) for p in rest],'· Pins',len(pins))
assert ok and len(ids)==20 and len({i['id'] for i in ids})==20
json.dump(ids,open('out/sonntag_metricool_ids.json','w'),ensure_ascii=False,indent=1); print('alles OK')
