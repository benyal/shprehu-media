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

# 1: Televizori, ora 21:10
bgA='linear-gradient(180deg,#10161C 0%,#141C24 60%,#1A222A 100%)'
tvglow=glow(1080*1+540,1560,760,.32,'120,170,210')
tv=D(1080*1+180,1420,720,330,'background:linear-gradient(180deg,#2B4A5E,#1E3446);border:12px solid #2A3038;border-radius:12px')+D(1080*1+500,1750,80,50,'background:#2A3038')+D(1080*1+380,1796,320,16,'background:#2A3038;border-radius:8px')
tv+=D(1080*1+260,1500,260,18,'background:rgba(201,214,220,.35);border-radius:9px')+D(1080*1+260,1540,440,18,'background:rgba(201,214,220,.25);border-radius:9px')+D(1080*1+260,1580,360,18,'background:rgba(201,214,220,.25);border-radius:9px')
floor=D(0,1812,W,108,'background:#0B1015')
couch=D(1080*3+120,1600,780,200,'background:#2E3A3C;border-radius:60px 60px 16px 16px')+D(1080*3+160,1520,700,120,'background:#26312F;border-radius:60px 60px 10px 10px')+D(1080*3+200,1560,160,120,'background:#8FB8A8;opacity:.5;border-radius:30px')
remote=D(1080*2+420,1740,34,120,'background:#20272E;border-radius:10px')+D(1080*2+380,1790,300,16,'background:#2A3038;border-radius:8px')
S=[slide(0,'dk','Ora 21:10 · Televizori','Ndez televizorin. <em>Por s’po e&nbsp;shikon.</em>','Vetëm që shtëpia të ketë zë.',HINT),
   slide(1,'dk','Zhurma','Një zë flet në dhomë. <em>Dhe heshtja ndihet pak më&nbsp;pak.</em>'),
   slide(2,'dk','Kanalet','Ndërron kanalin dy herë. <em>Pastaj e le në të&nbsp;parin.</em>'),
   slide(3,'dk','Pse ndodh','Heshtja e shtëpisë peshon më shumë <em>kur ke menduar gjithë&nbsp;ditën.</em>'),
   slide(4,'dk','E vërteta','S’ke nevojë për program. <em>Ke nevojë që dikush të të&nbsp;dëgjojë.</em>'),
   end(5,'Kur televizori s’mjafton, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-televizori']=page(bgA,tvglow+floor+tv+remote+couch+''.join(S))

# 2: Komplimentet, lista
W2=7560
bgB='linear-gradient(180deg,#F6F2EA 0%,#F2EADC 100%)'
line=D(0,1560,W2,16,'background:#D9CDB6;border-radius:8px')
bub=''
for i in range(1,6):
    x=i*1080+520; gold=(i==4)
    col='#D6A24C' if gold else '#B8AA92'
    bub+=D(x,1250,300,200,f"background:{'#FBF1D8' if gold else '#FFFFFF'};border:10px solid {col};border-radius:44px 44px 44px 8px")
    bub+=D(x+10,1250,280,200,f"font-family:'Fraunces',serif;font-weight:600;font-size:96px;line-height:200px;text-align:center;color:{'#B9862F' if gold else '#9C8F78'}",str(i))
    bub+=D(x+40,1560,10,0,'')
S=[slide(0,'lt','Kur dikush të bën kompliment','5 mënyra si i refuzojmë komplimentet. <em>E katërta e bëjmë pa e&nbsp;kuptuar.</em>','',HINT),
   slide(1,'lt','E para','Themi „ah, s’është gjë“. <em>Edhe pse ishte puna e gjithë&nbsp;javës.</em>'),
   slide(2,'lt','E dyta','Themi „e kam blerë me zbritje“. <em>Sikur të na pyesnin për&nbsp;çmimin.</em>'),
   slide(3,'lt','E treta','Themi „edhe ti je shumë i mirë“. <em>Që ta kthejmë&nbsp;menjëherë.</em>'),
   slide(4,'lt','E katërta','Ndërrojmë temën para se ta ndjejmë. <em>„Po ti, si&nbsp;je?“</em>','Dhe fjalën e mirë e lëmë pa e marrë.'),
   slide(5,'lt','E pesta','Natën i përsërisim në mendje. <em>Një nga një, ngadalë.</em>'),
   end(6,'Kur është e vështirë të pranosh, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['02-komplimentet']=page(bgB,line+bub+''.join(S),w=W2)

# 3: Pas mbarimit, ora 16:20
bgC='linear-gradient(180deg,#F3E4CB 0%,#EAD3AE 60%,#DDBF93 100%)'
sun=glow(1080*3+300,640,760,.38,'255,226,160')
desk=D(0,1650,W,270,'background:linear-gradient(180deg,#9A7650,#84633F)')+D(0,1640,W,16,'background:#B08D60')
lap=D(1080*1+200,1610,420,26,'background:#C9C2B2;border-radius:6px')+D(1080*1+220,1590,380,26,'background:#B8B2A2;border-radius:6px')
papers=''.join(D(1080*2+260+k*6,1560-k*22,300,22,'background:#FAF7F1;border:2px solid #E5DFD3;border-radius:2px') for k in range(5))
cup=D(1080*3+520,1540,110,100,'background:#FAF7F1;border-radius:6px 6px 26px 26px')+D(1080*3+620,1560,40,50,'border:12px solid #FAF7F1;border-left:none;border-radius:0 30px 30px 0')
win=D(1080*4+560,1000,360,460,'background:linear-gradient(180deg,#F8E3B0,#F2C98C);border:14px solid #CDBA9B;border-radius:6px;box-shadow:0 0 90px 24px rgba(255,226,160,.4)')+D(1080*4+733,1000,14,460,'background:#CDBA9B')
plant=D(1080*0+820,1520,90,120,'background:#8A6A3F;border-radius:6px 6px 24px 24px')+D(1080*0+840,1400,50,140,'background:#6E9C8C;border-radius:25px 25px 6px 6px')+D(1080*0+800,1440,60,90,'background:#8FB8A8;border-radius:30px;transform:rotate(-30deg)')
S=[slide(0,'lt','Ora 16:20 · Mbarove','Mbarove diçka që e prisje me muaj. <em>Dhe s’ndihesh siç&nbsp;mendoje.</em>','',HINT),
   slide(1,'lt','Tryeza','Mbyll laptopin ngadalë. <em>Pret që diçka të ndodhë brenda&nbsp;teje.</em>'),
   slide(2,'lt','Ndjesia','S’është gëzim, as trishtim. <em>Është një heshtje që s’e&nbsp;prisje.</em>'),
   slide(3,'lt','Pse ndodh','Gjithë kohës mendja ishte te rruga. <em>Tani ka mbërritur dhe s’di ku të&nbsp;shkojë.</em>'),
   slide(4,'lt','E vërteta','Edhe pas një suksesi mund të ndihesh bosh. <em>Kjo s’do të thotë se diçka s’shkon.</em>'),
   end(5,'Kur mbarimi nuk ndihet siç duhet, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-mbarimi']=page(bgC,sun+win+plant+desk+lap+papers+cup+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
