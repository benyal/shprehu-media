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



# 01 Çanta e gjyshes (ritual)
bgA='linear-gradient(180deg,#FAF7F1 0%,#F1EADB 100%)'
scene=D(-20,1600,W+40,320,'background:#B98A5E;background-image:repeating-linear-gradient(90deg,rgba(0,0,0,.05) 0 3px,transparent 3px 140px)')+D(0,1580,W,26,'background:#9C7049')
def jar(x,c='#B5443A',h=190):
    return D(x,1590-h,130,h,f'background:{c};border-radius:14px 14px 18px 18px;box-shadow:inset -14px 0 0 rgba(0,0,0,.08)')+D(x-6,1590-h-26,142,30,'background:#D6A24C;border-radius:8px')+D(x+18,1590-h+50,94,60,'background:#FBF8F1;border-radius:6px')
def nut(x,y,r=30):
    return D(x,y,r,r*0.85,'background:#9B7048;border-radius:50%;box-shadow:inset -6px -4px 0 rgba(0,0,0,.15)')
def cheese(x):
    return D(x,1450,230,140,'background:#EDE6D6;border-radius:10px;background-image:repeating-linear-gradient(0deg,rgba(34,31,28,.18) 0 4px,transparent 4px 18px)')+D(x+20,1470,90,40,'background:rgba(34,31,28,.35);border-radius:3px')
scene+=jar(560)+nut(780,1560)+nut(820,1550)+nut(800,1525)
scene+=jar(1080+520,'#C8783A',170)+jar(1080+700,'#B5443A',210)
scene+=cheese(2160+480)+''.join(nut(2160+760+k*36,1560-(k%2)*20) for k in range(4))
scene+=D(3240+330,1260,520,340,'background:#5E7F70;border-radius:30px 30px 18px 18px')+D(3240+460,1180,260,110,'border:18px solid #5E7F70;border-bottom:none;border-radius:120px 120px 0 0')+jar(3240+380,'#B5443A',150)+jar(3240+560,'#C8783A',170)
scene+=glow(4320+540,1420,400,.45)+D(4320+380,1300,320,300,'background:#5E7F70;border-radius:30px 30px 18px 18px')+D(4320+470,1230,140,90,'border:16px solid #5E7F70;border-bottom:none;border-radius:90px 90px 0 0')
S=[slide(0,'lt','Ritual i shtëpisë','Kur iknim nga gjyshja, <em>çanta s’mbyllej&nbsp;dot.</em>','',HINT),
   slide(1,'lt','Gjithmonë','Një kavanoz reçel. Arra. <em>Djathë i mbështjellë në&nbsp;gazetë.</em>'),
   slide(2,'lt','Edhe kur thoshim jo','„S’kemi ku i vëmë, gjyshe.“ <em>Ajo shtonte edhe&nbsp;një.</em>'),
   slide(3,'lt','E kuptuam vonë','Nuk na jepte vetëm ushqim. <em>Na jepte „mos harro që të&nbsp;duam“.</em>'),
   slide(4,'lt','Edhe sot','Disa njerëz s’e thonë „të dua“. <em>Ta mbushin&nbsp;çantën.</em>','Thuaju sot një fjalë të mirë atyre që ta&nbsp;mbushnin.'),
   end(5,'Kur të mungon ajo dashuri, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-canta']=page(bgA,scene+''.join(S))

# 02 „Mos i trego nënës, se mërzitet“ (rregull i pashkruar)
bgB='linear-gradient(90deg,#1F2A3C 0%,#26324A 55%,#2E4A43 100%)'
def house(x,lit=True,big=1.0):
    w=int(220*big);h=int(170*big)
    out=D(x,1600-h,w,h,'background:#3A4560')+D(x-20,1600-h-int(90*big),w+40,int(95*big),'background:#4A3F4E;clip-path:polygon(50% 0,100% 100%,0 100%)')
    out+=D(x+int(70*big),1600-h+int(50*big),int(80*big),int(70*big),f'background:{"#F2C879" if lit else "#2A3346"};box-shadow:{"0 0 40px rgba(242,200,121,.7)" if lit else "none"}')
    return out
ground=D(0,1600,W,320,'background:#1A2232')
road=D(300,1640,W-600,10,'background:repeating-linear-gradient(90deg,#3A4560 0 60px,transparent 60px 110px)')
stars=''.join(D(random.Random(k).randint(0,W),random.Random(k+3).randint(1000,1450),5,5,'background:#F3E6C4;border-radius:50%;opacity:.7') for k in range(45))
moon=D(2700,1080,90,90,'background:#F5E3B8;border-radius:50%;box-shadow:0 0 40px rgba(245,227,184,.5)')
scene=stars+moon+ground+road+house(640,True,1.1)+house(4320+700,True,1.0)+glow(4320+800,1500,300,.35)
S=[slide(0,'dk','Rregull i pashkruar','„Mos i trego nënës, <em>se&nbsp;mërzitet.“</em>','E themi për çdo hall. Po nëna, kur e merr&nbsp;vesh?',HINT),
   slide(1,'dk','Kur s’shkon mirë në punë','„Mirë jam, ma. <em>Gjithçka në&nbsp;rregull.“</em>'),
   slide(2,'dk','Kur je i sëmurë larg','„Pak e ftohur. <em>S’është&nbsp;asgjë.“</em>'),
   slide(3,'dk','Kështu mësuam','E mbrojmë nga hallet tona. <em>Dhe mbetemi vetëm me&nbsp;to.</em>'),
   slide(4,'dk','E vërteta','Ndoshta nëna do të donte <em>të mërzitej bashkë me&nbsp;ty.</em>','Jo çdo gjë. Por diçka e vërtetë, një&nbsp;herë.'),
   end(5,'Kur s’ke kujt t’ia thuash, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['02-nena']=page(bgB,scene+''.join(S))

# 03 5 gjëra kur kthehemi në fshat (listë me boshllëk), 7 slide
W7=7560
bgC='linear-gradient(90deg,#F6EEDC 0%,#F1E4C8 50%,#EBC9A0 85%,#E2A97E 100%)'
mt=''.join(D(i*700-100,1250+(i%3)*40,900,700,f'background:{["#9DB59E","#86A38B","#A9BFA6"][i%3]};clip-path:polygon(50% 0,100% 100%,0 100%)') for i in range(12))
fields=D(0,1650,W7,270,'background:#8FAE7E')
roadc=D(0,1700,W7,40,'background:#E8DCC2')
vill=''.join(D(4320+200+k*170,1560,120,90,'background:#FBF8F1')+D(4320+190+k*170,1510,140,55,'background:#B5644A;clip-path:polygon(50% 0,100% 100%,0 100%)') for k in range(4))
sunC=D(6480+600,1180,240,240,'background:radial-gradient(circle,#FFE2A8,#E8B96C);border-radius:50%')
S=[slide(0,'lt','Listë','5 gjëra që i bëjmë kur kthehemi në fshat. <em>E katërta s’duket&nbsp;fare.</em>','',HINT),
   slide(1,'lt','1','Ulim xhamin e makinës <em>sapo shohim&nbsp;malin.</em>'),
   slide(2,'lt','2','Pyesim „e kujt është kjo shtëpi?“ <em>për çdo shtëpi të&nbsp;re.</em>'),
   slide(3,'lt','3','Flemë si s’kemi fjetur <em>prej&nbsp;muajsh.</em>'),
   slide(4,'lt','4','Na bie një peshë <em>që s’dinim se e&nbsp;mbanim.</em>'),
   slide(5,'lt','5','Dhe në kthim pyesim veten: <em>pse&nbsp;ikëm?</em>','Ndoshta s’ishte vetëm fshati. Ishte që aty dikush të&nbsp;priste.'),
   end(6,'Kur të mungon ajo qetësi, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-fshati']=page(bgC,mt+fields+roadc+vill+sunC+''.join(S),W7)

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
