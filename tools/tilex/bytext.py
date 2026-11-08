# -*- coding: utf-8 -*-
"""Reihen über die Textblöcke (Menge + Name) rechts neben den Kacheln finden."""
import numpy as np, re
from scipy import ndimage as ndi
from PIL import Image
import pytesseract
from tilex import X0, Y0, Y1, HI

def text_blocks(im, tx1, xr=620):
    """im: float array HxWx3. Liefert Liste (top,bottom) der Textblöcke in der Zutaten-Textspalte."""
    reg=im[Y0:Y1, tx1+4:xr]
    navy=(reg[:,:,0]<120)&(reg[:,:,1]<130)&(reg[:,:,2]<170)
    prof=navy.sum(1)
    on=prof>=2
    bands=[];s=None
    for y,v in enumerate(on):
        if v and s is None: s=y
        if not v and s is not None: bands.append([s,y]); s=None
    if s is not None: bands.append([s,len(on)])
    bands=[b for b in bands if b[1]-b[0]>=8]
    blocks=[]
    for b in bands:
        if blocks and b[0]-blocks[-1][1]<24: blocks[-1][1]=b[1]
        else: blocks.append(list(b))
    blocks=[[a+Y0,b+Y0] for a,b in blocks if b-a>=28]
    return blocks

def rows_from_blocks(diff, blocks, tx1):
    hard=(diff[:, X0:tx1]>HI)
    centers=[(a+b)/2 for a,b in blocks]
    n=len(centers)
    if n==0: return []
    if n==1: cuts=[max(Y0,int(centers[0]-110)), min(Y1,int(centers[0]+110))]
    else:
        pitch=np.median(np.diff(centers))
        mids=[(centers[i]+centers[i+1])/2 for i in range(n-1)]
        cuts=[max(Y0,int(centers[0]-pitch/2))]+[int(m) for m in mids]+[min(Y1,int(centers[-1]+pitch/2))]
    rows=[]
    for a,b in zip(cuts[:-1],cuts[1:]):
        sub=hard[a:b]; ys=np.where(sub.sum(1)>0)[0]; xs=np.where(sub.sum(0)>0)[0]
        if len(ys)<20 or len(xs)<20: rows.append(None); continue
        rows.append([a+int(ys.min()), a+int(ys.max())+1, int(xs.min())+X0, int(xs.max())+1+X0])
    return rows

def ocr_block(pil, block, tx1, xr=780):
    a,b=block
    crop=pil.crop((tx1, max(0,a-8), xr, b+8))
    d=pytesseract.image_to_data(crop,lang='deu',config='--psm 6',output_type=pytesseract.Output.DICT)
    lines={}
    for i,t in enumerate(d['text']):
        if not t.strip() or int(d['conf'][i])<20: continue
        if not re.search(r'[A-Za-zÄÖÜäöüß0-9½¼¾]',t): continue
        k=(d['block_num'][i],d['par_num'][i],d['line_num'][i])
        lines.setdefault(k,dict(words=[],top=d['top'][i]))['words'].append(t)
    L=[' '.join(l['words']) for l in sorted(lines.values(),key=lambda l:l['top'])]
    if not L: return '',''
    amt=L[0]; name=' '.join(L[1:]).strip()
    if not name and len(L)==1:
        # Menge und Name in einer Zeile erkannt
        m=re.match(r'^(\S+(?:\s?(?:g|ml|Stück|EL|TL|Pck\.?|Päckchen|Prise|Zehen|Stange|Scheiben|Blatt|Dose|Glas|kg|l))?)\s+(.*)$',amt)
        if m: amt,name=m.group(1),m.group(2)
    return amt,name
