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


# 1: Plehrat, ora 22:10
bgA='linear-gradient(180deg,#0F1A22 0%,#16242A 55%,#1D2A2A 100%)'
random.seed(4)
stars=''.join(D(random.randint(0,W),random.randint(20,1150),4,4,'background:#EDE6D2;border-radius:50%;opacity:.55') for _ in range(140))
lamps=''
for x in (1080*0+880,1080*2+300,1080*4+820):
    lamps+=glow(x+70,1500,330,.28,'255,220,150')+D(x+64,1500,14,420,'background:#2E3B3C')+D(x+20,1484,110,26,'background:#EDE6D2;border-radius:13px;box-shadow:0 0 60px 24px rgba(255,220,150,.35)')
bld=''
for x in range(0,W,260):
    h=random.randint(120,260)
    bld+=D(x,1760-h,240,h,'background:#121D22')
    for k in range(3):
        if random.random()<.45: bld+=D(x+30+k*70,1760-h+40,36,46,'background:#E8C77A;opacity:.6;border-radius:3px')
bins=''
for x in (1080*1+560,1080*1+790):
    bins+=D(x,1590,200,200,'background:#3F6259;border-radius:10px 10px 6px 6px')+D(x-10,1572,220,30,'background:#2E4A43;border-radius:8px')
bag=D(1080*3+640,1650,140,140,'background:#C9C2B2;border-radius:60px 60px 30px 30px')+D(1080*3+690,1620,40,40,'border:6px solid #C9C2B2;border-radius:50%')
floor=D(0,1760,W,160,'background:#0C1418')
S=[slide(0,'dk','Ora 22:10 · „Po i nxjerr plehrat“','Del t’i hedhësh plehrat. <em>Por s’kthehesh&nbsp;menjëherë.</em>','Qesja shkon brenda në dy sekonda.',HINT),
   slide(1,'dk','Jashtë','Rri pak nën dritën e rrugës. <em>Askush s’ka nevojë për ty&nbsp;këtu.</em>'),
   slide(2,'dk','Telefoni','E ke në xhep, por s’e nxjerr. <em>Dhjetë minuta askush s’të&nbsp;gjen.</em>'),
   slide(3,'dk','Kthimi','Ngjitesh ngadalë. <em>Brenda thua „ishte ftohtë&nbsp;jashtë“.</em>'),
   slide(4,'dk','E vërteta','Nuk ike nga askush. <em>Të duhej pak ajër që s’e kërkove me&nbsp;zë.</em>'),
   end(5,'Kur dhjetë minuta s’mjaftojnë, <em>fol me dikë pa emër.</em>')]
sets['01-plehrat']=page(bgA,stars+bld+floor+lamps+bins+bag+''.join(S))

# 2: Kthimi nga puna, lista
W2=7560
bgB='linear-gradient(180deg,#F6F2EA 0%,#EFE8DB 100%)'
rail=D(0,1490,W2,22,'background:#B08D60;border-radius:11px')
hooks=''
for i in range(1,6):
    x=i*1080+540; gold=(i==4)
    hooks+=D(x-20,1500,40,60,f"background:{'#D6A24C' if gold else '#9C8F78'};border-radius:0 0 20px 20px")
    if gold:
        hooks+=D(x-170,1540,340,300,'background:linear-gradient(180deg,#3F6259,#2E4A43);border-radius:110px 110px 24px 24px')
    else:
        hooks+=D(x-40,1580,80,80,f"font-family:'Fraunces',serif;font-weight:600;font-size:56px;text-align:center;color:#B8AA92",str(i))
keys=D(1080*1+760,1700,90,50,'border:8px solid #B9862F;border-radius:50%')+D(1080*1+700,1820,360,18,'background:#D9CDB6;border-radius:9px')
phone=D(1080*3+780,1720,130,210,'background:#2B2B2B;border-radius:20px')
S=[slide(0,'lt','Ora 18:20 · Te dera','5 gjëra që i bëjmë kur kthehemi nga puna. <em>E katërta e bëjmë të&nbsp;gjithë.</em>','',HINT),
   slide(1,'lt','E para','I lë çelësat në tavolinë <em>me një zhurmë që thotë „mbarova“.</em>'),
   slide(2,'lt','E dyta','Pyet „a ka ndodhur gjë?“ <em>dhe shpreson që të thonë&nbsp;jo.</em>'),
   slide(3,'lt','E treta','Telefonin e kthen me ekran poshtë. <em>Vetëm për&nbsp;pak.</em>'),
   slide(4,'lt','E katërta','Ulesh me xhaketën veshur. <em>Dhe s’e heq për dhjetë&nbsp;minuta.</em>','Trupi është në shtëpi. Mendja ende&nbsp;jo.'),
   slide(5,'lt','E pesta','Kur të pyesin si ishte, <em>thua&nbsp;„normal“.</em>'),
   end(6,'Kur „normal“ s’është e vërteta, <em>thuaje pa emër.</em>')]
sets['02-puna']=page(bgB,rail+hooks+keys+phone+''.join(S),w=W2)

# 3: Seria mbaroi, ora 23:40
bgC='linear-gradient(180deg,#1B1A22 0%,#221F26 60%,#2A2420 100%)'
tv=glow(1080*1+540,1600,620,.30,'150,190,210')
tv+=D(1080*1+180,1480,720,300,'background:#0E1418;border:12px solid #3A3A40;border-radius:14px')
tv+=D(1080*1+230,1560,620,60,"color:#C9D6DC;font-family:'Fraunces',serif;font-style:italic;font-size:54px;text-align:center",'Fund')
tv+=D(1080*1+230,1650,620,10,'background:#3F6259;border-radius:5px')
tv+=D(1080*1+500,1780,80,60,'background:#3A3A40')
cred=''.join(D(1080*2+380,1500+k*46,320 - (k%3)*60,16,'background:rgba(201,214,220,.35);border-radius:8px') for k in range(7))
couch=D(0,1800,W,120,'background:#3A2F28')+D(1080*3+150,1640,780,170,'background:#5A4636;border-radius:60px 60px 14px 14px')+D(1080*3+220,1600,200,120,'background:#8FB8A8;opacity:.7;border-radius:30px')
lampw=glow(1080*4+800,1520,360,.35,'255,210,140')+D(1080*4+760,1500,80,320,'background:#2E2A2A')+D(1080*4+690,1420,220,100,'background:#C99A4E;border-radius:24px 24px 6px 6px')
S=[slide(0,'dk','Ora 23:40 · Episodi i fundit','Mbaron seria që e ndoqe me javë. <em>Dhe ndihesh sikur iku&nbsp;dikush.</em>','',HINT),
   slide(1,'dk','Titrat','I lë titrat të shkojnë deri në fund. <em>S’do të ngrihesh&nbsp;ende.</em>'),
   slide(2,'dk','Ndjesia','S’është trishtim i vërtetë. <em>Por shtëpia duket më e qetë se&nbsp;dje.</em>'),
   slide(3,'dk','Pse ndodh','Për disa javë, ata ishin shoqëria e mbrëmjes. <em>Tani mbrëmja ka një vend&nbsp;bosh.</em>'),
   slide(4,'dk','E vërteta','Nuk ke humbur asgjë. <em>Por diçka mbaroi, dhe kjo&nbsp;ndihet.</em>','Ndonjëherë na mungon jo seria, por&nbsp;shoqëria.'),
   end(5,'Kur mbrëmja ka një vend bosh, <em>fol me dikë pa emër.</em>')]
sets['03-seria']=page(bgC,tv+cred+couch+lampw+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
