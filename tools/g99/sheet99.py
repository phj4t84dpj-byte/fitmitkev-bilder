# -*- coding: utf-8 -*-
# G99: Kontaktbögen für Kev – 2 Bögen mit je 8 Boards (4 × 2), nummeriert in Posting-Reihenfolge, mit Uhrzeit.
import json, os
from PIL import Image, ImageDraw, ImageFont
D=os.path.dirname(os.path.abspath(__file__)); REPO=os.environ.get('REPO','/home/claude/fitmitkev-bilder')
P=json.load(open(f"{D}/out/sonntag_posts.json"))
def font(sz):
    for f in (f"{D}/../fonts/gf/ofl/poppins/Poppins-SemiBold.ttf","/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
        if os.path.exists(f): return ImageFont.truetype(f,sz)
    return ImageFont.load_default()
W,H,PAD,LAB=540,675,16,58
for b in range(2):
    sh=Image.new('RGB',(4*W+5*PAD,2*(H+LAB)+3*PAD+70),'white'); d=ImageDraw.Draw(sh)
    d.text((PAD,14),f"Sonntag 22.11.2026 – Bogen {b+1} von 2 (Beiträge {b*8+1}–{b*8+8})",fill=(20,30,70),font=font(34))
    for i,p in enumerate(P[b*8:b*8+8]):
        x=PAD+(i%4)*(W+PAD); y=70+PAD+(i//4)*(H+LAB+PAD)
        im=Image.open(f"{REPO}/boards/{p['media'].rsplit('/',1)[1]}").convert('RGB').resize((W,H),Image.LANCZOS); sh.paste(im,(x,y))
        lab=f"{p['n']:02d} · {p['date'][11:16]} · {p['alt']}"
        f=font(24)
        while d.textlength(lab,font=f)>W-8 and f.size>15: f=font(f.size-1)
        d.text((x+4,y+H+8),lab,fill=(20,30,70),font=f)
        d.text((x+4,y+H+34),("NEU" if p['neu'] else "bewährt (15.11.)")+(" · Rezept im Beitrag" if p['rezept_im_beitrag'] else ""),fill=(193,32,43) if p['neu'] else (90,90,90),font=font(18))
    sh.save(f"{D}/out/Sonntag-22-11-Bogen-{b+1}.jpg",quality=90); print(sh.size)
