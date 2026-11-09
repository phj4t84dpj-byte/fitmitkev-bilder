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
def food_cut(key):
    dst=f'{D}/hero_cut_m/{key}.png'
    os.makedirs(f'{D}/hero_cut_m',exist_ok=True)
    if os.path.exists(dst): return dst
    raw=f'{D}/hero_cut/{key}.png'
    if os.path.exists(raw):
        rgba=np.asarray(Image.open(raw).convert('RGBA')).copy(); h,w=rgba.shape[:2]
        rgba[:,:,3]=(rgba[:,:,3]*text_zone_mask(w,h)).astype(np.uint8)
        Image.fromarray(rgba).save(dst); return dst
    im=cv2.imread(f'{D}/hero/{key}.jpg'); h,w=im.shape[:2]
    mask=np.zeros((h,w),np.uint8)
    rect=(int(w*0.06),int(h*0.30),int(w*0.90),int(h*0.68))
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
    rgba[:,:,3]=(fg*text_zone_mask(w,h)).astype(np.uint8)
    Image.fromarray(rgba).save(dst); return dst
if __name__=='__main__':
    import g87_data as G
    for r in G.R:
        food_cut(r['key']); print('ok',r['key'],flush=True)
