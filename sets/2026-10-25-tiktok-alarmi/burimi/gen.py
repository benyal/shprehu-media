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

# 1: Kontrolli i fundit te dera, ora 22:40
bgA='linear-gradient(180deg,#13201F 0%,#1A2928 60%,#1F2F2C 100%)'
wall=D(0,0,W,1760,'background:repeating-linear-gradient(90deg,transparent 0 358px,rgba(143,184,168,.07) 358px 362px)')
floor=D(0,1760,W,160,'background:#0E1716')
dx=1080*1+420
door=D(dx,1130,420,630,'background:linear-gradient(180deg,#3A4A44,#2F3E39);border:12px solid #4B5E57;border-radius:10px 10px 0 0')
door+=D(dx+40,1190,340,200,'border:6px solid #4B5E57;border-radius:6px')+D(dx+40,1430,340,260,'border:6px solid #4B5E57;border-radius:6px')
door+=D(dx+330,1440,22,22,'background:#D6A24C;border-radius:50%')+D(dx+300,1340,80,16,'background:#D6A24C;border-radius:8px')
door+=D(dx+150,1500,120,10,'background:#9FB3AD;border-radius:5px')
lamp=glow(1080*2+260,1260,330,.28,'255,220,150')+D(1080*2+240,1230,40,70,'background:#EDE6D2;border-radius:8px;box-shadow:0 0 50px 20px rgba(255,220,150,.3)')
shoes=''.join(D(1080*3+160+k*150,1710,120,50,'background:#26302F;border-radius:30px 30px 8px 8px') for k in range(3))
hook=D(1080*4+600,1280,260,14,'background:#6B5645;border-radius:7px')+''.join(D(1080*4+640+k*70,1294,6,60,'background:#9FB3AD') + D(1080*4+620+k*70,1350,46,50,'border:7px solid #D6A24C;border-radius:50%') for k in range(3))
S=[slide(0,'dk','Ora 22:40 · Te dera','Mbyll derën. <em>Pastaj e provon edhe një&nbsp;herë.</em>','Sa për ta ditur që është mbyllur.',HINT),
   slide(1,'dk','Sobën','Shikon edhe sobën. <em>Edhe pse e fike para një&nbsp;ore.</em>'),
   slide(2,'dk','Pse','S’dyshon te dera. <em>Mendja do një gjë që mbyllet&nbsp;vërtet.</em>'),
   slide(3,'dk','Ora 22:43','Shkon në shtrat. <em>Dhe e dëgjon çelësin edhe një herë në&nbsp;mendje.</em>'),
   slide(4,'dk','E vërteta','Disa gjëra mbyllen me çelës. <em>Të tjerat duan t’i thuash me&nbsp;zë.</em>'),
   end(5,'Kur mendja s’mbyllet, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-dera']=page(bgA,wall+floor+door+lamp+shoes+hook+''.join(S))

# 2: Pritja e telefonates, lista
W2=7560
bgB='linear-gradient(180deg,#F6F2EA 0%,#F1E9DA 100%)'
rope=D(0,1240,W2,6,'background:#8A7A5E')
cloth=''
for i in range(1,6):
    x=i*1080+470; gold=(i==4)
    col='#F3D9A0' if gold else '#FFFFFF'
    bd='#D6A24C' if gold else '#CFC4AE'
    cloth+=D(x+30,1228,14,50,'background:#B9862F;border-radius:4px')+D(x+246,1228,14,50,'background:#B9862F;border-radius:4px')
    cloth+=D(x,1270,290,330,f'background:{col};border:8px solid {bd};border-radius:8px 8px 40px 40px;box-shadow:0 10px 24px rgba(120,90,50,.12)')
    cloth+=D(x,1330,290,160,f"font-family:'Fraunces',serif;font-weight:600;font-size:110px;line-height:160px;text-align:center;color:{'#B9862F' if gold else '#9C8F78'}",str(i))
phone=D(0+760,1500,170,300,'background:#2B2B2B;border-radius:26px;transform:rotate(-8deg);box-shadow:0 10px 24px rgba(0,0,0,.2)')+D(790,1530,110,200,'background:#3F6259;border-radius:14px;transform:rotate(-8deg);opacity:.9')
S=[slide(0,'lt','Kur presim një lajm','5 gjëra që i bëjmë kur presim një telefonatë të rëndësishme. <em>E katërta s’e&nbsp;pranojmë.</em>','',HINT),
   slide(1,'lt','E para','E shikojmë telefonin <em>çdo dy&nbsp;minuta.</em>'),
   slide(2,'lt','E dyta','I themi vetes „nuk po e pres“. <em>Dhe e vendosim&nbsp;afër.</em>'),
   slide(3,'lt','E treta','Pastrojmë shtëpinë pa arsye. <em>Dyert, raftet, edhe pjatat e&nbsp;pastra.</em>'),
   slide(4,'lt','E katërta','Bëjmë sikur s’na intereson. <em>Edhe pse mendja është vetëm&nbsp;aty.</em>'),
   slide(5,'lt','E pesta','Kur bie, i lëmë dy sekonda. <em>Që të mos duket se&nbsp;prisnim.</em>'),
   end(6,'Kur pritja të rëndon, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['02-telefonata']=page(bgB,rope+cloth+phone+''.join(S),w=W2)

# 3: Para alarmit, ora 06:55
bgC='linear-gradient(180deg,#1B2430 0%,#26323F 55%,#2F3B45 100%)'
dawn=D(0,1300,W,620,'background:linear-gradient(180deg,rgba(143,184,168,0),rgba(143,184,168,.16))')
win=D(1080*1+520,1010,380,500,'background:linear-gradient(180deg,#3E5568,#6F8A99);border:14px solid #4A5A63;border-radius:6px')+D(1080*1+700,1010,14,500,'background:#4A5A63')
bed=D(1080*2+120,1620,760,150,'background:#34414A;border-radius:24px')+D(1080*2+140,1560,200,90,'background:#8FB8A8;opacity:.55;border-radius:30px')+D(1080*2+340,1580,520,120,'background:#3E4F5A;border-radius:60px 60px 10px 10px')+D(1080*2+120,1500,30,270,'background:#26303A;border-radius:10px')
night=D(1080*3+240,1650,260,18,'background:#4A5A63;border-radius:9px')+D(1080*3+260,1668,20,110,'background:#4A5A63')+D(1080*3+460,1668,20,110,'background:#4A5A63')+D(1080*3+290,1560,160,92,'background:#10161C;border:4px solid #5A6A73;border-radius:14px')+D(1080*3+290,1560,160,92,"color:#E8B96C;font-weight:700;font-size:44px;text-align:center;line-height:92px;letter-spacing:.04em",'06:55')+glow(1080*3+370,1606,170,.28,'232,185,108')
ceil=D(1080*4+200,1470,520,26,'background:rgba(201,214,220,.18);border-radius:13px')+D(1080*4+240,1530,420,18,'background:rgba(201,214,220,.12);border-radius:9px')
floor=D(0,1790,W,130,'background:#141B22')
S=[slide(0,'dk','Ora 06:55 · Para alarmit','Zgjohesh pesë minuta para alarmit. <em>Mendja ka nisur&nbsp;punën.</em>','',HINT),
   slide(1,'dk','Dhoma','Tavani është ende gri. <em>Dhe lista e ditës është e&nbsp;gjatë.</em>'),
   slide(2,'dk','Telefoni','Nuk e merr, <em>që dita të mos fillojë para&nbsp;kohe.</em>'),
   slide(3,'dk','Pse ndodh','Trupi është ende në shtrat. <em>Por ti je tashmë në mbledhjen e orës&nbsp;dhjetë.</em>'),
   slide(4,'dk','E vërteta','Këto pesë minuta janë të tuat. <em>S’ke pse t’i&nbsp;mbushësh.</em>'),
   end(5,'Kur mendja ngrihet para teje, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-alarmi']=page(bgC,dawn+floor+win+bed+night+ceil+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
