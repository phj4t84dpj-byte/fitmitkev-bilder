import json, os
from PIL import Image, ImageDraw, ImageFont
D=os.path.dirname(os.path.abspath(__file__)); REPO='/home/claude/fitmitkev-bilder'
P=json.load(open(f'{D}/out/samstag_posts.json'))
P=sorted(P,key=lambda p:p['date'])
def img(p):
    if p['key']=='MW3': return f'{REPO}/mehrwert/MW3-Brot.jpg'
    if p['neu']: return f"{D}/out/{p['board']}.jpg"
    return f"{REPO}/boards/{p['board']}.jpg"
try: fnt=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',17)
except Exception: fnt=None
for s,part in enumerate([P[:9],P[9:]],1):
    W,H=432,540; sh=Image.new('RGB',(3*W,3*(H+40)),'white'); d=ImageDraw.Draw(sh)
    for i,p in enumerate(part):
        x,y=(i%3)*W,(i//3)*(H+40)
        sh.paste(Image.open(img(p)).convert('RGB').resize((W,H)),(x,y+40))
        lab=f"{p['date'][11:16]}  {p['alt'][:30]}"+('' if p['neu'] else '  (Wdh.)')
        d.text((x+8,y+8),lab,fill=(0,0,0),font=fnt)
    sh.save(f'{D}/out/Samstag-Boards-{s}-von-2.jpg',quality=88); print(s,len(part))
