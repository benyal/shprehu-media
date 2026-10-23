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

# 1: Nen dush, ora 22:30
bgA='linear-gradient(180deg,#0F1B20 0%,#1A2E34 55%,#223C42 100%)'
random.seed(31)
tiles=''
for r in range(9):
    for c in range(60):
        tiles+=D(c*110,1190+r*82,106,78,'background:rgba(143,184,168,.07);border-radius:4px')
steam=''.join(glow(random.randint(0,W),random.randint(300,1500),random.randint(180,420),.10,'200,225,230') for _ in range(26))
drops=''
for _ in range(190):
    x=random.randint(30,W-30); y=random.randint(130,1100); h=random.randint(26,70)
    drops+=D(x,y,4,h,'background:linear-gradient(180deg,rgba(200,230,240,0),rgba(200,230,240,.55));border-radius:3px')
head_=D(40,70,300,34,'background:#6C8087;border-radius:12px')+D(150,100,80,60,'background:#56666B;border-radius:8px')
head_+=''.join(D(70+i*18,128+(i%2)*6,3,110,'background:linear-gradient(180deg,rgba(210,235,245,.6),rgba(210,235,245,0))') for i in range(13))
mirror=D(5*1080+560,330,300,420,'border:10px solid #3A4B50;background:rgba(190,215,222,.18);border-radius:24px')+D(5*1080+640,470,140,16,'background:rgba(255,255,255,.35);border-radius:8px;transform:rotate(8deg)')
lamp=glow(1080*4+800,200,420,.22,'255,200,130')
S=[slide(0,'dk','Ora 22:30 · Nën dush','Uji rrjedh. <em>Ti po provon bisedën që s’e bën kurrë.</em>','Me zë të ulët, para pasqyrës së avullt.',HINT),
   slide(1,'dk','Çfarë i thua','Fjalinë e parë e di përmendësh. <em>Të dytën e ndryshon çdo herë.</em>','Dhe e fut sërish në fillim.'),
   slide(2,'dk','Kujt ia thua','Nënës. Shokut. Dikujt që të ka lënduar. <em>Në kokë, të gjithë të dëgjojnë.</em>'),
   slide(3,'dk','Pse nën dush','Aty askush s’të ndërpret. <em>As ti s’e ndalon veten.</em>','Uji mbulon zërin dhe ia lejon vetes të flasë.'),
   slide(4,'dk','E vërteta','Bisedat që i provon kaq shumë <em>shpesh kanë nevojë vetëm për një fjali të parë.</em>','Dhe një vend ku ta thuash pa u frikësuar.'),
   end(5,'Prove fjalinë e parë, <em>pa emër.</em>')]
sets['01-dushi']=page(bgA,tiles+steam+lamp+head_+drops+mirror+''.join(S))

# 2: Pesë mënyra si e kërkojmë ndihmën
W2=7560
bgB='linear-gradient(180deg,#F6F2EA 0%,#F3EFE7 74%,#E4DACA 74%,#DCD0BC 100%)'
doors=''
for i in range(1,6):
    x=i*1080+300
    gold=(i==4)
    doors+=D(x,1030,300,700,f"background:{'#E9D3A2' if gold else '#CFC3AE'};border:10px solid {'#B9862F' if gold else '#9C8F78'};border-radius:10px 10px 0 0")
    doors+=D(x+235,1390,18,18,f"background:{'#B9862F' if gold else '#7A6F5A'};border-radius:50%")
    if gold:
        doors+=D(x+60,1060,180,670,'background:linear-gradient(180deg,rgba(255,226,150,.9),rgba(255,226,150,.5))')
        doors+=D(x+300,1730,200,40,'background:linear-gradient(90deg,rgba(255,226,150,.8),rgba(255,226,150,0));transform:skewX(-35deg)')
    doors+=D(x+60,1090,180,30,f"font-weight:800;font-size:26px;letter-spacing:.12em;color:{'#7A5A1F' if gold else '#7A6F5A'};text-align:center",str(i))
floor_l=D(0,1730,W2,6,'background:#B8AA92')
S=[slide(0,'lt','Në shqip','5 mënyra si e kërkojmë ndihmën, <em>pa e kërkuar.</em>','E katërta është e vërteta.',HINT),
   slide(1,'lt','E para','„Je i zënë?“ <em>Dhe pret përgjigjen para se të vazhdosh.</em>'),
   slide(2,'lt','E dyta','„Po kaloja këndej.“ <em>Nuk kalonte askund.</em>'),
   slide(3,'lt','E treta','„S’ke ndonjë punë sot?“ <em>Të duhej vetëm dikush.</em>'),
   slide(4,'lt','E katërta','„Kam një pyetje të vogël.“ <em>Pyetja s’është e vogël.</em>','Dhe e di që kush e dëgjon, e ka kuptuar.'),
   slide(5,'lt','E pesta','„Hajde pimë diçka, kur të kesh kohë.“ <em>Dhe e mban atë ditë të lirë.</em>'),
   end(6,'Kur s’ke kujt t’ia thuash drejt, <em>thuaje pa emër.</em>')]
sets['02-dyert']=page(bgB,floor_l+doors+''.join(S),w=W2)

# 3: Ora 21:10, kuzhina e pastër
bgC='linear-gradient(180deg,#141C20 0%,#1B262B 62%,#0E1417 62%,#0A1013 100%)'
counter=D(0,1500,W,420,'background:linear-gradient(180deg,#26343A,#1A252A)')+D(0,1494,W,8,'background:#3A4A50')
random.seed(11)
lamps=''
for lx in (500,1900,3300,4700,6000):
    lamps+=glow(lx,1290,330,.36,'255,205,130')+D(lx-3,0,6,1080,'background:#0C1215')+D(lx-70,1050,140,100,'background:#E7C57A;border-radius:70px 70px 8px 8px;box-shadow:0 0 50px 18px rgba(255,205,130,.4)')
table=D(1080*3+70,1350,420,18,'background:#5A4636;border-radius:6px')+D(1080*3+90,1368,10,130,'background:#4A392C')+D(1080*3+470,1368,10,130,'background:#4A392C')
glass=D(1080*3+220,1290,40,60,'background:rgba(220,240,245,.55);border-radius:4px 4px 10px 10px')
rack=''.join(D(1500+k*34,1330,8,170,'background:#7B8C92;border-radius:4px') for k in range(8))+D(1480,1488,300,12,'background:#6A7A80;border-radius:6px')
towel=D(1080*5+120,1110,70,230,'background:linear-gradient(180deg,#3F6259,#2E4A43);border-radius:6px 6px 14px 14px')
S=[slide(0,'dk','Ora 21:10 · Pas darke','Të gjitha punët mbaruan. <em>Por s’ndihesh i lehtë.</em>','Pjatat janë larë. Tryeza është pastruar.',HINT),
   slide(1,'dk','Çfarë pret','Mendoje se kur t’i mbaroje gjithçka, <em>do të pushoje.</em>','Atë që e kishe lënë për më vonë.'),
   slide(2,'dk','Çfarë ndodh','Duart nuk kanë më çfarë të bëjnë. <em>Mendja ka tani gjithë kohën.</em>'),
   slide(3,'dk','Pse','Gjithë ditën mbajtëm veten të zënë. <em>Heshtja del kur mbarojnë punët.</em>','Është e zakonshme dhe nuk do të thotë se po bën diçka keq.'),
   slide(4,'dk','E vërteta','Pushimi nuk vjen kur mbaron lista. <em>Vjen kur të lejon vetes ta ndiesh.</em>','Edhe një fjali e thënë me zë e lehtëson pak.'),
   end(5,'Kur punët mbarojnë dhe mendimet nisin, <em>thuaji dikujt.</em>')]
sets['03-kuzhina']=page(bgC,counter+lamps+table+glass+rack+towel+''.join(S))

if __name__=='__main__':
    for k,v in sets.items():
        open(f'set-{k}.html','w').write(v)
    print(len(sets),'sets')
