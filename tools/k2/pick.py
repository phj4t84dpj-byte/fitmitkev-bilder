# Kandidaten-Bogen: pro Rezept oben die 4 Zubereitungs-Seeds, unten die 4 Gericht-Seeds
import glob, os, sys
from PIL import Image, ImageDraw, ImageFont
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D)
f=ImageFont.truetype(f"{S}/fonts/gf/ofl/poppins/Poppins-Bold.ttf",26)
key=sys.argv[1]
tops=sorted(glob.glob(f"{D}/raw/{key}_top_s*.jpg")); bots=sorted(glob.glob(f"{D}/raw/{key}_bot_s*.jpg"))
CW=520; sheet=Image.new('RGB',(4*CW+50,int(CW/1.8)+int(CW/1.5)+100),(255,255,255)); d=ImageDraw.Draw(sheet)
for i,p in enumerate(tops):
    im=Image.open(p); im=im.resize((CW,int(CW/1.8))); sheet.paste(im,(10+i*(CW+10),40)); d.text((10+i*(CW+10),8),os.path.basename(p),font=f,fill=(0,0,0))
y=40+int(CW/1.8)+40
for i,p in enumerate(bots):
    im=Image.open(p); im=im.resize((CW,int(CW/1.5))); sheet.paste(im,(10+i*(CW+10),y)); d.text((10+i*(CW+10),y-32),os.path.basename(p),font=f,fill=(0,0,0))
out=f"{D}/_pick_{key}.jpg"; sheet.save(out,quality=85); print(out,sheet.size)
