# G100: Datum und info-JSON je Beitrag für createScheduledPost. Aufruf: python3 payload100.py <von> <bis> <commit-hash>
import json, sys, os
D=os.path.dirname(os.path.abspath(__file__)); a,b,H=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
for p in json.load(open(f"{D}/out/montag_posts.json")):
    if not a<=p['n']<=b: continue
    info={"autoPublish":True,"draft":False,"firstCommentText":p['fc'],"hasNotReadNotes":False,"media":[p['media'].replace('/main/',f'/{H}/')],"mediaAltText":[p['alt']],
          "providers":[{"network":"facebook"}],"publicationDate":{"dateTime":p['date'],"timezone":"Europe/Berlin"},"shortener":False,"smartLinkData":{"ids":[]},"text":p['text'],"facebookData":{"type":"POST"}}
    print(f"##### {p['n']} {p['date']}+01:00"); print(json.dumps(info,ensure_ascii=False))
