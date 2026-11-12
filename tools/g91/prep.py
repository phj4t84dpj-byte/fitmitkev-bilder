# -*- coding: utf-8 -*-
"""Hero vorbereiten: gewähltes Rohbild (raw/) spiegeln / skalieren / verschieben, damit das Gericht frei neben
Kachelspalte, Titel, Badge und Vorher-Nachher-Foto liegt. Ränder werden aus der Bildkante fortgesetzt und weichgezeichnet
(keine sichtbare Naht wie beim reinen CSS-Verschieben). Angaben in Board-Pixeln (1080x1350); s skaliert um die Ecke rechts unten.
Danach wird der Freisteller neu berechnet (Text-Maske liegt dann in den richtigen Koordinaten)."""
import cv2, numpy as np, json, os, sys
D=os.path.dirname(os.path.abspath(__file__))
T={
 'MarmorBowl':        dict(s=0.72, dx=30),
 'Pide':              dict(s=0.72),
 'Poffertjes':        dict(s=0.64, dx=30),
 'OfenOmelett':       dict(s=0.76),
 'Milchreis':         dict(s=0.68, dx=40, dy=15),
 'SmashWrap':         dict(s=0.76, dx=20),
 'HimbeerSkyr':       dict(s=0.66, dx=20, dy=10),
 'Champignons':       dict(s=0.74),
 'ApfelkuchenBowl':   dict(s=0.74, dx=30),
 'Souvlaki':          dict(s=0.76, dy=10),
 'LebkuchenBlech':    dict(s=0.68, dy=20),
 'Reibekuchen':       dict(s=0.86, dx=51, dy=-50),
 'Crepes':            dict(s=0.72, dx=20, dy=15),
 'Plaetzchen':        dict(s=0.78),
 'Langos':            dict(s=0.74),
 'Eierschecke':       dict(s=0.64, dx=20),
 'Gulasch':           dict(s=0.72),
 'Rouladen':          dict(s=0.76),
 'FrankfurterKranz':  dict(s=0.66, dx=20, dy=25),
 'Schupfnudeln':      dict(s=0.74),
}
def prep(key):
    sel=json.load(open(f'{D}/hero/_auswahl.json'))[key]
    im=cv2.imread(f'{D}/raw/{sel}.jpg'); t=T.get(key,{})
    if t.get('mirror'): im=np.ascontiguousarray(im[:,::-1])
    if t.get('cl'):                      # (n, y0, y1) in Rohbild-Pixeln: Gegenstand/Licht am linken Bildrand entfernen (Spalte n nach links fortsetzen)
        n,y0,y1=t['cl']; im=im.copy(); im[y0:y1,:n]=im[y0:y1,n:n+1]
    h,w=im.shape[:2]; f=w/1080; s=t.get('s',1.0)
    rw,rh=round(w*s),round(h*s)
    rs=im if s==1.0 else cv2.resize(im,(rw,rh),interpolation=cv2.INTER_AREA if s<1 else cv2.INTER_LANCZOS4)
    x0=w-rw+round(t.get('dx',0)*f); y0=h-rh+round(t.get('dy',0)*f)
    xi=np.arange(w)-x0; yi=np.arange(h)-y0
    if t.get('pad','rep')=='ref':        # seitlich spiegeln statt die Randspalte zu wiederholen: Lichter bleiben rund, Formen/Tischkanten laufen weiter (keine Streifen)
        xr=np.where(xi<0,-xi-1,xi); xr=np.where(xr>=rw,2*rw-xr-1,xr); xr=np.clip(xr,0,rw-1)
    else: xr=np.clip(xi,0,rw-1)          # pad='rep': Randspalte wiederholen (besser, wenn ein runder Teller am Rand angeschnitten ist)
    out=rs[np.clip(yi,0,rh-1)][:,xr]
    # Links/rechts wird die Kantenspalte unverändert fortgesetzt (Tischkante/Horizont laufen gerade weiter);
    # nur der oben/unten angesetzte Streifen wird weichgezeichnet (sonst senkrechte Lichterstreifen).
    valid=np.repeat(((yi>=0)&(yi<rh)).astype(np.float32)[:,None],w,axis=1)
    a=np.ones((h,w),np.float32)
    if valid.min()<1: a=np.clip((cv2.GaussianBlur(valid,(0,0),8)-0.5)*2,0,1)   # oben/unten: weicher Übergang erst außerhalb des echten Bildes
    if t.get('soft',True):               # seitlich: direkt an der Bildkante noch scharf (kein Sprung), nach außen über 150 px zunehmend weich (Streifen verlaufen)
        d=np.maximum(np.maximum(-xi,xi-(rw-1)),0).astype(np.float32)[None,:]
        a=np.minimum(a,np.clip(1-d/(150*f),0,1))
    if a.min()<1:
        bl=cv2.GaussianBlur(out,(0,0),28)
        out=(out*a[:,:,None]+bl*(1-a[:,:,None])).astype(np.uint8)
    cv2.imwrite(f'{D}/hero/{key}.jpg',out,[cv2.IMWRITE_JPEG_QUALITY,95])
    mp=f'{D}/hero/_meta.json'; M=json.load(open(mp)) if os.path.exists(mp) else {}
    M[key]=dict(x0=round(x0/f,1),x1=round((x0+rw)/f,1),y0=round(y0/f,1),y1=round((y0+rh)/f,1))   # echte Bildfläche in Board-Pixeln (außerhalb = angesetzter Rand)
    json.dump(M,open(mp,'w'),indent=1)
    for p in (f'{D}/hero_cut/{key}.png',f'{D}/hero_cut_m/{key}.png'):
        if os.path.exists(p): os.remove(p)
    print('prep',key,sel,t)
if __name__=='__main__':
    for k in (sys.argv[1:] or list(json.load(open(f'{D}/hero/_auswahl.json')))): prep(k)
