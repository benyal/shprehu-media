import random, sys
SK='/home/user/Shprehu-3.5/.claude/skills/shprehu-social-ads'
W=6480
CSS='''
html,body{width:6480px;height:1920px;overflow:hidden}
.pano{position:absolute;left:0;top:0;width:6480px;height:1920px;overflow:hidden}
.slide{position:absolute;top:0;width:1080px;height:1920px}
.safe{position:absolute;left:96px;right:150px;top:250px;bottom:460px;display:flex;flex-direction:column}
.tag{font-size:30px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;display:flex;gap:18px;align-items:center;margin-bottom:44px}
.tag::before{content:'';width:46px;height:3px;background:var(--gold);border-radius:2px}
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

sets={}
HINT='Rrëshqit →'

# 1: Sa merr?
random.seed(11)
cups=''
for k in range(0,34):
    x=40+k*190
    c=['#FFFFFF','#F7F1E3','#FFFFFF'][k%3]
    cups+=D(x,1640,150,26,'background:#D9CFBA;border-radius:0 0 80px 80px/0 0 26px 26px')
    cups+=D(x+20,1560,110,80,f'background:{c};border:3px solid #CFC4AC;border-radius:6px 6px 55px 55px/6px 6px 70px 70px')
    cups+=D(x+112,1578,34,40,'border:6px solid #CFC4AC;border-left:0;border-radius:0 24px 24px 0')
    cups+=D(x+36,1574,78,14,'background:#6B4A33;border-radius:50%;opacity:.85')
    if k%4==1: cups+=D(x+40,1480,10,60,'background:rgba(138,128,115,.35);border-radius:6px')+D(x+70,1500,10,50,'background:rgba(138,128,115,.3);border-radius:6px')
table=D(0,1700,W,220,'background:#E4DAC4')+D(0,1700,W,8,'background:#CFC4AC')
S=[slide(0,'lt','Në kafe · 11:20','Herët a vonë vjen pyetja: <em>„Sa merr?“</em>','Edhe kafja ftohet kur përgjigjja nuk është e lehtë.',HINT),
   slide(1,'lt','Pyetja','Duket e pafajshme. <em>Përgjigja nuk është.</em>','Ti numëron, ai numëron, dhe të dy e dini kush „fitoi“.'),
   slide(2,'lt','Pas përgjigjes','Dikush buzëqesh me mirëkuptim. Dikush <em>ndihet më i vogël.</em>','Për një numër që s’tregon sa je lodhur dhe as sa vlen.'),
   slide(3,'lt','Një rrogë','Rroga s’tregon <em>sa ke hequr</em> për ta fituar.','As sa i mirë je. As sa i dobishëm je.'),
   slide(4,'lt','Ndryshe','Provo të pyesësh: <em>„Si po të ecën puna?“</em>','Pyetja që hap një bisedë, jo një krahasim.'),
   end(5,'Ç’nuk thua te kafeja, <em>thuaje pa emër.</em>')]
sets['01-sa-merr']=page('#F3EFE7',table+cups+''.join(S))

# 2: Dita 20
days=''
for d in range(1,32):
    x=40+(d-1)*205
    if d==20:
        days+=D(x-18,1536,140,140,'border:6px solid #E8B96C;border-radius:50%;box-shadow:0 0 60px rgba(232,185,108,.45)')
    op=1 if d<=20 else .35
    days+=D(x,1560,104,92,f'display:flex;align-items:center;justify-content:center;font-size:46px;font-weight:700;color:#FAF7F1;opacity:{op}',str(d))
    if d<20: days+=D(x+8,1670,88,6,'background:#8FB8A8;border-radius:3px;opacity:.5')
note=('<div style="margin-top:40px;background:#F7F2E2;border-radius:26px;padding:34px 40px;color:#221F1C;box-shadow:0 20px 50px rgba(0,0,0,.35);font-size:44px;line-height:1.1">'
 '<div style="font-size:28px;font-weight:700;color:#B9822F;letter-spacing:.1em;margin-bottom:18px">SHËNIME · 20 E MUAJIT</div>'
 +''.join(f'<div style="display:flex;align-items:center;gap:22px;padding:14px 0;border-bottom:2px solid #E3D9BE"><span style="width:34px;height:34px;border-radius:50%;background:#3F6259;flex:none"></span>{t}</div>' for t in ['Qiraja','Drita dhe uji','Interneti','Ilaçet e nënës','Benzina'])
 +'<div style="display:flex;align-items:center;gap:22px;padding:14px 0"><span style="width:34px;height:34px;border-radius:50%;border:4px solid #B9822F;flex:none"></span><span style="color:#B9822F">Unë</span></div></div>')
S=[slide(0,'dk','20 · Fundi i muajit','Dita 20 e muajit ka <em>matematikën e vet.</em>','Ajo që s’e di askush, përveç teje.',HINT),
   slide(1,'dk','Lista','Në listë futet gjithkush. <em>Vetja shkruhet e fundit.</em>','',' ',note),
   slide(2,'dk','Llogaria','Muaji nuk numërohet më me ditë, <em>por me ushqim.</em>','Dhe me një „mjafton“ që e thua vetes shpesh.'),
   slide(3,'dk','Në shtëpi','Të pyesin si je. Ti thua: <em>„Mirë, pak i lodhur.“</em>','Dhe llogaria vazhdon në kokë.'),
   slide(4,'dk','E vërteta','Halli i parasë s’është turp. <em>Turp do të ishte</em> ta mbaje vetëm.','Pesha ndahet më lehtë kur e thua me zë.'),
   end(5,'Thuaje diku, <em>pa emër.</em>')]
sets['02-dita-20']=page('linear-gradient(90deg,#2C4A42,#243C36 50%,#1C2F2A)',days+''.join(S))

# 3: Me këste
bars=''
random.seed(3)
x=30
while x<W-60:
    w=random.choice([4,4,6,8,10,4,6]); bars+=D(x,1560,w,150,'background:#2A2622'); x+=w+random.choice([6,8,10,14])
bars+=D(0,1730,W,60,'font-size:30px;letter-spacing:.9em;color:#8A8073;text-align:left;white-space:nowrap;overflow:hidden',''.join(['KËSTI 1   KËSTI 2   KËSTI 3   KËSTI 4   ']*18))
zig=D(0,0,W,40,'background:repeating-linear-gradient(135deg,#FAF7F1 0 20px,transparent 20px 40px)')
receipt=('<div style="margin-top:40px;background:#fff;border:2px dashed #CFC4AC;border-radius:6px;padding:34px 40px;font-family:\'Inter\',monospace;font-size:40px;line-height:1.1;color:#221F1C;box-shadow:0 14px 40px rgba(34,31,28,.12)">'
 '<div style="font-weight:800;letter-spacing:.14em;font-size:30px;color:#8A8073;margin-bottom:16px">SHTËPIA JONË · FATURË</div>'
 +''.join(f'<div style="display:flex;justify-content:space-between;padding:14px 0;border-bottom:2px dotted #CFC4AC"><span>{a}</span><span style="color:#8A8073">{b}</span></div>' for a,b in [('Frigoriferi','kësti i muajit'),('Divani','kësti i muajit'),('Televizori','kësti i muajit'),('Telefoni','kësti i muajit')])
 +'<div style="display:flex;justify-content:space-between;padding:14px 0;color:#3F6259;font-weight:800"><span>Qetësia</span><span>s’shitet me këste</span></div></div>')
S=[slide(0,'lt','Në shumë shtëpi','Gjithçka është <em>me këste.</em> Përveç qetësisë.','',HINT),
   slide(1,'lt','Fatura e shtëpisë','Çdo gjë e ka <em>datën e vet.</em>','',' ',receipt),
   slide(2,'lt','Çdo datë 5','Njoftimi vjen, dhe <em>stomaku shtrëngohet.</em>','Edhe pse kësti është i vogël.'),
   slide(3,'lt','Pesha','Nuk rëndon shuma. <em>Rëndon përsëritja.</em>','Çdo muaj, pa pushim, pa një „mjaft“.'),
   slide(4,'lt','Ndryshe','Mos e mbaj llogarinë vetëm në kokë. <em>Thuaje me zë.</em>','Dikujt që nuk gjykon.'),
   end(5,'Dikush të dëgjon, <em>pa emër.</em>')]
sets['03-me-keste']=page('#FAF7F1',zig+bars+''.join(S))

# 4: Ilaçet
org=''
lab=['H','M','M','E','P','S','D']
for k in range(0,33):
    x=40+k*195
    org+=D(x,1540,170,190,'background:#fff;border:4px solid #A9C2B6;border-radius:18px;box-shadow:0 8px 20px rgba(34,31,28,.08)')
    org+=D(x,1540,170,50,'display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:800;color:#3F6259;letter-spacing:.1em',lab[k%7])
    if k%7!=6:
        org+=D(x+34,1620,102,40,'background:linear-gradient(90deg,#D6A24C 50%,#F3EFE7 50%);border-radius:30px;border:3px solid #CFC4AC;transform:rotate(-12deg)')
        org+=D(x+60,1675,52,30,'background:#8FB8A8;border-radius:50%;opacity:.8')
S=[slide(0,'lt','Çanta e nënës','Në çantën e nënës ka gjithmonë <em>një qese me ilaçe.</em>','',HINT),
   slide(1,'lt','Ti i di','Emrat, orët, <em>sa herë në ditë.</em>','Fjalë që s’i kishe dëgjuar kurrë, tani i di përmendësh.'),
   slide(2,'lt','Pa e zgjedhur','Je bërë <em>mjeku i shtëpisë,</em> pa e thënë askujt.','Pranë punës, pranë ditës tënde.'),
   slide(3,'lt','Pyetja','Të gjithë pyesin si është ajo. <em>Pak njerëz pyesin si e mban ti.</em>'),
   slide(4,'lt','E vërteta','Kujdesi për dikë të dashur <em>lodh.</em> Dhe s’është turp ta thuash.','Ke të drejtë të jesh i lodhur edhe kur do shumë.'),
   end(5,'Edhe ti ke nevojë <em>të flasësh.</em>')]
sets['04-ilacet']=page('#E3EDE7',D(0,1700,W,220,'background:#CFE0D7')+org+''.join(S))

# 5: Duro
stones=''
random.seed(5)
cols=['#8FB8A8','#6E9C8C','#B9C9BF','#E8B96C','#7A8F86']
x=30;n=0
while x<5000:
    w=random.randint(120,200);h=random.randint(70,110)
    layers=min(6,int(x/950)+1)
    for L in range(layers):
        stones+=D(x+L*12-6,1690-h*(L+1)+L*8,w,h,f'background:{random.choice(cols)};border-radius:40% 45% 38% 42%/55% 50% 45% 50%;opacity:.92;border:3px solid rgba(0,0,0,.18)')
    x+=w+8
S=[slide(0,'dk','Un fjalë','Sa herë të kanë thënë <em>„duro“,</em> dhe sa herë „të dëgjoj“?','',HINT),
   slide(1,'dk','Duro','Duket si kujdes. Shpesh do të thotë: <em>mos e thuaj me zë.</em>'),
   slide(2,'dk','Në shkollë, në punë, në shtëpi','Duruam. Durimi u bë virtyt, dhe <em>heshtja u bë „forcë“.</em>'),
   slide(3,'dk','Barra','Durimi ka vlerë kur ka <em>fund.</em> Pa fund, bëhet gur mbi gur.','Dhe një ditë s’mban më.'),
   slide(4,'dk','E vërteta','Ta thuash një hall me zë <em>nuk e zvogëlon forcën tënde.</em>','E bën më të lehtë për ta mbajtur.'),
   end(5,'Thuaje diku, <em>pa emër.</em>')]
sets['05-duro']=page('linear-gradient(90deg,#26403A,#1F332E 70%,#1B2D28)',stones+''.join(S))

# 6: Dy punë
hrs=''
for h in range(0,25):
    x=60+h*250
    hrs+=D(x,1600,3,56,'background:rgba(250,247,241,.4)')
    hrs+=D(x-30,1668,64,40,'font-size:30px;font-weight:700;color:#8FB8A8;text-align:center',f'{(5+h)%24:02d}')
hrs+=D(60,1612,250*8,32,'background:#E8B96C;border-radius:8px')+D(60,1560,250*8,40,'font-size:28px;font-weight:700;color:#E8B96C','PUNA E PARË')
hrs+=D(60+250*8+40,1612,250*3.2,32,'background:#8FB8A8;border-radius:8px')+D(60+250*8+40,1560,250*5,40,'font-size:28px;font-weight:700;color:#8FB8A8','UDHËTIM')
hrs+=D(60+250*11.6,1612,250*6,32,'background:#D6A24C;border-radius:8px')+D(60+250*11.6,1560,250*6,40,'font-size:28px;font-weight:700;color:#D6A24C','PUNA E DYTË')
hrs+=D(60+250*18.2,1612,250*2,32,'background:#FAF7F1;border-radius:8px;opacity:.9')+D(60+250*18.2,1560,300,40,'font-size:28px;font-weight:700;color:#FAF7F1','GJUMI')
S=[slide(0,'dk','Mëngjes · mbrëmje','Mëngjesi në një punë. <em>Mbrëmja në tjetrën.</em>','',HINT),
   slide(1,'dk','Fjala e njerëzve','Të thonë: <em>„Sa i fortë je.“</em>','Dhe fjala „i fortë“ të mbyll gojën.'),
   slide(2,'dk','Koha','S’ke kohë të jesh i lodhur. <em>Lodhja pret radhën.</em>'),
   slide(3,'dk','Fshehurazi','Edhe të fortët thyhen. <em>Vetëm se askush s’i sheh.</em>','Ndodh në autobus, ose para derës së shtëpisë.'),
   slide(4,'dk','E vërteta','Dy punë janë forcë. <em>Një ditë e qetë</em> s’është dobësi.'),
   end(5,'Ke të drejtë <em>të pushosh.</em>')]
sets['06-dy-pune']=page('linear-gradient(90deg,#2A4640,#243C36 50%,#1E322D)',hrs+''.join(S))

# 7: Do t'ju telefonojmë
ripples=''
for k in range(0,16):
    r=120+k*150
    op=max(.06,.5-k*.03)
    ripples+=D(-r+160,1650-r,r*2,r*2,f'border:4px solid rgba(232,185,108,{op});border-radius:50%')
phone=D(70,1560,160,260,'background:#1A2B26;border:6px solid #8FB8A8;border-radius:34px')+D(100,1600,100,14,'background:#E8B96C;border-radius:7px')+D(100,1640,100,14,'background:#8FB8A8;border-radius:7px;opacity:.6')
cov=D(0,1820,W,100,'background:#2E4A43')
S=[slide(0,'dk','Pas intervistës','<em>„Do t’ju telefonojmë.“</em> Dhe telefoni mbetet përbri teje.','',HINT),
   slide(1,'dk','Çdo zile','Çdo numër i panjohur <em>ta ngre zemrën.</em> Pastaj bie.'),
   slide(2,'dk','CV-ja','E dërgon edhe një herë, me të njëjtat fjalë dhe <em>pak më shumë shpresë.</em>'),
   slide(3,'dk','Njerëzit','Të pyesin: <em>„Ende pa punë?“</em>','Sikur ti të mos e dije.'),
   slide(4,'dk','E vërteta','Pritja është punë e rëndë, <em>edhe pse s’paguhet.</em>','Dhe nuk e bën më pak të vlefshëm.'),
   end(5,'Thuaje diku, <em>pa emër.</em>')]
sets['07-do-ju-telefonojme']=page('#2E4A43',ripples+phone+''.join(S))

# 8: Lavatriçja
drum=''
random.seed(8)
for k in range(0,12):
    x=-40+k*560
    drum+=D(x,1470,360,360,'border:12px solid #A9C2B6;border-radius:50%;background:#EEF4F0')
    drum+=D(x+60,1530,240,240,'border:6px solid #CFE0D7;border-radius:50%;background:rgba(143,184,168,.35)')
    drum+=D(x+120,1640,120,70,'background:rgba(63,98,89,.22);border-radius:50% 50% 8px 8px')
bub=''.join(D(random.randint(0,W),random.randint(1480,1780),random.randint(18,40),0,'',cls='')+D(random.randint(0,W),random.randint(1500,1760),random.randint(16,34),random.randint(16,34),'border:3px solid rgba(63,98,89,.35);border-radius:50%') for _ in range(40))
S=[slide(0,'lt','Zhurma e çuditshme','Muaji nuk prishet nga gjërat e mëdha. <em>Prishet nga lavatriçja.</em>','',HINT),
   slide(1,'lt','Në sekondë','Dëgjon zhurmën. <em>Dhe llogarit,</em> para se të pyesësh çmimin.'),
   slide(2,'lt','Para saj','Gjithçka ishte „në rregull“, <em>derisa u prish një gjë e vogël.</em>'),
   slide(3,'lt','Në fakt','S’është lavatriçja. <em>Është mungesa e dikujt</em> që thotë „e zgjidhim“.'),
   slide(4,'lt','E vërteta','S’ke pse t’i zgjidhësh <em>të gjitha vetëm.</em>','Thuaje me zë, edhe kur duket e vogël.'),
   end(5,'Dikush të dëgjon, <em>pa emër.</em>')]
sets['08-lavatrice']=page('#E8F0EC',D(0,1790,W,130,'background:#CFE0D7')+drum+bub+''.join(S))

# 9: Kutitë
boxes=''
random.seed(9)
labels=['LIBRA','ENËT','FOTO','VERA','DIMRI','LETRA','GJYSHJA','DIPLOMA']
x=20;i=0
while x<W-150:
    w=random.randint(190,300);h=random.randint(150,260)
    lab=labels[i%len(labels)];i+=1
    boxes+=D(x,1760-h,w,h,'background:#C9A878;border:3px solid #A8895A;border-radius:6px;box-shadow:inset 0 -14px 0 rgba(0,0,0,.08)')
    boxes+=D(x+w//2-26,1760-h,52,h,'background:rgba(255,255,255,.35)')
    boxes+=D(x+14,1760-h+h//2-4,w-28,44,'background:#F7F1E3;color:#4A443C;font-size:28px;font-weight:800;text-align:center;line-height:44px;letter-spacing:.1em;border-radius:4px;transform:rotate(-1.5deg)',lab)
    x+=w+random.randint(8,30)
S=[slide(0,'lt','Në qira','Kutitë <em>nuk hapen kurrë</em> plotësisht.','',HINT),
   slide(1,'lt','Një kuti','Një kuti për <em>„kur të kem shtëpinë time“.</em>','Libra, foto, një filxhan i gjyshes.'),
   slide(2,'lt','Muri','S’e varë pikturën, se <em>do të ikësh.</em>','Qiraja ka një rregull të pashkruar: mos u lidh shumë.'),
   slide(3,'lt','Në fakt','Jeta s’pret <em>shtëpinë tënde.</em> Ti je këtu sot.'),
   slide(4,'lt','Një cep','Ia ke borxh vetes një cep <em>ku ndihesh mirë tani.</em>','Edhe nëse është vetëm një karrige.'),
   end(5,'Thuaje diku, <em>pa emër.</em>')]
sets['09-kutite']=page('#EFE6D2',D(0,1760,W,160,'background:#DCCFB2')+boxes+''.join(S))

# 10: Diploma
shelf=D(0,1780,W,22,'background:#7A5C3C')+D(0,1802,W,60,'background:rgba(0,0,0,.18)')
items=''
random.seed(10)
x=40
cols=['#3F6259','#5E8C7D','#8FB8A8','#D6A24C','#B3643A','#2E4A43']
while x<W-200:
    if 520<x<900:
        x=900;continue
    w=random.randint(44,80);h=random.randint(130,250)
    items+=D(x,1780-h,w,h,f'background:{random.choice(cols)};border-radius:6px 6px 2px 2px')+D(x+8,1780-h+22,w-16,8,'background:rgba(255,255,255,.4);border-radius:4px')
    x+=w+4
frame=(D(540,1500,330,280,'background:#FFFDF6;border:14px solid #D6A24C;box-shadow:0 14px 30px rgba(34,31,28,.18);transform:rotate(-3deg);transform-origin:bottom left')
 +D(580,1550,250,14,'background:#CFC4AC;transform:rotate(-3deg)')+D(580,1590,250,10,'background:#E3DBC8;transform:rotate(-3deg)')+D(580,1620,200,10,'background:#E3DBC8;transform:rotate(-3deg)')
 +D(660,1680,64,64,'background:#B04A2C;border-radius:50%;transform:rotate(-3deg);opacity:.9'))
items+=frame
S=[slide(0,'lt','Mbi raft','Diploma qëndron në raft. <em>Ti punon diku tjetër.</em>','',HINT),
   slide(1,'lt','Pyetja','Të pyesin: <em>„Pse studive?“</em>','Dhe nuk di si t’i përgjigjesh me një fjali.'),
   slide(2,'lt','Plani','Dikur kishe plan. <em>Plani u bë „më parë të mbijetojmë“.</em>'),
   slide(3,'lt','Ajo që mbetet','Çfarë mësove <em>nuk fshihet</em> nga kjo punë.','Je më shumë se fusha ku punon sot.'),
   slide(4,'lt','E vërteta','Është e rëndë të jesh <em>në mes</em> të asaj që ke ëndërruar dhe asaj që të del.'),
   end(5,'Edhe kjo <em>mund të thuhet.</em>')]
sets['10-diploma']=page('#FAF7F1',shelf+items+''.join(S))

if __name__=='__main__':
    for k,v in sets.items():
        open(f'set-{k}.html','w').write(v)
    print(len(sets),'sets')
