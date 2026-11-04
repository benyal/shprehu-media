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

# 1: Ninullat e gjyshes (urtësi e gjyshes)
bgA='linear-gradient(180deg,#1B2130 0%,#222A3A 60%,#293246 100%)'
floorA=D(0,1700,W,220,'background:#151A24')
moonA=D(1080*0+780,960,130,130,'background:#F3E6C4;border-radius:50%;box-shadow:0 0 80px rgba(243,230,196,.45)')
rnd=random.Random(42)
stars=''.join(D(rnd.randint(0,W),rnd.randint(960,1450),6,6,f'background:#F3E6C4;border-radius:50%;opacity:.{rnd.randint(3,7)}') for _ in range(70))
cx=1080+540
cradle=glow(cx,1500,330,.30)+D(cx-260,1440,520,180,'background:linear-gradient(180deg,#A8844F,#8A6A3F);border-radius:30px 30px 200px 200px')
cradle+=D(cx-300,1600,600,30,'background:#5E4630;border-radius:50%/0 0 100% 100%')+D(cx-200,1470,400,40,'background:#E9E1C8;border-radius:20px')
cradle+=''.join(D(cx-220+k*110,1530,40,40,'border:5px solid #D6A24C;transform:rotate(45deg);opacity:.75') for k in range(4))
notes=''
for k in range(22):
    t=k/21; x=int(cx+180+t*3300); y=int(1360-math.sin(t*math.pi*2.4)*120)
    notes+=D(x,y,26,20,'background:#E8B96C;border-radius:50%;opacity:.8')+D(x+20,y-56,6,62,'background:#E8B96C;opacity:.8')
pillow=D(4320+300,1560,480,120,'background:#E9E1C8;border-radius:60px')+glow(4320+540,1560,260,.3)
S=[slide(0,'dk','Urtësi e gjyshes','Gjyshja këndonte ninulla. <em>Edhe kur fëmija kishte&nbsp;fjetur.</em>','',HINT),
   slide(1,'dk','„Nina nana“','Zëri i saj ishte i ulët. <em>Fjalët, gjithmonë të&nbsp;njëjtat.</em>'),
   slide(2,'dk','Pse vazhdonte','Ninulla s’ishte vetëm për ne. <em>Ishte edhe për&nbsp;të.</em>'),
   slide(3,'dk','E dinte','Një zë i qetë <em>e qetëson edhe atë që&nbsp;këndon.</em>'),
   slide(4,'dk','Sot','Edhe ti mund t’i flasësh vetes <em>me atë&nbsp;zë.</em>','Ngadalë, butë, pa&nbsp;nxitim.'),
   end(5,'Kur s’e gjen dot atë zë, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-ninulla']=page(bgA,stars+moonA+floorA+cradle+notes+pillow+''.join(S))

# 2: „Ç’po rri kot?“ (rregull i pashkruar)
bgB='linear-gradient(180deg,#F6F1E6 0%,#EFE6D4 100%)'
floorB=D(0,1700,W,220,'background:#D9C8A6')
def chores(x):
    s=D(x,1560,180,140,'background:#C9CED0;border-radius:10px 10px 30px 30px')+''.join(D(x+20+k*40,1520-k*6,30,60,'background:#FAF7F1;border:4px solid #CFC4AE;border-radius:50%') for k in range(4))
    return s
broom=D(1080+700,1180,18,520,'background:#8A6A3F;transform:rotate(12deg)')+D(1080+690,1600,110,100,'background:#C9A35E;clip-path:polygon(30% 0,70% 0,100% 100%,0 100%);transform:rotate(12deg)')
bucket=D(1080+300,1560,170,140,'background:#8FB8A8;clip-path:polygon(0 0,100% 0,88% 100%,12% 100%)')
books=''.join(D(2160+280+k*20,1520-k*70,360,62,f"background:{['#3F6259','#D6A24C','#8FB8A8','#C54F35'][k]};border-radius:6px") for k in range(4))
chair=D(3240+380,1400,300,30,'background:#8A6A3F;border-radius:8px')+D(3240+380,1150,30,280,'background:#8A6A3F')+D(3240+400,1430,22,270,'background:#5E4630')+D(3240+640,1430,22,270,'background:#5E4630')
sofa=glow(4320+540,1500,360,.35)+D(4320+160,1500,760,200,'background:#3F6259;border-radius:40px 40px 14px 14px')+D(4320+160,1420,760,110,'background:#2E4A43;border-radius:40px')+D(4320+520,1420,160,90,'background:#E8B96C;border-radius:30px')
S=[slide(0,'lt','Rregull i pashkruar','„Ç’po rri kot?“ <em>Dhe u ngritëm, edhe kur s’kishim&nbsp;fuqi.</em>','',HINT),
   slide(1,'lt','Në shtëpi','Kur uleshe, dikush të gjente punë. <em>Gjithmonë.</em>','Enët, oborri, dyqani, mësimet.'),
   slide(2,'lt','Kështu mësuam','Që pushimi duhet merituar. <em>Dhe s’e meritonim&nbsp;kurrë.</em>'),
   slide(3,'lt','Sot','Ulesh pas punës <em>dhe&nbsp;ndihesh&nbsp;fajtor.</em>'),
   slide(4,'lt','E vërteta','Të rrish pak „kot“ s’është dembeli. <em>Është&nbsp;frymë.</em>'),
   end(5,'Rri pak. <em>Dhe fol me dikë pa&nbsp;emër.</em>')]
sets['02-kot']=page(bgB,floorB+chores(380)+broom+bucket+books+chair+sofa+''.join(S))

# 3: Rrobat pranë sobës (sjellje e fshehur me orë)
bgC='linear-gradient(180deg,#2E4A43 0%,#355449 60%,#3B5C50 100%)'
floorC=D(0,1700,W,220,'background:#24392F')
sx=1080+500
stove=glow(sx+120,1520,380,.45,'255,170,100')+D(sx,1380,260,320,'background:linear-gradient(180deg,#3A3F4A,#2A2E36);border-radius:14px')+D(sx+40,1560,180,90,'background:radial-gradient(ellipse at 50% 70%,#FFD08A,#E2702F 60%,#7A2E14);border-radius:10px')+D(sx+90,1080,80,300,'background:#3A3F4A')
stool=D(sx-460,1520,300,26,'background:#8A6A3F;border-radius:8px')+D(sx-440,1546,20,154,'background:#5E4630')+D(sx-200,1546,20,154,'background:#5E4630')
clothes=D(sx-450,1440,280,80,'background:#8FB8A8;border-radius:12px')+D(sx-430,1400,240,50,'background:#E9E1C8;border-radius:10px')+D(sx-420,1370,220,36,'background:#D6A24C;border-radius:8px')
heat=''.join(D(sx-380+k*60,1300-(k%2)*30,8,60,'background:rgba(255,206,140,.45);border-radius:4px;transform:rotate(10deg)') for k in range(4))
clock=D(80+2160+500,1100,200,200,'border:12px solid #8A6A3F;border-radius:50%;background:#FAF7F1')+D(2160+590,1140,12,70,'background:#221F1C;transform-origin:6px 70px;transform:rotate(180deg)')+D(2160+591,1150,10,60,'background:#221F1C;transform-origin:5px 60px;transform:rotate(180deg)')
win=D(3240+300,1050,420,360,'background:linear-gradient(180deg,#B9C9D9,#E9D3B0);border:18px solid #4A4F5A;border-radius:6px')+D(3240+500,1050,18,360,'background:#4A4F5A')
bag=D(3240+320,1500,280,200,'background:#C54F35;border-radius:30px 30px 14px 14px')+D(3240+400,1460,120,60,'border:12px solid #9E3A26;border-bottom:none;border-radius:30px 30px 0 0')
coatC=D(4320+380,1240,320,440,'background:#E8B96C;border-radius:120px 120px 20px 20px')+glow(4320+540,1450,330,.35)+D(4320+520,1200,40,40,'background:#D6A24C;border-radius:50%')
S=[slide(0,'dk','Ora 06:30 · Dimër','Rrobat e shkollës ishin të ngrohta. <em>Dikush i kishte vënë pranë sobës që&nbsp;natën.</em>','',HINT),
   slide(1,'dk','Ora 23:00','Kur flinin të gjithë, <em>ajo i palonte mbi&nbsp;stol.</em>'),
   slide(2,'dk','Ora 06:00','Ngrihej e para <em>dhe e ndizte sobën para&nbsp;nesh.</em>'),
   slide(3,'dk','Ti','Visheshe pa e ditur <em>pse ishin të&nbsp;ngrohta.</em>'),
   slide(4,'dk','Sot e kupton','Disa „të dua“ nuk thuheshin. <em>Visheshin.</em>'),
   end(5,'Kur të ftohet shpirti, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-rrobat']=page(bgC,floorC+stool+clothes+heat+stove+clock+win+bag+coatC+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
