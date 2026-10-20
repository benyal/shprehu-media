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

import math, os
IG=os.environ.get('IG')=='1'
HH=1350 if IG else 1920
OY=570 if IG else 0
CSS=CSS.replace('height:1920px',f'height:{HH}px')
if IG: CSS=CSS.replace('top:250px;bottom:460px','top:140px;bottom:100px')
def D(x,y,w,h,style='',inner='',cls=''):
    return f'<div class="abs {cls}" style="left:{x}px;top:{y-OY}px;width:{w}px;height:{h}px;{style}">{inner}</div>'
sets={}
HINT='Rrëshqit →'
def glow(x,y,r,a=.5):
    return D(x-r,y-r,2*r,2*r,f'background:radial-gradient(circle,rgba(255,214,140,{a}),rgba(255,214,140,0) 66%);border-radius:50%')
def steam(x,y,n=3):
    return ''.join(D(x+i*22,y-i*10,34,80,f'background:rgba(255,240,215,{.22-i*.05:.2f});border-radius:50%;filter:blur(9px)') for i in range(n))

# 1: Çaj mali per gjithçka
shelf=D(0,1566,W,18,'background:#5A3C22')+D(0,1584,W,6,'background:rgba(0,0,0,.35)')
herbs=''
random.seed(3)
for x in range(430,W,430):
    herbs+=D(x+34,1360,3,60,'background:#8A7A5A')
    for k in range(3):
        herbs+=D(x+k*26-6,1410,56,170,f'background:linear-gradient(180deg,#8CA06A,#4F6B3A);clip-path:polygon(50% 0,100% 88%,50% 100%,0 88%);opacity:{.95-k*.12:.2f};transform:rotate({k*6-6}deg)')
glasses=''
for x in range(300,W,610):
    glasses+=glow(x+30,1500,260,.4)+D(x,1496,60,70,'background:linear-gradient(180deg,rgba(255,255,255,.35),rgba(214,140,50,.85));border-radius:6px 6px 12px 12px;border:3px solid rgba(255,255,255,.4)')+D(x-14,1562,88,8,'background:#FAF7F1;border-radius:50%')+steam(x+10,1480)
kett=''
for x in (1200,3900,5600):
    kett+=D(x,1480,130,86,'background:#B9BEC2;border-radius:30px 30px 14px 14px')+D(x+110,1500,50,14,'background:#B9BEC2;transform:rotate(-24deg)')+D(x+20,1456,90,26,'border:8px solid #8E9498;border-bottom:0;border-radius:50px 50px 0 0')+steam(x+50,1460)
jars=''.join(D(x,1500,80,66,'background:linear-gradient(180deg,#9AA86F,#6E8049);border-radius:10px;border:3px solid rgba(255,255,255,.35)')+D(x+10,1486,60,16,'background:#C9B88F;border-radius:4px') for x in (850,2150,3150,4700))
table=D(0,1760,W,160,'background:linear-gradient(180deg,#5A3C22,#3A2514)')+D(0,1756,W,8,'background:#7A5634')
S=[slide(0,'dk','Në kuzhinë · 07:00','„Çaj mali <em>për gjithçka.</em>“','Për gripin, për barkun, për nervat. Dhe për zemrën?',HINT),
   slide(1,'dk','Receta','Nëna e ka gjithmonë një tufë <em>në raft.</em>','Dhe një fjali: „Pije, se të bën mirë.“'),
   slide(2,'dk','Çfarë ka brenda','Në gotë ka bimë. Në fjalinë e saj ka <em>kujdes.</em>','Kështu e thoshte, pa e thënë.'),
   slide(3,'dk','Pyetja','A të ka ndihmuar ndonjëherë një çaj <em>të flasësh?</em>','Shkruaj në koment: po ose jo.'),
   slide(4,'dk','E vërteta','Çaji ngroh. Një fjalë e thënë me zë <em>ngroh më gjatë.</em>','Edhe kur s’ka kush ta përgatisë për ty.'),
   end(5,'Kur çaji nuk mjafton, <em>thuaje pa emër.</em>')]
sets['01-caj-mali']=page('linear-gradient(180deg,#1F1710 0%,#33241A 60%,#4A3322 100%)',shelf+herbs+jars+kett+glasses+table+''.join(S))

# 2: Rreth sobes
def soba(x):
    return (glow(x+150,1640,560,.6)+D(x+110,1050,40,500,'background:#15100D')+D(x,1480,300,330,'background:#1B1512;border-radius:20px 20px 6px 6px')
            +D(x+50,1540,200,140,'background:radial-gradient(circle,#FFB347,#E0661A);border-radius:12px;box-shadow:0 0 60px 20px rgba(255,150,50,.5)')
            +D(x+40,1810,220,12,'background:#0B0806'))
def chair(x,flip=False):
    return D(x,1560,120,260,'background:#120D0A;border-radius:14px 14px 4px 4px')+D(x-20,1700,160,18,'background:#120D0A;border-radius:6px')
wood=''.join(D(x,1790,160,36,'background:#3A2514;border-radius:18px;border:3px solid #24170C') for x in (60,260,70)) 
rooms=''
for x in (3000,3820,4640):
    rooms+=(D(x,1400,560,500,'background:#0E1319;border:8px solid #06090C')
            +D(x+120,1580,320,200,'background:radial-gradient(circle,rgba(120,170,255,.4),rgba(120,170,255,0) 70%)')
            +D(x+250,1700,60,110,'background:#1A2430;border-radius:8px;border:3px solid #6E8FB8;box-shadow:0 0 36px 12px rgba(120,170,255,.45)')
            +D(x+150,1760,260,140,'background:#0A0F14;border-radius:60px 60px 0 0'))
floor=D(0,1860,W,60,'background:linear-gradient(180deg,#3A2514,#241509)')
S=[slide(0,'dk','Në dimër · 19:30','Dikur flisnim <em>rreth sobës.</em>','Sot secili rri në dhomën e vet.',HINT),
   slide(1,'dk','Soba','Aty thuheshin gjërat që <em>nuk thuheshin gjetkë.</em>','Me duart nga zjarri dhe sytë në flakë.'),
   slide(2,'dk','Tani','Shtëpia ngrohet pa zjarr. <em>Bisedat ftohen.</em>','Nuk është faji i askujt. Ndodh.'),
   slide(3,'dk','Pyetja','Kush e nis sot <em>bisedën?</em> Ti apo ata?','Shkruaj në koment: unë ose ata.'),
   slide(4,'dk','E vërteta','Një pyetje te darka mjafton: <em>„Si ishte dita?“</em>','Dhe pastaj ia lë heshtjes të dëgjojë.'),
   end(5,'Kur s’ka sobë për të folur, <em>fol pa emër.</em>')]
sets['02-soba']=page('linear-gradient(180deg,#1A0F09 0%,#28170D 55%,#37200F 100%)',floor+soba(700)+chair(300)+chair(1250)+chair(1420)+wood+rooms+''.join(S))

# 3: Mos u lodh
ctr=D(0,1700,W,220,'background:linear-gradient(180deg,#4A2F1A,#331F10)')+D(0,1694,W,10,'background:#6B4A2F')
tiles=D(0,1420,W,274,'background:repeating-linear-gradient(90deg,transparent 0 118px,rgba(0,0,0,.25) 118px 120px),repeating-linear-gradient(0deg,#6E6048 0 88px,rgba(0,0,0,.3) 88px 90px);opacity:.55')
def stack(x,n):
    return ''.join(D(x+(k%2)*6,1694-16*(k+1),200,16,'background:#FAF7F1;border-radius:50%;box-shadow:0 2px 4px rgba(0,0,0,.35)') for k in range(n))
pile=stack(500,9)+stack(3500,12)+stack(5200,6)
kettle=D(1700,1578,150,116,'background:#B9BEC2;border-radius:34px 34px 14px 14px')+D(1830,1600,56,14,'background:#B9BEC2;transform:rotate(-24deg)')+D(1720,1552,110,28,'border:9px solid #8E9498;border-bottom:0;border-radius:60px 60px 0 0')+steam(1760,1560)
pot=D(2500,1556,220,138,'background:#2F3A3F;border-radius:10px')+D(2490,1546,240,18,'background:#3E4B51;border-radius:8px')+D(2584,1522,52,24,'background:#3E4B51;border-radius:12px')
mugs=''.join(D(x,1480,64,60,'background:#E9E0CC;border-radius:6px 6px 22px 22px')+D(x+54,1494,26,30,'border:6px solid #E9E0CC;border-left:0;border-radius:0 16px 16px 0')+D(x+30,1460,4,24,'background:#8A7A5A') for x in range(1000,1500,110))
apron=D(2950,1370,12,50,'background:#8A7A5A')+D(2890,1410,140,230,'background:#3F6259;border-radius:10px 10px 50px 50px')
win=D(4300,1400,380,260,'background:#0D1620;border:10px solid #5A3C22')+D(4466,1400,8,260,'background:#5A3C22')+D(4540,1450,40,40,'background:#F3EFE7;border-radius:50%;box-shadow:0 0 40px 14px rgba(243,239,231,.25)')
lights=glow(1000,1560,640,.5)+glow(3300,1560,620,.5)+glow(5000,1560,560,.4)
S=[slide(0,'dk','Në kuzhinë · 22:40','Tërë ditën na thonë <em>„mos u lodh“.</em>','Askush nuk pyet: je lodhur?',HINT),
   slide(1,'dk','Fjalia','Është fjali e mirë. <em>Thuhet me dashuri.</em>','Por shpesh zëvendëson pyetjen.'),
   slide(2,'dk','Rregulli i pashkruar','Themi „mos u lodh“, <em>por vazhdojmë të punojmë.</em>','Se kështu bëhet. Se s’ka kush tjetër.'),
   slide(3,'dk','Pyetja','Kur e ke thënë i fundit <em>„jam lodhur“</em> me zë?','Shkruaj në koment: sot, javën e kaluar, kurrë.'),
   slide(4,'dk','E vërteta','Lodhja nuk është <em>dobësi.</em> Është shenjë që ke bërë shumë.','Mund të thuhet. Dhe të dëgjohet.'),
   end(5,'Për „jam lodhur“, <em>thuaje pa emër.</em>')]
sets['03-mos-u-lodh']=page('linear-gradient(180deg,#1A110B 0%,#2B1B10 55%,#3C2715 100%)',lights+tiles+win+ctr+apron+mugs+pot+kettle+pile+''.join(S))

if __name__=='__main__':
    for k,v in sets.items():
        open(f'set-{k}{"-ig" if IG else ""}.html','w').write(v)
    print(len(sets),'sets',HH)
