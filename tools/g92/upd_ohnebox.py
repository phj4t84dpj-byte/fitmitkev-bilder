# Druckt updateScheduledPost-Payloads für den Box-Test: Bild gegen die Version ohne Box tauschen, sonst alles gleich
import json,sys
P={p['n']:p for p in json.load(open('out/samstag_posts.json'))}
I={i['n']:i for i in json.load(open('out/samstag_metricool_ids.json'))}
OHNE=[2,4,5,7,8,10,13,15,18,19]; V='e87f947'
for n in [int(x) for x in sys.argv[1:]]:
    p=P[n]; i=I[n]; assert n in OHNE
    info={"autoPublish":True,"draft":False,"firstCommentText":p['fc'],"hasNotReadNotes":False,
          "media":[f"https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/G92-{p['key']}-ohneBox.jpg?v={V}"],
          "mediaAltText":[p['alt']],"providers":[{"network":"facebook"}],"publicationDate":{"dateTime":p['date'][:19],"timezone":"Europe/Berlin"},
          "shortener":False,"smartLinkData":{"ids":[]},"text":p['text'],"facebookData":{"type":"POST"}}
    print(f"### {n} {p['key']} id={i['id']} uuid={i['uuid']}")
    print(json.dumps(info,ensure_ascii=False,separators=(',',':')))
