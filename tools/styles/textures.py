# -*- coding: utf-8 -*-
"""Prozedurale Hintergrund-Texturen (2160x2700) + Verlaufs-Alpha -> ein RGBA-Overlay pro Stil.
Das Overlay ersetzt die drei Beige-Verläufe des G87-Renderers (gleiche Alpha-Komposition),
bringt aber Farbe und Struktur mit (Stein, Holz, Tafel, Papier, Samt mit Bokeh)."""
import numpy as np, os
from scipy import ndimage as ndi
from PIL import Image
W,H=2160,2700
D=os.path.dirname(os.path.abspath(__file__))

def noise(sigma,amp,seed=0,shape=(H,W)):
    n=np.random.default_rng(seed).standard_normal(shape).astype(np.float32)
    if np.any(np.asarray(sigma)>0): n=ndi.gaussian_filter(n,sigma)
    n/=(n.std()+1e-6)
    return n*amp

def flat(rgb):
    img=np.empty((H,W,3),np.float32); img[:]=rgb; return img

def stone():
    img=flat((47,49,54))
    v=noise(45,9,1)+noise(7,5,2)+noise(0.9,6,3)
    img+=v[:,:,None]*np.array([1,1,1.06],np.float32)
    sp=(np.random.default_rng(4).random((H,W))>0.9985).astype(np.float32)
    img+=(ndi.gaussian_filter(sp,0.8)*40)[:,:,None]
    return np.clip(img,0,255)

def festive():
    img=flat((104,16,28))
    img+=noise(60,7,21)[:,:,None]*np.array([1.2,0.6,0.7],np.float32)
    img+=noise(1.0,3,22)[:,:,None]
    r=np.random.default_rng(23); gold=np.array([243,197,92],np.float32)
    for i in range(80):
        cx=r.uniform(0,W); cy=abs(r.normal(0,0.33))*H
        if cy>H*0.78: continue
        rad=r.uniform(16,95); a=r.uniform(0.10,0.5)
        x0,x1=int(max(0,cx-rad-6)),int(min(W,cx+rad+6)); y0,y1=int(max(0,cy-rad-6)),int(min(H,cy+rad+6))
        if x1<=x0 or y1<=y0: continue
        yy,xx=np.mgrid[y0:y1,x0:x1]; d=np.hypot(xx-cx,yy-cy)
        m=np.clip((rad-d)/(rad*0.22),0,1)*(0.75+0.35*np.clip((d-rad*0.6)/(rad*0.4),0,1))
        m=(m*a)[:,:,None]
        img[y0:y1,x0:x1]=img[y0:y1,x0:x1]*(1-m)+gold*m
    return np.clip(img,0,255)

def whitewood():
    img=flat((238,232,222))
    v=noise((80,2.2),5.5,31)+noise((30,1.2),2.5,32)+noise(0.8,2,33)
    img+=v[:,:,None]*np.array([1,0.95,0.85],np.float32)
    pw=216
    for k in range(0,W,pw):
        img[:,k:k+pw]+=np.random.default_rng(40+k).uniform(-4,4)
        if k>0:
            img[:,k-2:k+2]-=16; img[:,k+2:k+5]-=6
    return np.clip(img,0,255)

def chalk():
    img=flat((35,47,41))
    img+=(noise(2,3.5,51)+noise(0.8,2.5,52))[:,:,None]
    r=np.random.default_rng(53)
    for i in range(14):
        cx,cy=r.uniform(0,W),r.uniform(0,H); sx,sy=r.uniform(250,650),r.uniform(90,260); amp=r.uniform(6,16)
        x0,x1=int(max(0,cx-3*sx)),int(min(W,cx+3*sx)); y0,y1=int(max(0,cy-3*sy)),int(min(H,cy+3*sy))
        yy,xx=np.mgrid[y0:y1,x0:x1]
        m=np.exp(-(((xx-cx)/sx)**2+((yy-cy)/sy)**2)/2)
        img[y0:y1,x0:x1]+=(m*amp)[:,:,None]*np.array([1,1,0.97],np.float32)
    dust=(r.random((H,W))>0.9993).astype(np.float32)
    img+=(ndi.gaussian_filter(dust,1.1)*90)[:,:,None]
    return np.clip(img,0,255)

def chalkwhite():
    """Kreide-Textur für Schrift (background-clip:text)"""
    a=0.72+0.28*np.clip(noise((1.5,6),1,61)*0.5+0.5,0,1)
    a=np.clip(a-0.18*(np.random.default_rng(62).random((H,W))>0.97),0,1)
    rgb=flat((246,243,236))
    return rgb,a

def paper():
    img=flat((247,240,226))
    img+=noise(1.2,3,71)[:,:,None]+noise(30,3,72)[:,:,None]*np.array([1,0.9,0.7],np.float32)
    yy,xx=np.mgrid[0:H,0:W]; rr=np.hypot((xx-W/2)/(W/2),(yy-H/2)/(H/2))
    img*=(1-0.07*np.clip(rr-0.4,0,1))[:,:,None]
    return np.clip(img,0,255)

def cream():
    img=flat((239,230,216))
    img+=noise(1.0,2.5,81)[:,:,None]+noise(40,3,82)[:,:,None]*np.array([1,0.95,0.85],np.float32)
    return np.clip(img,0,255)

def gingham_frame(rgb,A,band=44,cell=22):
    yy,xx=np.mgrid[0:H,0:W]
    frame=(xx<band)|(xx>=W-band)|(yy<band)|(yy>=H-band)
    sx=((xx//cell)%2==0); sy=((yy//cell)%2==0)
    red=np.array([198,40,52],np.float32); white=np.array([252,248,240],np.float32); pink=np.array([228,150,156],np.float32)
    col=np.where((sx&sy)[:,:,None],red,np.where((sx|sy)[:,:,None],pink,white))
    rgb=np.where(frame[:,:,None],col,rgb); A=np.where(frame,1.0,A).astype(np.float32)
    inner=((xx>=band)&(xx<band+4))|((xx<W-band)&(xx>=W-band-4))|((yy>=band)&(yy<band+4))|((yy<H-band)&(yy>=H-band-4))
    rgb=np.where(inner[:,:,None],np.array([255,251,242],np.float32),rgb); A=np.where(inner,1.0,A).astype(np.float32)
    return rgb,A

TEX={'beige':lambda:flat((181,157,132)),'stone':stone,'festive':festive,'whitewood':whitewood,'chalk':chalk,'paper':paper,'cream':cream}

def ramp(stops,n):
    xs=np.linspace(0,1,n); return np.interp(xs,[s[0] for s in stops],[s[1] for s in stops]).astype(np.float32)

def build_alpha(st):
    AT=np.zeros(H,np.float32); AT[:1640]=ramp(st['aT'],1640)
    AL=np.zeros(W,np.float32); AL[:1040]=ramp(st['aL'],1040)
    ALm=np.zeros((H,1),np.float32); ALm[:2200]=1
    AB=np.zeros((H,W),np.float32); AB[1700:,:840]=ramp(st['aB'],840)[None,:]
    return (1-(1-AT[:,None])*(1-AL[None,:]*ALm)*(1-AB)).astype(np.float32)

def save_rgba(rgb,a,path):
    Image.fromarray(np.dstack([np.clip(rgb,0,255),np.clip(a,0,1)*255]).astype(np.uint8),'RGBA').save(path,compress_level=1)

def build_overlay(key,st,out):
    p=f"{out}/ov_{key}.png"
    if os.path.exists(p): return p
    rgb=TEX[st['tex']](); A=build_alpha(st)
    if st.get('frame'): rgb,A=gingham_frame(rgb,A)
    save_rgba(rgb,A,p); return p

def build_chalkwhite(out):
    p=f"{out}/chalkwhite.png"
    if not os.path.exists(p):
        rgb,a=chalkwhite(); save_rgba(rgb,a,p)
    return p
