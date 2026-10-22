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
def page(bg,body,w=6480):
    return head().replace('6480px',f'{w}px')+f'</style></head><body><div class="pano" style="background:{bg}">{body}</div></body></html>'
def glow(x,y,r,a=.5,c='255,214,140'):
    return D(x-r,y-r,2*r,2*r,f'background:radial-gradient(circle,rgba({c},{a}),rgba({c},0) 66%);border-radius:50%')

# 1: Galeria, ora 01:30
bgA='linear-gradient(180deg,#13221E 0%,#1E3731 60%,#27453C 100%)'
years=[('2025',330),('2024',1000),('2023',1950),('2022',2900),('2021',3800),('2020',4420),('2019',4700)]
random.seed(19)
tiles=''
cols=[('#6E9C8C','#2E4A43'),('#8FB8A8','#3F6259'),('#D6A24C','#7A5A2A'),('#B9825A','#4A3322'),('#5E7F8F','#243B47'),('#A9B98F','#4F5F3A')]
x=330; ci=0
while x<5400:
    for r in range(3):
        a,b=random.choice(cols)
        warm=x/5400
        op=1-0.35*warm
        tiles+=D(x,1536+r*130,114,114,f'background:linear-gradient(135deg,{a},{b});border-radius:10px;opacity:{op:.2f}')
        if random.random()<.5: tiles+=D(x+62,1536+r*130+20,24,24,'background:rgba(255,240,200,.75);border-radius:50%;opacity:.8')
    x+=130
lab=''
for y_,xx in years:
    lab+=D(xx+10,1488,140,36,'font-size:30px;font-weight:800;letter-spacing:.1em;color:#8FB8A8',y_)+D(xx-6,1488,3,430,'background:rgba(143,184,168,.25)')
hi=glow(4760,1654,260,.55)+D(4690,1636,142,142,'background:linear-gradient(135deg,#F2D58F,#B9825A);border-radius:12px;border:6px solid #E8B96C;box-shadow:0 0 50px 14px rgba(232,185,108,.55)')+D(4740,1664,32,32,'background:#FFF4C8;border-radius:50%')
S=[slide(0,'dk','Ora 01:30 · Në shtrat','Zbret në galeri. <em>Deri te foto e 2019-ës.</em>','Dhe rri aty, pa e ditur pse.',HINT),
   slide(1,'dk','Si fillon','Doje të shihje një gjë. <em>Dhe gjete një tjetër.</em>','Gishti vazhdon, foto pas fotoje, vit pas viti.'),
   slide(2,'dk','Çfarë ka brenda','Njerëz që i ke ende. <em>Dhe njerëz që s’i ke më afër.</em>','Një tryezë. Një verë. Një ditë që s’dukej e veçantë.'),
   slide(3,'dk','Pse e bëjmë','Nuk e kërkojmë të kaluarën. <em>Kërkojmë ndjesinë e atyre ditëve.</em>','Kur s’kishim aq hall në kokë.'),
   slide(4,'dk','E vërteta','Ta mallosh një ditë nuk do të thotë se je i mbërthyer. <em>Do të thotë se ke dashur.</em>','Dhe malli ka vend. Edhe pa u thënë me zë.'),
   end(5,'Kur malli s’ka kujt, <em>thuaje pa emër.</em>')]
sets['01-galeria']=page(bgA,tiles+lab+hi+''.join(S))

# 2: 5 menyra per te thene "me mungon"
W2=7560
bgB='#F3EFE7'
cord=''
for k in range(0,int(6600/22)):
    xx=40+k*22
    yy=1700+math.sin(xx/380)*46
    cord+=D(xx,yy-34,26,68,'border:6px solid #3F6259;border-radius:50%;opacity:.92')
def disc(x,n,gold=False):
    bgc='#D6A24C' if gold else '#3F6259'
    return D(x,1560,86,86,f'background:{bgc};border-radius:50%;color:#FAF7F1;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 24px rgba(34,31,28,.25)',str(n))
discs=''.join(disc(1080*i+150,i,gold=(i==4)) for i in range(1,6))
hand=lambda x:D(x,1650,160,60,'background:#2E4A43;border-radius:30px')+D(x-20,1620,70,120,'background:#2E4A43;border-radius:26px')+D(x+110,1620,70,120,'background:#2E4A43;border-radius:26px')
hands=hand(40)+hand(6120)
S=[slide(0,'lt','Në shqip','„Më mungon“ <em>nuk e themi.</em> E themi ndryshe.','5 mënyra që i njeh. E katërta e kemi bërë të gjithë.',HINT),
   slide(1,'lt','E para','„Po kaloja aty pari.“ <em>Nuk kalonte kurrë aty pari.</em>','Por një orë më vonë, ishe te dera.'),
   slide(2,'lt','E dyta','„S’kam ndonjë punë, <em>thjesht të telefonova.</em>“','Dhe flet gjatë, sepse s’e kishe mbyllur dot.'),
   slide(3,'lt','E treta','„Të pashë një foto dhe <em>të kujtova.</em>“','Dhe ia dërgon, pa tekst tjetër.'),
   slide(4,'lt','E katërta','„Kur po vjen?“ <em>Pyetja që do të thotë: kam nevojë të të shoh.</em>','Këtë e kemi thënë të gjithë.'),
   slide(5,'lt','E pesta','„Hajde, se po të presim për darkë.“ <em>Të gjitha thonë të njëjtën gjë.</em>','Më mungon. Dhe e kuptojnë vetëm ata që të njohin.'),
   end(6,'Nëse s’je gati t’ia thuash, <em>thuaje pa emër.</em>')]
sets['02-me-mungon']=page(bgB,cord+hands+discs+''.join(S),w=W2)

# 3: Muzgu, ora 16:40
bgC=('linear-gradient(180deg,rgba(8,14,18,.5),rgba(8,14,18,0) 60%),'
     'linear-gradient(90deg,#41606A 0%,#2D464F 30%,#1A2D33 60%,#101C20 100%)')
def ridge(base,amp,f,ph):
    return lambda x: base-amp*(0.5+0.5*math.sin(x/f+ph))
rA=ridge(1700,120,500,1); rB=ridge(1790,70,380,3)
def rsvg(fn,col):
    pts=' '.join(f'L{x},{fn(x):.0f}' for x in range(0,W+60,60))
    return f'<path d="M0,1920 {pts} L{W},1920 Z" fill="{col}"/>'
lines=[]
def branch(x0,y0,ang,length,depth,w):
    if depth==0 or length<9: return
    x1=x0+math.sin(ang)*length; y1=y0-math.cos(ang)*length
    lines.append(f'<line x1="{x0:.0f}" y1="{y0:.0f}" x2="{x1:.0f}" y2="{y1:.0f}" stroke="#070D0F" stroke-width="{w:.1f}" stroke-linecap="round"/>')
    kids=[-0.55,0.5]+([random.uniform(-.12,.12)] if depth>3 else [])
    for da in kids:
        branch(x1,y1,ang+da+random.uniform(-.18,.18),length*random.uniform(.68,.8),depth-1,max(1.3,w*.72))
random.seed(88)
for tx,th in [(720,430),(1500,360),(2350,470),(3300,390),(4150,450),(5000,380),(5800,420)]:
    branch(tx,rB(tx)+8,0,th*.3,7,11)
svgC=(f'<svg class="abs" style="left:0;top:0" width="{W}" height="1920" viewBox="0 0 {W} 1920">'+rsvg(rA,'#0F1A1D')+rsvg(rB,'#080F11')+''.join(lines)+'</svg>')
sun=glow(300,1640,520,.7,'255,190,110')+D(170,1500,260,260,'background:radial-gradient(circle,#FFE9B0,#F0A94E);border-radius:50%')
random.seed(7)
wins=''
for _ in range(70):
    xx=random.randint(0,W)
    if random.random()>(xx/W)*1.1+.15: continue
    yy=int(rA(xx))+random.randint(14,60)
    wins+=D(xx,yy,9,9,'background:#FFD98C;box-shadow:0 0 14px 5px rgba(255,217,140,.5);border-radius:2px')
S=[slide(0,'dk','Ora 16:40 · Nëntor','Errësohet. <em>Dhe të bie një mërzi pa emër.</em>','Të dielën orët kthehen një orë mbrapa. Muzgu vjen më herët.',HINT),
   slide(1,'dk','Ndjesia','Nuk ka ndodhur asgjë. <em>Por diçka rëndon.</em>','Si kur dita mbaron para se ta kesh përdorur.'),
   slide(2,'dk','Si e kalojmë','Ndezim dritën. Ndezim televizorin. <em>Ndezim gjithçka që flet.</em>','Që të mos dëgjohet heshtja.'),
   slide(3,'dk','Pse ndodh','Dielli ikën herët, <em>dhe mendja mbetet vetëm me veten.</em>','Është e zakonshme. Shumë njerëz e ndiejnë në dimër.'),
   slide(4,'dk','Çfarë ndihmon','Një shëtitje para errësirës. <em>Një fjalë e thënë me zë.</em>','Jo për ta zgjidhur. Për ta mbajtur më lehtë.'),
   end(5,'Kur errësohet herët, <em>thuaje pa emër.</em>')]
sets['03-muzgu']=page(bgC,sun+svgC+wins+''.join(S))

if __name__=='__main__':
    for k,v in sets.items():
        open(f'set-{k}.html','w').write(v)
    print(len(sets),'sets')
