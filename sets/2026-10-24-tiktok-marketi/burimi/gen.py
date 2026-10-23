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

# 1: Marketi pa liste, ora 20:40
bgA='linear-gradient(180deg,#14201F 0%,#1C2C2A 60%,#232F2C 100%)'
shelves=''
for x in range(0,W,360):
    shelves+=D(x+20,1480,320,260,'background:#24312E;border:6px solid #33433F;border-radius:6px')
    for r in range(2):
        y=1490+r*120
        shelves+=D(x+30,y+110,300,10,'background:#3F524D')
        random.seed(x*7+r)
        cx=x+40
        while cx<x+310:
            w=random.randint(30,58);h=random.randint(50,85)
            col=random.choice(['#8FB8A8','#D6A24C','#B9825A','#6E9C8C','#E9D3A2','#5E7F8F'])
            shelves+=D(cx,y+110-h,w,h,f'background:{col};opacity:.55;border-radius:5px 5px 2px 2px')
            cx+=w+10
lights=''.join(D(x,40,260,14,'background:#EDE6D2;box-shadow:0 0 50px 18px rgba(237,230,210,.25);border-radius:7px') for x in range(150,W,900))
cart=D(1080*4+600,1600,260,130,'border:8px solid #9FB3AD;border-top:none;border-radius:0 0 18px 18px')+D(1080*4+560,1560,60,10,'background:#9FB3AD')+D(1080*4+630,1735,40,40,'border:7px solid #9FB3AD;border-radius:50%')+D(1080*4+800,1735,40,40,'border:7px solid #9FB3AD;border-radius:50%')
floor=D(0,1745,W,175,'background:#101716')
S=[slide(0,'dk','Ora 20:40 · „Po dal te marketi“','Merr çelësat. <em>Por s’të duhet&nbsp;asgjë.</em>','Ecën mes rafteve pa listë.',HINT),
   slide(1,'dk','Në raft','Lexon çmimet e gjërave <em>që s’do t’i blesh&nbsp;kurrë.</em>'),
   slide(2,'dk','Pse aty','Drita është e fortë, njerëzit s’të njohin. <em>Askush s’të pyet si&nbsp;je.</em>'),
   slide(3,'dk','Në arkë','Blen një çamçakëz <em>që dalja të ketë një&nbsp;arsye.</em>','Dhe kthehesh pak më lehtë.'),
   slide(4,'dk','E vërteta','Ndonjëherë s’duam të blejmë asgjë. <em>Duam vetëm njëzet minuta për&nbsp;veten.</em>'),
   end(5,'Kur të duhen njëzet minuta, <em>fol me dikë pa emër.</em>')]
sets['01-marketi']=page(bgA,lights+shelves+floor+cart+''.join(S))

# 2: Pasqyra, lista
W2=7560
bgB='linear-gradient(180deg,#F6F2EA 0%,#F3EFE7 100%)'
mirror=''
for i in range(1,6):
    x=i*1080+640; gold=(i==4)
    mirror+=D(x,1150,300,460,f"background:linear-gradient(160deg,rgba(255,255,255,.95),rgba(207,222,218,.8));border:12px solid {'#D6A24C' if gold else '#B8AA92'};border-radius:150px 150px 20px 20px")
    mirror+=D(x+70,1210,60,250,'background:rgba(255,255,255,.7);border-radius:30px;transform:rotate(18deg)')
    mirror+=D(x+110,1630,80,40,f"font-family:'Fraunces',serif;font-weight:600;font-size:40px;text-align:center;color:{'#B9862F' if gold else '#9C8F78'}",str(i))
shelf=D(0,1700,W2,14,'background:#D9CDB6')
S=[slide(0,'lt','Ora 07:45 · Para pasqyrës','5 gjëra që i bëjmë para se të dalim. <em>E katërta s’e thotë askush.</em>','',HINT),
   slide(1,'lt','E para','Rregullon flokët. <em>Pastaj i rregullon&nbsp;sërish.</em>'),
   slide(2,'lt','E dyta','Provon një buzëqeshje. <em>Që të jetë gati kur të pyesin.</em>'),
   slide(3,'lt','E treta','I thua vetes „vetëm sot“. <em>E ke thënë edhe&nbsp;dje.</em>'),
   slide(4,'lt','E katërta','Shikon sytë e tu dhe pyet: <em>„a duket që s’kam fjetur?“</em>','Dhe vendos të mos duket.'),
   slide(5,'lt','E pesta','Merr frymë thellë te dera. <em>Dhe del si njeri që s’ka asgjë.</em>'),
   end(6,'Kur s’do ta fshehësh dot më, <em>thuaje pa emër.</em>')]
sets['02-pasqyra']=page(bgB,shelf+mirror+''.join(S),w=W2)

# 3: E shtuna, ora 15:30
bgC='linear-gradient(180deg,#F3E7D3 0%,#EFDCC0 55%,#E4CDAA 100%)'
sun=glow(1080*2+540,520,700,.35,'255,226,160')
win=''
for x in (1080*1+640,1080*3+640):
    win+=D(x,1180,330,430,'background:linear-gradient(180deg,#BFD6DD,#F2E3BE);border:14px solid #FAF7F1;border-radius:8px;box-shadow:0 10px 30px rgba(120,90,50,.18)')+D(x+158,1180,14,430,'background:#FAF7F1')
cal=D(1080*4+620,1170,320,360,'background:#FAF7F1;border-radius:14px;box-shadow:0 10px 30px rgba(120,90,50,.18)')+D(1080*4+620,1170,320,70,'background:#3F6259;border-radius:14px 14px 0 0')+D(1080*4+620,1185,320,40,"color:#FAF7F1;font-weight:800;font-size:28px;text-align:center;letter-spacing:.12em",'E SHTUNË')
cal+=''.join(D(1080*4+650+(k%5)*55,1270+(k//5)*55,40,40,'border:3px solid #D9CDB6;border-radius:8px') for k in range(20))
couch=D(0,1650,6480,40,'background:#C9B08A')+D(1080*2+250,1560,560,110,'background:#8FB8A8;border-radius:40px 40px 10px 10px')
S=[slide(0,'lt','Ora 15:30 · E shtunë','Gjithë javën e prisje. <em>Tani s’di çfarë të bësh me&nbsp;të.</em>','',HINT),
   slide(1,'lt','Ndjesia','Nuk je i mërzitur. <em>Je i zbrazët, pa arsye.</em>'),
   slide(2,'lt','Çfarë bën','Hap telefonin, e mbyll. <em>Nis një seri, e lë pas pesë&nbsp;minutash.</em>'),
   slide(3,'lt','Pse ndodh','Gjithë javën trupi ishte në garë. <em>Kur ndalon, ndjen sa ishte lodhur.</em>'),
   slide(4,'lt','E vërteta','S’ka nevojë ta mbushësh. <em>Edhe një ditë e qetë është pushim.</em>','Dhe një bisedë e shkurtër e bën më të lehtë.'),
   end(5,'Kur fundjava ndihet bosh, <em>fol me dikë pa emër.</em>')]
sets['03-shtuna']=page(bgC,sun+win+cal+couch+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
