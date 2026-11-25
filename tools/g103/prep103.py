# -*- coding: utf-8 -*-
"""Hero vorbereiten: gewähltes Rohbild (raw/) spiegeln / skalieren / verschieben, damit das Gericht frei neben
Kachelspalte, Titel, Badge und Vorher-Nachher-Foto liegt. Ränder werden aus der Bildkante fortgesetzt und weichgezeichnet
(keine sichtbare Naht wie beim reinen CSS-Verschieben). Angaben in Board-Pixeln (1080x1350); s skaliert um die Ecke rechts unten.
Danach wird der Freisteller neu berechnet (Text-Maske liegt dann in den richtigen Koordinaten)."""
import cv2, numpy as np, json, os, sys
D=os.path.dirname(os.path.abspath(__file__))
KEYS=['KlossKasseler','KlossScheiben','KlossLauch','WinterWoelkchen','DoenerKartoffeln','NudelsalatNacht','MilchschnitteBowl','Gewuerzkuchen','BlitzKaesekuchen','Zupfkuchen','GyrosBowl','KaeseLauchSuppe']
T={'BlitzKaesekuchen':dict(s=0.80,glatt=True),'DoenerKartoffeln':dict(s=0.66,dy=20,glatt=True),'KlossScheiben':dict(s=0.70,glatt=True),'Gewuerzkuchen':dict(s=0.74,glatt=True),
   'GyrosBowl':dict(s=0.72,glatt=True,cl=(150,100,500)),'KaeseLauchSuppe':dict(s=0.74,glatt=True),'MilchschnitteBowl':dict(s=0.74,glatt=True),'NudelsalatNacht':dict(s=0.72,glatt=True),
   'Zupfkuchen':dict(s=0.72,glatt=True),'KlossKasseler':dict(s=0.78,glatt=True),'WinterWoelkchen':dict(s=0.74,glatt=True),'KlossLauch':dict(s=0.70,glatt=True)}
def prep(key):
    sel=json.load(open(f'{D}/hero/_auswahl.json'))[key]
    im=cv2.imread(f'{D}/raw/{sel}.jpg'); t=T.get(key,{})
    if t.get('mirror'): im=np.ascontiguousarray(im[:,::-1])
    if t.get('ct'):                      # n: die obersten n Zeilen des Rohbilds durch Zeile n ersetzen (dunkler Gegenstand am oberen Bildrand, der sonst als Streifen hinter den Titel verlängert würde)
        im=im.copy(); im[:t['ct']]=im[t['ct']:t['ct']+1]
    if t.get('cl'):                      # (n, y0, y1) in Rohbild-Pixeln: Gegenstand/Licht am linken Bildrand entfernen (Spalte n nach links fortsetzen)
        n,y0,y1=t['cl']; im=im.copy(); im[y0:y1,:n]=im[y0:y1,n:n+1]
    if t.get('cr'):                      # (n, y0, y1) in Rohbild-Pixeln: dunkle Wandecke am rechten Bildrand entfernen (Spalte w-n-1 nach rechts fortsetzen)
        n,y0,y1=t['cr']; im=im.copy(); im[y0:y1,-n:]=im[y0:y1,-n-1:-n]
    if t.get('vf'):                      # (x0, x1, y0, y1) in Rohbild-Pixeln (nach dem Spiegeln): Gegenstand übermalen – jede Spalte läuft gerade von Zeile y0 nach Zeile y1 (für Reste am Bildrand, die `cl` nicht greift, weil daneben schon das Gericht liegt)
        x0_,x1_,y0_,y1_=t['vf']; im=im.copy().astype(np.float32); w_=np.linspace(0,1,y1_-y0_)[:,None,None]
        im[y0_:y1_,x0_:x1_]=im[y0_:y0_+1,x0_:x1_]*(1-w_)+im[y1_:y1_+1,x0_:x1_]*w_
        im[y0_:y1_,x0_:x1_]=cv2.GaussianBlur(im[y0_:y1_,x0_:x1_],(0,0),5); im=im.astype(np.uint8)
    if t.get('holz'):                    # (Polygon, x_achse, y_achse) in Rohbild-Pixeln (nach dem Spiegeln): Serviette/Tuch am unteren Bildrand durch Tischholz ersetzen –
        poly,xa,ya=t['holz']; hh,ww=im.shape[:2]; src=im.copy()   # unterhalb y_achse wird das Holz rechts von x_achse nach links gespiegelt, darüber die gefüllten Zeilen nach oben (Maserung läuft senkrecht weiter)
        sx=np.clip(2*xa-1-np.arange(xa),0,ww-1); src[ya:,:xa]=im[ya:,sx]
        n=hh-ya; k=(ya-1-np.arange(ya))%(2*n); sy=ya+np.where(k<n,k,2*n-1-k); src[:ya,:xa]=src[sy][:,:xa]
        m=np.zeros((hh,ww),np.float32); cv2.fillPoly(m,[np.array(poly,np.int32)],1.0); m=cv2.GaussianBlur(m,(0,0),3)[:,:,None]
        im=(im*(1-m)+src*m).astype(np.uint8)
    if t.get('keil'):                    # (x_von, [(y, x_kante), …]): Rest zwischen übermalter Fläche und Rand des Gerichts zeilenweise mit der Farbe links daneben füllen (Kante des Gerichts als Stützpunkte)
        xf,kn=t['keil']; im=im.copy(); ys=[k[0] for k in kn]; xs=[k[1] for k in kn]
        for y in range(ys[0],ys[-1]+1):
            xe=int(np.interp(y,ys,xs))-2
            if xe>xf: im[y,xf:xe]=im[y,xf-1]
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
    if t.get('glatt') and y0>0:          # oben angesetzter Rand ohne Lichter-Streifen: die erste echte Zeile wird von hellen Punkten befreit (Öffnung über 220 px) und stark geglättet,
        row=out[y0:y0+1].copy(); k=int(220*f)|1                       # damit füllt sich der Rand; die obersten 70 px des echten Bildes blenden weich hinein (angeschnittene Lichter laufen aus)
        row=cv2.GaussianBlur(cv2.morphologyEx(row,cv2.MORPH_OPEN,np.ones((1,k),np.uint8)),(0,0),sigmaX=60*f,sigmaY=0.1)
        ramp=np.clip((np.arange(h)-y0)/(70*f),0,1)[:,None,None]
        out=(out*ramp+np.repeat(row,h,axis=0)*(1-ramp)).astype(np.uint8)
    cv2.imwrite(f'{D}/hero/{key}.jpg',out,[cv2.IMWRITE_JPEG_QUALITY,95])
    mp=f'{D}/hero/_meta.json'; M=json.load(open(mp)) if os.path.exists(mp) else {}
    M[key]=dict(x0=round(x0/f,1),x1=round((x0+rw)/f,1),y0=round(y0/f,1),y1=round((y0+rh)/f,1))   # echte Bildfläche in Board-Pixeln (außerhalb = angesetzter Rand)
    json.dump(M,open(mp,'w'),indent=1)
    for p in (f'{D}/hero_cut/{key}.png',f'{D}/hero_cut_m/{key}.png'):
        if os.path.exists(p): os.remove(p)
    print('prep',key,sel,t)
if __name__=='__main__':
    for k in (sys.argv[1:] or list(json.load(open(f'{D}/hero/_auswahl.json')))): prep(k)
