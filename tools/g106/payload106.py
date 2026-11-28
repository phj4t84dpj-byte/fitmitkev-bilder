# Druckt die Metricool-Payloads (createScheduledPost) für die Beiträge a..b aus sonntag_posts.json (G106) bzw. n4_posts.json (N4: Argument n4)
import json, sys, os
D=os.path.dirname(os.path.abspath(__file__))
if sys.argv[1]=='n4':
    P=json.load(open(f"{D}/../n4/n4_posts.json")); a,b=int(sys.argv[2]),int(sys.argv[3])
    for i,p in enumerate(P[a-1:b],a):
        info={"autoPublish":True,"draft":False,"firstCommentText":p['fc'],"hasNotReadNotes":False,"media":[p['media']],"mediaAltText":[p['alt']],
              "providers":[{"network":"facebook"}],"publicationDate":{"dateTime":p['date'],"timezone":"Europe/Berlin"},"shortener":False,
              "smartLinkData":{"ids":[]},"text":p['text'],"facebookData":{"type":"POST"}}
        print(f"### {i} {p['key']} blog={p['blog']} date={p['date']}+01:00"); print(json.dumps(info,ensure_ascii=False,separators=(',',':')))
    sys.exit()
P=json.load(open(f"{D}/sonntag_posts.json")); a,b=int(sys.argv[1]),int(sys.argv[2])
P=sorted(P,key=lambda p:p['date'])
for i,p in enumerate(P[a-1:b],a):
    info={"autoPublish":True,"draft":False,"firstCommentText":p['fc'],"hasNotReadNotes":False,"media":[p['media']],"mediaAltText":[p['alt']],
          "providers":[{"network":"facebook"}],"publicationDate":{"dateTime":p['date'],"timezone":"Europe/Berlin"},"shortener":False,
          "smartLinkData":{"ids":[]},"text":p['text'],"facebookData":{"type":"POST"}}
    print(f"### {i} {p['key']} date={p['date']}+01:00"); print(json.dumps(info,ensure_ascii=False,separators=(',',':')))
