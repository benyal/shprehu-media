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

# 1: Pazari i gjyshit (sjellje e fshehur me orë)
bgA='linear-gradient(180deg,#EEF2EC 0%,#F5EFE3 55%,#EFE4CF 100%)'
groundA=D(0,1700,W,220,'background:linear-gradient(180deg,#CDBB98,#BCA67F)')
sunA=glow(1080*2+760,1020,260,.45)+D(1080*2+700,960,120,120,'background:#F1CF8A;border-radius:50%')
def stall(x,w,stripe,goods):
    s=D(x,1300,w,90,f'background:repeating-linear-gradient(90deg,{stripe} 0 60px,#FAF7F1 60px 120px);border-radius:12px 12px 30px 30px')
    s+=D(x+20,1390,14,310,'background:#8A6A3F')+D(x+w-34,1390,14,310,'background:#8A6A3F')
    s+=D(x+20,1560,w-40,30,'background:#A8844F;border-radius:6px')+D(x+40,1590,w-80,110,'background:#C9A35E;border-radius:4px')
    for k in range(goods[1]):
        s+=D(x+60+k*int((w-160)/max(1,goods[1]-1)),1500,64,64,f'background:{goods[0]};border-radius:50%;box-shadow:inset -8px -8px 0 rgba(0,0,0,.12)')
    return s
stalls=stall(380,620,'#3F6259',('#C54F35',6))+stall(1080+560,600,'#D6A24C',('#E8B96C',5))+stall(2160+620,560,'#3F6259',('#8FB8A8',5))+stall(3240+200,560,'#D6A24C',('#C54F35',4))
bench=D(4320+220,1560,560,26,'background:#8A6A3F;border-radius:8px')+D(4320+220,1500,560,22,'background:#8A6A3F;border-radius:8px')+D(4320+250,1586,20,114,'background:#5E4630')+D(4320+740,1586,20,114,'background:#5E4630')
plis=D(4320+560,1450,130,62,'background:linear-gradient(180deg,#FFFFFF,#E9E4DA);border-radius:65px 65px 10px 10px;box-shadow:0 8px 16px rgba(80,55,30,.18)')
plis0=D(140,1380,110,52,'background:linear-gradient(180deg,#FFFFFF,#E9E4DA);border-radius:55px 55px 8px 8px;box-shadow:0 8px 16px rgba(80,55,30,.18)')+D(186,1350,18,30,'background:#8A6A3F;border-radius:4px')
S=[slide(0,'lt','E enjte · Ora 08:00','Gjyshi shkonte në pazar çdo të enjte. <em>Shpesh kthehej pa blerë&nbsp;asgjë.</em>','',HINT),
   slide(1,'lt','Ora 08:30','Vishte xhaketën e mirë. <em>Si të kishte&nbsp;takim.</em>'),
   slide(2,'lt','Ora 10:00','Pyeste për çmime që s’i interesonin. <em>Vetëm sa të&nbsp;fliste.</em>'),
   slide(3,'lt','Ora 12:00','„S’kishte gjë të mirë sot.“ <em>Por kthehej më i&nbsp;lehtë.</em>'),
   slide(4,'lt','E vërteta','S’shkonte për të blerë. <em>Shkonte që dikush ta&nbsp;dëgjonte.</em>','Edhe sot, secili prej nesh ka nevojë për „pazarin“&nbsp;e&nbsp;vet.'),
   end(5,'Kur s’ke pazarin tënd, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-pazari']=page(bgA,sunA+groundA+stalls+bench+plis+''.join(S))

# 2: „Ti je i ri, çfarë hallesh ke?“ (rregull i pashkruar)
bgB='linear-gradient(180deg,#F4EFE5 0%,#EFE6D5 100%)'
tableB=D(0,1600,W,40,'background:#A8844F')+D(0,1640,W,280,'background:#D9C8A6')
def weight(x,s,gold=False,base=1600):
    c1,c2=('#E8B96C','#B9862F') if gold else ('#6F6A62','#4A4642')
    return D(x,base-int(140*s),int(150*s),int(140*s),f'background:linear-gradient(180deg,{c1},{c2});clip-path:polygon(18% 0,82% 0,100% 100%,0 100%);border-radius:6px')+D(x+int(55*s),base-int(170*s),int(40*s),int(34*s),f'border:{max(5,int(8*s))}px solid {c2};border-radius:50% 50% 0 0;border-bottom:none')
weights=weight(300,1.6)+weight(620,1.2)+weight(1080+420,1.9)+weight(1080+760,.9)+weight(2160+380,1.4)+weight(2160+700,.8)
scx=3240+1080
scale=D(scx-10,1180,20,420,'background:#8A6A3F')+D(scx-120,1580,240,24,'background:#8A6A3F;border-radius:8px')+D(scx-560,1200,1120,14,'background:#8A6A3F;border-radius:7px')
for side in (-1,1):
    px=scx+side*500
    scale+=D(px-4,1214,4,170,'background:#6F6A62;transform:rotate(12deg);transform-origin:top')+D(px,1214,4,170,'background:#6F6A62;transform:rotate(-12deg);transform-origin:top')
    scale+=D(px-170,1380,340,30,'background:#C9A35E;border-radius:0 0 170px 170px')
scale+=weight(scx-568,.9,base=1384)+''+D(scx+430,1300,140,80,'background:radial-gradient(circle,#F1CF8A,#D6A24C);border-radius:50% 50% 40% 40%')
scale=glow(scx,1260,360,.35)+scale
S=[slide(0,'lt','Rregull i pashkruar','„Ti je i ri, çfarë hallesh ke?“ <em>Dhe e mbyllëm gojën para se ta&nbsp;hapnim.</em>','',HINT),
   slide(1,'lt','E dëgjuam shpesh','„Në moshën tënde, unë…“ <em>Dhe halli ynë dukej i&nbsp;vogël.</em>'),
   slide(2,'lt','Kështu mësuam','Ta krahasojmë hallin <em>në vend që ta&nbsp;themi.</em>'),
   slide(3,'lt','Por','Lodhja në njëzet vjeç <em>është lodhje e&nbsp;vërtetë.</em>','Edhe kur dikush tjetër e ka pasur më&nbsp;rëndë.'),
   slide(4,'lt','E vërteta','Halli s’matet <em>me&nbsp;vite.</em>','Kush e ndjen, ka të drejtë ta&nbsp;thotë.'),
   end(5,'Edhe halli yt ka vend. <em>Fol me dikë pa&nbsp;emër.</em>')]
sets['02-iri']=page(bgB,tableB+weights+scale+''.join(S))

# 3: Emri i gjyshit (ritual shqiptar me kuptim të ri)
bgC='linear-gradient(180deg,#2E4A43 0%,#355449 60%,#3B5C50 100%)'
groundC=D(0,1660,W,260,'background:#24392F')
tree=D(1080+380,1080,200,600,'background:linear-gradient(90deg,#5E4630,#7F5C38,#5E4630);border-radius:40px 40px 0 0')
rnd=random.Random(41)
roots=''.join(D(1080+480-k*150,1660+k*30,320+k*40,18,f'background:#5E4630;border-radius:9px;transform:rotate({8+k*6}deg);transform-origin:right') for k in range(6))
roots+=''.join(D(1080+480,1660+k*30,320+k*40,18,f'background:#5E4630;border-radius:9px;transform:rotate({-8-k*6}deg);transform-origin:left') for k in range(4))
branch=D(1080+520,1120,1900,26,'background:#7F5C38;border-radius:13px;transform:rotate(-3deg);transform-origin:left')
leaves=''
for k in range(46):
    x=1080+200+rnd.randint(0,2300); y=rnd.randint(980,1240)-int((x-1280)*0.05)
    gold=False
    c='#E8B96C' if gold else ['#8FB8A8','#6E9585','#A9C9BB'][k%3]
    leaves+=D(x,y,70,40,f'background:{c};border-radius:0 70% 0 70%;transform:rotate({rnd.randint(-40,40)}deg);opacity:.92')
newb=D(3240+180,1036,1520,18,'background:#7F5C38;border-radius:9px;transform:rotate(14deg);transform-origin:left')
newleaves=''.join(D(4320+140+k*120,1250+k*30-(k%2)*40,80,46,'background:#E8B96C;border-radius:0 70% 0 70%;transform:rotate(-20deg)') for k in range(6))+glow(4320+480,1340,260,.35)
S=[slide(0,'dk','Emri','Të vunë emrin e gjyshit ose të gjyshes. <em>Bashkë me të, erdhën edhe&nbsp;pritjet.</em>','',HINT),
   slide(1,'dk','Urimi','„Ta trashëgosh emrin me nder.“ <em>Ishte urim. Dhe&nbsp;detyrë.</em>'),
   slide(2,'dk','Te çdo i afërm','„E ka emrin e gjyshit.“ <em>Dhe të gjithë të shikonin pak më&nbsp;gjatë.</em>'),
   slide(3,'dk','Sot','E mban emrin <em>si një peshë të&nbsp;bukur.</em>','Krenari dhe frikë njëherësh: a&nbsp;do&nbsp;t’ia&nbsp;dal?'),
   slide(4,'dk','E vërteta','Emri vjen me histori. <em>Jeta mund të jetë e&nbsp;jotja.</em>','Mund ta nderosh emrin pa u bërë kopja&nbsp;e&nbsp;tij.'),
   end(5,'Kur pesha e emrit rëndon, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-emri']=page(bgC,groundC+roots+tree+branch+leaves+newb+newleaves+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
