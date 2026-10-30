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

# 1: Askush s'dëgjonte si gjyshja (urtësia e gjyshes)
bgA='linear-gradient(180deg,#3A2A22 0%,#4A3428 55%,#56402F 100%)'
kilim=D(0,1700,W,220,"background:repeating-linear-gradient(90deg,#9E3B2C 0 60px,#C98057 60px 120px,#E8B96C 120px 150px,#3F6259 150px 200px,#C98057 200px 260px);opacity:.92")+D(0,1700,W,30,"background:repeating-linear-gradient(90deg,#FAF7F1 0 20px,transparent 20px 40px);opacity:.6")
sofa=D(0,1480,W,230,'background:linear-gradient(180deg,#7A4A35,#64392A);border-radius:30px 30px 0 0')
glowA=glow(1080*0+620,1300,520,.22,'255,205,130')+glow(1080*2+540,1300,520,.18,'255,205,130')+glow(1080*4+540,1300,520,.2,'255,205,130')
cush=''.join(D(1080*k+x,1360,230,170,f'background:{c};border-radius:40px 40px 20px 20px;box-shadow:0 10px 20px rgba(0,0,0,.25)') for k,x,c in [(0,420,'#C98057'),(0,660,'#E8B96C'),(1,300,'#C98057'),(1,540,'#E8B96C')])
hands=glow(1080*3+560,1420,320,.25,'255,205,130')+D(1080*3+280,1380,340,130,'background:#E3B98E;border-radius:70px')+D(1080*3+500,1330,320,130,'background:#C99A72;border-radius:70px;box-shadow:0 10px 20px rgba(0,0,0,.2)')
lampA=D(1080*2+700,1060,40,420,'background:#2E2A2A')+D(1080*2+600,980,240,110,'background:#E8B96C;border-radius:30px 30px 8px 8px')
moon=D(1080*4+760,1000,130,130,'background:#F3E6C4;border-radius:50%;box-shadow:0 0 70px rgba(243,230,196,.5)')
S=[slide(0,'dk','Gjyshja','Askush s’dëgjonte si gjyshja. <em>Dhe ajo s’kishte lexuar asnjë&nbsp;libër.</em>','',HINT),
   slide(1,'dk','E para','Të ulte pranë vetes, <em>jo&nbsp;përballë.</em>','Sot e dimë: pranë njëri-tjetrit flitet më lehtë.'),
   slide(2,'dk','E dyta','Nuk të ndërpriste. <em>Thoshte vetëm „hë,&nbsp;pastaj?“</em>'),
   slide(3,'dk','E treta','Të mbante dorën <em>pa thënë&nbsp;asgjë.</em>'),
   slide(4,'dk','Në fund','„Mirë që e nxore. <em>Tani&nbsp;fli.“</em>'),
   end(5,'Kur s’ke pranë dikë që të dëgjon kështu, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-gjyshja']=page(bgA,glowA+sofa+cush+hands+lampA+moon+kilim+''.join(S))

# 2: „Burrat nuk qajnë“ (rregull i pashkruar)
bgB='linear-gradient(180deg,#1C2128 0%,#232A33 60%,#2A323C 100%)'
rnd=random.Random(36)
rain=''.join(D(rnd.randint(0,W),rnd.randint(900,1800),3,rnd.randint(40,90),'background:rgba(180,200,220,.18);border-radius:2px;transform:rotate(12deg)') for _ in range(160))
def tear(x,y,s,gold=False):
    c='#E8B96C' if gold else 'rgba(190,215,235,.85)'
    return D(x,y,s,int(s*1.3),f'background:{c};border-radius:50% 50% 50% 50%/60% 60% 40% 40%;transform:rotate(180deg);clip-path:polygon(50% 0,100% 55%,92% 82%,72% 98%,28% 98%,8% 82%,0 55%)')
tears=tear(1080*0+640,1300,140)+tear(1080*1+560,1340,110)+tear(1080*2+520,1360,90)+tear(1080*3+500,1380,70)+glow(1080*4+560,1440,300,.35,'232,185,108')+tear(1080*4+480,1330,170,True)
groundB=D(0,1780,W,140,'background:#14181E')
S=[slide(0,'dk','Rregull i pashkruar','„Burrat nuk qajnë.“ <em>Kush e ka shpikur këtë&nbsp;rregull?</em>','',HINT),
   slide(1,'dk','Kur e dëgjuam','Na e thanë kur ishim pesë vjeç. <em>Dhe e&nbsp;besuam.</em>'),
   slide(2,'dk','Çfarë mësuam','Ta mbajmë brenda. <em>Ta kthejmë në zemërim ose në&nbsp;heshtje.</em>'),
   slide(3,'dk','Brezat','Gjyshi e mbajti. Babai e mbajti. <em>Tani e mbajmë&nbsp;ne.</em>'),
   slide(4,'dk','E vërteta','Lotët nuk e bëjnë burrin më pak burrë. <em>E bëjnë&nbsp;njeri.</em>'),
   end(5,'Kur s’mund ta mbash më brenda, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['02-burrat']=page(bgB,rain+groundB+tears+''.join(S))

# 3: Vizita te i sëmuri (ritual shqiptar)
W3=7560
bgC='linear-gradient(180deg,#F6F2EA 0%,#F1E9DA 70%,#E9DDC6 100%)'
floorC=D(0,1720,W3,200,'background:linear-gradient(180deg,#D9C9AC,#CBB894)')
def bag(x,y):
    org=''.join(D(x+dx,y+dy,90,90,'background:radial-gradient(circle at 35% 35%,#FFB866,#E8892E);border-radius:50%') for dx,dy in [(30,-50),(110,-70),(70,-110),(150,-40)])
    return org+D(x,y,280,300,'background:rgba(250,247,241,.75);border:4px solid rgba(200,190,170,.9);border-radius:16px 16px 26px 26px')+D(x+40,y-30,60,60,'border:8px solid rgba(200,190,170,.9);border-radius:30px 30px 0 0;border-bottom:none')+D(x+180,y-30,60,60,'border:8px solid rgba(200,190,170,.9);border-radius:30px 30px 0 0;border-bottom:none')
def bottle(x,y,c):
    return D(x,y,90,260,f'background:{c};border-radius:18px 18px 12px 12px;opacity:.9')+D(x+28,y-50,34,60,f'background:{c};border-radius:8px')+D(x+22,y-64,46,22,'background:#3F6259;border-radius:6px')
bagC=bag(1080*0+560,1420)+bag(1080*1+330,1420)+bottle(1080*1+680,1460,'#F2A23A')+bottle(1080*1+790,1460,'#E8C04A')
chairs=''.join(D(1080*2+x,1380,150,40,'background:#8A6A3F;border-radius:8px')+D(1080*2+x,1420,20,300,'background:#6E5232')+D(1080*2+x+130,1420,20,300,'background:#6E5232')+D(1080*2+x,1220,20,200,'background:#6E5232') for x in [250,650])
bed=D(1080*3+200,1440,700,180,'background:#FAF7F1;border-radius:20px;box-shadow:0 10px 20px rgba(0,0,0,.08)')+D(1080*3+200,1380,200,90,'background:#FFFFFF;border-radius:40px')+D(1080*3+180,1300,30,420,'background:#B9BCB8;border-radius:8px')
phoneC=D(1080*4+450,1300,260,460,'background:#221F1C;border-radius:40px')+D(1080*4+468,1318,224,424,'background:#F3EFE7;border-radius:28px',"<div style=\"position:absolute;left:18px;right:18px;top:150px;padding:16px;border-radius:18px;background:#3F6259;color:#FAF7F1;font-family:Inter;font-weight:600;font-size:24px\">Shërim të shpejtë!</div>")
door=D(1080*5+380,1060,340,660,'background:linear-gradient(180deg,#A8845C,#94714C);border:16px solid #FAF7F1;border-bottom:none;border-radius:6px 6px 0 0')+D(1080*5+640,1060,80,660,'background:linear-gradient(90deg,rgba(255,226,170,.0),rgba(255,226,170,.55))')+glow(1080*5+700,1400,360,.35,'255,214,150')
S=[slide(0,'lt','Te ne, dikur','Kur dikush sëmurej, nuk i shkruanim. <em>Shkonim.</em>','',HINT),
   slide(1,'lt','Me çfarë','Me një qese portokalle <em>dhe dy shishe&nbsp;lëng.</em>'),
   slide(2,'lt','Sa','Rrinim një orë. <em>Shpesh pa folur&nbsp;shumë.</em>'),
   slide(3,'lt','Pse','Nuk e shëronte trupin. <em>E shëronte&nbsp;vetminë.</em>'),
   slide(4,'lt','Sot','Shkruajmë „shërim të shpejtë“. <em>Dhe mendojmë që&nbsp;mjafton.</em>'),
   slide(5,'lt','E vërteta','Ndonjëherë mjafton të shkosh. <em>Edhe pa&nbsp;fjalë.</em>'),
   end(6,'Kur s’ka kush të vijë, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-vizita']=page(bgC,floorC+bagC+chairs+bed+phoneC+door+''.join(S),w=W3)

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
