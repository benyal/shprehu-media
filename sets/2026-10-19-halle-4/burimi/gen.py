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

import math
sets={}
HINT='Rrëshqit →'

def stars(n,seed,xmax=W,ymax=900):
    random.seed(seed); o=''
    for _ in range(n):
        x=random.randint(20,xmax-20); y=random.randint(30,ymax); r=random.choice([2,2,3,4])
        o+=D(x,y,r,r,f'background:#FAF7F1;border-radius:50%;opacity:{random.uniform(.3,.85):.2f}')
    return o

def glow(x,y,r,a=.5):
    return D(x-r,y-r,2*r,2*r,f'background:radial-gradient(circle,rgba(255,214,140,{a}),rgba(255,214,140,0) 66%);border-radius:50%')

# A: Po ti, kur? (tryeza ne oborr me drita)
def garland(a,b,y0,sag):
    mx=(a+b)/2
    svg=f'<svg class="abs" style="left:0;top:0" width="{W}" height="1920" viewBox="0 0 {W} 1920"><path d="M{a},{y0} Q{mx},{y0+2*sag} {b},{y0}" fill="none" stroke="#0B0F12" stroke-width="5"/></svg>'
    bulbs=''
    for k in range(1,9):
        t=k/9; x=(1-t)**2*a+2*(1-t)*t*mx+t*t*b; y=(1-t)**2*y0+2*(1-t)*t*(y0+2*sag)+t*t*y0
        bulbs+=glow(x,y+20,90,.42)+D(x-13,y,26,34,'background:#FFE6A8;border-radius:50% 50% 45% 45%;box-shadow:0 0 30px 10px rgba(255,224,150,.55)')
    return svg+bulbs
gar=''.join(garland(a,a+1100,1150,70) for a in range(-100,W,1100))
chairs=''.join(D(x,1380,190,290,'background:#150F0B;border-radius:22px 22px 4px 4px')+D(x+20,1400,150,30,'background:#241912;border-radius:10px') for x in range(120,W,540) if x!=3180)
chairs+=D(3040,1400,190,270,'background:#150F0B;border-radius:22px 22px 4px 4px;transform:rotate(-14deg)')+D(3060,1470,200,150,'background:#3F6259;border-radius:16px;transform:rotate(-8deg);opacity:.9')
cloth=D(0,1690,W,230,'background:linear-gradient(180deg,#F1EADA,#D9CFB8)')+D(0,1684,W,16,'background:#FAF7F1')
tab=''
for x in range(60,W,330):
    tab+=D(x,1650,160,32,'background:#FAF7F1;border-radius:50%;box-shadow:0 8px 14px rgba(0,0,0,.25)')+D(x+30,1634,100,12,'background:#E6DDCB;border-radius:50%')
    tab+=D(x+190,1596,34,88,'background:linear-gradient(180deg,rgba(255,214,140,.35),rgba(214,162,76,.8));border-radius:4px 4px 10px 10px')
for x in range(250,W,990):
    tab+=D(x,1560,46,120,'background:#FAF7F1;border-radius:6px')+D(x+20,1514,6,40,'background:#3A2C1E')+glow(x+23,1500,150,.55)+D(x+8,1470,30,52,'background:radial-gradient(ellipse at 50% 70%,#FFF4C8,#F2B544 55%,rgba(242,181,68,0) 72%);border-radius:50%')
S=[slide(0,'dk','Në tryezë · 14:30','„Po ti, <em>kur?</em>“','Pyetja që vjen para ëmbëlsirës.',HINT),
   slide(1,'dk','Pyetja','Kur martohesh. Kur bën fëmijë. <em>Kur e gjen punën.</em>','E pyesin me dashuri. Dhe prapë rëndon.'),
   slide(2,'dk','Përgjigjja','Buzëqesh dhe thua: <em>„Kur të vijë koha.“</em>','Pastaj shikon pjatën.'),
   slide(3,'dk','Pyetja','A është pyetje e mirë, apo <em>presion i butë?</em>','Shkruaj në koment: dashuri ose presion.'),
   slide(4,'dk','E vërteta','Koha jote <em>s’ka orar</em> të përbashkët me tryezën.','Ke të drejtë të thuash: ende s’e di.'),
   end(5,'Për pyetjet pa përgjigje, <em>thuaje pa emër.</em>')]
sets['01-po-ti-kur']=page('linear-gradient(180deg,#121C26 0%,#1A2933 55%,#26302E 100%)',stars(150,41,ymax=800)+gar+chairs+cloth+tab+''.join(S))

# B: Do te takohemi se shpejti (rruga me llamba gjithnje me larg)
xs=[420,1100,1950,3000,4300,5800]
lamps=''
for x in xs:
    lamps+=(glow(x,1180,330,.5)+D(x-5,1200,11,540,'background:#0B0F13')+D(x-60,1186,80,14,'background:#0B0F13')+D(x-70,1196,36,22,'background:#FFE6A8;border-radius:0 0 18px 18px;box-shadow:0 0 50px 20px rgba(255,224,150,.6)')
            +D(x-300,1700,600,220,'background:radial-gradient(ellipse at 50% 0,rgba(255,214,140,.38),rgba(255,214,140,0) 70%)')
            +D(x-140,1830,280,36,'background:radial-gradient(ellipse,rgba(255,224,150,.5),rgba(255,224,150,0) 70%)'))
random.seed(55)
far=''
for _ in range(180):
    x=random.randint(0,W); 
    if random.random()<x/W*1.2: continue
    far+=D(x,random.randint(1500,1580),5,5,'background:#FFD98C;border-radius:50%;box-shadow:0 0 12px 4px rgba(255,217,140,.5);opacity:.8')
road=(D(0,1700,W,220,'background:linear-gradient(180deg,#151A20,#0E1217)')+D(0,1696,W,8,'background:#2A333D')
      +''.join(D(x,1812,120,8,'background:#5E6A72;opacity:.6') for x in range(0,W,260)))
hills=D(0,1560,W,140,'background:#0D1217')
bench=D(3300,1640,300,18,'background:#0A0D10')+D(3320,1580,260,14,'background:#0A0D10')+D(3330,1656,12,50,'background:#0A0D10')+D(3556,1656,12,50,'background:#0A0D10')
S=[slide(0,'dk','Në telefon · 22:20','„Do të takohemi <em>së shpejti.</em>“','E thamë të gjithë. Pa e menduar.',HINT),
   slide(1,'dk','Së shpejti','„Së shpejti“ ka kohë të gjatë <em>në shqip.</em>','Ditët kalojnë, dhe fjala mbetet e njëjtë.'),
   slide(2,'dk','Shoku','Nuk ka ndryshuar. <em>Vetëm jeta u mbush me hall.</em>','Dhe të dy po presin që tjetri të shkruajë i pari.'),
   slide(3,'dk','Pyetja','Kush duhet të shkruajë i pari? <em>Ti apo ai?</em>','Shkruaj në koment: unë ose ai.'),
   slide(4,'dk','E vërteta','Një mesazh i shkurtër <em>mjafton:</em> „Të mendova.“','Nuk ka nevojë për arsye.'),
   end(5,'Nëse s’je gati t’i shkruash dikujt, <em>thuaje pa emër.</em>')]
sets['02-se-shpejti']=page('linear-gradient(180deg,#151F2C 0%,#223347 50%,#4A4E5B 78%,#C98B5B 92%)',stars(150,52,ymax=700)+far+hills+road+bench+lamps+''.join(S))

# C: Vitrina (gotat e mira per mysafire)
wall=D(0,0,W,1920,'background:repeating-linear-gradient(90deg,rgba(255,255,255,.018) 0 40px,transparent 40px 80px)')
def frame(x,y,w,h):
    return D(x,y,w,h,'background:#2E1F13;border:8px solid #8A6A3E;box-shadow:0 10px 24px rgba(0,0,0,.4)')+D(x+16,y+16,w-32,h-32,'background:linear-gradient(135deg,#6E5A44,#3C2E22)')
frames=''.join(frame(x,y,w,h) for x,y,w,h in [(1500,1050,150,190),(1690,1000,200,150),(1930,1070,170,210),(3500,1020,180,220),(3730,1080,230,160),(4000,1010,160,200)])
vit=D(480,1260,760,660,'background:#3A2414;border:10px solid #5A3C22')
vit+=D(500,1280,720,610,'background:linear-gradient(135deg,rgba(255,235,190,.16),rgba(255,235,190,.04));border:2px solid rgba(255,230,180,.2)')
vit+=D(500,1440,720,14,'background:#5A3C22')+D(500,1610,720,14,'background:#5A3C22')+glow(860,1560,460,.35)
for i in range(6):
    x=540+i*110
    vit+=D(x,1380,72,56,'background:#F3EFE7;border-radius:6px 6px 36px 36px/6px 6px 40px 40px')+D(x-4,1376,80,10,'background:#D6A24C;border-radius:4px')+D(x+60,1396,26,30,'border:6px solid #F3EFE7;border-left:0;border-radius:0 18px 18px 0')
    vit+=D(x-6,1546,84,56,'background:#F3EFE7;border-radius:50% 50% 8px 8px/70% 70% 8px 8px;opacity:.95')
vit+=D(560,1470,70,70,'background:linear-gradient(180deg,#F2D58F,#C9A04A);border-radius:50% 50% 10px 10px/30% 30% 10px 10px')+D(580,1442,30,34,'background:#C9A04A;border-radius:6px')
for i in range(4):
    vit+=D(540+i*160,1650,140,140,'background:radial-gradient(circle,#FAF7F1 0 56%,#D6A24C 58% 64%,#FAF7F1 66%);border-radius:50%;opacity:.95')
floor=D(0,1860,W,60,'background:linear-gradient(180deg,#4A2F1A,#2E1D10)')+D(0,1856,W,6,'background:#6B4A2F')
lampx=2750
lamp=(glow(lampx,1480,620,.55)+D(lampx-6,1560,12,300,'background:#1B130D')+D(lampx-90,1420,180,150,'background:linear-gradient(180deg,#F8E3B0,#E7BD72);clip-path:polygon(18% 0,82% 0,100% 100%,0 100%);box-shadow:0 0 80px 30px rgba(255,214,140,.4)')
      +D(lampx-70,1856,140,12,'background:#1B130D'))
side=D(2380,1780,720,26,'background:#4A2F1A')+D(2420,1806,18,56,'background:#2E1D10')+D(3042,1806,18,56,'background:#2E1D10')+D(2500,1768,500,14,'background:radial-gradient(ellipse,#F3EFE7 0 60%,transparent 62%)')
mx=4400
mug=(D(mx-200,1790,520,28,'background:#4A2F1A')+D(mx-160,1818,18,44,'background:#2E1D10')+D(mx+262,1818,18,44,'background:#2E1D10')
     +D(mx,1716,100,76,'background:#BFB08E;border-radius:6px 6px 24px 24px')+D(mx+92,1730,34,40,'border:8px solid #BFB08E;border-left:0;border-radius:0 22px 22px 0')+D(mx+38,1716,5,40,'background:#2A1E10;transform:rotate(14deg)')
     +''.join(D(mx+24+i*22,1640-i*8,34,74,f'background:rgba(255,235,200,{.22-i*.05:.2f});border-radius:50%;filter:blur(8px)') for i in range(3)))
S=[slide(0,'dk','Në sallon · 20:10','„Këtë e <em>ruajmë për mysafirë.</em>“','Gotat e mira, në vitrinë, prej vitesh.',HINT),
   slide(1,'dk','Në vitrinë','Takëmi i mirë nuk përdoret. <em>Ruhet për një ditë të madhe.</em>','Që nuk vjen shpesh.'),
   slide(2,'dk','Në kuzhinë','Ndërkohë ti pi çaj <em>në gotën e plasaritur.</em>','Sepse ti je në shtëpi, jo mysafir.'),
   slide(3,'dk','Pyetja','A i ruan edhe ti <em>gjërat e mira</em> për më vonë?','Shkruaj në koment: po ose jo.'),
   slide(4,'dk','E vërteta','Edhe ti <em>je dikush.</em> Edhe ti e meriton gotën&nbsp;e&nbsp;mirë.','Dhe që të të dëgjojnë, jo vetëm kur vjen dikush.'),
   end(5,'Edhe ti je mysafir këtu. <em>Fol pa emër.</em>')]
sets['03-vitrina']=page('linear-gradient(180deg,#1B130D 0%,#2A1C12 55%,#3B2716 100%)',wall+frames+vit+floor+side+lamp+mug+''.join(S))

if __name__=='__main__':
    for k,v in sets.items():
        open(f'set-{k}.html','w').write(v)
    print(len(sets),'sets')
