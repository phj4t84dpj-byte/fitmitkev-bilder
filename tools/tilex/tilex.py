# -*- coding: utf-8 -*-
"""Original-Zutatenkacheln aus den gesicherten Facebook-Boards (2160x2700) ausschneiden.
Hintergrund = glatter Verlauf, horizontal konstant -> bg(y) aus dem linken Rand schätzen,
Differenz -> Alpha (weiche Schatten bleiben), Löcher im Objekt füllen, Farben entmischen.
Zuordnung Zutat <-> Reihe über archiv/rezepte.json (zutaten in Reihenfolge)."""
import numpy as np, json, os, re, sys, glob
from PIL import Image
from scipy import ndimage as ndi

REPO='/home/claude/fitmitkev-bilder'
OUT=os.path.dirname(os.path.abspath(__file__))+'/crops'
os.makedirs(OUT,exist_ok=True)
X0,X1=44,300          # Kachelspalte (Text beginnt bei ~275-405 je nach Breite der Kachel)
Y0,Y1=70,1500
LO,HI=7,34            # Differenz -> Alpha-Rampe

def norm(s):
    s=s.lower()
    s=re.sub(r'\(.*?\)','',s)
    s=s.replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss')
    s=re.sub(r'[^a-z0-9]+','_',s).strip('_')
    return s

def extract(path):
    im=np.asarray(Image.open(path).convert('RGB')).astype(np.float32)
    H,W,_=im.shape
    if (W,H)!=(2160,2700): return None,'size'
    bg=np.median(im[:,4:36,:],axis=1)                 # (H,3)
    diff=np.abs(im-bg[:,None,:]).max(2)                # (H,W)
    hardall=ndi.binary_opening(diff[Y0:Y1]>HI,iterations=1)
    # Textspalte finden: erste Lücke (>=10 leere Spalten) zwischen x=200 und 340
    occ=hardall[:,200:340].sum(0)>0
    tx1=268; run=0
    for i,o in enumerate(occ):
        if not o:
            run+=1
            if run>=10 and i-run+1>30:      # Lücke beginnt bei x=200+i-run+1
                tx1=200+i-run+1; break
        else: run=0
    hard=hardall[:,X0:tx1]
    prof=hard.sum(1)
    bands=[];s=None
    for y,v in enumerate(prof>0):
        if v and s is None: s=y
        if not v and s is not None: bands.append([s,y]); s=None
    if s is not None: bands.append([s,len(prof)])
    # kleine Lücken schließen
    merged=[]
    for b in bands:
        if merged and b[0]-merged[-1][1]<8: merged[-1][1]=b[1]
        else: merged.append(b)
    bands=[b for b in merged if b[1]-b[0]>=40]
    rows=[]
    for y0,y1 in bands:
        sub=hard[y0:y1]; xs=np.where(sub.sum(0)>0)[0]
        rows.append([y0+Y0,y1+Y0,int(xs.min())+X0,int(xs.max())+X0+1])
    return (im,bg,diff,rows,tx1),'ok'

def merge_to(rows,n):
    """mehr Bänder als Zutaten -> die engsten Nachbarn zusammenlegen"""
    rows=[list(r) for r in rows]
    while len(rows)>n:
        gaps=[rows[i+1][0]-rows[i][1] for i in range(len(rows)-1)]
        i=int(np.argmin(gaps))
        a,b=rows[i],rows[i+1]
        rows[i:i+2]=[[a[0],b[1],min(a[2],b[2]),max(a[3],b[3])]]
    return rows

def split_to(rows,n,diff,x0,x1):
    """weniger Bänder als Zutaten -> höchstes Band am Profil-Minimum teilen"""
    rows=[list(r) for r in rows]
    prof=ndi.gaussian_filter1d((diff[:,x0:x1]>HI).sum(1).astype(float),3)
    tries=0
    while len(rows)<n and tries<20:
        tries+=1
        i=int(np.argmax([r[1]-r[0] for r in rows]))
        y0,y1=rows[i][0],rows[i][1]
        if y1-y0<200: break
        seg=prof[y0+60:y1-60]
        if len(seg)<5: break
        cut_y=y0+60+int(np.argmin(seg))
        a=[y0,cut_y,rows[i][2],rows[i][3]]; b=[cut_y,y1,rows[i][2],rows[i][3]]
        rows[i:i+1]=[a,b]
    return rows

def cut(im,bg,diff,row,pad=14,tx1=268,ytop=0,ybot=None):
    """Objekt = von Kanten umschlossene Fläche (Sobel auf der Luminanz + deutliche Farbabweichung, Löcher gefüllt);
    so werden auch weiße Schalen auf hellgrauem Grund vollständig deckend. Der weiche dunkle Schein um die
    Original-Kacheln wird als multiplikativer Schatten übernommen (Alpha = relative Abdunklung, Farbe schwarz).
    Kantenpixel: Alpha relativ zum lokalen Objektkontrast, Farbe entmischt."""
    y0,y1,x0,x1=row
    if ybot is None: ybot=im.shape[0]
    y0=max(ytop,y0-pad); y1=min(ybot,y1+pad); x0=max(0,x0-pad); x1=min(tx1,x1+pad)
    d=diff[y0:y1,x0:x1]; p=im[y0:y1,x0:x1]; b=bg[y0:y1][:,None,:]
    dm=ndi.median_filter(d,size=3)
    lum=ndi.median_filter(p.mean(2),size=3); blum=b.mean(2)
    gx=ndi.sobel(lum,axis=1); gy=ndi.sobel(lum,axis=0); g=np.hypot(gx,gy)
    sat=p.max(2)-p.min(2)
    edges=(g>38)|(d>60)|(sat>40)
    edges=ndi.binary_closing(edges,iterations=2)
    obj=ndi.binary_fill_holes(edges)
    obj=ndi.binary_opening(obj,iterations=2)
    # größte Komponenten behalten (Krümel/Rauschen weg), alles >= 1 % der größten
    lab,n=ndi.label(obj)
    if n>1:
        sizes=ndi.sum(obj,lab,range(1,n+1)); big=sizes.max()
        keep=[i+1 for i,sz in enumerate(sizes) if sz>=0.01*big and sz>=40]
        obj=np.isin(lab,keep)
    core=ndi.binary_erosion(obj,iterations=1)
    edge=ndi.binary_dilation(obj,iterations=3)&~core
    allowed=ndi.binary_dilation(obj,iterations=40)
    a_shadow=np.clip(1-lum/np.maximum(blum,1)-0.015,0,1)          # relative Abdunklung -> Schatten (schwarz)
    if core.any():
        dsm=ndi.median_filter(d,size=5)
        idxc=ndi.distance_transform_edt(~core,return_distances=False,return_indices=True)
        D=np.maximum(dsm[idxc[0],idxc[1]],24)
        a_edge=np.clip(dm/D,0,1)
    else:
        a_edge=np.clip((dm-12)/(HI-12),0,1)
    a=a_shadow.copy()
    a=np.where(edge,np.maximum(a_edge,a_shadow*0.5),a)
    a=np.where(core,1.0,a)*allowed
    a=ndi.gaussian_filter(a,0.6)
    a=np.where(a<0.03,0,a)
    a3=a[:,:,None]
    unmixed=np.clip((p-(1-a3)*b)/np.maximum(a3,0.05),0,255)
    isobj=core|(edge&(a_edge>=a_shadow*0.5))
    col=np.where(isobj[:,:,None],np.where(a3>0.1,unmixed,p),np.zeros_like(p))   # Schatten = schwarz mit Alpha
    # Kantenpixel zur Farbe des nächsten Kernpixels ziehen (weiße Anti-Aliasing-Säume der Originalkacheln dämpfen)
    if core.any():
        colcore=col[idxc[0],idxc[1]]
        band=(edge&isobj)[:,:,None]
        col=np.where(band,0.45*col+0.55*colcore,col)
    col=np.clip(col,0,255)
    tr=~isobj
    if tr.any() and (~tr).any():
        idx=ndi.distance_transform_edt(tr,return_distances=False,return_indices=True)
        col=np.where(tr[:,:,None]&(a3<=0.03),col[idx[0],idx[1]],col)
    rgba=np.dstack([col,a*255]).astype(np.uint8)
    return Image.fromarray(rgba,'RGBA')

if __name__=='__main__':
    R=json.load(open(f'{REPO}/archiv/rezepte.json'))
    byboard={}
    for r in R:
        bb=r.get('bild_board')
        if bb: byboard[os.path.basename(bb)]=r
    # Zuordnung voller Boards: boards/G86-Key.jpg <-> archiv/boards/g86_G86Key.jpg
    files=sorted(glob.glob(f'{REPO}/boards/G*.jpg'))+sorted(glob.glob(f'{REPO}/boards/[KHO][HK]*.jpg'))
    log=open(f'{OUT}/../log.txt','w'); meta=[]
    for f in files:
        base=os.path.basename(f)[:-4]            # G86-BamiGoreng
        m=re.match(r'(G\d+)-(.*)',base)
        if m: ser,key=m.group(1).lower(),m.group(1)+m.group(2)   # g86, G86BamiGoreng
        else: ser,key='gk',base
        r=byboard.get(f'{ser}_{key}.jpg')
        if r is None:
            # Suche nach key
            cands=[x for x in R if x['key']==key]
            r=cands[0] if cands else None
        if r is None: log.write(f'{base}\tkein Rezept\n'); continue
        res,st=extract(f)
        if res is None: log.write(f'{base}\t{st}\n'); continue
        im,bg,diff,rows,tx1=res
        zut=r['zutaten']
        if len(rows)>len(zut): rows=merge_to(rows,len(zut))
        if len(rows)<len(zut): rows=split_to(rows,len(zut),diff,X0,tx1)
        if len(rows)!=len(zut) or any(b-a>300 for a,b,_,_ in rows):
            log.write(f'{base}\tReihen {len(rows)} != Zutaten {len(zut)}\t{[(a,b) for a,b,_,_ in rows]}\n'); continue
        for i,(row,z) in enumerate(zip(rows,zut)):
            name=norm(z['zutat'])
            ytop=rows[i-1][1] if i>0 else 0
            ybot=rows[i+1][0] if i+1<len(rows) else im.shape[0]
            t=cut(im,bg,diff,row,tx1=tx1,ytop=ytop,ybot=ybot)
            fn=f'{OUT}/{name}__{base}_{i}.png'; t.save(fn)
            meta.append(dict(name=name,zutat=z['zutat'],board=base,i=i,row=row,w=t.width,h=t.height,clip=bool(row[3]+14>=tx1)))
        log.write(f'{base}\tok {len(rows)}\n')
    json.dump(meta,open(f'{OUT}/../meta.json','w'),ensure_ascii=False)
    print('crops',len(meta))
