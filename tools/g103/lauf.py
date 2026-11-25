# Läufe 10.–23.11. aus Metricool (FBPO02/03/12/23) mit den Plan-JSONs im Repo zusammenführen: welches Rezept lief wann mit welcher Reichweite?
import json, glob, datetime as dt, statistics as st, sys, collections
F='/root/.claude/projects/-home-claude/62a14d94-6bfc-5e5c-b2da-15988fbe030e/tool-results/mcp-Metricool_Social_Media_Management-getAnalyticsDataByMetrics-1795504845975-xdxpvx.txt'
s=open(F).read(); rows=json.JSONDecoder().raw_decode(s[s.index('{"rows"'):])[0]['rows']
R='/home/claude/fitmitkev-bilder/tools'
PL={}
for f in glob.glob(f'{R}/g*/*posts*.json')+glob.glob(f'{R}/gta/*posts*.json'):
    try: P=json.load(open(f))
    except Exception: continue
    if not isinstance(P,list): continue
    for p in P:
        if isinstance(p,dict) and p.get('text') and p.get('alt'):
            PL.setdefault(p['text'].strip(),[]).append(dict(key=p.get('key'),alt=p['alt'],kcal=p.get('kcal'),suess=p.get('suess'),src=f.split('/tools/')[1],fc=p.get('fc'),media=p.get('media')))
L=[]
for ts,text,reach,clicks in rows:
    t=dt.datetime.strptime(ts,'%Y%m%d%H%M%S')+dt.timedelta(hours=1)
    m=PL.get((text or '').strip())
    L.append(dict(t=t,tag=t.strftime('%Y-%m-%d'),zeit=t.strftime('%H:%M'),reach=int(float(reach or 0)),klicks=int(float(clicks or 0)),text=text or '',alt=m[0]['alt'] if m else None,key=m[0]['key'] if m else None,suess=m[0]['suess'] if m else None,srcs=[x['src'] for x in m] if m else []))
def rezept(p): return ('Rezept im 1. Kommentar' in p['text'] or 'kcal' in p['text'][:40]) and not p['text'].startswith('Werbung')
MED={}
for tag in sorted({p['tag'] for p in L}):
    rr=[p['reach'] for p in L if p['tag']==tag and rezept(p)]
    MED[tag]=st.median(rr) if rr else 0
for p in L: p['x']=round(p['reach']/MED[p['tag']],1) if MED[p['tag']] else 0
json.dump([dict(p,t=p['t'].isoformat()) for p in L],open('laeufe.json','w'),ensure_ascii=False,indent=0)
if __name__=='__main__':
    print(len(L),'Beiträge; ohne Zuordnung:',sum(1 for p in L if not p['alt']))
    print({k:round(v) for k,v in MED.items()})
    tag=sys.argv[1] if len(sys.argv)>1 else '2026-11-17'
    for p in sorted([p for p in L if p['tag']==tag],key=lambda p:-p['reach']):
        print(f"{p['zeit']} {p['reach']:>7} {p['x']:>5}× {p['klicks']:>5} | {(p['alt'] or p['text'][:60]).replace(chr(10),' ')} | {p['key']}")
