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

# 1: Sinia e gjyshes (ritual shqiptar me kuptim të ri)
bgA='linear-gradient(180deg,#F6F1E6 0%,#F0E7D6 62%,#E7DAC1 100%)'
floorA=D(0,1640,W,280,'background:repeating-linear-gradient(90deg,#C9AE85 0 214px,#BFA37A 214px 216px)')
rug=D(300,1660,W-600,200,'background:#3F6259;border-radius:10px')+''.join(D(380+k*90,1740,40,40,f"background:{'#D6A24C' if k%2 else '#8FB8A8'};transform:rotate(45deg)") for k in range((W-760)//90))
def sini(cx,w):
    s=D(cx-w//2,1560,w,120,'background:radial-gradient(ellipse at 50% 40%,#C79A5F,#A87B45);border-radius:50%;box-shadow:0 14px 30px rgba(80,55,30,.25)')
    s+=D(cx-w//2+40,1620,w-80,60,'background:#7F5C38;border-radius:0 0 50% 50%/0 0 100% 100%;z-index:-1')
    return s
sinis=sini(1080*1+540,1500)+sini(1080*3+540,1200)
bread=D(1080*2-170,1520,340,90,'background:radial-gradient(ellipse at 50% 30%,#EBC27A,#C98A3E);border-radius:50%')+D(1080*2-10,1516,20,96,'background:#F0E7D6;transform:rotate(18deg)')
spoons=''.join(D(x,1580,120,18,f'background:#8A6A3F;border-radius:9px;transform:rotate({r}deg)')+D(x-34,1572,46,32,f'background:#8A6A3F;border-radius:50%;transform:rotate({r}deg)') for x,r in [(1080+380,-8),(1080+620,6),(2160+380,8),(3240+260,-6),(3240+520,4),(3240+760,-10)])
cushions=''.join(D(x,1650,230,70,'background:#8FB8A8;border-radius:30px;border:6px solid #FAF7F1') for x in [1080+60,1080+800,2160+500,3240+100,3240+760])
extra=D(3240+430,1650,230,70,'background:#D6A24C;border-radius:30px;border:6px solid #FAF7F1')
bowl=D(4320+320,1490,300,110,'background:linear-gradient(180deg,#FAF7F1,#E4DACB);border-radius:20px 20px 150px 150px')+glow(4320+470,1470,160,.35)
S=[slide(0,'lt','E diel · Ora 13:00','Te sinia e gjyshes s’kishte krye të tryezës. <em>Ishte e&nbsp;rrumbullakët.</em>','',HINT),
   slide(1,'lt','Përdhe','Të gjithë uleshin përdhe. <em>Sy më&nbsp;sy.</em>','Askush më lart, askush më poshtë. Të gjithë e shihnin njëri-tjetrin.'),
   slide(2,'lt','Buka','Buka s’pritej me thikë. <em>Thyhej me dorë dhe&nbsp;ndahej.</em>'),
   slide(3,'lt','Kur vinte dikush','„Ngushtohuni pak.“ <em>Gjithmonë kishte vend për edhe&nbsp;një.</em>'),
   slide(4,'lt','E vërteta','Një hall i ndarë si buka <em>bëhet më i&nbsp;vogël.</em>','Mjafton dikush që të bën&nbsp;vend.'),
   end(5,'Kur s’ke ku të ulesh me hallin, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-sinia']=page(bgA,floorA+rug+sinis+bread+spoons+cushions+extra+bowl+''.join(S))

# 2: „Hesht, se po flasin të mëdhenjtë“ (rregull i pashkruar)
bgB='linear-gradient(180deg,#F4EFE5 0%,#EFE6D5 100%)'
floorB=D(0,1700,W,220,'background:#D9C8A6')
sofa=D(320,1580,1480,120,'background:#3F6259;border-radius:30px 30px 10px 10px')+D(320,1510,1480,100,'background:#2E4A43;border-radius:30px')
stool=D(1950,1600,180,30,'background:#8A6A3F;border-radius:8px')+D(1970,1630,18,70,'background:#5E4630')+D(2092,1630,18,70,'background:#5E4630')+D(1080*3+640,1600,180,30,'background:#8A6A3F;border-radius:8px')+D(1080*3+660,1630,18,70,'background:#5E4630')+D(1080*3+782,1630,18,70,'background:#5E4630')
def bub(x,y,w,h,c='#FFFFFF',bd='#CFC4AE',inner=''):
    return D(x,y,w,h,f"background:{c};border:7px solid {bd};border-radius:46px;display:flex;align-items:center;justify-content:center;font-family:'Fraunces',serif;font-weight:600;font-size:70px;color:#9C8F78",inner)+D(x+60,y+h-4,50,40,f'background:{bd};clip-path:polygon(0 0,100% 0,0 100%)')
bubbles=bub(360,1180,400,190)+bub(880,1250,340,160)+bub(1330,1160,420,200)
small=bub(1960,1430,150,110,inner='…')+bub(1080*3+650,1430,150,110,inner='…')+D(2160+300,1250,420,200,'opacity:.45',bub(0,0,420,200,inner='Po ti?'))
big=bub(1080*4+240,1160,600,300,'#F3D9A0','#D6A24C','Unë mendoj…')+D(1080*4+440,1600,180,30,'background:#8A6A3F;border-radius:8px')+D(1080*4+460,1630,18,70,'background:#5E4630')+D(1080*4+582,1630,18,70,'background:#5E4630')
S=[slide(0,'lt','Rregull i pashkruar','„Hesht, se po flasin të mëdhenjtë.“ <em>Dhe ne heshtëm. Edhe kur&nbsp;u&nbsp;rritëm.</em>','',HINT),
   slide(1,'lt','Në dhomën e ndenjes','Fëmija rrinte në cep. <em>Dëgjonte gjithçka, s’thoshte&nbsp;asgjë.</em>'),
   slide(2,'lt','Pyetja','„Po ti, çka mendon?“ <em>Rrallë na e&nbsp;pyesnin.</em>'),
   slide(3,'lt','Sot','Jemi të mëdhenj. <em>Dhe ende presim që dikush të na japë&nbsp;fjalën.</em>','Në punë, në familje, te shokët: e mbajmë mendimin për&nbsp;vete.'),
   slide(4,'lt','E vërteta','Fjalën s’ta jep më kush. <em>Tani e merr&nbsp;vetë.</em>','Edhe kur zëri dridhet, ka&nbsp;vend.'),
   end(5,'Nëse ke vite që hesht, <em>nis me dikë pa&nbsp;emër.</em>')]
sets['02-hesht']=page(bgB,floorB+sofa+bubbles+stool+small+big+''.join(S))

# 3: Kartëmonedha e gjyshes (sjellje e fshehur, ora 18:40)
bgC='linear-gradient(180deg,#2E4A43 0%,#355449 60%,#3B5C50 100%)'
wallC=D(0,1700,W,220,'background:#24392F')
door=D(420,1000,520,700,'background:linear-gradient(180deg,#9C7449,#7F5C38);border-radius:8px 8px 0 0')+D(460,1050,440,280,'border:6px solid rgba(255,255,255,.12);border-radius:6px')+D(460,1370,440,290,'border:6px solid rgba(255,255,255,.12);border-radius:6px')
hook=D(960,1200,60,24,'background:#D6A24C;border-radius:12px')
coat=D(860,1220,320,460,'background:#8FB8A8;border-radius:120px 120px 20px 20px')+D(1080+20,1460,150,130,'background:#7DA594;border-radius:0 0 20px 20px;border-top:6px solid #6E9585')
note1=D(1080+60,1430,90,60,'background:#E9E1C8;border:4px solid #C9BD9B;transform:rotate(-12deg)')
def knot(x,y,open_=False):
    if not open_:
        return D(x,y,260,200,'background:#FAF7F1;border-radius:50% 50% 40% 40%;box-shadow:0 14px 30px rgba(0,0,0,.25)')+D(x+90,y-50,80,80,'background:#FAF7F1;border-radius:40% 40% 20% 20%;transform:rotate(45deg)')+''.join(D(x+30+k*50,y+60,24,24,'background:#D6A24C;transform:rotate(45deg);opacity:.8') for k in range(4))
    return D(x,y,460,300,'background:#FAF7F1;transform:rotate(45deg) scale(.8);box-shadow:0 14px 30px rgba(0,0,0,.25)')+D(x+150,y+110,170,90,'background:#E9E1C8;border:5px solid #C9BD9B;transform:rotate(-8deg)')+D(x+232,y+110,4,90,'background:rgba(150,140,110,.5);transform:rotate(-8deg)')
knots=knot(2160+420,1440)+knot(3240+300,1360,True)
wallet=D(4320+280,1460,440,240,'background:#7F5C38;border-radius:20px')+D(4320+340,1400,230,110,'background:#E9E1C8;border:5px solid #C9BD9B;transform:rotate(-6deg)')+glow(4320+460,1440,220,.35)
S=[slide(0,'dk','Ora 18:40 · Kur ikje','Gjyshja ta fuste në xhep një kartëmonedhë të palosur. <em>„Mos i thuaj&nbsp;kujt.“</em>','',HINT),
   slide(1,'dk','Nga shamia','E mbante të lidhur në një shami. <em>Me nyje që&nbsp;s’zgjidhej&nbsp;lehtë.</em>'),
   slide(2,'dk','Ti','„Jo, gjyshe, s’ka nevojë.“ <em>Ajo s’pranonte&nbsp;kurrë.</em>'),
   slide(3,'dk','Sot e kupton','S’ishin paratë. <em>Ishte mënyra e saj për të thënë „të&nbsp;mendoj“.</em>'),
   slide(4,'dk','E vërteta','Ndoshta e ke ende diku. <em>Pa e&nbsp;shpenzuar.</em>','Sepse disa gjëra s’kanë vlerë në&nbsp;dyqan.'),
   end(5,'Për pak vëmendje pa kushte, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-gjyshja']=page(bgC,wallC+door+hook+coat+note1+knots+wallet+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
