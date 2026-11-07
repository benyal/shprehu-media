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


# 01 Arra e gjyshit (urtësi)
bgA='linear-gradient(180deg,#FAF7F1 0%,#F1ECDF 60%,#E3DCC8 100%)'
groundA=D(0,1640,W,280,'background:linear-gradient(180deg,#9C7A4E,#7E6140)')+D(0,1620,W,40,'background:#8FA77A;border-radius:0 0 40% 40%/0 0 100% 100%')
def leaf(x,y,s,rot,c='#5E8A6E'):
    return D(x,y,int(46*s),int(26*s),f'background:{c};border-radius:50% 0 50% 0;transform:rotate({rot}deg)')
def tree(cx,base,h,crown,trunk=30):
    out=D(cx-trunk//2,base-h,trunk,h,'background:linear-gradient(90deg,#6B4B2E,#86603C);border-radius:10px')
    out+=D(cx-crown//2,base-h-int(crown*0.62),crown,int(crown*0.82),'background:radial-gradient(ellipse at 45% 40%,#7FA57F,#4E7A5E 70%);border-radius:50%')
    return out
sap=D(540-6,1500,12,130,'background:#7E6140;border-radius:6px')+leaf(540-50,1500,1.1,-25)+leaf(540+4,1480,1.1,25)+leaf(540-30,1540,0.9,-10)
shovel=D(760,1380,14,250,'background:#7E6140;transform:rotate(18deg);border-radius:6px')+D(800,1600,80,60,'background:#9AA3A8;border-radius:0 0 30px 30px;transform:rotate(18deg)')
t1=tree(1080+540,1640,260,300,26)
t2=tree(2160+540,1640,360,560,46)+D(2160+150,1560,780,50,'background:rgba(60,70,50,.18);border-radius:50%')+D(2160+620,1520,220,20,'background:#7E6140;border-radius:6px')+D(2160+640,1540,14,80,'background:#6B4B2E')+D(2160+820,1540,14,80,'background:#6B4B2E')
nuts=''.join(D(3240+300+k*120,1560-(k%2)*24,70,62,'background:radial-gradient(circle at 40% 35%,#C9A574,#9C7A4E);border-radius:46% 54% 50% 50%') for k in range(5))
glow4=glow(4320+540,1530,300,.45)+D(4320+534,1470,12,160,'background:#7E6140;border-radius:6px')+leaf(4320+490,1470,1.2,-25,'#6E9A78')+leaf(4320+546,1450,1.2,25,'#6E9A78')
S=[slide(0,'lt','Urtësi e gjyshit','Gjyshi mbolli një arrë në 70 vjeç. <em>Arra jep fryte pas 15&nbsp;vjetësh.</em>','',HINT),
   slide(1,'lt','E pyetën pse','„S’e mbolla për vete.“ <em>Kaq tha, dhe vazhdoi&nbsp;punën.</em>'),
   slide(2,'lt','Sot','Nipat ulen nën hijen e saj. <em>Ai s’i pa kurrë&nbsp;arrat.</em>'),
   slide(3,'lt','E dinte','Disa gjëra i bën <em>për dikë që s’e ke takuar&nbsp;ende.</em>'),
   slide(4,'lt','Edhe ti','Ndoshta ai dikush <em>je ti, pas një&nbsp;viti.</em>','Shkruaji sot një letër vetes që do të&nbsp;jesh.'),
   end(5,'Te Shprehu ka tani <em>„Letër&nbsp;vetes“.</em>')]
sets['01-arra']=page(bgA,groundA+sap+shovel+t1+t2+nuts+glow4+''.join(S))

# 02 „Jo, faleminderit“ (rregull i pashkruar)
bgB='linear-gradient(180deg,#F6EFE3 0%,#F0E6D4 100%)'
tableB=D(0,1500,W,420,'background:linear-gradient(180deg,#B5875A,#946A44)')+D(0,1490,W,22,'background:#C99B6B')+''.join(D(0,1560+k*80,W,3,'background:rgba(70,40,20,.15)') for k in range(4))
def plate(x,y,fill=0):
    out=D(x,y,240,70,'background:#FFFDF8;border:6px solid #E6D9C3;border-radius:50%;box-shadow:0 10px 18px rgba(80,50,20,.18)')
    for k in range(fill):
        out+=D(x+50+k*34,y+8-k*6,70,44,'background:linear-gradient(160deg,#E8B96C,#C98B45);clip-path:polygon(0 100%,50% 0,100% 100%);transform:rotate('+str(k*8-8)+'deg)')
    return out
platesB=plate(300,1420,1)+plate(1080+330,1420,4)+D(1080+700,1250,40,200,'background:#9AA3A8;border-radius:20px;transform:rotate(-30deg)')+D(1080+740,1380,90,50,'background:#9AA3A8;border-radius:0 0 45px 45px;transform:rotate(-30deg)')+plate(2160+380,1420,6)+plate(3240+180,1420,3)+plate(3240+560,1420,3)+plate(4320+400,1420,0)+D(4320+470,1380,100,60,'background:#E8E2D4;border-radius:8px;transform:rotate(-6deg)')
S=[slide(0,'lt','Rregull i pashkruar','Te ne, „jo, faleminderit“ <em>do të thotë „po, por&nbsp;pak“.</em>','',HINT),
   slide(1,'lt','Në tryezë','Mysafiri thotë „jo“. <em>Nikoqiri mbush&nbsp;pjatën.</em>','„Vetëm pak, sa për&nbsp;hatër.“'),
   slide(2,'lt','Kështu mësuam','Që „jo“ <em>s’është&nbsp;përgjigje.</em>'),
   slide(3,'lt','Sot','Themi „po“ kur duam të themi „jo“. <em>Në punë, me shokët, me&nbsp;familjen.</em>'),
   slide(4,'lt','E vërteta','Një „jo“ e butë s’është mosmirënjohje. <em>Është&nbsp;kufi.</em>'),
   end(5,'Mëso ta thuash. <em>Fol me dikë pa&nbsp;emër.</em>')]
sets['02-jo']=page(bgB,tableB+platesB+''.join(S))

# 03 5 gjëra në sirtar (listë me boshllëk)
W3=7560
bgC='linear-gradient(180deg,#2B241D 0%,#3A2F25 100%)'
drawer=D(80,1180,W3-1240,520,'background:linear-gradient(180deg,#8C6440,#6E4C2F);border-radius:18px;box-shadow:inset 0 18px 30px rgba(0,0,0,.35)')+D(80,1180,W3-1240,30,'background:#A57A50;border-radius:18px 18px 0 0')
items=''
items+=D(1080+330,1330,300,240,'background:radial-gradient(circle at 40% 35%,#F2EEE6,#CFC7B8);border-radius:44% 56% 48% 52%')+''.join(D(1080+360+k*50,1360+(k%2)*60,90,40,'border:4px solid #B9B0A0;border-radius:50%') for k in range(4))
for k,(x,rot) in enumerate([(2160+300,-20),(2160+470,15),(2160+620,-8)]):
    items+=D(x,1380,60,60,f'border:12px solid #D6A24C;border-radius:50%;transform:rotate({rot}deg)')+D(x+56,1402,130,16,f'background:#D6A24C;border-radius:6px;transform:rotate({rot}deg)')
items+=D(3240+300,1330,420,260,'background:radial-gradient(circle at 50% 40%,#3E6FA8,#26507F);border-radius:50%/40%;box-shadow:0 10px 0 #1C3C60')+D(3240+380,1400,260,90,'border:6px dashed #E8D9A8;border-radius:50%')
items+=glow(4320+540,1450,300,.35)+''.join(D(4320+300+k*70,1360-k*14,260,170,f'background:#F3EBDD;border:2px solid #D9CCB4;transform:rotate({k*6-6}deg);border-radius:6px') for k in range(3))+D(4320+460,1400,90,8,'background:#D6A24C;transform:rotate(6deg)')
items+=D(5400+330,1340,360,250,'background:#F7F4EE;border:2px solid #D9D2C4;transform:rotate(-4deg)')+''.join(D(5400+370,1380+k*36,280,10,'background:#CFC8BA;transform:rotate(-4deg)') for k in range(5))
def slide7(i,cls,tag,h,sub='',hint=''):
    return slide(i,cls,tag,h,sub,hint)
S=[slide(0,'dk','Sirtari i kuzhinës','5 gjëra që çdo shtëpi shqiptare i mban në sirtar. <em>E katërta s’mbyllet&nbsp;kurrë.</em>','',HINT),
   slide(1,'dk','1','Qesja plot <em>me&nbsp;qese.</em>'),
   slide(2,'dk','2','Çelësa që askush s’e di <em>ku&nbsp;hapin.</em>'),
   slide(3,'dk','3','Kutia e biskotave <em>me pe dhe&nbsp;gjilpëra.</em>'),
   slide(4,'dk','4','Fjalët që s’ia thamë <em>njëri-tjetrit.</em>','Sirtari mbyllet. Ato mbeten&nbsp;aty.'),
   slide(5,'dk','5','Garancia e një televizori <em>që s’e kemi më prej 10&nbsp;vjetësh.</em>'),
   end(6,'Disa fjalë duhen nxjerrë nga sirtari. <em>Fol me dikë pa&nbsp;emër.</em>')]
sets['03-sirtari']=page(bgC,drawer+items+''.join(S),w=W3)

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
