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

# 1: Besa (urtësi e gjyshërve me kthesë)
bgA='linear-gradient(180deg,#F6F1E6 0%,#EFE6D4 100%)'
floorA=D(0,1720,W,200,'background:#E2D4B8')
rope=D(0,1496,1080*3+300,16,'background:repeating-linear-gradient(115deg,#A8844F 0 14px,#8A6A3F 14px 28px);border-radius:8px')
rope+=D(1080*3+520,1496,1080*2,16,'background:repeating-linear-gradient(115deg,#A8844F 0 14px,#8A6A3F 14px 28px);border-radius:8px')
fray=''.join(D(1080*3+300+k*6,1490+(k%3-1)*10,60,4,f'background:#8A6A3F;transform:rotate({(k%5-2)*14}deg);transform-origin:left') for k in range(8))
fray+=''.join(D(1080*3+470-k*6,1490+(k%3-1)*10,60,4,f'background:#8A6A3F;transform:rotate({180+(k%5-2)*14}deg);transform-origin:right') for k in range(8))
def knot(cx,gold=False):
    c1,c2=('#E8B96C','#C9913A') if gold else ('#B89260','#8A6A3F')
    s=D(cx-60,1444,120,120,f'background:radial-gradient(circle at 40% 35%,{c1},{c2});border-radius:46% 54% 50% 50%;box-shadow:0 10px 22px rgba(80,55,30,.25)')
    s+=D(cx-14,1444,28,120,f'background:{c2};opacity:.55;border-radius:14px;transform:rotate(30deg)')
    return (glow(cx,1504,220,.45) if gold else '')+s
knots=knot(540)+knot(1080+540)+knot(2160+540)+knot(4320+540,True)
S=[slide(0,'lt','Urtësi e gjyshërve','Gjyshërit s’kishin kontrata. <em>Kishin&nbsp;besën.</em>','',HINT),
   slide(1,'lt','Fjala e dhënë','Një fjalë e dhënë <em>vlente më shumë se një&nbsp;letër.</em>'),
   slide(2,'lt','Edhe kur kushtonte','Besa s’thyhej. <em>As kur ishte e&nbsp;vështirë.</em>'),
   slide(3,'lt','Sot','Ua mbajmë fjalën të gjithëve. <em>Përveç&nbsp;vetes.</em>','„Nesër pushoj.“ „Do flas me dikë.“ „Do kujdesem për veten.“ Dhe nesër s’vjen&nbsp;kurrë.'),
   slide(4,'lt','E vërteta','Edhe vetes <em>i ke borxh një&nbsp;besë.</em>'),
   end(5,'Jepi vetes besën <em>dhe fol me dikë pa&nbsp;emër.</em>')]
sets['01-besa']=page(bgA,floorA+rope+fray+knots+''.join(S))

# 2: 5 rregulla të pashkruara të shtëpisë shqiptare (listë me boshllëk)
W2=7560
bgB='linear-gradient(180deg,#F6F2EA 0%,#F1E9DA 100%)'
wall=D(0,1250,W2,470,'background:#EDE3D0')+D(0,1720,W2,200,'background:#D9C8A6')
def frame(i,inner,gold=False):
    x=i*1080+220; bd='#D6A24C' if gold else '#CFC4AE'
    s=D(x,1290,560,400,f'background:#FBF8F1;border:10px solid {bd};border-radius:16px')
    s+=D(x+20,1310,72,72,f"background:{bd};border-radius:12px;font-family:'Fraunces',serif;font-weight:600;font-size:46px;color:#FFFFFF;text-align:center;line-height:72px",str(i))
    return s+inner
shoes=''.join(D(1080+430+k*120,1590,100,48,'background:#5E4630;border-radius:40px 50px 8px 8px') for k in range(3))
phone=D(2160+440,1430,160,230,'background:#4A4642;border-radius:24px')+D(2160+462,1460,116,90,'background:#BFD3C8;border-radius:6px')+''.join(D(2160+470+(k%3)*36,1570+(k//3)*26,24,16,'background:#8A8580;border-radius:4px') for k in range(6))
tray=D(3240+380,1600,320,30,'background:#C9A35E;border-radius:50%')+''.join(D(3240+410+k*90,1530,56,76,'background:rgba(190,120,60,.75);border:5px solid rgba(255,255,255,.8);border-radius:6px 6px 14px 14px') for k in range(3))
chair=D(4320+460,1430,150,220,'border:12px solid #B9862F;border-bottom:none;border-radius:10px 10px 0 0')+D(4320+440,1570,190,20,'background:#B9862F;border-radius:6px')+D(4320+450,1590,14,80,'background:#B9862F')+D(4320+606,1590,14,80,'background:#B9862F')
lamp=glow(5400+500,1470,180,.55)+D(5400+430,1400,140,90,'background:#E8B96C;border-radius:70px 70px 10px 10px')+D(5400+494,1490,12,170,'background:#8A6A3F')
frames=frame(1,shoes)+frame(2,phone)+frame(3,tray)+frame(4,chair,True)+frame(5,lamp)
S=[slide(0,'lt','Shtëpia shqiptare','5 rregulla të pashkruara të shtëpisë shqiptare. <em>E katërta duhet ta&nbsp;ndryshojmë.</em>','',HINT),
   slide(1,'lt','E para','Këpucët hiqen <em>te&nbsp;dera.</em>'),
   slide(2,'lt','E dyta','Telefonit i përgjigjesh <em>me&nbsp;„urdhëro“.</em>'),
   slide(3,'lt','E treta','Kush vjen, s’ikën <em>pa pirë&nbsp;diçka.</em>'),
   slide(4,'lt','E katërta','Për hallin tënd flitet i fundit. <em>Nëse&nbsp;flitet.</em>','Pyet për të gjithë, dhe për veten thua „mirë“. Këtë mund ta&nbsp;ndryshojmë.'),
   slide(5,'lt','E pesta','Drita e fundit fiket <em>kur të gjithë janë&nbsp;brenda.</em>'),
   end(6,'Hallin tënd mos e lër të fundit. <em>Fol me dikë pa&nbsp;emër.</em>')]
sets['02-rregullat']=page(bgB,wall+frames+''.join(S),w=W2)

# 3: „Më bjer një zile“ (ritual shqiptar, ora 22:10)
bgC='linear-gradient(180deg,#1B2130 0%,#222A3A 60%,#293246 100%)'
floorC=D(0,1720,W,200,'background:#151A24')
waves=''
for k in range(14):
    r=200+k*260
    waves+=D(560-r,1460-r,2*r,2*r,f'border:5px solid rgba(232,185,108,{max(.06,.32-k*.02):.2f});border-radius:50%')
def oldphone(x,label):
    s=D(x,1300,220,400,'background:linear-gradient(180deg,#5A5F68,#3E424A);border-radius:40px;box-shadow:0 20px 40px rgba(0,0,0,.4)')
    s+=D(x+28,1350,164,130,"background:#BFD3C8;border-radius:8px;font-family:Inter;font-weight:700;font-size:22px;color:#2E4A43;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.25;padding:8px",label)
    s+=''.join(D(x+34+(k%3)*56,1510+(k//3)*44,44,28,'background:#2E3238;border-radius:8px') for k in range(9))
    return s
phones=oldphone(450,'1 thirrje<br>e humbur')+oldphone(2160+430,'1 thirrje<br>e humbur')
smart=D(4320+380,1180,320,540,'background:#2E3238;border-radius:44px;box-shadow:0 20px 40px rgba(0,0,0,.4)')+D(4320+400,1210,280,480,'background:#F6F2EA;border-radius:30px')
smart+=''.join(D(4320+(430 if k%2 else 520),1240+k*70,140,46,f"background:{'#FFFFFF' if k%2 else '#3F6259'};border-radius:18px") for k in range(6))
moon=D(1080+760,980,120,120,'background:#F3E6C4;border-radius:50%;box-shadow:0 0 70px rgba(243,230,196,.45)')
S=[slide(0,'dk','Ora 22:10 · Sapo arrite','„Më bjer një zile kur të arrish.“ <em>Dhe një zile&nbsp;mjaftonte.</em>','',HINT),
   slide(1,'dk','Kodi','Një zile: arrita mirë. <em>Dy zile: më thirr&nbsp;ti.</em>'),
   slide(2,'dk','Nga nëna','Një zile në mesditë. <em>Do të thoshte: „a je&nbsp;mirë?“</em>'),
   slide(3,'dk','Pa fjalë','S’kishte kredi për të folur. <em>Kishte gjithmonë për një&nbsp;zile.</em>'),
   slide(4,'dk','Sot','Kemi mesazhe pa fund. <em>Por rrallë themi si jemi&nbsp;vërtet.</em>'),
   end(5,'Kur s’mjafton një zile, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-zilja']=page(bgC,waves+floorC+moon+phones+smart+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
