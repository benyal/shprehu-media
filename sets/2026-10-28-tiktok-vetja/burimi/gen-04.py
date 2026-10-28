import random, sys
SK='/home/user/Shprehu-3.5/.claude/skills/shprehu-social-ads'
W=6480
CSS='''
html,body{width:6480px;height:1920px;overflow:hidden}
.pano{position:absolute;left:0;top:0;width:6480px;height:1920px;overflow:hidden}
.slide{position:absolute;top:0;width:1080px;height:1920px}
.safe{position:absolute;left:96px;right:150px;top:250px;bottom:460px;display:flex;flex-direction:column}
.tag{font-size:30px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;display:flex;gap:18px;align-items:center;margin-bottom:44px}

h1{font-family:'Fraunces',serif;font-weight:600;font-size:108px;line-height:1.05;letter-spacing:-0.02em}
h1 em{font-style:italic;font-weight:500}
p{font-size:46px;line-height:1.38;margin-top:40px}
.hint{margin-top:auto;font-size:34px;font-weight:600;letter-spacing:.02em}
.dk{color:#FAF7F1}.dk p{color:rgba(250,247,241,.86)}.dk .tag{color:#8FB8A8}.dk h1 em{color:#E8B96C}.dk .hint{color:#E8B96C}
.lt{color:#221F1C}.lt p{color:#4A443C}.lt .tag{color:#3F6259}.lt h1 em{color:#3F6259}.lt .hint{color:#3F6259}
.end{position:absolute;top:0;width:1080px;height:1920px;background:#2E4A43;color:#FAF7F1}
.end .safe{justify-content:center}
.end img{width:150px;height:150px;border-radius:38px;box-shadow:0 16px 50px rgba(0,0,0,.3)}
.end h1{margin-top:56px;font-size:104px}.end h1 em{color:#E8B96C}
.end .tags{margin-top:34px;font-size:38px;color:#8FB8A8;font-weight:500}
.end .url{margin-top:48px;font-size:60px;font-weight:700}
.end .fine{margin-top:44px;font-size:28px;line-height:1.45;color:rgba(250,247,241,.72)}
.abs{position:absolute}
'''
def head():
    return f'<!doctype html><html lang="sq"><head><meta charset="utf-8"><link rel="stylesheet" href="file://{SK}/assets/brand.css"><style>{CSS}'
def slide(i,cls,tag,h,sub='',hint='',extra=''):
    return (f'<div class="slide {cls}" style="left:{i*1080}px"><div class="safe"><div class="tag">{tag}</div><h1>{h}</h1>'
            f'{f"<p>{sub}</p>" if sub else ""}{extra}{f"<div class=hint>{hint}</div>" if hint else ""}</div></div>')
def end(i,h):
    return (f'<div class="end" style="left:{i*1080}px"><div class="safe"><img src="file://{SK}/assets/logo-mark.png" alt=""><h1>{h}</h1>'
            '<div class="tags">Anonim · Falas · Në shqip</div><div class="url">shprehu.cc</div>'
            '<div class="fine">Shprehu nuk është shërbim urgjence. Në rrezik, telefono 112.</div></div></div>')
def page(bg,body,css=''):
    return head()+css+f'</style></head><body><div class="pano" style="background:{bg}">{body}</div></body></html>'
def D(x,y,w,h,style='',inner='',cls=''):
    return f'<div class="abs {cls}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{style}">{inner}</div>'
import math,random
sets={}
HINT='Rrëshqit →'
def page(bg,body,w=6480):
    return head().replace('6480px',f'{w}px')+f'</style></head><body><div class="pano" style="background:{bg}">{body}</div></body></html>'
def glow(x,y,r,a=.5,c='255,214,140'):
    return D(x-r,y-r,2*r,2*r,f'background:radial-gradient(circle,rgba({c},{a}),rgba({c},0) 66%);border-radius:50%')
W=6480

# 4: Tre sekondat e para, ora 07:00
bgD='linear-gradient(90deg,#F3D9B8 0%,#F6E6CC 18%,#F4EEE2 40%,#EEF1EA 70%,#E6EEE8 100%)'
sunD=glow(1080*0+760,1460,420,.65,'255,200,130')+D(1080*0+690,1390,140,140,'background:#F7C98A;border-radius:50%')
sill=D(0,1700,W,220,'background:linear-gradient(180deg,#E7DCC8,#D9CBB2)')
pillow=D(1080*0+120,1600,420,110,'background:#FAF7F1;border-radius:56px;box-shadow:0 10px 20px rgba(120,90,50,.12)')
birds=glow(1080*1+540,1450,380,.35,'255,215,150')+''.join(D(1080*1+x,y,130,46,f'border-top:6px solid #6B6152;border-radius:50% 50% 0 0;transform:rotate({r}deg)'.replace('6px','10px')) for x,y,r in [(260,1250,-8),(470,1170,6),(640,1300,-4),(380,1400,4)])
def card(x,y,label,col):
    return D(x,y,300,120,f"background:#FAF7F1;border-left:14px solid {col};border-radius:16px;box-shadow:0 12px 24px rgba(80,60,40,.12);font-family:Inter;font-weight:700;font-size:36px;color:#221F1C;line-height:120px;padding-left:28px;box-sizing:border-box",label)
cards=card(1080*2+120,1300,'Takimi','#8FB8A8')+card(1080*2+420,1450,'Mesazhi','#E8B96C')+card(1080*2+180,1600,'Fatura','#C98057')
bag=D(1080*3+360,1360,360,300,'background:#8A6A3F;border-radius:30px 30px 40px 40px;box-shadow:0 14px 26px rgba(80,60,40,.18)')+D(1080*3+450,1290,180,100,'border:18px solid #6E5232;border-bottom:none;border-radius:90px 90px 0 0')
win=D(1080*4+300,1200,480,480,'background:linear-gradient(180deg,#FFF1D2,#F4E6C8);border:18px solid #FAF7F1;border-radius:8px;box-shadow:0 10px 20px rgba(0,0,0,.06)')+glow(1080*4+540,1440,360,.45,'255,220,150')
S=[slide(0,'lt','Ora 07:00 · Sapo zgjohesh','Për tre sekonda s’mban mend asgjë. <em>Pastaj të kujtohen të&nbsp;gjitha.</em>','',HINT),
   slide(1,'lt','Sekonda e parë','Drita, jastëku, zogjtë jashtë. <em>Asnjë&nbsp;hall.</em>'),
   slide(2,'lt','Pastaj','Mendja i rendit një nga një: <em>takimi, mesazhi,&nbsp;fatura.</em>'),
   slide(3,'lt','Pse ndodh','Mendja zgjohet pak pas teje. <em>Dhe sjell me vete gjithë&nbsp;çantën.</em>'),
   slide(4,'lt','E vërteta','Ato tre sekonda janë të tuat. <em>Mund t’i zgjasësh me një frymë të&nbsp;thellë.</em>'),
   end(5,'Kur mendja zgjohet e rëndë, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['04-sekondat']=page(bgD,sunD+sill+pillow+birds+cards+bag+win+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
