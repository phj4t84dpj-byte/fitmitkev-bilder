# -*- coding: utf-8 -*-
"""Hero vorbereiten: gewähltes Rohbild (raw/) spiegeln / skalieren / verschieben, damit das Gericht frei neben
Kachelspalte, Titel, Badge und Vorher-Nachher-Foto liegt. Ränder werden aus der Bildkante fortgesetzt und weichgezeichnet
(keine sichtbare Naht wie beim reinen CSS-Verschieben). Angaben in Board-Pixeln (1080x1350); s skaliert um die Ecke rechts unten.
Danach wird der Freisteller neu berechnet (Text-Maske liegt dann in den richtigen Koordinaten)."""
import cv2, numpy as np, json, os, sys
D=os.path.dirname(os.path.abspath(__file__))
T={
 'NusseckenOats':       dict(s=0.80, dx=25),            # beide Gläser frei rechts neben Kacheln und Foto
 'Weckmann':            dict(mirror=True, dx=60, dy=50),# gespiegelt: zwei ganze Weckmänner sichtbar, der angeschnittene liegt unter den Kacheln
 'Mutzen':              dict(dx=70),
 'KoenigsbergerKlopse': dict(dx=80),
 'ZitronenBowl':        dict(mirror=True, s=0.72, dy=-40),  # ganze Form mit beiden Griffen frei; gespiegelt, damit die angeschnittene Zitrone am rechten Bildrand liegt
 'KokosMandelTiramisu': dict(s=0.80, dy=40),            # ganze Form mit beiden Griffen frei
 'Frikadellen':         dict(dx=65),
 'Reibekuchen':         dict(s=0.86, dx=51, dy=-50),    # alle drei Reibekuchen frei neben dem Foto UND Apfelmus-Schale ganz im Bild
 'GyrosAuflauf':        dict(dx=55),
 'Flammkuchen':         dict(s=0.84, dx=45),            # ganzer Flammkuchen frei, nichts hinter Badge/Foto
}
def prep(key):
    sel=json.load(open(f'{D}/hero/_auswahl.json'))[key]
    im=cv2.imread(f'{D}/raw/{sel}.jpg'); t=T.get(key,{})
    if t.get('mirror'): im=np.ascontiguousarray(im[:,::-1])
    h,w=im.shape[:2]; f=w/1080; s=t.get('s',1.0)
    rw,rh=round(w*s),round(h*s)
    rs=im if s==1.0 else cv2.resize(im,(rw,rh),interpolation=cv2.INTER_AREA if s<1 else cv2.INTER_LANCZOS4)
    x0=w-rw+round(t.get('dx',0)*f); y0=h-rh+round(t.get('dy',0)*f)
    xi=np.arange(w)-x0; yi=np.arange(h)-y0
    out=rs[np.clip(yi,0,rh-1)][:,np.clip(xi,0,rw-1)]
    # Links/rechts wird die Kantenspalte unverändert fortgesetzt (Tischkante/Horizont laufen gerade weiter);
    # nur der oben/unten angesetzte Streifen wird weichgezeichnet (sonst senkrechte Lichterstreifen).
    valid=np.repeat(((yi>=0)&(yi<rh)).astype(np.float32)[:,None],w,axis=1)
    if t.get('soft'): valid=valid*((xi>=0)&(xi<rw)).astype(np.float32)[None,:]   # auch den seitlichen Streifen weichzeichnen (wenn am Bildrand ein Gegenstand liegt)
    if valid.min()<1:
        a=cv2.GaussianBlur(valid,(0,0),8)[:,:,None]; a=np.clip((a-0.5)*2,0,1)   # weicher Übergang erst außerhalb des echten Bildes
        bl=cv2.GaussianBlur(out,(0,0),28)
        out=(out*a+bl*(1-a)).astype(np.uint8)
    cv2.imwrite(f'{D}/hero/{key}.jpg',out,[cv2.IMWRITE_JPEG_QUALITY,95])
    for p in (f'{D}/hero_cut/{key}.png',f'{D}/hero_cut_m/{key}.png'):
        if os.path.exists(p): os.remove(p)
    print('prep',key,sel,t)
if __name__=='__main__':
    for k in (sys.argv[1:] or list(T)): prep(k)
