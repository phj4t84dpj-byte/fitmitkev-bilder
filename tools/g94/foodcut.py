# -*- coding: utf-8 -*-
"""Essen aus dem Hero freistellen (GrabCut), damit es als oberste Ebene über den Beige-Verläufen liegt."""
import cv2, numpy as np, os, sys
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f'{D}/hero_cut',exist_ok=True)
def text_zone_mask(w,h):
    """Alpha-Maske (0..1): dort, wo Kachelspalte und Titelblock liegen, bleibt das Essen hinter dem Verlauf
    (sonst läuft es in den Text). CSS-px (1080x1350) -> Bildpixel; weiche Kante 40 px."""
    sx,sy=w/1080,h/1350
    m=np.ones((h,w),np.float32)
    yy,xx=np.mgrid[0:h,0:w]
    X=xx/sx; Y=yy/sy
    def box(x0,x1,y0,y1,f=40):
        dx=np.maximum(np.maximum(x0-X,X-x1),0); dy=np.maximum(np.maximum(y0-Y,Y-y1),0)
        d=np.hypot(dx,dy); return np.clip(d/f,0,1)        # 0 innen, 1 ab f px außerhalb
    m=np.minimum(m,box(0,430,0,765))      # Kachelspalte
    m=np.minimum(m,box(380,1080,0,612))   # Hook/Titel/kcal
    return m
# Bei hellen Tischen nimmt GrabCut die Tischplatte mit: sie läge dann unverblasst über dem Beige-Verlauf und stünde links unten
# als heller Kasten zwischen Kachelspalte und Badge. Für diese Motive wird die Tischfläche wieder aus dem Freisteller genommen.
TABLE_OFF=set()
def table_mask(rgb,a):
    """0..1: tischfarbene Fläche, die mit dem Bereich links zwischen Kachelspalte und Badge zusammenhängt (nur x < 560 Board-px)."""
    h,w=a.shape; sx,sy=w/1080,h/1350
    lab=cv2.cvtColor(cv2.GaussianBlur(np.ascontiguousarray(rgb[:,:,::-1]),(0,0),4),cv2.COLOR_BGR2LAB).astype(np.float32)
    zone=np.zeros((h,w),bool); zone[int(805*sy):int(888*sy),int(75*sx):int(300*sx)]=True
    sel=zone&(a>0.5)
    if sel.sum()<0.3*zone.sum(): return np.zeros((h,w),np.float32)
    med=np.median(lab[sel],axis=0)
    t=(np.linalg.norm(lab-med,axis=2)<18).astype(np.uint8)
    t=cv2.morphologyEx(t,cv2.MORPH_CLOSE,np.ones((31,31),np.uint8))     # Fugen der Holzplanken schließen
    t=cv2.morphologyEx(t,cv2.MORPH_OPEN,np.ones((15,15),np.uint8))
    n,lab2=cv2.connectedComponents(t)
    keep=np.unique(lab2[sel]); keep=keep[keep>0]
    t=np.isin(lab2,keep).astype(np.float32)
    X=(np.arange(w)/sx)[None,:]
    t=t*np.clip((560-X)/40,0,1)
    return cv2.GaussianBlur(t,(0,0),10)
RECT={}
def food_cut(key):
    dst=f'{D}/hero_cut_m/{key}.png'
    os.makedirs(f'{D}/hero_cut_m',exist_ok=True)
    if os.path.exists(dst): return dst
    raw=f'{D}/hero_cut/{key}.png'
    if os.path.exists(raw):
        rgba=np.asarray(Image.open(raw).convert('RGBA')).copy(); h,w=rgba.shape[:2]
        a=rgba[:,:,3].astype(np.float32)
        if key in TABLE_OFF: a=a*(1-table_mask(rgba[:,:,:3],a/255))
        mp=f'{D}/hero/_meta.json'
        if os.path.exists(mp):
            import json
            m=json.load(open(mp)).get(key)
            if m:
                X=(np.arange(w)/(w/1080))[None,:]; Y=(np.arange(h)/(h/1350))[:,None]
                a=a*np.clip((X-m['x0'])/30,0,1)*np.clip((m['x1']-X)/30+ (1 if m['x1']>=1079 else 0),0,1)*np.clip((Y-m['y0'])/30+(1 if m['y0']<=1 else 0),0,1)*np.clip((m['y1']-Y)/30+(1 if m['y1']>=1349 else 0),0,1)
        rgba[:,:,3]=(a*text_zone_mask(w,h)).astype(np.uint8)
        Image.fromarray(rgba).save(dst); return dst
    im=cv2.imread(f'{D}/hero/{key}.jpg'); h,w=im.shape[:2]
    mask=np.zeros((h,w),np.uint8)
    rect=(int(w*0.06),int(h*0.30),int(w*0.90),int(h*0.68))
    if key in RECT:                                    # eigener Rahmen in Board-Pixeln (x0,y0,x1,y1), z. B. für verkleinerte Bowls
        x0,y0,x1,y1=RECT[key]; sx,sy=w/1080,h/1350; rect=(int(x0*sx),int(y0*sy),int((x1-x0)*sx),int((y1-y0)*sy))
    bgd=np.zeros((1,65),np.float64); fgd=np.zeros((1,65),np.float64)
    cv2.grabCut(im,mask,rect,bgd,fgd,5,cv2.GC_INIT_WITH_RECT)
    fg=np.where((mask==cv2.GC_FGD)|(mask==cv2.GC_PR_FGD),255,0).astype(np.uint8)
    fg=cv2.morphologyEx(fg,cv2.MORPH_CLOSE,np.ones((15,15),np.uint8))
    n,lab,stats,_=cv2.connectedComponentsWithStats(fg)
    if n>1:
        keep=[i for i in range(1,n) if stats[i,cv2.CC_STAT_AREA]>0.02*h*w]
        fg=np.isin(lab,keep).astype(np.uint8)*255
    fg=cv2.GaussianBlur(fg,(0,0),4)
    rgba=cv2.cvtColor(im,cv2.COLOR_BGR2RGBA); rgba[:,:,3]=fg
    Image.fromarray(rgba).save(raw)
    return food_cut(key)          # Maskierung (Textzonen, ggf. Tisch) in einem Weg über den gespeicherten Rohschnitt
if __name__=='__main__':
    import g94_data as G
    for r in G.R:
        food_cut(r['key']); print('ok',r['key'],flush=True)
