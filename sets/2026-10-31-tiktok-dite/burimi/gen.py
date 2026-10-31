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

# 1: 5 fjalë të urta të gjyshërve (urtësi + listë me boshllëk)
W2=7560
bgA='linear-gradient(180deg,#F6F1E6 0%,#F1E9DA 100%)'
cloth=D(0,1470,W2,330,'background:#FBF8F1;box-shadow:0 -6px 24px rgba(120,90,50,.10)')
border=''
for row,y in [(0,1500),(1,1752)]:
    for k in range(0,W2//44):
        c='#3F6259' if k%3 else '#D6A24C'
        border+=D(k*44+10,y,22,22,f'background:{c};transform:rotate(45deg)')
thread=D(0,1630,W2,6,'background:repeating-linear-gradient(90deg,#3F6259 0 34px,transparent 34px 56px)')
motifs=''
for i in range(1,6):
    cx=i*1080+520; gold=(i==4)
    c='#D6A24C' if gold else '#3F6259'
    for dx,dy in [(-120,0),(120,0),(0,-100),(0,100),(-85,-70),(85,-70),(-85,70),(85,70)]:
        motifs+=D(cx+dx-18,1633+dy-18,36,36,f'background:{c};transform:rotate(45deg);opacity:.9')
    motifs+=D(cx-80,1553,160,160,f'background:#FBF8F1;border:6px solid {c};transform:rotate(45deg)')
    motifs+=D(cx-80,1553,160,160,f"font-family:'Fraunces',serif;font-weight:600;font-size:92px;text-align:center;line-height:160px;color:{'#B9862F' if gold else '#3F6259'}",str(i))
needle=D(1080*5+760,1600,300,10,'background:linear-gradient(90deg,#9AA3A0,#D9DEDC);border-radius:5px;transform:rotate(-14deg)')
S=[slide(0,'lt','Fjalë të urta','5 fjalë të gjyshërve që janë psikologji e pastër. <em>E katërta na duhet më shumë&nbsp;sot.</em>','',HINT),
   slide(1,'lt mid','E para','„Kush pyet, <em>s’humb&nbsp;udhë.“</em>','Të kërkosh ndihmë s’është dobësi. Është rruga më e&nbsp;shkurtër.'),
   slide(2,'lt mid','E dyta','„Gjuha s’ka kocka, <em>por kocka&nbsp;thyen.“</em>','Edhe fjalët që ia themi&nbsp;vetes.'),
   slide(3,'lt mid','E treta','„Fjala e ëmbël e nxjerr gjarprin <em>nga&nbsp;vrima.“</em>','Butësia i hap njerëzit më shumë se zëri i&nbsp;lartë.'),
   slide(4,'lt mid','E katërta','„I ngopuri <em>s’i&nbsp;beson të&nbsp;uriturit.“</em>','Kur je mirë, harron sa rëndë e ka tjetri. Mos ia mat hallin me kutin&nbsp;tënd.'),
   slide(5,'lt mid','E pesta','„Miku njihet <em>në ditë të&nbsp;keqe.“</em>','Dhe ndonjëherë, ai mik mund të jesh&nbsp;ti.'),
   end(6,'Kur s’ke kë të pyesësh, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-fjalet']=page(bgA,cloth+border+thread+motifs+needle+''.join(S),w=W2).replace('</style>','.mid .safe{justify-content:center;padding-bottom:120px}.mid h1{font-size:118px}</style>',1)

# 2: „Mos e trego, se të marrin mësysh“ (rregull i pashkruar)
bgB='linear-gradient(180deg,#EEF2EC 0%,#F4EFE4 55%,#EFE5D1 100%)'
sunB=glow(1080*1+820,980,260,.45)+D(1080*1+760,920,120,120,'background:#F1CF8A;border-radius:50%')
groundB=D(0,1700,W,220,'background:linear-gradient(180deg,#CDBB98,#BCA67F)')
G='#BDB5A8'
house=(D(380,1440,1600,30,f'background:{G}')+D(380,1160,1600,30,f'background:{G}')
      +''.join(D(x,1160,46,540,f'background:{G}') for x in [380,780,1180,1580,1934])
      +''.join(D(x,1060,10,100,'background:#6F6A62') for x in [395,420,795,820,1195,1220,1595,1620,1950,1975])
      +''.join(D(x,y,90,44,'background:#C98A62;border:3px solid #E9DCCB') for x in range(440,760,96) for y in range(1480,1700,48))
      +D(1640,1500,180,200,'background:#8F6B48;border-radius:4px'))
garlic=''.join(D(1650+k*36,1470+(k%2)*8,34,40,'background:#F4EEE2;border:3px solid #D8CDB8;border-radius:50% 50% 45% 45%') for k in range(5))
doll=(D(1300,1190,4,90,'background:#6F6A62')+D(1272,1270,60,60,'background:#E9D5B5;border-radius:50%')
      +D(1252,1325,100,140,'background:#3F6259;clip-path:polygon(50% 0,100% 100%,0 100%)')
      +D(1232,1345,140,16,'background:#3F6259;border-radius:8px'))
def chest(x,open_=False):
    s=D(x,1480,460,220,'background:linear-gradient(180deg,#9C7449,#7F5C38);border-radius:10px')
    s+=''.join(D(x+40+k*100,1520,60,60,'border:5px solid #D6A24C;transform:rotate(45deg);opacity:.7') for k in range(4))
    if open_:
        s=glow(x+230,1420,330,.55)+s+D(x,1300,460,60,'background:#8A6540;border-radius:10px;transform:perspective(600px) rotateX(55deg);transform-origin:bottom')
    else:
        s+=D(x-6,1440,472,60,'background:#8A6540;border-radius:12px 12px 4px 4px')+D(x+205,1470,50,64,'background:#D6A24C;border-radius:8px')
    return s
chests=chest(1080*2+300)+chest(1080*4+300,True)
key=D(1080*3+420,1660,120,20,'background:#D6A24C;border-radius:10px')+D(1080*3+380,1640,60,60,'border:12px solid #D6A24C;border-radius:50%')
S=[slide(0,'lt','Rregull i pashkruar','„Mos e trego, se të marrin mësysh.“ <em>Kështu mësuam ta fshehim edhe të&nbsp;mirën.</em>','',HINT),
   slide(1,'lt','Në çdo lagje','Kukulla në katin e dytë. <em>Hudhra mbi&nbsp;derë.</em>','Shtëpia e re duhej ruajtur nga syri i keq. Edhe lajmi i&nbsp;mirë.'),
   slide(2,'lt','Që fëmijë','Mos e thuaj sa fiton. <em>Mos e thuaj që je&nbsp;mirë.</em>','As që e more punën, as që po ndërton. Prit sa të jetë e&nbsp;sigurt.'),
   slide(3,'lt','Dhe e keqja?','As ajo s’thuhet. <em>Ajo është „punë e&nbsp;shtëpisë“.</em>','Kështu s’flasim as për të mirën, as për të&nbsp;keqen.'),
   slide(4,'lt','E vërteta','Mësyshin s’e ka parë kush. <em>Heshtjen po, çdo&nbsp;ditë.</em>','Një gëzim i thënë bëhet më i madh. Një hall i thënë bëhet më i&nbsp;lehtë.'),
   end(5,'E mirë apo e rëndë, <em>thuaje te dikush pa&nbsp;emër.</em>')]
sets['02-mesysh']=page(bgB,sunB+groundB+house+garlic+doll+chests+key+''.join(S))

# 3: Ajvari në oborr (ritual shqiptar me kuptim të ri)
bgC='linear-gradient(180deg,#F3EFE4 0%,#F6EBD6 60%,#EEDDBF 100%)'
suns=''.join(glow(1080*i+760,y,240,.42)+D(1080*i+705,y-55,110,110,'background:#F1CF8A;border-radius:50%') for i,y in [(0,1250),(1,1080),(2,980),(3,1040),(4,1180)])
groundC=D(0,1700,W,220,'background:linear-gradient(180deg,#C9B48C,#B59E76)')
rnd=random.Random(38)
smoke=''
for k in range(46):
    t=k/45; x=int(760+t*4900); y=int(1420-math.sin(t*math.pi*3)*60-t*80+rnd.randint(-20,20)); r=rnd.randint(50,95)
    smoke+=D(x-r,y-r,2*r,2*r,f'background:radial-gradient(circle,rgba(150,145,138,.{rnd.randint(16,26)}),rgba(150,145,138,0) 70%);border-radius:50%')
def pepper(x,y,rot,c='#B8402E'):
    return D(x,y,90,30,f'background:linear-gradient(180deg,{c},#8E2E22);border-radius:15px 40px 40px 15px;transform:rotate({rot}deg)')+D(x-14,y+8,18,12,f'background:#3F6259;border-radius:4px;transform:rotate({rot}deg)')
roaster=D(600,1500,300,200,'background:linear-gradient(90deg,#4A4642,#6B6661,#4A4642);border-radius:14px')+D(570,1470,360,34,'background:#2F2C29;border-radius:8px')+glow(750,1640,120,.5,'255,150,80')
roaster+=''.join(pepper(600+k*70,1438+(k%2)*6,(k*17)%40-20) for k in range(4))
stools=''.join(D(1080+x,1600,150,24,'background:#8A6A3F;border-radius:6px')+D(1080+x+20,1624,16,76,'background:#5E4630')+D(1080+x+114,1624,16,76,'background:#5E4630') for x in [260,520,780])
bowl=D(2160+320,1560,420,140,'background:linear-gradient(180deg,#C7CCCB,#9DA3A2);border-radius:20px 20px 200px 200px')
bowl+=''.join(pepper(2160+360+k*58,1530+(k%3)*8,(k*29)%50-25) for k in range(6))
wire=D(3240,1200,2160,4,'background:#6F6A62')+D(3236,1200,12,500,'background:#6F6A62')
rope=''.join(D(3330+k*72,1206,30,104,f'background:linear-gradient(180deg,#B8402E,#8E2E22);border-radius:12px 12px 16px 16px/12px 12px 60px 60px') for k in range(10))
table=D(4320+180,1540,620,26,'background:#8A6A3F;border-radius:6px')+D(4320+220,1566,20,134,'background:#5E4630')+D(4320+740,1566,20,134,'background:#5E4630')
jars=''.join(D(4320+220+k*120,1420,96,120,'background:linear-gradient(180deg,#C54F35,#9E3A26);border:5px solid rgba(255,255,255,.55);border-radius:12px 12px 16px 16px')+D(4320+226+k*120,1404,84,24,'background:#D6A24C;border-radius:6px') for k in range(5))
S=[slide(0,'lt','Tetor · Ora 09:00','Oborri mbushej me tym specash. <em>Askush s’e bënte ajvarin&nbsp;vetëm.</em>','',HINT),
   slide(1,'lt','Ora 10:30','Fqinjat vinin pa i ftuar. <em>Secila me thikën e&nbsp;vet.</em>'),
   slide(2,'lt','Ora 12:00','Duart qëronin speca. <em>Gojët nxirrnin&nbsp;hallet.</em>','Ato që s’i thoshe në tryezë, dilnin aty, mes&nbsp;tymit.'),
   slide(3,'lt','Ora 14:30','Askush s’e quante „ndihmë“. <em>Por&nbsp;ishte.</em>','Një hall i thënë mes punës peshonte më pak.'),
   slide(4,'lt','Sot','Ajvarin e blejmë gati. <em>Muhabetin s’e shet&nbsp;kush.</em>','Por nevoja për një oborr ku flitet s’ka&nbsp;ikur.'),
   end(5,'Kur të mungon ai oborr, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-ajvari']=page(bgC,suns+smoke+groundC+roaster+stools+bowl+wire+rope+table+jars+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
