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


HINT='Rrëshqit →'
def page(bg,body,w=6480):
    return head().replace('6480px',f'{w}px')+f'</style></head><body><div class="pano" style="background:{bg}">{body}</div></body></html>'
def glow(x,y,r,a=.5,c='255,214,140'):
    return D(x-r,y-r,2*r,2*r,f'background:radial-gradient(circle,rgba({c},{a}),rgba({c},0) 66%);border-radius:50%')
W=6480
sets={}



# 01 Çanta e gjyshes (ritual)

# 01 Gjyshi s'hidhte asgjë (urtësi)
bgA='linear-gradient(180deg,#FAF7F1 0%,#EFE6D3 100%)'
bench=D(-20,1600,W+40,320,'background:#8C6A4A;background-image:repeating-linear-gradient(90deg,rgba(0,0,0,.06) 0 3px,transparent 3px 160px)')+D(0,1580,W,26,'background:#6E5038')
def radio(x):
    return D(x,1330,360,250,'background:#7A5536;border-radius:26px;box-shadow:inset -16px 0 0 rgba(0,0,0,.12)')+D(x+30,1370,170,170,'background:repeating-radial-gradient(circle,#3A2A1E 0 6px,#5A4330 6px 12px);border-radius:50%')+D(x+230,1380,100,40,'background:#E8D9B5;border-radius:6px')+D(x+250,1450,30,30,'background:#D6A24C;border-radius:50%')+D(x+300,1240,8,110,'background:#5A4330;transform:rotate(18deg)')
def tape(x,y,w=120,r=-12):
    return D(x,y,w,26,f'background:rgba(240,232,210,.9);transform:rotate({r}deg);border-radius:3px')
def chair(x):
    return D(x,1180,26,420,'background:#9C7049')+D(x+230,1180,26,420,'background:#9C7049')+D(x,1360,256,30,'background:#B4875C')+D(x,1180,256,24,'background:#B4875C')+D(x,1260,256,18,'background:#B4875C')
def clock(x):
    return D(x,1240,300,300,'background:#FBF8F1;border:18px solid #9C7049;border-radius:50%')+D(x+159,1300,10,110,'background:#221F1C;border-radius:5px')+D(x+159,1390,90,10,'background:#221F1C;border-radius:5px')
def tools(x):
    return D(x,1540,260,24,'background:#6E6E6E;border-radius:6px')+D(x+250,1520,60,64,'background:#B5443A;border-radius:10px')+D(x+40,1500,140,22,'background:#9AA3A0;border-radius:4px;transform:rotate(-20deg)')
scene=bench+radio(560)+tape(600,1350)+tools(80)
scene+=chair(1080+560)+D(1080+560,1300,256,14,'background:#C9B48A')+tape(1080+600,1300,150,4)+tape(1080+640,1360,120,-8)
scene+=clock(2160+560)+tools(2160+120)
scene+=glow(3240+700,1400,380,.5)+radio(3240+560)
scene+=glow(4320+540,1380,420,.45)+D(4320+300,1540,480,40,'background:#B4875C;border-radius:8px')+D(4320+420,1420,240,120,'background:#3F6259;border-radius:24px 24px 8px 8px')+D(4320+505,1360,70,60,'background:#E8D9B5;border-radius:12px')
S=[slide(0,'lt','Te gjyshi','Gjyshi s’hidhte asgjë. <em>E&nbsp;ndreqte.</em>','',HINT),
   slide(1,'lt','Radioja','Kur s’kapte valën, i jepte një goditje të lehtë. <em>Dhe radioja&nbsp;këndonte.</em>'),
   slide(2,'lt','Karrigia','Kur lëkundej, e lidhte me tel. <em>Dhe e mbajti edhe dhjetë&nbsp;vjet.</em>'),
   slide(3,'lt','Ora','„S’është prishur“, thoshte. <em>„Është lodhur&nbsp;pak.“</em>'),
   slide(4,'lt','E kuptuam vonë','Edhe ne lodhemi pak ndonjëherë. <em>S’jemi për t’u hedhur. Ndreqemi&nbsp;ngadalë.</em>','Me pak durim dhe me dikë që ta mban&nbsp;karrigen.'),
   end(5,'Kur ndihesh pak i lodhur, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-ndreqja']=page(bgA,scene+''.join(S))

# 02 "S'të ka hije" (rregull i pashkruar)
bgB='linear-gradient(180deg,#2E4A43 0%,#24413A 100%)'
W6=6480
lamp=lambda x:D(x,0,6,1000,'background:rgba(250,247,241,.25)')+D(x-40,990,86,60,'background:#E8B96C;border-radius:40px 40px 10px 10px;box-shadow:0 30px 120px 30px rgba(232,185,108,.35)')
def swing(x,ang=0):
    return D(x,1000,6,420,f'background:rgba(250,247,241,.5);transform-origin:top;transform:rotate({ang}deg)')+D(x+200,1000,6,420,f'background:rgba(250,247,241,.5);transform-origin:top;transform:rotate({ang}deg)')+D(x-10-ang*7,1410,226,30,'background:#D6A24C;border-radius:8px')+D(x-200,990,620,14,'background:rgba(250,247,241,.35);border-radius:7px')
def bubble(x,y,t,w=520):
    return D(x,y,w,0,'',f'<div style="background:#FAF7F1;color:#221F1C;border-radius:28px;padding:26px 34px;font-size:44px;font-weight:600;line-height:1.25;box-shadow:0 14px 40px rgba(0,0,0,.25)">{t}</div>')
scene=D(-20,1620,W6+40,300,'background:#1E3530')
scene+=bubble(560,1150,'„S’të ka hije.“')+bubble(1080+430,1100,'„Je i/e rritur tani.“',560)+bubble(1080+520,1330,'„Mos u bëj si fëmijë.“',520)
scene+=swing(2160+640,-8)+swing(3240+560,12)+glow(3240+700,1300,420,.35,'232,185,108')
scene+=glow(4320+700,1300,460,.3,'232,185,108')
S=[slide(0,'dk','Rregull i pashkruar','„S’të ka hije.“ <em>Kush e vendos çfarë të ka&nbsp;hije?</em>','',HINT),
   slide(1,'dk','E dëgjojmë','Kur qesh me zë. Kur kërcen në dasmë pa pritur. <em>Kur qan para të&nbsp;tjerëve.</em>'),
   slide(2,'dk','Dhe mësojmë','Të jemi „seriozë“. <em>Edhe kur brenda s’jemi&nbsp;mirë.</em>'),
   slide(3,'dk','Por','Një kolovajzë s’pyet për moshë. <em>As një ndjenjë.</em>'),
   slide(4,'dk','E vërteta','Të ka hije të jesh njeri. <em>Të qeshësh, të lodhesh, të thuash „s’jam&nbsp;mirë“.</em>','Hije s’ka vetëm heshtja që të&nbsp;rëndon.'),
   end(5,'Kur s’ke ku ta thuash, <em>thuaje pa&nbsp;emër.</em>')]
sets['02-hije']=page(bgB,scene+''.join(S),W6)

# 03 5 gjëra që na i mësoi shkolla (listë me boshllëk)
W7=7560
bgC='linear-gradient(180deg,#F6F1E6 0%,#EDE4D1 100%)'
board=D(-20,1060,W7+40,300,'background:#2F4A40;border-top:22px solid #8C6A4A;border-bottom:22px solid #8C6A4A')
chalk=lambda x,t:D(x,1130,900,0,'',f'<div style="font-family:Sacramento,cursive;font-size:96px;color:rgba(250,247,241,.82);white-space:nowrap">{t}</div>')
desk=D(-20,1600,W7+40,320,'background:#B98A5E;background-image:repeating-linear-gradient(90deg,rgba(0,0,0,.05) 0 3px,transparent 3px 140px)')
def book(x,c,t):
    return D(x,1430,300,170,f'background:{c};border-radius:8px 14px 14px 8px;box-shadow:inset 18px 0 0 rgba(0,0,0,.12)',f'<div style="color:#FAF7F1;font-weight:700;font-size:34px;padding:56px 0 0 46px">{t}</div>')
scene=desk+book(620,'#B5443A','Abetare')+book(1080+600,'#3F6259','Ditari')+D(2160+560,1300,330,300,'background:#FBF8F1;border-radius:6px;background-image:repeating-linear-gradient(0deg,rgba(63,98,89,.25) 0 2px,transparent 2px 46px)')+D(3240+520,1380,380,220,'background:#FBF8F1;border-radius:6px')+D(4320+520,1360,360,240,'background:rgba(232,185,108,.0)')+glow(4320+700,1420,380,.5)+D(5400+560,1420,300,180,'background:#5E7F70;border-radius:12px')
S=[slide(0,'lt','Listë','5 gjëra që na i mësoi shkolla. <em>E katërta s’na e mësoi&nbsp;kurrë.</em>','',HINT),
   slide(1,'lt','1','Abetaren <em>përmendsh, faqe pas&nbsp;faqeje.</em>'),
   slide(2,'lt','2','Të ngrihemi në këmbë <em>kur hyn&nbsp;mësuesi.</em>'),
   slide(3,'lt','3','Hartimin „Pranvera“ <em>me të njëjtat fjali çdo&nbsp;vit.</em>'),
   slide(4,'lt','4','Të themi „jam mërzitur“. <em>Këtë s’na e mësoi&nbsp;kurrë.</em>'),
   slide(5,'lt','5','Që gabimi s’është turp. <em>Këtë e mësojmë&nbsp;tani.</em>','S’është vonë për mësimin që na&nbsp;mungoi.'),
   end(6,'Ku ta mësosh si thuhet, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-shkolla']=page(bgC,board+chalk(220,'Mësimi i sotëm')+scene+''.join(S),W7)

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
