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

HINT='Rrëshqit →'
def page(bg,body,w=6480):
    return head().replace('6480px',f'{w}px')+f'</style></head><body><div class="pano" style="background:{bg}">{body}</div></body></html>'
def glow(x,y,r,a=.5,c='255,214,140'):
    return D(x-r,y-r,2*r,2*r,f'background:radial-gradient(circle,rgba({c},{a}),rgba({c},0) 66%);border-radius:50%')
W=6480
sets={}


HINT='Rrëshqit →'
def page(bg,body,w=6480):
    return head().replace('6480px',f'{w}px')+f'</style></head><body><div class="pano" style="background:{bg}">{body}</div></body></html>'
def glow(x,y,r,a=.5,c='255,214,140'):
    return D(x-r,y-r,2*r,2*r,f'background:radial-gradient(circle,rgba({c},{a}),rgba({c},0) 66%);border-radius:50%')
W=6480
sets={}

# 01 Përparësja e gjyshes (urtësi)
bgA='linear-gradient(180deg,#FAF7F1 0%,#F1EADB 100%)'
cloth='background:#5E7F70;background-image:repeating-linear-gradient(0deg,rgba(255,255,255,.10) 0 14px,transparent 14px 44px),repeating-linear-gradient(90deg,rgba(255,255,255,.10) 0 14px,transparent 14px 44px)'
apron=D(-40,1510,W+80,520,cloth+';border-radius:40px 40px 0 0')+D(0,1470,W,26,'background:#D6A24C;border-radius:13px')
apron+=D(380,1340,10,150,'background:#D6A24C;transform:rotate(20deg)')+D(600,1340,10,150,'background:#D6A24C;transform:rotate(-20deg)')
def pocket(x):
    return D(x,1590,560,340,'background:#4E6E60;border:6px dashed rgba(250,247,241,.55);border-radius:12px 12px 60px 60px;box-shadow:inset 0 22px 0 rgba(0,0,0,.12)')
apron+=pocket(1080+260)+pocket(2160+260)+pocket(3240+260)
apron+=D(1080+380,1510,300,150,'background:#FFFDF8;border:2px solid #D9CCB4;transform:rotate(-6deg);border-radius:6px')+''.join(D(1080+410,1540+k*30,220,8,'background:#CFC7B8;transform:rotate(-6deg)') for k in range(4))
apron+=D(2160+450,1470,170,170,'background:#F3E6C4;border-radius:50%;box-shadow:inset -40px -10px 0 #4E6E60')
apron+=''.join(D(3240+420+k*90,1390-k*120,70,40,f'background:#E8B96C;border-radius:50% 0 50% 0;transform:rotate({k*25-20}deg);opacity:{1-k*0.25}') for k in range(4))
S=[slide(0,'lt','Urtësi e gjyshes','Përparësja e gjyshes kishte tri xhepa. <em>Një për çdo&nbsp;hall.</em>','',HINT),
   slide(1,'lt','Xhepi i parë','Hallet që zgjidhen sot. <em>I zgjidhte para&nbsp;drekës.</em>'),
   slide(2,'lt','Xhepi i dytë','Hallet e nesërme. <em>„Nesër i shohim me sy të&nbsp;freskët.“</em>'),
   slide(3,'lt','Xhepi i tretë','Hallet që s’varen nga ti. <em>Ato i linte të&nbsp;kalonin.</em>'),
   slide(4,'lt','Edhe ti','S’ke pse t’i mbash të gjitha <em>në një&nbsp;xhep.</em>','Disa sot, disa nesër, disa lëri të&nbsp;shkojnë.'),
   end(5,'Kur s’di ku t’i vendosësh, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-perparesja']=page(bgA,apron+''.join(S))

# 02 „Mbylle dritaren, se të zë rryma!“ (rregull i pashkruar)
bgB='linear-gradient(180deg,#EEF1EC 0%,#E1E7E0 100%)'
wall=D(0,1250,W,670,'background:#E7DCC7')+D(0,1250,W,14,'background:#CDBE9F')
def window(x,openw=False):
    out=D(x,1340,420,460,'background:linear-gradient(180deg,#BFD8E4,#E9F1EC);border:18px solid #7F5C38;border-radius:6px')
    if openw:
        out+=D(x+18,1358,384,424,'background:linear-gradient(180deg,#9CC6DA,#DDEEE6)')+D(x-160,1358,170,424,'background:rgba(255,253,248,.85);border:6px solid #7F5C38;transform:skewY(-12deg)')
        out+=''.join(D(x+60,1430+k*90,260-k*30,8,'background:rgba(255,255,255,.9);border-radius:4px') for k in range(4))
        out+=glow(x+300,1420,160,.6)
    else:
        out+=D(x+202,1340,16,460,'background:#7F5C38')+D(x+18,1358,180,424,'background:repeating-linear-gradient(90deg,rgba(244,236,222,.95) 0 22px,rgba(226,214,192,.95) 22px 40px)')+D(x+222,1358,180,424,'background:repeating-linear-gradient(90deg,rgba(244,236,222,.95) 0 22px,rgba(226,214,192,.95) 22px 40px)')
    return out
wins=wall+window(330)+window(1080+330)+window(2160+330)+window(3240+330)+window(4320+430,True)
S=[slide(0,'lt','Rregull i pashkruar','„Mbylle dritaren, <em>se të zë&nbsp;rryma!“</em>','Te ne, rryma është rreziku më i madh i&nbsp;shtëpisë.',HINT),
   slide(1,'lt','Në çdo shtëpi','Dritaret mbyllur. Dyert mbyllur. <em>Edhe në&nbsp;gusht.</em>'),
   slide(2,'lt','Kështu mësuam','Mbyllim gjithçka që lëviz. <em>Edhe atë që&nbsp;ndiejmë.</em>'),
   slide(3,'lt','Por','Një dhomë pa ajër <em>rëndohet.</em>','Edhe një zemër që s’flet&nbsp;kurrë.'),
   slide(4,'lt','E vërteta','Hape pak dritaren. <em>Lëre të hyjë pak&nbsp;ajër.</em>'),
   end(5,'Thuaje atë që mban brenda. <em>Fol me dikë pa&nbsp;emër.</em>')]
sets['02-rryma']=page(bgB,wins+''.join(S))

# 03 Nëna zgjohet e para (ora 05:50)
bgC='linear-gradient(90deg,#1B2233 0%,#232C42 35%,#3A3F5C 60%,#8C6A6E 80%,#E8B98C 100%)'
sill=D(0,1560,W,40,'background:#5E4630')+D(0,1600,W,320,'background:rgba(20,22,30,.55)')
frame=''.join(D(i*1080+180,1060,720,520,'border:20px solid rgba(94,70,48,.9);border-bottom:none;border-radius:8px 8px 0 0')+D(i*1080+530,1060,20,500,'background:rgba(94,70,48,.9)') for i in range(5))
stars=''.join(D(random.Random(k).randint(0,2600),random.Random(k+99).randint(1080,1500),6,6,'background:#F3E6C4;border-radius:50%;opacity:.8') for k in range(30))
sun=D(4320+420,1420,240,240,'background:radial-gradient(circle,#FFE2A8,#E8B96C);border-radius:50%')+glow(4320+540,1540,420,.5)
cup=D(2160+640,1470,110,90,'background:#F3EEE3;border-radius:0 0 30px 30px')+D(2160+740,1490,40,40,'border:10px solid #F3EEE3;border-radius:50%')+''.join(D(2160+665+k*26,1370,8,80,'background:rgba(243,238,227,.5);border-radius:4px;transform:rotate('+str(k*8-8)+'deg)') for k in range(3))
stove=glow(1080+300,1500,220,.55,'255,150,90')+D(1080+220,1500,160,60,'background:#3A2E28;border-radius:8px')
S=[slide(0,'dk','Ora 05:50','Nëna zgjohet e para. <em>Jo për&nbsp;punët.</em>','',HINT),
   slide(1,'dk','05:52','Ndez sobën. Vë ujin në zjarr. <em>Pa ndezur dritën e&nbsp;madhe.</em>'),
   slide(2,'dk','05:58','Ulet te dritarja me filxhanin. <em>Dhjetë minuta. Askush s’e&nbsp;thërret.</em>'),
   slide(3,'dk','06:10','Pastaj zgjohen të gjithë. <em>Dhe dita s’është më e&nbsp;saja.</em>'),
   slide(4,'dk','E kuptova vonë','Ato dhjetë minuta <em>e mbanin gjithë&nbsp;ditën.</em>','Gjej edhe ti dhjetë minutat e&nbsp;tua.'),
   end(5,'Kur s’ke kë t’ia thuash, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-nena']=page(bgC,stars+sun+frame+sill+cup+stove+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
