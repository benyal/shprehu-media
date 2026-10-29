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

# 1: Numri i panjohur, ora 19:00
bgA='linear-gradient(180deg,#1E2430 0%,#262D3A 60%,#2D3442 100%)'
def ph(x,y,inner,ring=False):
    g=glow(x+190,y+300,420,.22,'232,185,108') if ring else ''
    return g+D(x,y,380,720,'background:#0E1218;border:8px solid #3A4554;border-radius:54px')+D(x+22,y+22,336,676,'background:#F3EFE7;border-radius:38px;overflow:hidden',inner)
call=("<div style=\"position:absolute;left:0;right:0;top:120px;text-align:center;font-family:Inter;font-weight:700;font-size:30px;color:#6B6152\">Numër i panjohur</div>"
      "<div style=\"position:absolute;left:0;right:0;top:170px;text-align:center;font-family:Inter;font-weight:800;font-size:40px;color:#221F1C\">+383 ••• •••</div>"
      "<div style=\"position:absolute;left:60px;top:520px;width:96px;height:96px;border-radius:50%;background:#B04A2C\"></div>"
      "<div style=\"position:absolute;right:60px;top:520px;width:96px;height:96px;border-radius:50%;background:#3F6259\"></div>")
search=("<div style=\"position:absolute;left:24px;right:24px;top:70px;height:70px;border-radius:35px;background:#FFFFFF;border:3px solid #DDD4C3;font-family:Inter;font-weight:600;font-size:28px;color:#221F1C;line-height:64px;padding-left:28px;white-space:nowrap;overflow:hidden\">+383 ••• •••</div>"
        +''.join(f"<div style=\"position:absolute;left:30px;top:{190+k*110}px;width:{[280,230,260,200][k]}px;height:22px;border-radius:11px;background:{['#8FB8A8','#E6DFD1','#E6DFD1','#E6DFD1'][k]}\"></div><div style=\"position:absolute;left:30px;top:{224+k*110}px;width:{[220,250,180,240][k]}px;height:16px;border-radius:8px;background:#EEE8DC\"></div>" for k in range(4)))
missed=("<div style=\"position:absolute;left:24px;right:24px;top:90px;height:110px;border-radius:22px;background:#FFFFFF;font-family:Inter;font-weight:700;font-size:28px;color:#B04A2C;padding:22px 26px;box-sizing:border-box\">1 thirrje e humbur<br><span style=\"color:#6B6152;font-weight:600;font-size:24px\">+383 ••• •••</span></div>"
        "<div style=\"position:absolute;left:24px;right:24px;top:230px;height:110px;border-radius:22px;background:#FFFFFF;font-family:Inter;font-weight:700;font-size:28px;color:#221F1C;padding:22px 26px;box-sizing:border-box\">Mesazh<br><span style=\"color:#6B6152;font-weight:600;font-size:24px\">Pakoja juaj është te dera.</span></div>")
phones=ph(1080*0+600,1080,call,True)+ph(1080*1+520,1080,search)+ph(1080*3+480,1080,missed)
waves=''.join(D(1080*0+600+190-r,1080+300-r,2*r,2*r,f'border:4px solid rgba(232,185,108,.{a});border-radius:50%') for r,a in [(300,35),(380,22),(460,12)])
floorA=D(0,1800,W,120,'background:#161B24')
S=[slide(0,'dk','Ora 19:00 · Numër i panjohur','Bie telefoni nga një numër i panjohur. <em>Dhe ti e lë të&nbsp;bjerë.</em>','',HINT),
   slide(1,'dk','Pastaj','E kërkon numrin në Google. <em>Si&nbsp;detektiv.</em>'),
   slide(2,'dk','Pse','Mendja pret më të keqen <em>para se ta dijë kush&nbsp;është.</em>'),
   slide(3,'dk','Zakonisht','Ishte kurieri. <em>Ose dikush që gaboi&nbsp;numrin.</em>'),
   slide(4,'dk','E vërteta','Nuk je i vetmi. <em>Shumë prej nesh e presin telefonin me&nbsp;frikë.</em>'),
   end(5,'Kur mendja pret gjithmonë më të keqen, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-numri']=page(bgA,floorA+waves+phones+''.join(S))

# 2: 5 gjëra kur na thonë „dukesh i lodhur“
W2=7560
bgB='linear-gradient(180deg,#F6F2EA 0%,#F1E9DA 100%)'
shelfB=D(0,1700,W2,18,'background:#CFC4AE')+D(0,1718,W2,202,'background:#E6DAC0')
cand=''
for i in range(1,6):
    x=i*1080+500; gold=(i==4); h=[0,330,280,230,150,200][i]
    col='#F3D9A0' if gold else '#FFFFFF'; bd='#D6A24C' if gold else '#CFC4AE'
    cand+=glow(x+60,1700-h-60,170,.45 if gold else .25,'255,214,140')
    cand+=D(x,1700-h,120,h,f'background:{col};border:6px solid {bd};border-radius:10px 10px 4px 4px')
    cand+=D(x+56,1700-h-26,8,26,'background:#6B6152;border-radius:4px')
    cand+=D(x+44,1700-h-90,32,62,"background:radial-gradient(ellipse at 50% 70%,#FFE29A 0%,#F5B04C 60%,rgba(245,176,76,0) 100%);border-radius:50% 50% 50% 50%/60% 60% 40% 40%")
    cand+=D(x-40,1600,200,90,f"font-family:'Fraunces',serif;font-weight:600;font-size:64px;text-align:center;color:{'#B9862F' if gold else '#9C8F78'}",str(i)) if False else ''
S=[slide(0,'lt','Kur të thonë „dukesh i lodhur“','5 gjëra që i bëjmë kur na thonë „dukesh i lodhur“. <em>E katërta ndodh&nbsp;gjithmonë.</em>','',HINT),
   slide(1,'lt','E para','Themi „s’kam fjetur mirë“. <em>Edhe kur kemi&nbsp;fjetur.</em>'),
   slide(2,'lt','E dyta','Shikohemi në pasqyrë <em>në rastin e&nbsp;parë.</em>'),
   slide(3,'lt','E treta','Buzëqeshim më shumë <em>gjithë&nbsp;ditën.</em>'),
   slide(4,'lt','E katërta','Fillojmë të ndihemi <em>edhe më të&nbsp;lodhur.</em>'),
   slide(5,'lt','E pesta','Nuk e themi <em>pse jemi lodhur në të&nbsp;vërtetë.</em>'),
   end(6,'Kur lodhja s’është vetëm nga gjumi, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['02-lodhur']=page(bgB,shelfB+cand+''.join(S),w=W2)

# 3: Kënga e vjetër, ora 21:15
bgC='linear-gradient(180deg,#2B2233 0%,#35293C 55%,#3F3040 100%)'
def cassette(x,y,spin=0):
    reel=lambda cx:D(cx,y+120,110,110,f'border-radius:50%;background:repeating-conic-gradient(#221F1C 0 20deg,#FAF7F1 20deg 40deg);transform:rotate({spin}deg);border:10px solid #FAF7F1')
    return (D(x,y,560,340,'background:#E8B96C;border-radius:26px;box-shadow:0 20px 40px rgba(0,0,0,.35)')+
            D(x+40,y+30,480,70,"background:#FAF7F1;border-radius:10px;font-family:'Fraunces',serif;font-style:italic;font-size:38px;color:#3F6259;line-height:70px;padding-left:24px;box-sizing:border-box",'Këngët e mia')+
            D(x+100,y+110,360,140,'background:#5A4A3A;border-radius:70px')+reel(x+110)+reel(x+340))
cas=glow(1080*0+700,1440,420,.25,'232,185,108')+cassette(1080*0+380,1300,0)+cassette(1080*1+260,1300,40)
radio=D(1080*2+260,1300,560,360,'background:#8A6A3F;border-radius:30px')+D(1080*2+300,1340,220,280,'background:repeating-linear-gradient(0deg,#5E4630 0 10px,#7A5B3E 10px 20px);border-radius:20px')+D(1080*2+560,1360,220,60,'background:#FAF7F1;border-radius:8px')+D(1080*2+640,1360,6,60,'background:#B04A2C')+D(1080*2+600,1470,90,90,'background:#3F6259;border-radius:50%')
notes=''.join(D(1080*3+x,y+50,40,30,'background:rgba(232,185,108,.85);border-radius:50%;transform:rotate(-20deg)')+D(1080*3+x+32,y-20,7,80,'background:rgba(232,185,108,.85);border-radius:3px')+D(1080*3+x+32,y-20,34,10,'background:rgba(232,185,108,.85);border-radius:3px;transform:rotate(20deg);transform-origin:0 0') for x,y in [(300,1300),(520,1220),(700,1380),(420,1460)])
casC=cassette(1080*4+260,1340,80)
S=[slide(0,'dk','Ora 21:15 · Një këngë e vjetër','Bie një këngë që dëgjoje në 16 vjeç. <em>Dhe për tre minuta je sërish&nbsp;atje.</em>','',HINT),
   slide(1,'dk','Fjalët','E di përmendësh çdo fjalë. <em>Pas kaq shumë&nbsp;vitesh.</em>'),
   slide(2,'dk','Pse','Këngët e mbajnë kohën <em>më mirë se&nbsp;fotot.</em>'),
   slide(3,'dk','Pastaj','Kënga mbaron. <em>Dhe ti e lëshon edhe një&nbsp;herë.</em>'),
   slide(4,'dk','E vërteta','Malli nuk do të thotë që je keq. <em>Do të thotë që ke pasur diçka të&nbsp;bukur.</em>'),
   end(5,'Kur malli rëndon, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-kenga']=page(bgC,cas+radio+notes+casC+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
