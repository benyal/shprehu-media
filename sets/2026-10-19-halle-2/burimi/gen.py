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

sets={}
HINT='Rrëshqit →'

# A: 15 euro
grid=D(0,0,W,1920,'background-image:linear-gradient(rgba(63,98,89,.10) 2px,transparent 2px),linear-gradient(90deg,rgba(63,98,89,.10) 2px,transparent 2px);background-size:60px 60px')
grid+=D(70,0,4,1920,'background:rgba(176,74,44,.45)')
ruler=D(0,1660,W,120,'background:#F1D9A0;border-top:3px solid #C9A65B;border-bottom:3px solid #C9A65B')
for k in range(0,W//27):
    x=k*27
    h=48 if k%10==0 else (32 if k%5==0 else 20)
    ruler+=D(x,1663,3,h,'background:#8A6A2E')
    if k%10==0: ruler+=D(x+6,1715,80,40,'font-size:26px;font-weight:700;color:#8A6A2E',str(k//10))
pencils=''
for i,(x,c) in enumerate([(700,'#D6A24C'),(1750,'#3F6259'),(2900,'#B04A2C'),(3950,'#5E8C7D'),(5050,'#D6A24C'),(6000,'#3F6259')]):
    pencils+=D(x,1560,300,46,f'background:{c};border-radius:6px 0 0 6px;transform:rotate(-4deg)')
    pencils+=D(x+300,1548,0,0,f'border-left:60px solid #E8C99A;border-top:24px solid transparent;border-bottom:24px solid transparent;transform:rotate(-4deg);transform-origin:-300px 23px')
note=('<div style="margin-top:46px;background:#FFFDF6;border-radius:10px;padding:34px 40px;box-shadow:0 18px 40px rgba(34,31,28,.14);transform:rotate(-2deg);font-size:38px;line-height:1.4;color:#4A443C;max-width:720px">'
      '<div style="font-size:26px;font-weight:800;letter-spacing:.12em;color:#B04A2C;margin-bottom:10px">NJOFTIM PËR PRINDËRIT</div>'
      'Për ekskursionin e javës tjetër, ju lutemi sillni pagesën deri nesër.</div>')
coins=('<div style="margin-top:56px;display:flex;gap:26px;align-items:flex-end">'
      +''.join(f'<div style="width:{s}px;height:{s}px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#F2D58F,#C9A04A);border:5px solid #A9822F;display:flex;align-items:center;justify-content:center;font-size:{s//3}px;font-weight:800;color:#6E5320">{t}</div>' for s,t in [(150,'2'),(130,'1'),(110,'1'),(96,'0.5'),(84,'0.2')])+'</div>')
S=[slide(0,'lt','Çanta e shkollës · 21:40','„Ma, nesër duhen <em>15&nbsp;euro</em> për shkollë.“','Fëmija e thotë lehtë. Prindi e dëgjon ndryshe.',HINT),
   slide(1,'lt','Letra në çantë','Vjen e palosur, <em>në fund të çantës.</em>','',' ',note),
   slide(2,'lt','Përgjigja','„S’ka gjë, <em>i gjejmë.</em>“','E thotë pa u menduar, sepse ashtu thuhet në shtëpi.'),
   slide(3,'lt','Pas derës','Pastaj numëron vetëm, <em>në kuzhinë.</em>','Dy herë. Si të kishte ndryshuar diçka.',' ',coins),
   slide(4,'lt','Rregulli i pashkruar','„Fëmija s’duhet ta dijë <em>kurrë</em> që s’kemi.“','Fëmija s’ka pse ta mbajë hallin. Por as ti s’ke pse ta mbash vetëm.'),
   end(5,'Atë që s’ia thua fëmijës, <em>thuaje&nbsp;pa&nbsp;emër.</em>')]
sets['01-15-euro']=page('#FAF7F1',grid+ruler+pencils+''.join(S))

# B: muajin tjetër (ekrani i krisur)
def crack():
    import math
    random.seed(21)
    paths=[]
    x,y=0,1720
    pts=[(x,y)]
    while x<W:
        x+=random.randint(70,160); y=max(1520,min(1880,y+random.randint(-90,90))); pts.append((x,y))
    paths.append(' '.join(f'{"M" if i==0 else "L"}{a},{b}' for i,(a,b) in enumerate(pts)))
    for (a,b) in pts[3::4]:
        L=[(a,b)]
        ang=random.choice([-1,1])*random.uniform(0.6,1.3)
        for _ in range(random.randint(2,4)):
            a+=math.cos(ang)*random.randint(50,110); b+=math.sin(ang)*random.randint(50,110); ang+=random.uniform(-.5,.5)
            L.append((a,max(1480,min(1910,b))))
        paths.append(' '.join(f'{"M" if i==0 else "L"}{p:.0f},{q:.0f}' for i,(p,q) in enumerate(L)))
    cx,cy=820,1660
    for k in range(9):
        ang=k*2*math.pi/9+.3; r=random.randint(120,260)
        paths.append(f'M{cx},{cy} L{cx+math.cos(ang)*r*.5:.0f},{cy+math.sin(ang)*r*.5+random.randint(-14,14):.0f} L{cx+math.cos(ang)*r:.0f},{cy+math.sin(ang)*r:.0f}')
    rings=''.join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(250,247,241,.18)" stroke-width="2" stroke-dasharray="{d}"/>' for r,d in [(60,'30 18'),(130,'50 30')])
    return (f'<svg class="abs" style="left:0;top:0" width="{W}" height="1920" viewBox="0 0 {W} 1920">'
            +''.join(f'<path d="{p}" fill="none" stroke="rgba(250,247,241,.55)" stroke-width="3"/><path d="{p}" fill="none" stroke="rgba(143,184,168,.25)" stroke-width="9" transform="translate(4,3)"/>' for p in paths)
            +rings+'</svg>')
glass=D(0,0,W,1920,'background:linear-gradient(115deg,rgba(255,255,255,.05) 0 18%,transparent 18% 40%,rgba(255,255,255,.035) 40% 47%,transparent 47%)')
lst=('<div style="margin-top:44px;background:rgba(250,247,241,.08);border:2px solid rgba(250,247,241,.18);border-radius:24px;padding:30px 38px;font-size:42px;color:#FAF7F1">'
     '<div style="font-size:26px;font-weight:800;letter-spacing:.12em;color:#8FB8A8;margin-bottom:12px">SHËNIME · MUAJIN TJETËR</div>'
     +''.join(f'<div style="display:flex;gap:22px;align-items:center;padding:14px 0;border-bottom:2px solid rgba(250,247,241,.12)"><span style="width:30px;height:30px;border-radius:8px;border:3px solid #8FB8A8;flex:none"></span>{t}</div>' for t in ['Ekrani i telefonit','Tabani i këpucës','Dentisti','Syzet e reja'])
     +'<div style="display:flex;gap:22px;align-items:center;padding:14px 0;color:#E8B96C"><span style="width:30px;height:30px;border-radius:8px;border:3px solid #E8B96C;flex:none"></span>Si ndihem unë</div></div>')
S=[slide(0,'dk','Ekrani · që nga marsi','Ekrani u kris në mars. <em>Ende „muajin tjetër“.</em>','Punon. Pak me kujdes, por punon.',HINT),
   slide(1,'dk','Lista','Nuk është vetëm <em>telefoni.</em>','',' ',lst),
   slide(2,'dk','Si thuhet në shtëpi','„S’ka nevojë, <em>punon ende.</em>“','E thamë për gjërat. Pastaj nisëm ta themi edhe për veten.'),
   slide(3,'dk','Rregulli i pashkruar','Së pari të tjerët, <em>pastaj ti.</em> Nëse&nbsp;mbetet.','Sa herë ka mbetur?'),
   slide(4,'dk','E vërteta','Disa gjëra mund të presin. <em>Si ndihesh ti, jo&nbsp;gjithmonë.</em>','Të flasësh nuk kushton. As nuk pret muajin tjetër.'),
   end(5,'Falas, pa emër. <em>Sot, jo muajin tjetër.</em>')]
sets['02-muajin-tjeter']=page('linear-gradient(90deg,#1E2B27,#172320 60%,#13201C)',glass+crack()+''.join(S))

# C: iku drita
glow=''
for x,r,o in [(760,620,.55),(1650,520,.35),(2700,560,.4),(3750,500,.3),(5075,620,.45)]:
    glow+=D(x-r,1640-r,2*r,2*r,f'background:radial-gradient(circle,rgba(232,185,108,{o}),rgba(232,185,108,0) 70%);border-radius:50%')
table=D(0,1760,W,160,'background:#2B2018')+D(0,1756,W,8,'background:#4A3726')
def candle(x,h=200):
    return (D(x,1760-h,70,h,'background:linear-gradient(90deg,#F3E9D2,#FFFDF6 40%,#E3D6B8);border-radius:10px 10px 4px 4px')
            +D(x-30,1752,130,16,'background:#8A6A3E;border-radius:8px')
            +D(x+33,1760-h-30,4,30,'background:#3A2C1E')
            +D(x+14,1760-h-96,42,80,'background:radial-gradient(ellipse at 50% 70%,#FFF4C8,#F2B544 55%,rgba(242,181,68,0) 72%);border-radius:50% 50% 50% 50%/60% 60% 40% 40%'))
props=candle(720)
props+=(D(1560,1640,120,118,'background:#F7F1E3;border:4px solid #CFC4AC;border-radius:6px 6px 55px 55px/6px 6px 70px 70px')
        +D(2620,1700,190,56,'background:#1A1512;border:4px solid #4A3E33;border-radius:14px')
        +D(2640,1714,40,28,'background:#D6A24C;border-radius:4px')
        +D(2700,1708,100,40,'font-size:28px;font-weight:800;color:#E8B96C','14%')
        +D(3700,1690,140,68,'background:#C9A04A;border-radius:10px 10px 30px 30px;opacity:.85'))
bulb=D(5000,1180,150,190,'background:radial-gradient(circle at 50% 40%,#FFF6D6,#F2C766 60%,#D6A24C);border-radius:50% 50% 45% 45%/55% 55% 45% 45%;box-shadow:0 0 140px 60px rgba(242,199,102,.45)')+D(5040,1360,70,50,'background:#8A8073;border-radius:6px')+D(5072,980,6,200,'background:#4A3E33')
S=[slide(0,'dk','Në shtëpi · 20:15','Iku drita. <em>Dhe papritur, filluam të flasim.</em>','Pa televizor, pa wifi. Vetëm një qiri në tavolinë.',HINT),
   slide(1,'dk','Rreth qiririt','Telefoni në 14%. <em>Askush s’e merr në dorë.</em>','Ruhet për ndonjë thirrje. Dhe mbeten fjalët.'),
   slide(2,'dk','Në errësirë','Në errësirë <em>thuhen gjëra</em> që ditën&nbsp;s’thuhen.','Sepse askush s’të sheh në fytyrë.'),
   slide(3,'dk','Pyetja','A duhet <em>të ikë drita</em> që të flasim me njëri-tjetrin?','Shkruaje në koment: po apo jo.'),
   slide(4,'dk','E vërteta','Fjalët nuk kanë pse <em>ta presin errësirën.</em>','Mund të thuhen edhe sot, me dritën ndezur.'),
   end(5,'Kur s’ke kujt t’ia thuash, <em>thuaje&nbsp;pa&nbsp;emër.</em>')]
sets['03-iku-drita']=page('linear-gradient(90deg,#15110D,#1C1610 45%,#2A2117 80%,#3A2E1E)',glow+table+props+bulb+''.join(S))

if __name__=='__main__':
    for k,v in sets.items():
        open(f'set-{k}.html','w').write(v)
    print(len(sets),'sets')
