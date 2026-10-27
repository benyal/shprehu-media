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

# 1: Copa e fundit e byrekut, ora 19:30
bgA='linear-gradient(180deg,#2B2420 0%,#3A2E26 55%,#4A3A2E 100%)'
lamp=glow(1080*0+700,900,600,.28,'255,205,130')+glow(1080*2+500,950,560,.22,'255,205,130')+glow(1080*4+600,950,560,.26,'255,205,130')
table=D(0,1560,W,24,'background:#B08D60')+D(0,1584,W,336,'background:linear-gradient(180deg,#8E6E4B,#6E5338)')
cloth=D(0,1520,W,48,'background:repeating-linear-gradient(90deg,#E8DCC6 0 60px,#D9C7A8 60px 120px);opacity:.9')
def tray(x,y,r,slice_deg):
    return (D(x-r-16,y-r-16,2*r+32,2*r+32,'background:#B9BCB8;border-radius:50%;box-shadow:0 18px 30px rgba(0,0,0,.35)')+
            D(x-r,y-r,2*r,2*r,f'border-radius:50%;background:conic-gradient(#E3B567 0deg {slice_deg}deg,#9DA19C {slice_deg}deg 360deg)')+
            D(x-r,y-r,2*r,2*r,f'border-radius:50%;background:conic-gradient(rgba(140,90,40,.35) 0deg 1.5deg,transparent 1.5deg {slice_deg-1.5}deg,rgba(140,90,40,.35) {slice_deg-1.5}deg {slice_deg}deg,transparent {slice_deg}deg)'))
trays=tray(1080*0+620,1430,210,60)+tray(1080*1+520,1430,210,60)
plate=D(1080*2+380,1395,330,90,'background:#FAF7F1;border-radius:50%;box-shadow:0 10px 20px rgba(0,0,0,.3)')
plate2=D(1080*4+360,1395,330,90,'background:#FAF7F1;border-radius:50%;box-shadow:0 10px 20px rgba(0,0,0,.3)')+D(1080*4+460,1380,140,70,'background:#E3B567;clip-path:polygon(0 100%,50% 0,100% 100%);border-radius:6px')
glass=D(1080*3+520,1300,110,230,'background:linear-gradient(180deg,rgba(220,235,240,.25),rgba(220,235,240,.45));border:6px solid rgba(240,245,245,.6);border-radius:6px 6px 16px 16px')
bread=D(1080*3+250,1440,170,90,'background:#D9B27A;border-radius:60px 60px 18px 18px')+D(1080*3+300,1420,90,40,'background:#F3EBD8;border-radius:10px')
S=[slide(0,'dk','Ora 19:30 · Te tryeza','Mbetet një copë byrek. <em>Dhe ti thua „s’kam&nbsp;uri“.</em>','',HINT),
   slide(1,'dk','Pse','Nuk është gënjeshtër e madhe. <em>Është mënyra jonë për të&nbsp;dashur.</em>'),
   slide(2,'dk','E njohim','E kemi parë te nëna. <em>Tani e bëjmë edhe ne pa e vënë&nbsp;re.</em>'),
   slide(3,'dk','Më vonë','Ha diçka në këmbë, në kuzhinë, <em>kur s’të sheh&nbsp;askush.</em>'),
   slide(4,'dk','E vërteta','Edhe ti numërohesh te tryeza. <em>Edhe pjesa jote ka&nbsp;vend.</em>'),
   end(5,'Kur gjithmonë u lë vend të tjerëve, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-byreku']=page(bgA,lamp+cloth+table+trays+plate+glass+bread+plate2+''.join(S))

# 2: 5 gjëra kur s'na zë gjumi
W2=7560
bgB='linear-gradient(180deg,#0F1726 0%,#17223A 55%,#1F2B44 100%)'
rnd=random.Random(27)
stars=''.join(D(rnd.randint(0,W2),rnd.randint(980,1500),4,4,'background:#FAF7F1;border-radius:50%%;opacity:.%d'%rnd.randint(3,8)) for _ in range(140))
moon=D(1080*0+760,1060,150,150,'background:#F3E6C4;border-radius:50%;box-shadow:0 0 80px rgba(243,230,196,.45)')
bed=D(0,1700,W2,30,'background:#2C3A56')+D(0,1730,W2,190,'background:linear-gradient(180deg,#24314B,#1B263B)')
pil=D(1080*1+120,1600,380,110,'background:#C9D3E3;border-radius:50px')+D(1080*1+120,1600,380,110,'background:linear-gradient(90deg,rgba(255,255,255,.0),rgba(255,255,255,.35));border-radius:50px')
times=['00:40','01:05','01:30','01:55','02:20']
clocks=''
for i,t in enumerate(times):
    x=(i+1)*1080+620
    clocks+=D(x,1520,270,120,"background:#0B0F18;border:5px solid #2C3A56;border-radius:18px;font-family:'Inter',sans-serif;font-weight:800;font-size:64px;color:#E8B96C;text-align:center;line-height:110px",t)
glassB=D(1080*5+330,1520,100,180,'background:linear-gradient(180deg,rgba(200,220,240,.2),rgba(200,220,240,.4));border:5px solid rgba(220,230,245,.55);border-radius:6px 6px 14px 14px')
S=[slide(0,'dk','Kur s’të zë gjumi','5 gjëra që i bëjmë kur s’na zë gjumi. <em>E katërta e bëjmë të&nbsp;gjithë.</em>','',HINT),
   slide(1,'dk','E para','E kthejmë jastëkun <em>nga ana e&nbsp;ftohtë.</em>'),
   slide(2,'dk','E dyta','Shikojmë orën „vetëm një herë“. <em>Pastaj edhe&nbsp;pesë.</em>'),
   slide(3,'dk','E treta','Kujtojmë një fjali që e thamë gabim <em>para shumë&nbsp;vitesh.</em>'),
   slide(4,'dk','E katërta','Numërojmë: „Nëse fle tani, i kam pesë orë.“ <em>Pastaj katër e&nbsp;gjysmë.</em>'),
   slide(5,'dk','E pesta','Ngrihemi për një gotë ujë <em>që s’na&nbsp;duhej.</em>'),
   end(6,'Kur mendja s’pushon natën, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['02-gjumi']=page(bgB,stars+moon+bed+pil+clocks+glassB+''.join(S),w=W2)

# 3: Lajmi i mire, ora 12:30
bgC='linear-gradient(180deg,#F6F2EA 0%,#EFE8DA 60%,#E6DCC9 100%)'
sun=glow(1080*0+880,1100,520,.55,'255,222,150')+glow(1080*3+500,1150,520,.35,'255,222,150')
rnd=random.Random(12)
conf=''.join(D(rnd.randint(430,1010),rnd.randint(990,1340),18,18,f"background:{rnd.choice(['#D6A24C','#8FB8A8','#3F6259','#E8B96C'])};border-radius:{rnd.choice(['50%','4px'])};transform:rotate({rnd.randint(0,90)}deg);opacity:.85") for _ in range(40))
def phone(x,y,inner):
    return D(x,y,380,700,'background:#221F1C;border-radius:52px;box-shadow:0 24px 50px rgba(60,40,20,.25)')+D(x+18,y+18,344,664,'background:#FAF7F1;border-radius:38px;overflow:hidden',inner)
ok=("<div style=\"position:absolute;left:112px;top:180px;width:120px;height:120px;border-radius:50%;background:#3F6259\"></div>"
    "<div style=\"position:absolute;left:146px;top:210px;width:34px;height:60px;border-right:14px solid #FAF7F1;border-bottom:14px solid #FAF7F1;transform:rotate(45deg)\"></div>"
    "<div style=\"position:absolute;left:0;right:0;top:340px;text-align:center;font-family:Inter;font-weight:800;font-size:40px;color:#221F1C\">U pranua</div>")
rows=''.join(f"<div style=\"position:absolute;left:30px;top:{60+k*110}px;width:70px;height:70px;border-radius:50%;background:{['#8FB8A8','#E8B96C','#C9BFA9','#3F6259','#D6A24C','#8FB8A8'][k]}\"></div><div style=\"position:absolute;left:120px;top:{78+k*110}px;width:{[170,140,190,120,160,150][k]}px;height:30px;border-radius:15px;background:#E6DFD1\"></div>" for k in range(6))
note=("<div style=\"position:absolute;left:30px;top:70px;font-family:Inter;font-weight:800;font-size:34px;color:#221F1C\">Shënime</div>"
      "<div style=\"position:absolute;left:30px;top:140px;width:270px;height:22px;border-radius:11px;background:#D6A24C;opacity:.7\"></div>"
      "<div style=\"position:absolute;left:30px;top:190px;width:220px;height:22px;border-radius:11px;background:#E6DFD1\"></div>"
      "<div style=\"position:absolute;left:30px;top:240px;width:250px;height:22px;border-radius:11px;background:#E6DFD1\"></div>")
ph=phone(1080*0+560,1080,ok)+phone(1080*1+480,1080,rows)+phone(1080*3+460,1080,note)
cupC=D(1080*2+430,1620,150,120,'background:#FAF7F1;border-radius:8px 8px 34px 34px;box-shadow:0 10px 20px rgba(0,0,0,.08)')+D(1080*2+572,1645,50,64,'border:14px solid #FAF7F1;border-left:none;border-radius:0 34px 34px 0')
tableC=D(0,1740,W,180,'background:linear-gradient(180deg,#CDB792,#B89D74)')
S=[slide(0,'lt','Ora 12:30 · Lajm i mirë','Merr një lajm të mirë. <em>Dhe s’di kujt t’ia tregosh i&nbsp;pari.</em>','',HINT),
   slide(1,'lt','Kontaktet','Hap kontaktet. <em>Rrëshqet poshtë, pastaj sërish&nbsp;lart.</em>'),
   slide(2,'lt','Pse ndodh','Gëzimi do dikë që e dëgjon, <em>jo vetëm një&nbsp;njoftim.</em>'),
   slide(3,'lt','Pastaj','E shkruan në një shënim, <em>vetëm për&nbsp;veten.</em>'),
   slide(4,'lt','E vërteta','Edhe të mirat e vogla <em>meritojnë dikë që&nbsp;gëzohet.</em>'),
   end(5,'Kur s’ke kujt t’ia thuash, as të mirën, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-lajmi']=page(bgC,sun+conf+tableC+ph+cupC+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
