# Schnelle Layout-Vorschau ohne Rendern: vorbereitete Heros (hero/<Key>.jpg) auf 1080x1350 mit den Board-Zonen überlagert.
# orange = Box „So geht's“ (seit G91, Unterkante je nach Textlänge ca. 700–735); rot = Kachelspalte + Titelblock (dort wird das Essen ausgeblendet), blau = Badge + Vorher-Nachher-Foto (decken ab), grün = Pfeil.
import sys, os, json
from PIL import Image, ImageDraw, ImageFont
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D)
F=ImageFont.truetype(f"{S}/fonts/gf/ofl/poppins/Poppins-SemiBold.ttf",30)
keys=sys.argv[1:] or list(json.load(open(f'{D}/hero/_auswahl.json')))
tiles=[]
for k in keys:
    p=f'{D}/hero/{k}.jpg'
    if not os.path.exists(p): continue
    im=Image.open(p).convert('RGB').resize((1080,1350),Image.LANCZOS).convert('RGBA')
    ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
    d.rectangle((0,0,430,765),fill=(200,30,30,70),outline=(200,30,30,255),width=3)
    d.rectangle((380,0,1080,612),fill=(200,30,30,70),outline=(200,30,30,255),width=3)
    d.rectangle((100,890,291,951),fill=(30,60,200,150)); d.rectangle((43,968,323,1256),fill=(30,60,200,150))
    d.rectangle((296,588,436,688),outline=(20,160,60,255),width=3)
    d.rectangle((452,470,1060,735),fill=(240,140,20,90),outline=(240,140,20,255),width=3)   # Box „So geht's“ (seit G91)
    for x in range(0,1080,108): d.line((x,0,x,1350),fill=(255,255,255,60))
    for y in range(0,1350,135): d.line((0,y,1080,y),fill=(255,255,255,60))
    im=Image.alpha_composite(im,ov); ImageDraw.Draw(im).text((440,20),k,font=F,fill=(255,255,255,255))
    tiles.append(im.convert('RGB').resize((540,675),Image.LANCZOS))
per=8
for s in range(0,len(tiles),per):
    ch=tiles[s:s+per]; rows=(len(ch)+3)//4
    sh=Image.new('RGB',(4*540,rows*675),(255,255,255))
    for i,t in enumerate(ch): sh.paste(t,((i%4)*540,(i//4)*675))
    out=f'{D}/out/_zonen_{s//per+1}.jpg'; sh.save(out,quality=85); print(out,sh.size)
