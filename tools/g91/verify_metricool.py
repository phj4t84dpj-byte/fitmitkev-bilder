import json,sys,re
T='/root/.claude/projects/-home-claude/62a14d94-6bfc-5e5c-b2da-15988fbe030e.jsonl'
best=None
def walk(o):
    if isinstance(o,str):
        if o.startswith('{"data":[{"id":424243447') : yield o
    elif isinstance(o,dict):
        for v in o.values(): yield from walk(v)
    elif isinstance(o,list):
        for v in o: yield from walk(v)
for line in open(T,encoding='utf-8'):
    if '424245593' not in line or '424243447' not in line: continue
    try: j=json.loads(line)
    except Exception: continue
    for s in walk(j):
        try:
            d=json.loads(s)
            if len(d['data'])>=16: best=d
        except Exception as e: pass
assert best, 'Antwort nicht gefunden'
live=best['data']
soll=json.load(open('out/freitag_posts.json',encoding='utf-8'))
print('live',len(live),'soll',len(soll))
assert len(live)==16==len(soll)
live=sorted(live,key=lambda p:p['publicationDate']['dateTime'])
ids=[]
ok=True
for p,s in zip(live,soll):
    dt=p['publicationDate']['dateTime']
    sd=s['date'][:19]
    chk=dict(zeit=dt==sd, text=p['text']==s['text'], fc=p['firstCommentText']==s['fc'], alt=p['mediaAltText']==[s['alt']],
             status=p['providers'][0]['status']=='PENDING' and p['providers'][0]['network']=='facebook' and len(p['providers'])==1,
             auto=p['autoPublish'] is True and p['draft'] is False, media=len(p['media'])==1 and p['media'][0].startswith('https://static.metricool.com/'),
             typ=p['facebookData']['type']=='POST', tz=p['publicationDate']['timezone']=='Europe/Berlin')
    bad=[k for k,v in chk.items() if not v]
    if bad: ok=False
    print(f"{s['n']:>2} {dt[11:16]} {s['key']:<22} id={p['id']} {'OK' if not bad else 'FEHLER '+str(bad)}")
    ids.append(dict(n=s['n'],key=s['key'],date=dt,id=p['id'],uuid=p['uuid'],media=p['media'][0],hashtags=s.get('hashtags'),gruppe=s.get('gruppe'),kcal=s.get('kcal'),suess=s.get('suess')))
assert len({i['id'] for i in ids})==16 and len({i['uuid'] for i in ids})==16
assert len({p['text'] for p in live})==16
print('ALLES OK' if ok else 'ABWEICHUNGEN')
json.dump(ids,open('out/donnerstag_metricool_ids.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
