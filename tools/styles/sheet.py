# -*- coding: utf-8 -*-
"""Kontaktbogen: 4 Spalten (2 Stile je Reihe, je süß + herzhaft), Stilname über jedem Paar."""
import os, sys
from PIL import Image, ImageDraw, ImageFont
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D); OUT=f"{D}/out"
sys.path.insert(0,D)
from render_styles import STYLES
FB=f"{S}/fonts/gf/ofl/poppins/Poppins-Bold.ttf"; FS=f"{S}/fonts/gf/ofl/poppins/Poppins-SemiBold.ttf"
KEYS=sys.argv[2:] or ['BratapfelSkyrKuchen','LasagneSuppe']
order=['aktuell','anthrazit','festlich','landhaus','editorial','kreide','rezeptkarte']
M=16; CW=(2160-5*M)//4; CH=round(CW*1.25); LAB=44; HEAD=84
rows=(len(order)+1)//2
WH=HEAD+rows*(LAB+CH+M)+M
sheet=Image.new('RGB',(2160,WH),(246,243,238)); d=ImageDraw.Draw(sheet)
fH=ImageFont.truetype(FB,34); fL=ImageFont.truetype(FB,24); fT=ImageFont.truetype(FS,22)
d.text((M,22),"Stil-Vorschläge – gleiche Rezepte, Kacheln & Texte, nur Farbwelt, Schrift und Hintergrund wechseln",font=fH,fill=(20,30,60))
for i,sk in enumerate(order):
    r,c=divmod(i,2); x0=M+c*2*(CW+M); y0=HEAD+r*(LAB+CH+M)
    d.rounded_rectangle((x0,y0,x0+2*CW+M,y0+LAB-6),radius=10,fill=(20,30,60) if sk!='aktuell' else (120,90,60))
    d.text((x0+14,y0+7),STYLES[sk]['name'],font=fL,fill=(255,255,255))
    for j,key in enumerate(KEYS):
        p=f"{OUT}/STIL-{sk}-{key}.jpg"
        if not os.path.exists(p): continue
        im=Image.open(p).convert('RGB').resize((CW,CH),Image.LANCZOS)
        sheet.paste(im,(x0+j*(CW+M),y0+LAB))
# freie Zelle: Hinweis
if len(order)%2==1:
    r,c=divmod(len(order),2); x0=M+c*2*(CW+M); y0=HEAD+r*(LAB+CH+M)
    d.rounded_rectangle((x0,y0+LAB,x0+2*CW+M,y0+LAB+CH),radius=18,fill=(255,255,255),outline=(210,205,195),width=3)
    txt=["So liest du den Bogen:","","• Jede Reihe zeigt zwei Stile,","  jeweils links süß (Bratapfel-Skyr-Kuchen),","  rechts herzhaft (Lasagne-Suppe).","","• Aufbau, Zutaten-Kacheln, Hook, Titeltext,","  kcal-Zeile, Badge, Vorher-Nachher-Foto","  und @fitmitkev bleiben überall gleich.","","• Es ändern sich nur Farbwelt, Hintergrund-","  Textur und die Schriften.","","• Jeder Stil lässt sich sofort auf alle","  Rezepte anwenden (gleicher Renderer).","","Sag mir einfach die Nummer, die dir gefällt –","oder was du kombinieren willst."]
    fx=ImageFont.truetype(FS,30); yy=y0+LAB+40
    for t in txt:
        d.text((x0+40,yy),t,font=fx if not t.endswith(':') else ImageFont.truetype(FB,32),fill=(30,30,40)); yy+=40
out=sys.argv[1] if len(sys.argv)>1 else f"{OUT}/Kontaktbogen-Stile.jpg"
sheet.save(out,quality=90); print(out,sheet.size)
