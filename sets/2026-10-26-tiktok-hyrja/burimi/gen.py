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

# 1: Hyrja ne shtepi, ora 19:40
bgA='linear-gradient(180deg,#1B1F26 0%,#232830 60%,#2A2D2F 100%)'
floor=D(0,1770,W,150,'background:#141619')
door=D(1080*0+560,1180,400,590,'background:linear-gradient(180deg,#3B3A3C,#303032);border:12px solid #4A4849;border-radius:8px 8px 0 0')+D(1080*0+560,1180,400,590,'background:linear-gradient(90deg,rgba(255,214,140,.0),rgba(255,214,140,.0))')
ajar=D(1080*0+960,1200,160,560,'background:linear-gradient(90deg,rgba(255,214,140,.55),rgba(255,214,140,0));filter:blur(8px)')
shoes=''.join(D(1080*1+300+k*170,1720,130,52,'background:#2A2E33;border-radius:32px 32px 8px 8px') for k in range(3))
hookw=D(1080*2+300,1250,300,14,'background:#6B5645;border-radius:7px')+D(1080*2+340,1264,130,360,'background:linear-gradient(180deg,#3F6259,#2E4A43);border-radius:50px 50px 20px 20px')+D(1080*2+490,1264,90,260,'background:#8A6A3F;border-radius:40px 40px 14px 14px')
kitchen=glow(1080*4+560,1560,520,.35,'255,214,140')+D(1080*4+340,1240,440,530,'background:linear-gradient(180deg,#4A3F34,#6A5740);border:12px solid #3A3028;border-radius:8px 8px 0 0')+D(1080*4+380,1290,360,440,'background:linear-gradient(180deg,rgba(255,226,170,.55),rgba(255,226,170,.2))')
S=[slide(0,'dk','Ora 19:40 · Te dera','Hyn në shtëpi. <em>Dhe thua „jam këtu!“ me zë më të lartë se ndihesh.</em>','',HINT),
   slide(1,'dk','Zëri','Buzëqeshja del para teje. <em>Ti vjen pak më&nbsp;pas.</em>'),
   slide(2,'dk','Pse','Nuk gënjen askënd. <em>Po e mban shtëpinë të&nbsp;qetë.</em>'),
   slide(3,'dk','Pastaj','Ulesh një minutë në korridor. <em>Para se të futesh te të&nbsp;tjerët.</em>'),
   slide(4,'dk','E vërteta','Edhe forca ka orë të lodhura. <em>S’ke pse t’i fshehësh&nbsp;gjithmonë.</em>'),
   end(5,'Kur zëri del më i fortë se ti, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-hyrja']=page(bgA,floor+door+ajar+shoes+hookw+kitchen+''.join(S))

# 2: Harrimi i diteliindjes, lista
W2=7560
bgB='linear-gradient(180deg,#F6F2EA 0%,#F1E9DA 100%)'
shelf=D(0,1700,W2,18,'background:#CFC4AE')+D(0,1718,W2,202,'background:#E6DAC0')
gifts=''
for i in range(1,6):
    x=i*1080+470; gold=(i==4)
    col='#F3D9A0' if gold else '#FFFFFF'; bd='#D6A24C' if gold else '#CFC4AE'
    gifts+=D(x,1450,300,250,f'background:{col};border:8px solid {bd};border-radius:10px;box-shadow:0 12px 24px rgba(120,90,50,.12)')
    gifts+=D(x+130,1450,40,250,f'background:{bd};opacity:.55')+D(x,1550,300,40,f'background:{bd};opacity:.35')
    gifts+=D(x+60,1380,90,80,f'border:10px solid {bd};border-radius:50%')+D(x+150,1380,90,80,f'border:10px solid {bd};border-radius:50%')
    gifts+=D(x,1450,300,250,f"font-family:'Fraunces',serif;font-weight:600;font-size:96px;text-align:center;line-height:250px;color:{'#B9862F' if gold else '#9C8F78'};text-shadow:0 0 0 #fff",str(i))
S=[slide(0,'lt','Kur harron një ditëlindje','5 gjëra që i bëjmë kur harrojmë ditëlindjen e dikujt. <em>E katërta e njohim të&nbsp;gjithë.</em>','',HINT),
   slide(1,'lt','E para','Shikojmë njoftimin <em>tri orë më&nbsp;vonë.</em>'),
   slide(2,'lt','E dyta','Mendojmë gjatë: <em>„më fal“ apo&nbsp;„gëzuar“?</em>'),
   slide(3,'lt','E treta','E rishkruajmë dy herë <em>dhe e fshijmë një&nbsp;herë.</em>'),
   slide(4,'lt','E katërta','Shtojmë „me vonesë, por nga zemra“. <em>Sikur t’i shpëtonte çdo&nbsp;gjë.</em>'),
   slide(5,'lt','E pesta','Ndihemi keq <em>më shumë se sa e meriton&nbsp;gabimi.</em>'),
   end(6,'Kur faji rëndon më shumë se gabimi, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['02-diteliindja']=page(bgB,shelf+gifts+''.join(S),w=W2)

# 3: Pas telefonates, ora 21:50
bgC='linear-gradient(180deg,#1A2230 0%,#222E3E 60%,#2B3744 100%)'
floor=D(0,1790,W,130,'background:#11171F')
couch=D(1080*1+120,1590,800,200,'background:#35455A;border-radius:60px 60px 14px 14px')+D(1080*1+160,1500,720,120,'background:#2D3B4E;border-radius:60px 60px 10px 10px')
phone=glow(1080*2+420,1640,280,.30,'160,200,230')+D(1080*2+340,1590,170,300,'background:#10161C;border:6px solid #3A4654;border-radius:26px;transform:rotate(-70deg);transform-origin:center;opacity:1')+D(1080*2+405,1640,40,3,'background:rgba(190,220,240,.0)')
lampw=glow(1080*3+700,1450,420,.30,'255,210,140')+D(1080*3+660,1470,80,320,'background:#2E2A2A')+D(1080*3+590,1390,220,100,'background:#C99A4E;border-radius:24px 24px 6px 6px')
cup=D(1080*4+420,1700,110,90,'background:#FAF7F1;border-radius:6px 6px 26px 26px')+D(1080*4+522,1720,40,50,'border:12px solid #FAF7F1;border-left:none;border-radius:0 30px 30px 0')+D(1080*4+450,1630,10,60,'background:rgba(255,255,255,.5);border-radius:5px;filter:blur(3px)')
S=[slide(0,'dk','Ora 21:50 · Pas telefonatës','Mbyll telefonatën me dikë që e do. <em>Dhe dhoma duket më e&nbsp;heshtur.</em>','',HINT),
   slide(1,'dk','Ekrani','Telefoni shuhet ngadalë. <em>Zëri i tij ende s’ka dalë nga&nbsp;dhoma.</em>'),
   slide(2,'dk','Pse ndodh','Sa më shumë na mungon dikush, <em>aq më e madhe duket heshtja pas&nbsp;tij.</em>'),
   slide(3,'dk','Pastaj','Ulesh pak më gjatë. <em>Nuk e merr menjëherë një gjë&nbsp;tjetër.</em>'),
   slide(4,'dk','E vërteta','Kjo s’është vetmi e keqe. <em>Është dashuri që s’ka ku të shkojë&nbsp;sonte.</em>'),
   end(5,'Kur heshtja pas telefonatës rëndon, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-telefonata']=page(bgC,floor+couch+phone+lampw+cup+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
