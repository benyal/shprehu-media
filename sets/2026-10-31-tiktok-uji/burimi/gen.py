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

# 1: Ujë pas (ritual shqiptar)
bgA='linear-gradient(180deg,#F6F1E6 0%,#EEE6D6 60%,#E4D8C2 100%)'
groundA=D(0,1700,W,220,'background:linear-gradient(180deg,#CDBB98,#BCA67F)')
road=D(1080*3,1700,1080*2,220,'background:linear-gradient(180deg,#B9AE9C,#A89C88);clip-path:polygon(0 100%,40% 0,60% 0,100% 100%)')
doorA=D(1080*0+560,1000,380,700,'background:linear-gradient(180deg,#A8845C,#94714C);border:18px solid #FAF7F1;border-bottom:none;border-radius:6px 6px 0 0')+D(1080*0+600,1300,26,26,'background:#E8B96C;border-radius:50%')
rnd=random.Random(37)
drops=''
for k in range(70):
    t=k/69; x=int(1080*0+760+t*1500); y=int(1560-math.sin(t*math.pi)*420+rnd.randint(-30,30))
    s=rnd.randint(14,30)
    drops+=D(x,y,s,int(s*1.3),f'background:rgba(120,180,210,.{rnd.randint(55,85)});border-radius:50% 50% 50% 50%/60% 60% 40% 40%')
splash=''.join(D(1080*2+x,1690,w,14,'background:rgba(120,180,210,.45);border-radius:7px') for x,w in [(300,200),(560,140),(420,120)])
suit=D(1080*3+560,1500,220,190,'background:#3F6259;border-radius:20px')+D(1080*3+620,1460,100,50,'border:12px solid #2E4A43;border-bottom:none;border-radius:30px 30px 0 0')
cupA=D(1080*4+420,1560,130,140,'background:rgba(220,235,240,.35);border:8px solid rgba(240,245,245,.9);border-radius:8px 8px 22px 22px')+D(1080*4+428,1610,114,82,'background:rgba(120,180,210,.55);border-radius:0 0 16px 16px')
S=[slide(0,'lt','Te ne, kur dikush nisej','Nëna i hidhte ujë pas. <em>Që rruga të shkonte si&nbsp;uji.</em>','',HINT),
   slide(1,'lt','Çfarë do të thoshte','„Shko mbarë. <em>Dhe kthehu&nbsp;shpejt.“</em>'),
   slide(2,'lt','Pse uji','Nuk e thoshte me fjalë. <em>E thoshte me një gotë&nbsp;ujë.</em>'),
   slide(3,'lt','Sot','Sot dërgojmë „arrite?“ <em>Është i njëjti&nbsp;ujë.</em>'),
   slide(4,'lt','E vërteta','Kush të hedh ujë pas <em>të pret të&nbsp;kthehesh.</em>'),
   end(5,'Kur të mungon dikush që të pret, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-uji']=page(bgA,groundA+road+doorA+drops+splash+suit+cupA+''.join(S))

# 2: „Po dal për bukë“, ora 21:40
bgB='linear-gradient(180deg,#1B2130 0%,#222A3A 60%,#293246 100%)'
street=D(0,1720,W,200,'background:#151A24')+D(0,1700,W,20,'background:#2E3646')
lamps=''.join(glow(1080*k+800,1180,300,.30,'255,214,150')+D(1080*k+790,1180,20,540,'background:#3A4252')+D(1080*k+740,1150,120,40,'background:#E8B96C;border-radius:20px 20px 6px 6px') for k in range(0,5))
shop=D(1080*1+120,1230,520,470,'background:#2E3646;border-radius:8px')+D(1080*1+160,1290,440,280,'background:radial-gradient(circle at 50% 40%,#FFE6B0,#E9B25E);border-radius:6px')+D(1080*1+160,1250,440,30,"background:#3F6259;border-radius:4px;font-family:Inter;font-weight:800;font-size:22px;color:#FAF7F1;text-align:center;line-height:30px;letter-spacing:.2em",'BUKË')
bench=D(1080*2+160,1560,520,26,'background:#8A6A3F;border-radius:8px')+D(1080*2+160,1500,520,22,'background:#8A6A3F;border-radius:8px')+D(1080*2+190,1586,20,120,'background:#5E4630')+D(1080*2+640,1586,20,120,'background:#5E4630')
bread=D(1080*3+300,1520,320,150,'background:linear-gradient(180deg,#E3B567,#C98A3E);border-radius:150px 150px 40px 40px;box-shadow:0 14px 26px rgba(0,0,0,.35)')+''.join(D(1080*3+x,1545,16,70,'background:rgba(255,240,200,.6);border-radius:8px;transform:rotate(25deg)') for x in [380,450,520])
moonB=D(1080*4+300,1000,130,130,'background:#F3E6C4;border-radius:50%;box-shadow:0 0 70px rgba(243,230,196,.45)')
S=[slide(0,'dk','Ora 21:40 · Në shtëpi','„Po dal për bukë.“ <em>Dhe ecën dyzet&nbsp;minuta.</em>','',HINT),
   slide(1,'dk','Dyqani','Është dy minuta larg. <em>Ti ulesh në stolin e&nbsp;parkut.</em>'),
   slide(2,'dk','Pse','Në shtëpi s’ka vend <em>për të qenë vetëm me&nbsp;veten.</em>'),
   slide(3,'dk','Pastaj','Kthehesh me bukën në dorë. <em>Dhe pak më&nbsp;lehtë.</em>'),
   slide(4,'dk','E vërteta','Edhe ti ke të drejtë për dyzet minuta <em>vetëm për&nbsp;vete.</em>'),
   end(5,'Kur s’ke ku të shkosh me mendimet, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['02-buka']=page(bgB,street+lamps+shop+bench+bread+moonB+''.join(S))

# 3: 5 fjali të nënës kur del nga shtëpia
W2=7560
bgC='linear-gradient(180deg,#F6F2EA 0%,#F1E9DA 100%)'
floorC=D(0,1720,W2,200,'background:#E6DAC0')
bubbles=''
for i in range(1,6):
    x=i*1080+300; gold=(i==4)
    col='#F3D9A0' if gold else '#FFFFFF'; bd='#D6A24C' if gold else '#CFC4AE'
    bubbles+=D(x,1340,440,240,f'background:{col};border:8px solid {bd};border-radius:60px;box-shadow:0 14px 26px rgba(120,90,50,.12)')
    bubbles+=D(x+70,1572,70,56,f'background:{bd};clip-path:polygon(0 0,100% 0,0 100%)')+D(x+78,1570,52,42,f'background:{col};clip-path:polygon(0 0,100% 0,0 100%)')
    bubbles+=D(x,1340,440,240,f"font-family:'Fraunces',serif;font-weight:600;font-size:110px;text-align:center;line-height:240px;color:{'#B9862F' if gold else '#9C8F78'}",str(i))
S=[slide(0,'lt','Kur del nga shtëpia','5 fjali që i thotë çdo nënë shqiptare kur del nga shtëpia. <em>E katërta s’është&nbsp;kontroll.</em>','',HINT),
   slide(1,'lt','E para','„Merr xhaketë, <em>se&nbsp;ftohet.“</em>'),
   slide(2,'lt','E dyta','„I ke marrë <em>çelësat?“</em>'),
   slide(3,'lt','E treta','„Mos u vono <em>shumë.“</em>'),
   slide(4,'lt','E katërta','„Më shkruaj kur të arrish.“ <em>S’është kontroll. Është&nbsp;dashuri.</em>'),
   slide(5,'lt','E pesta','„Hajde, <em>shko&nbsp;mbarë.“</em>'),
   end(6,'Kur s’ka kush të presë mesazhin tënd, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-nena']=page(bgC,floorC+bubbles+''.join(S),w=W2)

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
