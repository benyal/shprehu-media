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

# 1: Rruga tjeter, ora 13:25
bgA='linear-gradient(180deg,#EEF0EA 0%,#E3E8E0 60%,#D8DFD5 100%)'
random.seed(12)
bld=''
for x in range(0,W,300):
    h=random.randint(150,270)
    col=random.choice(['#DCD3BE','#D2D8CC','#E4D8C2','#CFD6D0'])
    bld+=D(x,1230-h,280,h,f'background:{col}')
    for r in range(2):
        for c in range(3):
            bld+=D(x+34+c*80,1230-h+30+r*70,48,44,'background:#9FB3AD;opacity:.55;border-radius:4px')
walk1=D(0,1230,W,70,'background:#CFC8B4')+D(0,1300,W,22,'background:#B9B29C')
road=D(0,1322,W,330,'background:#8B8F8E')+''.join(D(x,1478,150,12,'background:#E8E4D6;border-radius:6px') for x in range(40,W,300))
walk2=D(0,1652,W,22,'background:#B9B29C')+D(0,1674,W,246,'background:#CFC8B4')
def person(x,y,c='#3F6259'): return D(x,y,56,56,'background:#D8B898;border-radius:50%')+D(x-10,y+58,76,130,f'background:{c};border-radius:30px 30px 10px 10px')
fig=person(1080*1+300,1470,'#3F6259')+person(1080*3+500,1740,'#B9862F')+person(1080*0+820,1260,'#8A6A3F')
S=[slide(0,'lt','Ora 13:25 · Në rrugë','E sheh dikë që e njeh. <em>Dhe kalon&nbsp;në trotuarin tjetër.</em>','Jo se s’të pëlqen. Sot s’ke forcë të flasësh.',HINT),
   slide(1,'lt','Hapat','Përshpejton ritmin. <em>Shikon vitrinat sikur kërkon&nbsp;diçka.</em>'),
   slide(2,'lt','Telefoni','Nxjerr telefonin <em>dhe bën sikur po&nbsp;përgjigjesh.</em>'),
   slide(3,'lt','Pse','Nuk i ik njeriut. <em>I ik pyetjes „po ti, si&nbsp;je?“</em>'),
   slide(4,'lt','E vërteta','Sot s’ke forcë për biseda të vogla. <em>Edhe kjo është në&nbsp;rregull.</em>'),
   end(5,'Kur s’të flitet me ata që të njohin, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-trotuari']=page(bgA,bld+walk1+road+walk2+fig+''.join(S))

# 2: Cfare ke, lista me bileta radhe
W2=7560
bgB='linear-gradient(180deg,#F6F2EA 0%,#F1E9DA 100%)'
tick=''
for i in range(1,6):
    x=i*1080+420; gold=(i==4)
    col='#FBE9BE' if gold else '#FFFFFF'; bd='#D6A24C' if gold else '#CFC4AE'
    tick+=D(x,1300,360,300,f'background:{col};border:8px solid {bd};border-radius:16px;box-shadow:0 12px 26px rgba(120,90,50,.12)')
    tick+=D(x+20,1470,320,0,f'border-top:6px dashed {bd}')
    tick+=D(x,1320,360,130,"font-weight:800;font-size:30px;letter-spacing:.2em;text-align:center;line-height:130px;color:#9C8F78",'NUMRI')
    tick+=D(x,1470,360,130,f"font-family:'Fraunces',serif;font-weight:600;font-size:96px;text-align:center;line-height:130px;color:{'#B9862F' if gold else '#9C8F78'}",str(i))
counter=D(0,1700,W2,220,'background:#E4D6B9')+D(0,1690,W2,16,'background:#CBBFA7')
S=[slide(0,'lt','Kur na pyesin „çfarë ke?“','5 gjëra që i themi kur na pyesin „çfarë ke?“. <em>E katërta është e&nbsp;preferuara.</em>','',HINT),
   slide(1,'lt','E para','„S’kam gjë.“ <em>Me një buzëqeshje të&nbsp;shpejtë.</em>'),
   slide(2,'lt','E dyta','„Jam thjesht i lodhur.“ <em>Që e mbyll&nbsp;bisedën.</em>'),
   slide(3,'lt','E treta','„Po mendoj për punën.“ <em>Edhe pse s’është&nbsp;puna.</em>'),
   slide(4,'lt','E katërta','„Ma kalon vetë.“ <em>E themi para se të pyesin&nbsp;përsëri.</em>'),
   slide(5,'lt','E pesta','„Po, të tregoj nesër.“ <em>Dhe nesër e harrojmë me&nbsp;qëllim.</em>'),
   end(6,'Kur „s’kam gjë“ s’është e vërteta, <em>thuaje pa&nbsp;emër.</em>')]
sets['02-cfareke']=page(bgB,counter+tick+''.join(S),w=W2)

# 3: Rruga e shkolles, ora 17:10
bgC='linear-gradient(180deg,#F1DFC0 0%,#E8C9A0 55%,#D9B586 100%)'
sun=glow(1080*2+700,900,820,.38,'255,214,150')
school=D(1080*1+80,1080,860,680,'background:#E3CDA6')+''.join(D(1080*1+130+c*160,1170+r*190,90,120,'background:#9FB3AD;opacity:.7;border-radius:6px 6px 2px 2px') for r in range(3) for c in range(5))+D(1080*1+370,1500,200,260,'background:#8A6A3F;border-radius:100px 100px 0 0')
fence=''.join(D(1080*2+x,1560,16,200,'background:#4A5A55;border-radius:8px 8px 0 0') for x in range(0,1080,70))+D(1080*2,1620,1080,12,'background:#4A5A55')
bench=D(1080*3+260,1630,420,22,'background:#7A5A3A;border-radius:6px')+D(1080*3+280,1560,380,18,'background:#7A5A3A;border-radius:6px')+D(1080*3+300,1650,16,110,'background:#4A3B30')+D(1080*3+640,1650,16,110,'background:#4A3B30')
tree=D(1080*4+560,1300,40,460,'background:#5A4636')+''.join(D(1080*4+420+k*60,1180+(k%3)*40,170,130,'background:#D08A3E;opacity:.75;border-radius:50%') for k in range(5))+''.join(D(1080*4+420+k*90,1740+(k%2)*10,24,14,'background:#C77B33;border-radius:50%') for k in range(8))
ground=D(0,1760,W,160,'background:#C9AE86')
S=[slide(0,'lt','Ora 17:10 · Në qytetin tënd','Kalon pranë shkollës. <em>Gjithçka është njësoj, vetëm ti&nbsp;jo.</em>','',HINT),
   slide(1,'lt','Porta','Porta është e njëjtë. <em>Por tani ke hapa më të&nbsp;ngadaltë.</em>'),
   slide(2,'lt','Stoli','Stoli ku uleshe me shokët. <em>Është më i vogël se e mbaje&nbsp;mend.</em>'),
   slide(3,'lt','Pse ndodh','Vendi nuk ka ndryshuar. <em>Ti ke mbartur më shumë se&nbsp;mendon.</em>'),
   slide(4,'lt','E vërteta','Mund të të mungojë një kohë, <em>edhe kur s’do të ktheheshe për&nbsp;asgjë.</em>'),
   end(5,'Kur kujtesa rëndon pak, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-shkolla']=page(bgC,sun+ground+school+fence+bench+tree+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
