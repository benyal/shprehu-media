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


# 01 Ujë me sheqer (ritual, urtësi e gjyshes)
bgA='linear-gradient(180deg,#FAF7F1 0%,#F1EADB 100%)'
table=D(-20,1560,W+40,360,'background:#B98A5E;background-image:repeating-linear-gradient(90deg,rgba(0,0,0,.05) 0 3px,transparent 3px 120px)')+D(0,1540,W,30,'background:#9C7049')
cloth=D(150,1500,4900,70,'background:#FFFDF8;border-radius:10px;background-image:repeating-linear-gradient(90deg,#FFFDF8 0 40px,#F0E6D2 40px 80px)')
def glass(x,full=1.0):
    h=int(300*full)
    g=D(x,1200,220,340,'border:8px solid rgba(255,255,255,.95);border-top:none;border-radius:0 0 28px 28px;background:rgba(220,236,240,.35)')
    g+=D(x+8,1540-h,204,h-8,'background:linear-gradient(180deg,rgba(190,220,228,.75),rgba(160,200,212,.85));border-radius:0 0 22px 22px')
    return g
def spoon(x):
    return D(x,1060,14,330,'background:#C9CED2;border-radius:7px;transform:rotate(14deg)')
sugar=''.join(D(1080+400+(k*37)%180,1440+(k*53)%80,12,12,'background:#FFFFFF;border-radius:2px;opacity:.95') for k in range(14))
scene=table+cloth+glass(600)+glass(1080+430)+spoon(1080+560)+sugar+glass(2160+430,0.8)+glass(3240+430,0.5)+glass(4320+430,0.15)
scene+=glow(4320+540,1350,380,.45)
S=[slide(0,'lt','Ritual i shtëpisë','Kur dikush trembej ose mërzitej, <em>gjyshja sillte ujë me&nbsp;sheqer.</em>','',HINT),
   slide(1,'lt','Gjithmonë njësoj','„Pije pak. <em>Të&nbsp;kalon.“</em>'),
   slide(2,'lt','Nuk pyeste','S’të pyeste çfarë ke. <em>Ulej pranë teje derisa ta&nbsp;pije.</em>'),
   slide(3,'lt','E vërteta','Sheqeri s’shëronte asgjë. <em>Shëronte që dikush s’u&nbsp;largua.</em>'),
   slide(4,'lt','Edhe sot','Ndonjëherë s’duhen fjalë. <em>Duhet dikush që&nbsp;rri.</em>','Ulu pranë dikujt sot, ose lëre dikë të ulet pranë&nbsp;teje.'),
   end(5,'Kur të duhet dikush që rri, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-sheqeri']=page(bgA,scene+''.join(S))

# 02 „Mos e merr për zemër“ (rregull i pashkruar)
bgB='linear-gradient(180deg,#EEF1EC 0%,#E3E8E0 100%)'
def bubble(x,y,w,txt,dark=False):
    bg='#3F6259' if dark else '#FFFDF8'; c='#FAF7F1' if dark else '#221F1C'
    return D(x,y,w,110,f'background:{bg};border-radius:28px 28px 28px 6px;box-shadow:0 10px 24px rgba(30,40,35,.12);color:{c};font-size:36px;font-weight:600;display:flex;align-items:center;padding:0 34px;box-sizing:border-box',txt)
thread=D(0,1480,W,8,'background:#C9A27A;border-radius:4px')
scene=thread
pos=[(120,1530,'Mos e merr për zemër'),(1080+140,1560,'Ashtu është ai'),(1080+260,1380,'Mos e merr për zemër'),(2160+120,1540,'S’e pati qëllim'),(2160+240,1360,'Harroje'),(3240+140,1540,'Mos u bëj i ndjeshëm')]
for x,y,t in pos: scene+=bubble(x,y,len(t)*21+80,t)
scene+=bubble(4320+120,1530,820,'Më preku. Dhe kjo është në rregull.',True)
scene+=glow(4320+540,1560,360,.4)
S=[slide(0,'lt','Rregull i pashkruar','„Mos e merr <em>për&nbsp;zemër.“</em>','E themi për çdo gjë. Po ku ta çojmë&nbsp;atëherë?',HINT),
   slide(1,'lt','Kur të fyen dikush','„Mos e merr për zemër, <em>ashtu është&nbsp;ai.“</em>'),
   slide(2,'lt','Kur të lëndon dikush i afërt','„Mos e merr për zemër, <em>s’e pati&nbsp;qëllim.“</em>'),
   slide(3,'lt','Kështu mësuam','E mbajmë në fyt. E gëlltisim. <em>Bëjmë sikur s’ndodhi.</em>'),
   slide(4,'lt','E vërteta','Diçka që të preku, <em>ke të drejtë ta&nbsp;ndjesh.</em>','Ta pranosh që të preku është hapi i parë për ta lënë të&nbsp;ikë.'),
   end(5,'Kur s’di ku ta çosh, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['02-zemra']=page(bgB,scene+''.join(S))

# 03 Ora 23:30, biseda e vjetër
bgC='linear-gradient(90deg,#1B2233 0%,#1F2A3C 60%,#2E4A43 100%)'
def chat(x,y,w,left=True,op=1):
    return D(x if left else x+380-w+230,y,w,60,f'background:{"#33415A" if left else "#3F6259"};border-radius:24px;opacity:{op}')
scene=''
for i in range(5):
    bx=i*1080+(330 if i==0 else 190)
    scene+=D(bx,1420,700,520,'background:#121826;border-radius:60px 60px 0 0;border:10px solid #2C3650;border-bottom:none')
    for k in range(5):
        scene+=chat(bx+50,1500+k*90,[320,260,380,220,300][(k+i)%5],(k+i)%2==0,0.55+0.09*k)
    if i==1: scene+=D(bx+230,1440,240,44,'background:#2C3650;border-radius:22px;color:#AAB4C8;font-size:26px;display:flex;align-items:center;justify-content:center','12 mars 2019')
scene+=glow(4320+540,1500,380,.35,'232,185,108')
stars=''.join(D(random.Random(k).randint(0,W),random.Random(k+7).randint(980,1160),5,5,'background:#F3E6C4;border-radius:50%;opacity:.7') for k in range(40))
S=[slide(0,'dk','Ora 23:30','Hap bisedën me dikë me të cilin s’flet më. <em>Dhe shkon lart, deri në&nbsp;fillim.</em>','',HINT),
   slide(1,'dk','23:34','Viti 2019. <em>Qeshnit me gjëra që s’i mban mend&nbsp;më.</em>'),
   slide(2,'dk','23:41','Gjen një mesazh të gjatë që të shkroi dikur. <em>E&nbsp;lexon dy&nbsp;herë.</em>'),
   slide(3,'dk','23:50','Nuk e lexon që të kthehesh. <em>E&nbsp;lexon që të kujtosh se dikur ishe&nbsp;mirë.</em>'),
   slide(4,'dk','E vërteta','Ai version yt s’ka humbur. <em>Është ende&nbsp;aty.</em>','Dhe mund të kthehet, edhe me njerëz të&nbsp;rinj.'),
   end(5,'Kur mendja të çon pas, <em>fol me dikë sot, pa&nbsp;emër.</em>')]
sets['03-biseda']=page(bgC,stars+scene+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
