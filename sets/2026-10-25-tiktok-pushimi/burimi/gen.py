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

# 1: Canta per nesër, ora 21:50
bgA='linear-gradient(180deg,#1E1B22 0%,#26212A 60%,#2E2723 100%)'
floor=D(0,1760,W,160,'background:#171319')
lamp=glow(1080*0+840,1480,420,.26,'255,210,140')+D(1080*0+800,1480,80,300,'background:#2E2A2A')+D(1080*0+730,1400,220,100,'background:#C99A4E;border-radius:24px 24px 6px 6px')
bag=D(1080*1+300,1560,420,230,'background:linear-gradient(180deg,#3F6259,#2E4A43);border-radius:40px 40px 20px 20px')+D(1080*1+380,1500,260,70,'border:14px solid #2E4A43;border-bottom:none;border-radius:60px 60px 0 0')+D(1080*1+300,1640,420,12,'background:#223A35')
items=D(1080*2+260,1690,150,70,'background:#E8B96C;border-radius:10px')+D(1080*2+460,1620,120,150,'background:#8FB8A8;border-radius:60px 60px 10px 10px')+D(1080*2+620,1700,170,50,'background:#B9825A;border-radius:25px')+D(1080*2+700,1660,12,70,'background:#EDE6D2')
extra=D(1080*3+420,1700,120,60,'background:#EDE6D2;border-radius:30px 30px 10px 10px;opacity:.9')+D(1080*3+600,1660,90,100,'background:#D6A24C;border-radius:14px')
door=D(1080*4+600,1260,340,500,'background:#3A332F;border:10px solid #4A413B;border-radius:8px 8px 0 0')+D(1080*4+850,1500,20,20,'background:#D6A24C;border-radius:50%')
S=[slide(0,'dk','Ora 21:50 · Çanta për nesër','Përgatit çantën për nesër. <em>Dhe shton edhe një gjë „për çdo&nbsp;rast“.</em>','',HINT),
   slide(1,'dk','Brenda','Ngarkuesi, ombrella, ilaçi. <em>Sikur mund të parashikosh çdo&nbsp;gjë.</em>'),
   slide(2,'dk','Pastaj','Hap zinxhirin sërish. <em>Edhe një gjë të vogël, sa për çdo&nbsp;rast.</em>'),
   slide(3,'dk','Pse','Nuk po paketon çantën. <em>Po paketon&nbsp;qetësinë.</em>'),
   slide(4,'dk','E vërteta','Disa gjëra s’hyjnë në çantë. <em>Duhet t’ia thuash dikujt.</em>'),
   end(5,'Kur mendja s’paketohet, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-canta']=page(bgA,floor+lamp+bag+items+extra+door+''.join(S))

# 2: Pushimi, lista
W2=7560
bgB='linear-gradient(180deg,#F6F0DF 0%,#F0E6CC 55%,#E6D6B0 100%)'
sea=D(0,1330,W2,180,'background:linear-gradient(180deg,#9FC6C4,#7FB0B2)')+D(0,1510,W2,410,'background:linear-gradient(180deg,#E8D4A6,#DCC48E)')
sun=glow(1080*5+300,420,700,.35,'255,226,160')
stones=''
for i in range(1,6):
    x=i*1080+520; gold=(i==4)
    col='#F3D9A0' if gold else '#EFE9DC'; bd='#D6A24C' if gold else '#CFC4AE'
    stones+=D(x,1560,260,170,f'background:{col};border:8px solid {bd};border-radius:50% 50% 46% 46%;box-shadow:0 10px 22px rgba(120,90,50,.15)')
    stones+=D(x,1560,260,170,f"font-family:'Fraunces',serif;font-weight:600;font-size:90px;text-align:center;line-height:170px;color:{'#B9862F' if gold else '#9C8F78'}",str(i))
umb=D(1080*0+760,1300,10,300,'background:#8A6A3F')+D(1080*0+640,1230,260,90,'background:#C77B33;border-radius:130px 130px 0 0')
S=[slide(0,'lt','Kur kemi pushim','5 gjëra që i bëjmë kur kemi pushim. <em>E katërta është faji.</em>','',HINT),
   slide(1,'lt','E para','Planifikojmë më shumë <em>se sa mund të&nbsp;bëjmë.</em>'),
   slide(2,'lt','E dyta','Ditën e parë <em>s’pushojmë&nbsp;ende.</em>'),
   slide(3,'lt','E treta','Shikojmë postën e punës <em>„vetëm një&nbsp;herë“.</em>'),
   slide(4,'lt','E katërta','Ndihemi fajtorë <em>që s’po bëjmë&nbsp;asgjë.</em>','Sikur pushimi duhet të fitohet çdo ditë.'),
   slide(5,'lt','E pesta','Ditën e fundit <em>fillojmë të&nbsp;pushojmë.</em>'),
   end(6,'Kur s’ta lejon vetja të pushosh, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['02-pushimi']=page(bgB,sun+sea+umb+stones+''.join(S),w=W2)

# 3: Mbremje me shi, ora 20:30
bgC='linear-gradient(180deg,#18222E 0%,#1F2C3A 60%,#26343F 100%)'
rain=''.join(D(x,y,3,50+(x*7)%40,'background:rgba(170,200,220,.28);border-radius:2px') for x in range(40,W,70) for y in (160+(x*13)%200,520+(x*17)%260,900+(x*11)%240))
win=D(1080*1+320,1030,440,560,'background:linear-gradient(180deg,#2E4558,#41596B);border:16px solid #4A5A63;border-radius:6px')+D(1080*1+526,1030,16,560,'background:#4A5A63')+D(1080*1+300,1590,480,24,'background:#5A6A73;border-radius:6px')
drops=''.join(D(1080*1+350+k*60,1070+(k*53)%380,8,36,'background:rgba(200,225,240,.4);border-radius:4px') for k in range(7))
cup=D(1080*2+260,1530,120,90,'background:#FAF7F1;border-radius:6px 6px 26px 26px')+D(1080*2+372,1550,40,50,'border:12px solid #FAF7F1;border-left:none;border-radius:0 30px 30px 0')+D(1080*2+300,1460,10,60,'background:rgba(255,255,255,.55);border-radius:5px;filter:blur(3px)')+glow(1080*2+320,1560,300,.22,'255,210,140')
lampw=glow(1080*3+700,1450,400,.30,'255,210,140')+D(1080*3+660,1470,80,320,'background:#2E2A2A')+D(1080*3+590,1390,220,100,'background:#C99A4E;border-radius:24px 24px 6px 6px')
floor=D(0,1790,W,130,'background:#10181F')
S=[slide(0,'dk','Ora 20:30 · Bie shi','Gjithçka është në rregull. <em>Por mendja pret që diçka të shkojë&nbsp;keq.</em>','',HINT),
   slide(1,'dk','Dritarja','Pikat rrëshqasin ngadalë. <em>Ti rri e&nbsp;shikon.</em>'),
   slide(2,'dk','Çaji','Pi çajin e ngrohtë. <em>Dhe e ndjen sikur pret një&nbsp;lajm.</em>'),
   slide(3,'dk','Pse ndodh','Kur për një kohë të gjatë je ruajtur, <em>qetësia të duket e&nbsp;dyshimtë.</em>'),
   slide(4,'dk','E vërteta','S’ke pse ta shpjegosh sonte. <em>Mjafton ta vësh&nbsp;re.</em>'),
   end(5,'Kur qetësia nuk të qetëson, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-shi']=page(bgC,rain+floor+win+drops+cup+lampw+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
