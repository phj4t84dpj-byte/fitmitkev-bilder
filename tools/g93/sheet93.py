# Kontaktbögen G93: 4 Spalten x 3 Reihen, nummeriert in Posting-Reihenfolge
import os, sys, json
from PIL import Image, ImageDraw, ImageFont
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D); OUT=f"{D}/out"
FB=f"{S}/fonts/gf/ofl/poppins/Poppins-Bold.ttf"; FS=f"{S}/fonts/gf/ofl/poppins/Poppins-SemiBold.ttf"
posts=json.load(open(f"{OUT}/sonntag_posts.json"))
M=16; CW=(2160-5*M)//4; CH=round(CW*1.25); LAB=40; HEAD=70; PER=12
fH=ImageFont.truetype(FB,36); fL=ImageFont.truetype(FS,24)
for s in range(0,len(posts),PER):
    chunk=posts[s:s+PER]; rows=(len(chunk)+3)//4
    sheet=Image.new('RGB',(2160,HEAD+rows*(LAB+CH+M)+M),(246,243,238)); d=ImageDraw.Draw(sheet)
    d.text((M,18),f"Sonntag 15.11.2026 – Kontaktbogen {s//PER+1} von {(len(posts)+PER-1)//PER} (Beiträge {chunk[0]['n']}–{chunk[-1]['n']})",font=fH,fill=(20,30,60))
    for i,p in enumerate(chunk):
        r,c=divmod(i,4); x=M+c*(CW+M); y=HEAD+r*(LAB+CH+M)
        lab=f"{p['n']:02d} · {p['date'][11:16]} · {p['alt']}"+('' if p.get('box',True) else ' · ohne Box'); fs=24; fl=fL
        while d.textlength(lab,font=fl)>CW-4 and fs>15: fs-=1; fl=ImageFont.truetype(FS,fs)   # ganze Beschriftung, notfalls kleiner – nichts abschneiden
        d.text((x,y+6+(24-fs)//2),lab,font=fl,fill=(20,30,60))
        f=f"{OUT}/"+p['media'].rsplit('/',1)[1]
        if os.path.exists(f): sheet.paste(Image.open(f).convert('RGB').resize((CW,CH),Image.LANCZOS),(x,y+LAB))
    out=f"{OUT}/G93-Kontaktbogen-{s//PER+1}.jpg"; sheet.save(out,quality=88); print(out,sheet.size)
