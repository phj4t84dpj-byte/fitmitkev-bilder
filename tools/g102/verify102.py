# -*- coding: utf-8 -*-
# G102: Antworten von createScheduledPost aus dem Verlauf der Session holen und Feld für Feld mit out/mittwoch_posts.json vergleichen; schreibt out/mittwoch_metricool_ids.json.
import json, os
D=os.path.dirname(os.path.abspath(__file__)); T='/root/.claude/projects/-home-claude/62a14d94-6bfc-5e5c-b2da-15988fbe030e.jsonl'
got={}
def walk(o):
    if isinstance(o,str):
        s=o.strip()
        if s.startswith('{"data":{"id":'):
            try: d=json.loads(s)['data']
            except Exception: return
            if d.get('publicationDate',{}).get('dateTime','').startswith('2026-11-25') and d['providers'][0]['network']=='facebook': got.setdefault(d['publicationDate']['dateTime'],[]).append(d)
    elif isinstance(o,list):
        for x in o: walk(x)
    elif isinstance(o,dict):
        for x in o.values(): walk(x)
for line in open(T):
    if '2026-11-25T' not in line or 'plannerUrl' not in line: continue
    try: walk(json.loads(line))
    except Exception: pass
P=json.load(open(f"{D}/out/mittwoch_posts.json")); ok=0; ids=[]
for p in P:
    L=got.get(p['date'],[]); 
    L={d['id']:d for d in L}.values()
    assert len(L)==1,(p['n'],p['key'],'Anzahl Antworten',len(L))
    d=list(L)[0]
    chk=dict(text=d['text']==p['text'],kommentar=d['firstCommentText']==p['fc'],alt=d['mediaAltText']==[p['alt']],status=d['providers'][0]['status']=='PENDING',bild=len(d['media'])==1 and d['media'][0].startswith('https://static.metricool.com/'),
             typ=d['facebookData']['type']=='POST',auto=d['autoPublish'] is True and d['draft'] is False,nur_fb=len(d['providers'])==1)
    assert all(chk.values()),(p['n'],p['key'],chk)
    ok+=1; ids.append(dict(n=p['n'],key=p['key'],date=p['date'],id=d['id'],uuid=d['uuid'],media=d['media'][0],neu=p['neu'],buch=p['buch'],hashtags=p['hashtags']))
assert len({i['id'] for i in ids})==len(P)
json.dump(ids,open(f"{D}/out/mittwoch_metricool_ids.json","w"),ensure_ascii=False,indent=1)
print(ok,'von',len(P),'gleich dem Plan;',ids[0]['id'],'…',ids[-1]['id'])
