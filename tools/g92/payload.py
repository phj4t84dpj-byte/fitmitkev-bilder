# Druckt die Metricool-Payloads (createScheduledPost) für die Beiträge a..b aus samstag_posts.json
import json, sys
P=json.load(open(__file__.rsplit('/',1)[0]+'/out/samstag_posts.json'))
a,b=int(sys.argv[1]),int(sys.argv[2])
for p in P[a-1:b]:
    info={"autoPublish":True,"draft":False,"firstCommentText":p['fc'],"hasNotReadNotes":False,"media":[p['media']],"mediaAltText":[p['alt']],
          "providers":[{"network":"facebook"}],"publicationDate":{"dateTime":p['date'],"timezone":"Europe/Berlin"},"shortener":False,
          "smartLinkData":{"ids":[]},"text":p['text'],"facebookData":{"type":"POST"}}
    print(f"### {p['n']} date={p['date']}+01:00")
    print(json.dumps(info,ensure_ascii=False,separators=(',',':')))
