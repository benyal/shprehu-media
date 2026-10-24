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

# 1: Banja e zyres, ora 13:50
bgA='linear-gradient(180deg,#E9EFEC 0%,#DDE7E3 100%)'
tiles=D(0,0,W,1760,'background:repeating-linear-gradient(0deg,transparent 0 118px,rgba(143,184,168,.28) 118px 122px),repeating-linear-gradient(90deg,transparent 0 118px,rgba(143,184,168,.28) 118px 122px)')
floor=D(0,1760,W,160,'background:#C9D5CF')
sinks=''
for i in (1,3):
    x=1080*i+560
    sinks+=D(x,1180,340,430,'background:linear-gradient(160deg,rgba(255,255,255,.95),rgba(190,208,204,.8));border:12px solid #B5C3BE;border-radius:170px 170px 18px 18px')
    sinks+=D(x-40,1640,420,34,'background:#F7F7F2;border-radius:17px 17px 8px 8px;box-shadow:0 8px 20px rgba(0,0,0,.12)')
    sinks+=D(x+155,1560,30,90,'background:#9FB3AD;border-radius:6px')
door=D(1080*4+560,1180,360,580,'background:#CDBFA6;border:10px solid #B8A98C;border-radius:8px 8px 0 0')+D(1080*4+860,1470,22,22,'background:#D6A24C;border-radius:50%')+D(1080*4+690,1240,100,30,'background:#B04A2C;border-radius:6px')
S=[slide(0,'lt','Ora 13:50 · Banja e zyrës','Del nga zyra për tri minuta. <em>Por s’të duhet&nbsp;banja.</em>','Mbyll derën dhe qëndron.',HINT),
   slide(1,'lt','Në pasqyrë','Lan duart dy herë. <em>Sa për të dëgjuar&nbsp;heshtjen.</em>'),
   slide(2,'lt','Pse aty','Është i vetmi vend ku s’të pyet askush <em>„e mbarove raportin?“</em>'),
   slide(3,'lt','Kthimi','Kthehesh me buzëqeshjen e rregulluar. <em>Askush s’e vë re që&nbsp;mungove.</em>'),
   slide(4,'lt','E vërteta','Nuk po ik nga puna. <em>Po kërkon tri minuta pa e mbajtur&nbsp;fytyrën.</em>'),
   end(5,'Kur tri minuta s’mjaftojnë, <em>fol me dikë pa emër.</em>')]
sets['01-zyra']=page(bgA,tiles+floor+sinks+door+''.join(S))

# 2: Ikja nga shtepia e prinderve, lista
W2=7560
bgB='linear-gradient(180deg,#F6EEDD 0%,#F0E4CC 100%)'
road=D(0,1790,W2,130,'background:#CFC3AA')
blocks=''
for k,x in enumerate(range(0,W2,360)):
    h=380+(k*53)%220
    blocks+=D(x+10,1790-h,330,h,'background:#E4D6B9')
    for r in range(3):
        for c in range(3):
            blocks+=D(x+40+c*95,1790-h+40+r*100,60,70,'background:#B9C9C6;opacity:.7;border-radius:4px')
lit=D(1080*4+640,1180,200,300,'background:#E4D6B9')+D(1080*4+690,1240,100,130,'background:#F3C873;border-radius:4px;box-shadow:0 0 70px 24px rgba(243,200,115,.5)')+D(1080*4+715,1290,50,80,'background:#8A6A3F;border-radius:25px 25px 0 0')
mirror=D(1080*4+470,1470,520,300,'background:rgba(255,255,255,.55);border:10px solid #B8AA92;border-radius:150px 150px 20px 20px;opacity:.95')
S=[slide(0,'lt','Ora 17:30 · Te porta e prindërve','5 gjëra që i bëjmë kur ikim nga shtëpia e prindërve. <em>E katërta s’mbaron&nbsp;kurrë.</em>','',HINT),
   slide(1,'lt','E para','Themi „po shkoj“ <em>dhe qëndrojmë edhe njëzet&nbsp;minuta.</em>'),
   slide(2,'lt','E dyta','Marrim çantën me ushqim <em>që s’e kishim&nbsp;kërkuar.</em>'),
   slide(3,'lt','E treta','Dëgjojmë „vish xhaketë“ <em>edhe pse jemi të rritur&nbsp;prej kohësh.</em>'),
   slide(4,'lt','E katërta','Shikojmë dritaren në pasqyrën e makinës <em>derisa nëna të&nbsp;zhduket.</em>','Dhe ajo ende po tund dorën.'),
   slide(5,'lt','E pesta','Shkruajmë „arrita“ sapo hyjmë. <em>Që ajo të flejë e&nbsp;qetë.</em>'),
   end(6,'Kur ka gjëra që s’ia thua as nënës, <em>fol me dikë pa emër.</em>')]
sets['02-prinderit']=page(bgB,road+blocks+lit+mirror+''.join(S),w=W2)

# 3: Pas diteliindjes, ora 00:10
bgC='linear-gradient(180deg,#1C1B24 0%,#241F28 60%,#2B2421 100%)'
random.seed(9)
balls=''
for i,x in enumerate(range(300,W,640)):
    col=['#8FB8A8','#D6A24C','#B9825A','#6E9C8C'][i%4]
    balls+=D(x,1200+(i*37)%160,110,140,f'background:{col};opacity:.55;border-radius:50% 50% 48% 48%')+D(x+54,1340+(i*37)%160,3,260,'background:rgba(237,230,210,.3)')
table=D(1080*1+120,1640,1500,26,'background:#6B5645;border-radius:8px')+D(1080*1+200,1666,24,150,'background:#4A3B30')+D(1080*1+1500,1666,24,150,'background:#4A3B30')
cake=D(1080*2+160,1560,300,80,'background:#E9D6B0;border-radius:14px')+D(1080*2+300,1590,160,50,'background:#241F28;border-radius:0 14px 14px 0')+''.join(D(1080*2+190+k*70,1470,12,80,'background:#8FB8A8;border-radius:4px') for k in range(3))+''.join(glow(1080*2+196+k*70,1460,70,.35,'255,210,140') for k in range(3))
plates=''.join(D(1080*3+160+k*150,1620,120,18,'background:#EDE6D2;border-radius:9px') for k in range(3))+D(1080*3+640,1560,100,80,'background:#8FB8A8;opacity:.8;border-radius:6px 6px 24px 24px')
lampw=glow(1080*4+800,1500,380,.30,'255,210,140')+D(1080*4+760,1500,80,320,'background:#2E2A2A')+D(1080*4+690,1420,220,100,'background:#C99A4E;border-radius:24px 24px 6px 6px')
floor=D(0,1815,W,105,'background:#171319')
S=[slide(0,'dk','Ora 00:10 · Pas ditëlindjes','Të gjithë ikën. Torta mbeti përgjysmë. <em>Ti rri me dritën&nbsp;ndezur.</em>','',HINT),
   slide(1,'dk','Tryeza','Mbledh pjatat ngadalë. <em>Sikur s’të nxitonte kush ta mbyllësh&nbsp;ditën.</em>'),
   slide(2,'dk','Mesazhet','Përgjigjesh „faleminderit“ dhjetë herë. <em>Dhe s’di pse ndihesh pak i&nbsp;lodhur.</em>'),
   slide(3,'dk','Pse ndodh','Gjithë ditën ishe në qendër. <em>Tani heshtja ka&nbsp;zë.</em>'),
   slide(4,'dk','E vërteta','Je mirënjohës dhe i lodhur njëherësh. <em>Të dyja mund të jenë të&nbsp;vërteta.</em>'),
   end(5,'Kur festa mbaron dhe heshtja mbetet, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-diteliindja']=page(bgC,balls+floor+table+cake+plates+lampw+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
