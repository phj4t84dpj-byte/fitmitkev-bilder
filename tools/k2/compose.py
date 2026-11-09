# -*- coding: utf-8 -*-
"""Konzept 2: oben Zubereitungsschritt (Hände), unten fertiges Gericht, schmale weiße Trennlinie,
Titel-Label in Schreibschrift in der Mitte, kcal klein, @fitmitkev dezent. Ausgabe 1080x1350 (2x = 2160x2700)."""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D)
F=f"{S}/fonts/gf/ofl"
XMP=b'<?xpacket begin="\xef\xbb\xbf" id="W5M0MpCehiHzreSzNTczkc9d"?><x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description rdf:about="" xmlns:Iptc4xmpExt="http://iptc.org/std/Iptc4xmpExt/2008-02-29/" xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/" xmlns:dc="http://purl.org/dc/elements/1.1/" photoshop:Credit="Fitmitkev"><Iptc4xmpExt:DigitalSourceType>http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia</Iptc4xmpExt:DigitalSourceType><dc:creator><rdf:Seq><rdf:li>Fitmitkev</rdf:li></rdf:Seq></dc:creator><dc:description><rdf:Alt><rdf:li xml:lang="x-default">Rezeptgrafik, Foto KI-generiert</rdf:li></rdf:Alt></dc:description></rdf:Description></rdf:RDF></x:xmpmeta><?xpacket end="w"?>'
INFO={'BratapfelSkyrKuchen':('Bratapfel-Skyr-Kuchen','nur 145 kcal pro Stück'),
      'LasagneSuppe':('Lasagne-Suppe','nur 480 kcal pro Teller')}
NAVY=(18,33,63); RED=(193,32,43)
SC=2; W,H=1080*SC,1350*SC; TOP=600*SC; LINE=6*SC

def fit(im,w,h,zoom=1.0,ay=0.5):
    """Bild formatfüllend einpassen; zoom>1 schneidet enger, ay = vertikaler Anker (0 oben, 1 unten)"""
    s=max(w/im.width,h/im.height)*zoom; im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    x=(im.width-w)//2; y=round((im.height-h)*ay); return im.crop((x,y,x+w,y+h))

def compose(key,top,bot,out,label=True,badge=False,ztop=1.0,zbot=1.28):
    name,kcal=INFO[key]
    c=Image.new('RGB',(W,H),(255,255,255))
    c.paste(fit(Image.open(top).convert('RGB'),W,TOP,ztop,0.5),(0,0))
    c.paste(fit(Image.open(bot).convert('RGB'),W,H-TOP-LINE,zbot,0.92),(0,TOP+LINE))
    d=ImageDraw.Draw(c)
    d.rectangle((0,TOP,W,TOP+LINE),fill=(255,255,255))
    if label:
        fK=ImageFont.truetype(f"{F}/kaushanscript/KaushanScript-Regular.ttf",56*SC)
        fP=ImageFont.truetype(f"{F}/poppins/Poppins-SemiBold.ttf",26*SC)
        tw=d.textlength(name,font=fK); kw=d.textlength(kcal,font=fP)
        lw=int(max(tw,kw))+90*SC; lh=124*SC; x0=(W-lw)//2; y0=TOP+LINE//2-lh//2
        # weicher Schatten
        sh=Image.new('RGBA',(lw+40*SC,lh+40*SC),(0,0,0,0)); ds=ImageDraw.Draw(sh)
        ds.rounded_rectangle((20*SC,24*SC,20*SC+lw,24*SC+lh),radius=22*SC,fill=(0,0,0,90))
        sh=sh.filter(ImageFilter.GaussianBlur(10*SC)); c.paste(sh,(x0-20*SC,y0-20*SC),sh)
        d=ImageDraw.Draw(c)
        d.rounded_rectangle((x0,y0,x0+lw,y0+lh),radius=22*SC,fill=(255,255,255))
        d.text((W//2,y0+14*SC),name,font=fK,fill=NAVY,anchor='mt')
        d.text((W//2,y0+lh-16*SC),kcal,font=fP,fill=RED,anchor='mb')
    fI=ImageFont.truetype(f"{F}/kaushanscript/KaushanScript-Regular.ttf",30*SC)
    tx,ty=W-28*SC,H-24*SC
    d.text((tx+2*SC,ty+2*SC),"@fitmitkev",font=fI,fill=(0,0,0),anchor='rb')
    d.text((tx,ty),"@fitmitkev",font=fI,fill=(255,255,255),anchor='rb')
    if badge:
        fA=ImageFont.truetype(f"{F}/anton/Anton-Regular.ttf",40*SC)
        bw=d.textlength("-50 kg",font=fA)+44*SC; bx,by=28*SC,H-24*SC-54*SC
        d.rounded_rectangle((bx,by,bx+bw,by+54*SC),radius=12*SC,fill=(198,31,39))
        d.text((bx+bw/2,by+27*SC),"-50 kg",font=fA,fill=(255,255,255),anchor='mm')
    c.save(out,quality=92,xmp=XMP)
    return out

if __name__=='__main__':
    key,top,bot,out=sys.argv[1:5]
    compose(key,top,bot,out,badge='--badge' in sys.argv); print(out)

# ---------- Variante mit Zutaten-Kacheln links (wie auf Kevs Boards) ----------
import json, sys as _sys
_sys.path.insert(0,f"{S}/g87")
import g87_data as G
TL=f"{S}/tilex/tiles_orig"; MAP=json.load(open(f"{TL}/_map_g87.json"))

def left_fade(w,h,x_end=560*SC,y_full=720*SC,y_end=790*SC,color=(250,247,242)):
    import numpy as np
    xs=np.arange(w,dtype=np.float32); ax=np.interp(xs,[0,x_end*0.55,x_end],[0.9,0.76,0.0]).astype(np.float32)
    ys=np.arange(h,dtype=np.float32); ay=np.interp(ys,[0,y_full,y_end],[1,1,0]).astype(np.float32)
    a=(ax[None,:]*ay[:,None]*255).astype(np.uint8)
    rgb=np.empty((h,w,3),np.uint8); rgb[:]=color
    return Image.fromarray(np.dstack([rgb,a]),'RGBA')

def compose_tiles(key,top,bot,out,badge=False,ztop=1.15,zbot=1.1):
    name,kcal=INFO[key]; r={x['key']:x for x in G.R}[key]; zut=r['zutaten']; n=len(zut)
    c=Image.new('RGB',(W,H),(255,255,255))
    c.paste(fit(Image.open(top).convert('RGB'),W,TOP,ztop,0.5).crop((0,0,W,TOP)) if False else fit_ax(Image.open(top).convert('RGB'),W,TOP,ztop,0.5,0.0),(0,0))
    c.paste(fit(Image.open(bot).convert('RGB'),W,H-TOP-LINE,zbot,0.92),(0,TOP+LINE))
    d=ImageDraw.Draw(c); d.rectangle((0,TOP,W,TOP+LINE),fill=(255,255,255))
    c.paste(left_fade(W,H),(0,0),left_fade(W,H))
    d=ImageDraw.Draw(c)
    # Kacheln
    col_x=40*SC; y0=26*SC; y1=(724 if n>=8 else 700)*SC; rowh=(y1-y0)/n
    tiles=[Image.open(f"{TL}/{MAP.get(z['tile'],z['tile'])}.png").convert('RGBA') for z in zut]
    maxh=max(t.height for t in tiles); scale_t=min(1.2,(rowh-10*SC)/maxh)
    fA=ImageFont.truetype(f"{F}/poppins/Poppins-Bold.ttf",round(27*SC)); fN=ImageFont.truetype(f"{F}/poppins/Poppins-SemiBold.ttf",round(19*SC))
    for i,(z,t) in enumerate(zip(zut,tiles)):
        cy=y0+rowh*(i+0.5); tw,th=round(t.width*scale_t),round(t.height*scale_t); t=t.resize((tw,th),Image.LANCZOS)
        c.paste(t,(col_x+50*SC-tw//2,round(cy-th/2)),t)
        d.text((col_x+112*SC,cy-3*SC),z['menge'],font=fA,fill=NAVY,anchor='ls')
        d.text((col_x+112*SC,cy+3*SC),z['name'],font=fN,fill=NAVY,anchor='lt')
    # Label rechts der Spalte
    cx=((430+1080)//2)*SC; maxw=620*SC; fs=56
    while True:
        fK=ImageFont.truetype(f"{F}/kaushanscript/KaushanScript-Regular.ttf",fs*SC)
        if d.textlength(name,font=fK)+80*SC<=maxw or fs<=40: break
        fs-=2
    fP=ImageFont.truetype(f"{F}/poppins/Poppins-SemiBold.ttf",26*SC)
    lw=int(max(d.textlength(name,font=fK),d.textlength(kcal,font=fP)))+80*SC; lh=120*SC; x0=cx-lw//2; y0l=TOP+LINE//2-lh//2
    sh=Image.new('RGBA',(lw+40*SC,lh+40*SC),(0,0,0,0)); ds=ImageDraw.Draw(sh)
    ds.rounded_rectangle((20*SC,24*SC,20*SC+lw,24*SC+lh),radius=22*SC,fill=(0,0,0,90)); sh=sh.filter(ImageFilter.GaussianBlur(10*SC)); c.paste(sh,(x0-20*SC,y0l-20*SC),sh)
    d=ImageDraw.Draw(c); d.rounded_rectangle((x0,y0l,x0+lw,y0l+lh),radius=22*SC,fill=(255,255,255))
    d.text((cx,y0l+12*SC),name,font=fK,fill=NAVY,anchor='mt'); d.text((cx,y0l+lh-14*SC),kcal,font=fP,fill=RED,anchor='mb')
    fI=ImageFont.truetype(f"{F}/kaushanscript/KaushanScript-Regular.ttf",30*SC); tx,ty=W-28*SC,H-24*SC
    d.text((tx+2*SC,ty+2*SC),"@fitmitkev",font=fI,fill=(0,0,0),anchor='rb'); d.text((tx,ty),"@fitmitkev",font=fI,fill=(255,255,255),anchor='rb')
    if badge:
        fB=ImageFont.truetype(f"{F}/anton/Anton-Regular.ttf",40*SC); bw=d.textlength("-50 kg",font=fB)+44*SC; bx,by=28*SC,H-24*SC-54*SC
        d.rounded_rectangle((bx,by,bx+bw,by+54*SC),radius=12*SC,fill=(198,31,39)); d.text((bx+bw/2,by+27*SC),"-50 kg",font=fB,fill=(255,255,255),anchor='mm')
    c.save(out,quality=92,xmp=XMP); return out

def fit_ax(im,w,h,zoom=1.0,ay=0.5,ax=0.5):
    s=max(w/im.width,h/im.height)*zoom; im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    x=round((im.width-w)*ax); y=round((im.height-h)*ay); return im.crop((x,y,x+w,y+h))
