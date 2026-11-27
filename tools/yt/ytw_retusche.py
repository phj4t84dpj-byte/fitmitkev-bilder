# -*- coding: utf-8 -*-
"""YouTube-Reihe ab 30.11.: Wort „ABNEHM-“ aus zwei Thumbnails herausrechnen (Regel: kein „abnehmen“ auf Facebook-Bildern)
und durch ein neues Wort im selben Gelb ersetzen. Aufruf: python3 ytw_retusche.py <thumb-ordner> <ziel-ordner>"""
import sys, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
S='/tmp/claude-0/-home-claude/62a14d94-6bfc-5e5c-b2da-15988fbe030e/scratchpad'
FONT=f"{S}/fonts/gf/ofl/poppins/Poppins-ExtraBold.ttf"
# id: (Rechteck der ersten Titelzeile x0,y0,x1,y1 im 1280x720-Bild, neues Wort, Mitte x, Grundlinie y, Schriftgröße)
JOBS={'jbviLMbSITg':((780,18,1275,122),'OFEN-',1025,112,108),
      'TZUXs6jSD3c':((780,18,1275,122),'SPÄTZLE-',1025,112,108)}
src,dst=sys.argv[1],sys.argv[2]
for vid,((x0,y0,x1,y1),wort,cx,base,size) in JOBS.items():
    im=cv2.imread(f"{src}/{vid}.jpg"); H,W=im.shape[:2]
    hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    gelb=((hsv[:,:,0]>=18)&(hsv[:,:,0]<=38)&(hsv[:,:,1]>110)&(hsv[:,:,2]>150)).astype(np.uint8)
    m=np.zeros((H,W),np.uint8); m[y0:y1,x0:x1]=gelb[y0:y1,x0:x1]
    # Zeilen der ersten Titelzeile (bis kurz vor der zweiten), Spalten mit Rand; jede Zeile gerade von links nach rechts füllen
    zeilen=np.where(gelb[y0:y1+60,x0:x1].sum(1)>3)[0]+y0
    lücke=[y for y in range(zeilen[0],zeilen[-1]) if gelb[y,x0:x1].sum()<=3]
    ya=max(2,zeilen[0]-14); yb=(lücke[len(lücke)//2] if lücke else y1)
    sp=np.where(gelb[ya:yb,x0:x1].sum(0)>0)[0]+x0; xa=max(1,sp[0]-16); xb=min(W-2,sp[-1]+16)
    o=im.astype(np.float32).copy()
    t=((np.arange(xa,xb+1)-xa)/(xb-xa))[None,:,None]
    o[ya:yb,xa:xb+1]=im[ya:yb,xa:xa+1]*(1-t)+im[ya:yb,xb:xb+1]*t
    m=np.zeros((H,W),np.float32); m[ya:yb,xa:xb+1]=1; mb=cv2.GaussianBlur(m,(0,0),3)[:,:,None]
    o=o*(1-mb)+cv2.GaussianBlur(o,(0,0),6)*mb
    o+=np.random.default_rng(3).normal(0,1.6,o.shape).astype(np.float32)*mb
    o=np.clip(o,0,255).astype(np.uint8); print(vid,'Feld',xa,ya,xb,yb)
    # Farbe aus der zweiten Titelzeile nehmen
    farbe=np.median(im[130:200,850:1200][gelb[130:200,850:1200]>0],axis=0)[::-1].astype(int)
    pil=Image.fromarray(o[:,:,::-1]); d=ImageDraw.Draw(pil); f=ImageFont.truetype(FONT,size)
    while True:
        bb=d.textbbox((0,0),wort,font=f,anchor='ls',stroke_width=5)
        if bb[2]-bb[0]<=x1-x0-10 or size<60: break
        size-=4; f=ImageFont.truetype(FONT,size)
    d.text((cx-(bb[2]-bb[0])/2-bb[0],base),wort,font=f,fill=tuple(farbe),anchor='ls',stroke_width=5,stroke_fill=(15,15,15))
    pil.save(f"{dst}/{vid}.jpg",quality=95); print(vid,wort,size,tuple(farbe))
