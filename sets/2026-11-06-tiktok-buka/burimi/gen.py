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

HINT='Rrëshqit →'
def page(bg,body,w=6480):
    return head().replace('6480px',f'{w}px')+f'</style></head><body><div class="pano" style="background:{bg}">{body}</div></body></html>'
def glow(x,y,r,a=.5,c='255,214,140'):
    return D(x-r,y-r,2*r,2*r,f'background:radial-gradient(circle,rgba({c},{a}),rgba({c},0) 66%);border-radius:50%')
W=6480
sets={}

# 01 Buka e gjyshes (urtësi e gjyshes, ritual)
bgA='linear-gradient(180deg,#FAF7F1 0%,#F3EFE7 62%,#E9DFCC 100%)'
table=D(0,1560,W,360,'background:linear-gradient(180deg,#B07C4F,#8C5E3A)')+''.join(D(0,1600+k*70,W,4,'background:rgba(60,35,20,.18)') for k in range(5))
def loaf(x,y,s=1.0,kiss=False):
    w=int(300*s);h=int(170*s)
    out=D(x,y,w,h,f'background:radial-gradient(ellipse at 40% 30%,#E7B877,#C98B45 60%,#A46B32);border-radius:50% 50% 44% 44%/62% 62% 38% 38%;box-shadow:0 14px 30px rgba(80,45,15,.25)')
    for k in range(3):
        out+=D(x+int(w*(.25+.22*k)),y+int(h*.18),int(14*s),int(h*.5),'background:rgba(255,236,200,.55);border-radius:8px;transform:rotate(25deg)')
    return out
crumbs=''
rnd=random.Random(7)
for k in range(26):
    x=420+k*92+rnd.randint(-20,20); y=1540-int(math.sin(k/4)*14)+rnd.randint(-8,8)
    crumbs+=D(x,y,rnd.randint(10,18),rnd.randint(8,14),'background:#D9A35E;border-radius:40%')
def bird(x,y,flip=False):
    t='scaleX(-1)' if flip else ''
    return D(x,y,110,70,f'transform:{t}',D(0,10,90,60,'background:#5E6B66;border-radius:50% 60% 40% 50%')+D(70,0,44,44,'background:#5E6B66;border-radius:50%')+D(108,18,22,10,'background:#D6A24C;clip-path:polygon(0 0,100% 50%,0 100%)')+D(84,12,8,8,'background:#FAF7F1;border-radius:50%')+D(30,64,4,24,'background:#5E6B66')+D(52,64,4,24,'background:#5E6B66'))
sofra=D(2160+170,1330,740,90,'background:#9A6A40;border-radius:50%;box-shadow:0 18px 30px rgba(60,35,20,.25)')+D(2160+260,1410,30,150,'background:#7A5131')+D(2160+790,1410,30,150,'background:#7A5131')
plates=''.join(D(2160+240+k*150,1300,120,46,'background:#FAF7F1;border:5px solid #D9CDB5;border-radius:50%') for k in range(5))
shelf=D(3240+200,1080,680,26,'background:#7A5131;border-radius:6px')+D(3240+260,1106,22,70,'background:#6A4428')+D(3240+800,1106,22,70,'background:#6A4428')+glow(3240+540,980,260,.45)+loaf(3240+400,915,.95)
riseA=glow(4320+540,1300,420,.40)+D(4320+330,1500,420,26,'background:#7A5131;border-radius:6px')+D(4320+330,1120,420,26,'background:#7A5131;border-radius:6px')+loaf(4320+390,960,.9)+D(4320+525,1190,30,280,'background:linear-gradient(180deg,rgba(214,162,76,.0),rgba(214,162,76,.6))')+D(4320+505,1180,70,70,'border-left:14px solid #D6A24C;border-top:14px solid #D6A24C;transform:rotate(45deg)')
S=[slide(0,'lt','Urtësi e gjyshes','Kur i binte buka në tokë, gjyshja e puthte. <em>Dhe e vinte më&nbsp;lart.</em>','',HINT),
   slide(1,'lt','Te ne','Buka s’hidhej kurrë. <em>As&nbsp;thërrimet.</em>','I mblidhte në pëllëmbë dhe ua jepte&nbsp;zogjve.'),
   slide(2,'lt','E njëjta gjë','Edhe njerëzit nuk i hidhte. <em>As kur&nbsp;gabonin.</em>','Kushëriri që s’fliste, fqinji që e lëndoi: kishin gjithmonë vend në&nbsp;sofër.'),
   slide(3,'lt','E dinte','Atë që ka vlerë, <em>e ngre nga&nbsp;toka.</em>'),
   slide(4,'lt','Edhe ti','Kur bie, <em>vlera jote nuk&nbsp;bie.</em>','Ngrihu ngadalë dhe vendose veten pak më&nbsp;lart.'),
   end(5,'Kur s’ke fuqi të ngrihesh vetë, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-buka']=page(bgA,table+loaf(300,1430,1.1)+D(700,1500,40,12,'background:#D9A35E;border-radius:40%')+crumbs+bird(1080+620,1430)+bird(1080+820,1450,True)+sofra+plates+shelf+riseA+''.join(S))

# 02 „Mos qesh shumë, se do të qash“ (rregull i pashkruar)
bgB='linear-gradient(90deg,#2E4A43 0%,#283F3A 45%,#2E4A43 70%,#3F6259 100%)'
def bulbs():
    out=''
    for k in range(48):
        x=60+k*135
        y=int(1180+80*math.sin((x/1080)*math.pi*2-1.2)**2)
        on = x<1080 or x>4320
        dim = 1080<=x<=4320
        col='#F2C46D' if on else '#6E7C77'
        out+=D(x,y-60,3,60,'background:#1E2F2B')
        if on: out+=glow(x+2,y+30,90,.45)
        out+=D(x-18,y,40,56,f'background:{col};border-radius:50% 50% 45% 45%')+D(x-10,y-12,24,16,'background:#1E2F2B;border-radius:4px')
    wire=''.join(D(x,int(1120+80*math.sin((x/1080)*math.pi*2-1.2)**2),24,4,'background:#1E2F2B') for x in range(0,W,20))
    return wire+out
radio=D(1080+300,1420,520,280,'background:#8C5E3A;border-radius:28px;box-shadow:0 18px 40px rgba(0,0,0,.35)')+D(1080+340,1460,250,200,'background:repeating-linear-gradient(90deg,#5E3E25 0 10px,#7A5131 10px 20px);border-radius:14px')+D(1080+640,1470,130,130,'background:#E9E1C8;border-radius:50%')+D(1080+700,1480,10,60,'background:#221F1C;transform-origin:5px 60px;transform:rotate(-140deg)')+D(1080+650,1630,120,24,'background:#E9E1C8;border-radius:8px')
cloud=D(3240+300,1430,420,140,'background:#5C6E69;border-radius:80px')+D(3240+380,1360,200,200,'background:#5C6E69;border-radius:50%')+D(3240+520,1390,160,160,'background:#5C6E69;border-radius:50%')
sunB=glow(4320+540,1500,420,.55,'242,196,109')+D(4320+430,1390,220,220,'background:#F2C46D;border-radius:50%')
S=[slide(0,'dk','Rregull i pashkruar','„Mos qesh shumë, se do të qash.“ <em>Kush na e mësoi&nbsp;këtë?</em>','',HINT),
   slide(1,'dk','Në shtëpi','Qeshnim me zë në tryezë. <em>Dhe dikush na&nbsp;ndalte.</em>','„Mjaft, se s’është mirë. Pastaj vjen e&nbsp;keqja.“'),
   slide(2,'dk','Kështu mësuam','Ta ulim zërin <em>edhe kur jemi&nbsp;mirë.</em>'),
   slide(3,'dk','Sot','Kur na shkon mirë, <em>presim që diçka të&nbsp;prishet.</em>'),
   slide(4,'dk','E vërteta','Gëzimi s’është borxh <em>që paguhet me&nbsp;lot.</em>','Qesh. Ke të drejtë ta&nbsp;gëzosh.'),
   end(5,'Edhe gëzimi, edhe halli, <em>ndahen më lehtë me&nbsp;dikë.</em>')]
sets['02-qesh']=page(bgB,bulbs()+radio+cloud+sunB+''.join(S))

# 03 Nëna bën sikur fle (sjellje e fshehur me orë)
bgC='linear-gradient(180deg,#141A22 0%,#1B232D 70%,#202A35 100%)'
floorC=D(0,1700,W,220,'background:#10151C')
doorF=D(300,980,380,720,'background:#4A3828;border-radius:8px')+D(330,1010,320,300,'border:8px solid #3A2B1E;border-radius:4px')+D(620,1340,40,40,'background:#D6A24C;border-radius:50%')+D(650,1350,70,16,'background:#D6A24C;border-radius:6px')
lamp=glow(1080+540,1050,380,.42)+D(1080+500,940,80,60,'background:#E8B96C;border-radius:40px 40px 6px 6px')+D(1080+536,860,8,80,'background:#2A3340')+D(1080+380,1700,320,14,'background:rgba(232,185,108,.25);border-radius:50%')
kitchen=D(2160+180,1420,720,40,'background:#5E4630;border-radius:8px')+D(2160+230,1460,30,240,'background:#4A3828')+D(2160+820,1460,30,240,'background:#4A3828')+glow(2160+540,1380,240,.30)+D(2160+380,1360,320,50,'background:#E9E1C8;border-radius:50%')+D(2160+400,1300,280,90,'background:#D9CDB5;border-radius:50% 50% 10% 10%/90% 90% 10% 10%')+D(2160+680,1330,110,90,'background:#C9BFA8;border-radius:10px')
doorM=D(3240+340,920,400,780,'background:#3A3026;border-radius:8px')+D(3240+700,1300,30,30,'background:#8A7A60;border-radius:50%')+D(3240+340,1700,400,10,'background:linear-gradient(90deg,rgba(232,185,108,.0),rgba(232,185,108,.35),rgba(232,185,108,.0))')
winC=D(4320+300,900,480,560,'background:linear-gradient(180deg,#22314A,#2C3D58);border:18px solid #2A2420;border-radius:8px')+D(4320+530,900,18,560,'background:#2A2420')+D(4320+300,1170,480,18,'background:#2A2420')+D(4320+380,960,110,110,'background:#F3E6C4;border-radius:50%;box-shadow:0 0 60px rgba(243,230,196,.5)')
S=[slide(0,'dk','Ora 00:40','Hyn në shtëpi pa zhurmë. <em>Nëna bën sikur&nbsp;fle.</em>','',HINT),
   slide(1,'dk','Ora 00:41','Drita e korridorit është ndezur. <em>Dikush e la për&nbsp;ty.</em>'),
   slide(2,'dk','Në kuzhinë','Ushqimi në tavolinë, i mbuluar me një pjatë&nbsp;tjetër. <em>Që të mos&nbsp;ftohet.</em>'),
   slide(3,'dk','Ora 00:43','Kalon pranë dhomës së saj. <em>Drita poshtë derës&nbsp;fiket.</em>'),
   slide(4,'dk','E kupton','S’kishte fjetur. <em>Priste vetëm të dinte që je&nbsp;mirë.</em>','Disa njerëz s’flenë derisa të dëgjojnë çelësin në&nbsp;derë.'),
   end(5,'Kur s’ke kujt t’ia thuash si je, <em>në Shprehu dikush të&nbsp;dëgjon.</em>')]
sets['03-nena']=page(bgC,floorC+doorF+lamp+kitchen+doorM+winC+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
