import random, sys
SK='/home/user/Shprehu-3.5/.claude/skills/shprehu-social-ads'
W=6480
CSS='''
html,body{width:6480px;height:1920px;overflow:hidden}
.pano{position:absolute;left:0;top:0;width:6480px;height:1920px;overflow:hidden}
.slide{position:absolute;top:0;width:1080px;height:1920px}
.safe{position:absolute;left:96px;right:150px;top:250px;bottom:460px;display:flex;flex-direction:column}
.tag{font-size:30px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;display:flex;gap:18px;align-items:center;margin-bottom:44px}
.tag::before{content:'';width:46px;height:3px;background:var(--gold);border-radius:2px}
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

import math
sets={}
HINT='Rrëshqit →'

def stars(n,seed,xmax=W,ymax=900,fade=False):
    random.seed(seed); o=''
    for _ in range(n):
        x=random.randint(20,xmax-20); y=random.randint(30,ymax); r=random.choice([2,2,3,4])
        if fade and random.random()<x/xmax*1.1: continue
        o+=D(x,y,r,r,f'background:#FAF7F1;border-radius:50%;opacity:{random.uniform(.35,.9):.2f}')
    return o

# A: Ka njerez qe e kane me keq (malet ne muzg)
def ridge(seed,base,amp,f1,f2):
    random.seed(seed); p1=random.uniform(0,6); p2=random.uniform(0,6)
    return lambda x: base-amp*(0.5+0.5*math.sin(x/f1+p1))-amp*0.55*abs(math.sin(x/f2+p2))
def ridge_svg(fn,color,op=1):
    pts=' '.join(f'L{x},{fn(x):.0f}' for x in range(0,W+60,60))
    return f'<path d="M0,1920 {pts} L{W},1920 Z" fill="{color}" opacity="{op}"/>'
r1=ridge(1,1480,300,420,230); r2=ridge(2,1580,230,360,170); r3=ridge(3,1690,170,300,140); r4=ridge(4,1800,70,500,210)
svg=f'<svg class="abs" style="left:0;top:0" width="{W}" height="1920" viewBox="0 0 {W} 1920">'+ridge_svg(r1,'#5B7378')+ridge_svg(r2,'#364F57')+ridge_svg(r3,'#22393B')+ridge_svg(r4,'#12201F')+'</svg>'
def house(x,fn,lit=True):
    y=fn(x)-6
    h=D(x,y-70,92,70,'background:#0A1413')+D(x-8,y-104,108,38,'background:#0A1413;clip-path:polygon(0 100%,50% 0,100% 100%)')
    if lit: h+=D(x+30,y-52,26,26,'background:#F6C86A;box-shadow:0 0 70px 26px rgba(246,200,106,.45)')
    return h
houses=''.join(house(x,r4) for x in (700,1900,2900,4300,5200))+house(1300,r4,False)+house(3600,r4,False)
moon=D(3240-130,980,260,260,'background:radial-gradient(circle at 40% 40%,#FFF3D0,#F0CF8E);border-radius:50%;box-shadow:0 0 220px 90px rgba(240,207,142,.28)')
S=[slide(0,'dk','Në shtëpi · 22:10','„Ka njerëz që <em>e kanë më keq.</em>“','E dëgjuam kur ishim të lodhur. Dhe heshtëm.',HINT),
   slide(1,'dk','Fjalia','Duket si ngushëllim. <em>Ndodh që na mbyll gojën.</em>','Nuk e zvogëlon hallin. Vetëm e bën më të vështirë për ta thënë.'),
   slide(2,'dk','Rregulli i pashkruar','Hallin tonë e matim me të tjerët, <em>para se ta themi.</em>','Dhe shumicën e herëve, nuk e themi fare.'),
   slide(3,'dk','Pyetja','A bëhet halli yt më i vogël <em>kur dikush ka më keq?</em>','Shkruaj në koment: po ose jo.'),
   slide(4,'dk','E vërteta','Dikush ka më keq. <em>Edhe ti je i lodhur.</em> Të dyja janë të vërteta.','Halli s’ka garë. Thuhet edhe pa u matur.'),
   end(5,'Thuaje pa emër, <em>pa e matur me askënd.</em>')]
sets['01-me-keq']=page('linear-gradient(180deg,#16222E 0%,#223A4A 40%,#5E6F72 62%,#C98B5B 82%,#E8B96C 92%)',stars(160,5)+moon+svg+houses+''.join(S))

# B: Shyqyr (nata kthehet ne agim mbi çatite)
def roofs(seed,y0,hmin,hmax,col,litcol,wmin,wmax,lit_fn,xmax=5700):
    random.seed(seed); x=-40; o=''
    while x<xmax:
        w=random.randint(wmin,wmax); h=random.randint(hmin,hmax)
        o+=D(x,y0-h,w,h,f'background:{col}')+D(x-12,y0-h-w//4,w+24,w//4,f'background:{col};clip-path:polygon(0 100%,50% 0,100% 100%)')
        if random.random()<.45: o+=D(x+w*.7,y0-h-w//4-26,16,50,f'background:{col}')
        nw=random.choice([1,2])
        for k in range(nw):
            if random.random()<lit_fn(x):
                o+=D(x+w*(.2+.4*k),y0-h*.65,w*.18,h*.22,f'background:{litcol};box-shadow:0 0 50px 18px rgba(246,200,106,.35)')
        x+=w+random.randint(-10,20)
    return o
sunx=4780
sun=(D(sunx-900,1000,1800,1800,'background:radial-gradient(circle,rgba(240,190,110,.55),rgba(240,190,110,0) 62%);border-radius:50%')
     +D(sunx-150,1440,300,300,'background:radial-gradient(circle,#FFF0C4,#F2B95E);border-radius:50%'))
back=roofs(31,1760,110,190,'#243742','#F6C86A',120,200,lambda x:max(0,.8-x/5200))
front=roofs(32,1920,150,260,'#0D161B','#F6C86A',170,280,lambda x:max(0,.95-x/4200))
tel=''
S=[slide(0,'dk','Në telefon · 07:20','„Si je?“ „<em>Shyqyr.</em>“ Dhe biseda mbaron aty.','Një fjalë që e thotë çdo shqiptar, edhe kur s’është shumë mirë.',HINT),
   slide(1,'dk','Një fjalë, shumë kuptime','‘Shyqyr’ mund të thotë: <em>jam mirë.</em> Ose: <em>mos pyet më.</em>','Varet nga zëri që e thotë.'),
   slide(2,'dk','Pse e themi','Sepse të pyesin me mirësi, dhe ne <em>s’duam t’i rëndojmë.</em>','Kështu heshtja kalon për mirënjohje.'),
   slide(3,'dk','Pyetja','A të ka pyetur dikush pas ‘shyqyr’-it: <em>‘vërtet?’</em>','Shkruaj në koment: po ose jo.'),
   slide(4,'dk','E vërteta','Mund të jesh mirënjohës <em>dhe i lodhur</em> në të njëjtën ditë.','E para nuk e fshin të dytën.'),
   end(5,'Pas ‘shyqyr’-it, <em>thuaje të vërtetën.</em>')]
bg2=('linear-gradient(180deg,rgba(10,18,24,.55),rgba(10,18,24,0) 62%),'
     'linear-gradient(90deg,#141E28 0%,#1B2C3A 30%,#2F4A58 58%,#5D7A80 80%,#8FA79B 100%)')
sets['02-shyqyr']=page(bg2,stars(190,9,xmax=5400,fade=True)+sun+back+front+''.join(S))

# C: Çka ndodh ne shtepi (oborri, porta qe hapet pak)
wall=(D(0,1500,W,420,'background:repeating-linear-gradient(90deg,transparent 0 158px,rgba(0,0,0,.38) 158px 162px),repeating-linear-gradient(0deg,#3A352F 0 76px,#24211D 76px 80px)')
      +D(0,1470,W,40,'background:#4A443B;border-bottom:4px solid #1B1815'))
hs=(D(300,1120,620,360,'background:#16130F')+D(260,1010,700,130,'background:#16130F;clip-path:polygon(0 100%,50% 0,100% 100%)')
    +D(430,1230,90,110,'background:#F6C86A;box-shadow:0 0 120px 50px rgba(246,200,106,.4)')+D(700,1230,90,110,'background:#2A2216'))
trees=''
random.seed(77)
for x in (1500,2250,5000,5600):
    trees+=D(x,1050,260,430,'background:#0E1512;border-radius:50% 50% 30% 30%/60% 60% 30% 30%')
def lantern(x):
    return (D(x-44,1380,88,140,'background:#4A443B;border:3px solid #1B1815')
            +D(x-300,1100,600,600,'background:radial-gradient(circle,rgba(255,214,140,.5),rgba(255,214,140,0) 66%);border-radius:50%')
            +D(x-20,1330,40,56,'background:#FFE6A8;border-radius:50%;box-shadow:0 0 50px 22px rgba(255,220,150,.7)'))
lan=''.join(lantern(x) for x in (1100,2900,5100))
gate=(D(3520,1280,640,640,'background:linear-gradient(90deg,#FFD98C,#F6C86A 60%,#D9A74B)')
      +D(3520,1280,300,640,'background:#4B3421;border:8px solid #2B1D10;box-shadow:inset 0 0 60px rgba(0,0,0,.45)')
      +D(3540,1300,260,620,'background:repeating-linear-gradient(90deg,transparent 0 56px,rgba(0,0,0,.35) 56px 60px)')
      +D(4040,1290,120,630,'background:#4B3421;border:8px solid #2B1D10;transform:skewY(-4deg)')
      +D(3380,1800,900,120,'background:radial-gradient(ellipse at 50% 20%,rgba(255,214,140,.65),rgba(255,214,140,0) 70%)')
      +D(3480,1260,720,34,'background:#2B1D10'))
S=[slide(0,'dk','Oborri · 21:30','„Çka ndodh në shtëpi, <em>mbetet në shtëpi.</em>“','E dëgjuam qysh të vegjël. E besuam.',HINT),
   slide(1,'dk','Rregulli','Ishte për ta mbrojtur shtëpinë. <em>Ndonjëherë mbron vetëm heshtjen.</em>','Sepse nuk i themi as vëllait, as shokut.'),
   slide(2,'dk','Jashtë portës','Jashtë: <em>„gjithçka mirë.“</em> Brenda: gjithçka që s’u tha.','Edhe lodhja. Edhe merakët.'),
   slide(3,'dk','Pyetja','A është e drejtë që <em>një hall</em> të mbetet brenda katër mureve?','Shkruaj në koment: po ose jo.'),
   slide(4,'dk','E vërteta','Porta mund të hapet <em>pak,</em> pa e bërë shtëpinë bisedë publike.','Mjafton një vend ku thuhet pa emër.'),
   end(5,'Shtëpia mbetet shtëpi. <em>Hallin thuaje pa emër.</em>')]
sets['03-oborri']=page('linear-gradient(180deg,#0F1613 0%,#17211D 55%,#223028 100%)',stars(110,13,ymax=700)+trees+hs+wall+lan+gate+''.join(S))

if __name__=='__main__':
    for k,v in sets.items():
        open(f'set-{k}.html','w').write(v)
    print(len(sets),'sets')
