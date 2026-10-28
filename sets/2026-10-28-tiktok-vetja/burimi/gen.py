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

# 1: Biseda me veten, ora 00:30
bgA='linear-gradient(180deg,#141A24 0%,#1B2330 60%,#212A36 100%)'
rnd=random.Random(34)
dots=''.join(D(rnd.randint(0,W),rnd.randint(960,1450),3,3,'background:#FAF7F1;border-radius:50%%;opacity:.%d'%rnd.randint(2,6)) for _ in range(90))
def phoneA(x,y,inner):
    return glow(x+190,y+300,420,.18,'150,190,220')+D(x,y,380,720,'background:#0E1218;border:8px solid #2E3846;border-radius:54px')+D(x+22,y+22,336,676,'background:#1E2A33;border-radius:38px;overflow:hidden',inner)
head_="<div style=\"position:absolute;left:0;right:0;top:0;height:86px;background:#2E4A43;font-family:Inter;font-weight:700;font-size:30px;color:#FAF7F1;line-height:86px;padding-left:28px\">Ti (vetja)</div>"
def bub(top,w,gold=False,txt=''):
    bg='#D6A24C' if gold else '#3F6259'
    return f"<div style=\"position:absolute;right:20px;top:{top}px;width:{w}px;min-height:56px;border-radius:22px 22px 6px 22px;background:{bg};font-family:Inter;font-weight:600;font-size:26px;color:#FAF7F1;padding:14px 18px;box-sizing:border-box\">{txt}</div>"
p1=phoneA(1080*0+600,1080,head_+bub(120,240,txt='bukë, qumësht')+bub(200,200,txt='fjalëkalimi?')+bub(280,250,txt='[foto]'))
p2=phoneA(1080*1+520,1080,head_+bub(120,240,txt='bukë, qumësht')+bub(200,200,txt='fjalëkalimi?')+bub(280,250,txt='[foto]')+bub(380,300,True,'jam lodhur më shumë se sa e tregoj'))
p3=phoneA(1080*3+480,1080,head_+bub(380,300,True,'jam lodhur më shumë se sa e tregoj')+"<div style=\"position:absolute;right:24px;top:500px;font-family:Inter;font-size:24px;color:#8FB8A8\">Lexuar 00:34</div>")
lampA=glow(1080*2+560,1500,380,.25,'255,205,130')+D(1080*2+520,1520,80,260,'background:#2E2A2A')+D(1080*2+440,1440,240,100,'background:#C99A4E;border-radius:24px 24px 6px 6px')
bedA=D(0,1780,W,140,'background:#11161E')
S=[slide(0,'dk','Ora 00:30 · Biseda me veten','Hap bisedën me veten në telefon. <em>Dhe i shkruan vetes atë që s’ia the&nbsp;askujt.</em>','',HINT),
   slide(1,'dk','Ekrani','Aty ka lista, foto, fjalëkalime. <em>Dhe një fjali që s’e dërgove&nbsp;kurrë.</em>'),
   slide(2,'dk','Pse','Duhet ta shohësh të shkruar. <em>Që të mos duket aq e&nbsp;madhe.</em>'),
   slide(3,'dk','Pastaj','E lexon një herë. <em>Dhe fle pak më&nbsp;lehtë.</em>'),
   slide(4,'dk','E vërteta','Të shkruarit ndihmon. <em>Por ndonjëherë duhet që dikush ta&nbsp;lexojë.</em>'),
   end(5,'Kur ke diçka që s’ia ke thënë askujt, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['01-vetja']=page(bgA,dots+bedA+p1+p2+lampA+p3+''.join(S))

# 2: 5 gjëra kur dikush na kërkon falje
W2=7560
bgB='linear-gradient(180deg,#F6F2EA 0%,#EEF2EC 62%,#DCE9E6 100%)'
water=D(0,1560,W2,360,'background:linear-gradient(180deg,#BFD8D6,#A6C8C6)')+''.join(D(k*260,1600+(k%3)*60,180,6,'background:rgba(255,255,255,.55);border-radius:3px') for k in range(29))
boats=''
for i in range(1,6):
    x=i*1080+420; gold=(i==4)
    col='#F3D9A0' if gold else '#FFFFFF'; bd='#D6A24C' if gold else '#CFC4AE'
    boats+=D(x,1500,300,80,f'background:{col};clip-path:polygon(0 0,100% 0,82% 100%,18% 100%);filter:drop-shadow(0 6px 8px rgba(0,0,0,.1))')
    boats+=D(x+90,1360,120,140,f'background:{col};clip-path:polygon(50% 0,100% 100%,0 100%)')
    boats+=D(x+148,1360,4,140,f'background:{bd}')
    boats+=D(x,1500,300,80,f"font-family:'Fraunces',serif;font-weight:600;font-size:52px;text-align:center;line-height:70px;color:{'#B9862F' if gold else '#9C8F78'}",str(i))
S=[slide(0,'lt','Kur dikush kërkon falje','5 gjëra që i bëjmë kur dikush na kërkon falje. <em>E katërta e bëjmë pa e&nbsp;kuptuar.</em>','',HINT),
   slide(1,'lt','E para','Themi „s’ka gjë“ <em>para se ta mbarojë&nbsp;fjalinë.</em>'),
   slide(2,'lt','E dyta','Ndërrojmë temën <em>sa më&nbsp;shpejt.</em>'),
   slide(3,'lt','E treta','E mbajmë mend <em>gjithsesi, për&nbsp;vite.</em>'),
   slide(4,'lt','E katërta','Kërkojmë falje edhe ne, <em>edhe pse s’kishim&nbsp;faj.</em>'),
   slide(5,'lt','E pesta','Ia lehtësojmë atij <em>më shumë se&nbsp;vetes.</em>'),
   end(6,'Kur „s’ka gjë“ s’është e vërtetë, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['02-falja']=page(bgB,water+boats+''.join(S),w=W2)

# 3: „Ti je gjithmonë kaq i qetë“, ora 16:00
bgC='linear-gradient(180deg,#F4F1EA 0%,#E6EEEA 45%,#CFE0DD 62%,#2E5A5C 64%,#1F4447 100%)'
surf=D(0,1220,W,6,'background:rgba(255,255,255,.7)')
refl=''.join(D(k*340+60,1160+(k%2)*24,200,4,'background:rgba(255,255,255,.6);border-radius:2px') for k in range(19))
sunC=glow(1080*0+820,1020,300,.6,'255,224,160')
cur=''
rnd=random.Random(5)
for k in range(46):
    x=rnd.randint(0,W); y=rnd.randint(1320,1860); w=rnd.randint(160,420)
    cur+=D(x,y,w,w//3,f'border:6px solid rgba(143,184,168,.{rnd.randint(25,55)});border-color:rgba(143,184,168,.45) transparent transparent transparent;border-radius:50%')
S=[slide(0,'lt','Ora 16:00 · Në punë','„Ti je gjithmonë kaq i qetë.“ <em>Dhe ti&nbsp;buzëqesh.</em>','',HINT),
   slide(1,'lt','Brenda','Brenda ka qenë zhurmë <em>gjithë&nbsp;ditën.</em>'),
   slide(2,'lt','Pse','Qetësia që shihet <em>shpesh është punë e madhe&nbsp;brenda.</em>'),
   slide(3,'lt','Pastaj','Në shtëpi ulesh dhe s’flet <em>për një orë të&nbsp;tërë.</em>'),
   slide(4,'lt','E vërteta','Edhe të qetët <em>kanë nevojë të&nbsp;dëgjohen.</em>'),
   end(5,'Kur qetësia të lodh, <em>fol me dikë pa&nbsp;emër.</em>')]
sets['03-qetesia']=page(bgC,'<style>.slide .hint{color:#E8B96C}</style>'+sunC+refl+surf+cur+''.join(S))

if __name__=='__main__':
    for k,v in sets.items(): open(f'set-{k}.html','w').write(v)
    print(len(sets))
