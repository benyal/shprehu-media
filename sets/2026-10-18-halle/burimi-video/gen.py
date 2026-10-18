SK='/home/user/Shprehu-3.5/.claude/skills/shprehu-social-ads'
BASE='''<!doctype html><html lang="sq"><head><meta charset="utf-8"><link rel="stylesheet" href="file://%s/assets/brand.css"><style>
html,body{width:1080px;height:1920px;overflow:hidden}
.sc{position:absolute;inset:0;opacity:0}
.serif{font-family:'Fraunces',Georgia,serif;font-weight:600;letter-spacing:-0.025em}
em{font-style:italic;font-weight:500}
.t{position:absolute;left:96px;right:150px;opacity:0}
.tag{position:absolute;left:96px;right:150px;font-size:34px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;opacity:0}
.dk{background:#243C36;color:#FAF7F1}.dk em{color:#E8B96C}.dk .tag{color:#8FB8A8}
.gr{background:#2E4A43;color:#FAF7F1}.gr em{color:#E8B96C}.gr .tag{color:#8FB8A8}
.cr{background:#FAF7F1;color:#221F1C}.cr em{color:#3F6259}.cr .tag{color:#3F6259}
.sd{background:#F3EFE7;color:#221F1C}.sd em{color:#3F6259}.sd .tag{color:#3F6259}
.sub{font-size:52px;line-height:1.3}
.logo{position:absolute;left:96px;top:470px;display:flex;align-items:center;gap:26px;opacity:0}
.logo img{width:110px;height:110px;border-radius:26px}
.logo b{font-family:'Sacramento',cursive;font-weight:400;font-size:98px;line-height:1}
.url{position:absolute;left:96px;font-size:58px;font-weight:700;opacity:0}
.fine{position:absolute;left:96px;right:150px;font-size:32px;line-height:1.4;color:rgba(250,247,241,.8);opacity:0}
.abs{position:absolute}
''' % SK
ENGINE='''
const clamp=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const ease=x=>1-Math.pow(1-clamp(x),3);
const seg=(t,a,b)=>clamp((t-a)/(b-a));
function vis(t,a,d,b){ return ease(seg(t,a,a+d))*(b==null?1:1-ease(seg(t,b-0.3,b))); }
const els=[...document.querySelectorAll('[data-in]')];
function render(ms){
  const t=ms/1000;
  els.forEach(el=>{
    const a=parseFloat(el.dataset.in), b=el.dataset.out?parseFloat(el.dataset.out):null;
    const o=vis(t,a,el.classList.contains('sc')?0.3:0.55,b);
    el.style.opacity=o;
    if(!el.classList.contains('sc')){ const dy=parseFloat(el.dataset.dy||24); el.style.transform='translateY('+((1-o)*dy)+'px)'; }
  });
  if(window.extra) window.extra(t);
}
window.seek=render; render(0);
'''
def END(a, b, h='Thuaje diku, <em>pa emër.</em>', sub='Anonim, falas dhe në shqip. Dikush të dëgjon.'):
    return f'''<div class="sc gr" data-in="{a}" data-out="{b}"><div class="logo" data-in="{a+.3}"><img src="file://{SK}/assets/logo-mark.png" alt=""><b>Shprehu</b></div>
<div class="t serif" data-in="{a+.6}" style="top:690px;font-size:104px;line-height:1.06">{h}</div>
<div class="t sub" data-in="{a+1.2}" style="top:1050px;color:rgba(250,247,241,.92);font-size:52px">{sub}</div>
<div class="url" data-in="{a+1.8}" style="top:1280px">shprehu.cc</div>
<div class="fine" data-in="{a+2.2}" style="top:1400px">Shprehu nuk është shërbim urgjence. Në rrezik, telefono 112.</div></div>'''
def page(body,css='',js=''):
    return BASE+css+'</style></head><body>'+body+'<script>'+js+ENGINE+'</script></body></html>'

# ---------- V1: Defteri i dyqanit (18 s) ----------
lines=['Buka','Qumështi','Vaji','Sheqeri','Kafeja']
rows=''.join(f'<div class="t" data-in="{1.9+i*0.55}" data-dy="8" style="position:relative;left:0;right:0;height:92px;font-family:Fraunces,serif;font-style:italic;font-weight:500;font-size:64px;color:#2B3F8A;border-bottom:3px solid rgba(63,98,89,.25);line-height:92px;display:flex;justify-content:space-between"><span>{x}</span><span style="font-size:44px;color:#8A8073;font-style:normal">·····</span></div>' for i,x in enumerate(lines))
v1=f'''
<div class="sc sd" data-in="0" data-out="6.4">
 <div class="tag" data-in="0.2" style="top:300px">Te dyqani i lagjes</div>
 <div class="t serif" data-in="0.45" style="top:380px;font-size:112px;line-height:1.05">„Shkruaje <em>në defter.</em>“</div>
 <div class="abs" data-in="1.2" style="left:96px;width:834px;top:760px;background:#fff;border-radius:10px;padding:26px 44px 40px;box-shadow:0 24px 60px rgba(34,31,28,.16);transform-origin:top">
   <div style="font-size:30px;font-weight:700;letter-spacing:.12em;color:#B04A2C;margin-bottom:12px">DEFTERI · MUAJI</div>{rows}
 </div>
 <div class="t sub" data-in="5.0" style="top:1500px;color:#4A443C;font-size:48px">Pa para sot. Nesër i japim.</div>
</div>
<div class="sc dk" data-in="6.2" data-out="10.6">
 <div class="t serif" data-in="6.45" style="top:680px;font-size:100px;line-height:1.08">Në defter shkruhet çdo gjë që <em>të mungon.</em></div>
 <div class="t sub" data-in="8.0" style="top:1330px">Buka. Vaji. Sheqeri.</div>
 <div class="t serif" data-in="9.0" style="top:1500px;font-size:76px;line-height:1.1;color:#E8B96C">Askund s’shkruhet <em style="color:#FAF7F1">çfarë të rëndon.</em></div>
</div>
<div class="sc cr" data-in="10.4" data-out="14.2">
 <div class="t serif" data-in="10.65" style="top:720px;font-size:104px;line-height:1.06">Edhe halli ka nevojë <em>për një defter.</em></div>
 <div class="t sub" data-in="12.0" style="top:1300px;color:#4A443C">Një vend ku shkruhet pa u gjykuar dhe pa u kthyer „nesër“.</div>
</div>
'''+END(14.0,18.0)
open('v1-defteri.html','w').write(page(v1))

# ---------- V2: Eja nesër (17 s) ----------
v2css='''.led{position:absolute;left:96px;width:834px;top:620px;height:380px;background:#0F1A17;border:6px solid #3F6259;border-radius:22px;box-shadow:0 20px 60px rgba(0,0,0,.4)}
.led .l{position:absolute;left:0;right:0;top:26px;text-align:center;font-size:34px;font-weight:700;letter-spacing:.2em;color:#8FB8A8}
.led .n{position:absolute;left:0;right:0;top:80px;text-align:center;font-size:230px;font-weight:800;color:#E8B96C;font-variant-numeric:tabular-nums;line-height:1;text-shadow:0 0 40px rgba(232,185,108,.5)}
.tk{position:absolute;left:150px;width:730px;top:1120px;background:#FAF7F1;color:#221F1C;border-radius:8px;padding:30px 40px;box-shadow:0 20px 50px rgba(0,0,0,.35);transform:rotate(-1.5deg)}
.tk b{font-size:30px;letter-spacing:.14em;color:#8A8073}
.tk div{font-size:150px;font-weight:800;line-height:1.05}
'''
v2=f'''
<div class="sc dk" data-in="0" data-out="6.4">
 <div class="tag" data-in="0.2" style="top:300px">Në zyrë · 14:10</div>
 <div class="t serif" data-in="0.45" style="top:370px;font-size:84px;line-height:1.08">Pret të thërrasin <em>numrin tënd.</em></div>
 <div class="led" data-in="1.0"><div class="l">TANI</div><div class="n" id="num">38</div></div>
 <div class="tk" data-in="1.5"><b>NUMRI YT</b><div>47</div></div>
</div>
<div class="sc cr" data-in="6.2" data-out="10.2">
 <div class="t serif" data-in="6.5" style="top:700px;font-size:150px;line-height:1.02">„Eja <em>nesër.</em>“</div>
 <div class="t sub" data-in="8.0" style="top:1060px;color:#4A443C">Dhe ti e di që nesër do të jetë e njëjta radhë.</div>
</div>
<div class="sc gr" data-in="10.0" data-out="13.4">
 <div class="t serif" data-in="10.3" style="top:700px;font-size:100px;line-height:1.08">Nuk lodh vetëm pritja. <em>Lodh ndjenja</em> që askush s’të dëgjon.</div>
 <div class="t sub" data-in="11.8" style="top:1420px;color:#E8B96C;font-weight:600">Dhe ajo mund të thuhet.</div>
</div>
'''+END(13.2,17.2)
v2js='''window.extra=function(t){var n=38+Math.floor(clamp((t-1.6)/3.6)*8);document.getElementById('num').textContent=n;};'''
open('v2-eja-neser.html','w').write(page(v2,v2css,v2js))

# ---------- V3: Shtëpia që nuk mbaron (19 s) ----------
house=''
for i,(t0,y) in enumerate([(1.6,1300),(3.0,1100),(4.4,900)]):
    wins=''.join(f'<div class="abs" style="left:{40+k*105}px;top:36px;width:62px;height:78px;background:#E8DFC8;border:5px solid #243C36;border-radius:4px"></div>' for k in range(0,5))
    house+=f'<div class="abs" data-in="{t0}" data-dy="-60" style="left:196px;top:{y}px;width:600px;height:200px;background:#C9B79A;border:6px solid #243C36">{wins}</div>'
rebar=''.join(f'<div class="abs" data-in="5.4" data-dy="30" style="left:{210+k*150}px;top:{760+(k%2)*14}px;width:10px;height:{140-(k%2)*14}px;background:#B3643A"></div>' for k in range(0,4))
slab=f'<div class="abs" data-in="5.2" style="left:176px;top:896px;width:640px;height:20px;background:#8A8073"></div>'
ground='<div class="abs" style="left:0;top:1500px;width:1080px;height:420px;background:#1A2B26"></div><div class="abs" style="left:0;top:1500px;width:1080px;height:10px;background:#3F6259"></div>'
v3=f'''
<div class="sc dk" data-in="0" data-out="8.6">
 {ground}
 <div class="tag" data-in="0.2" style="top:260px">Në çdo qytet shqiptar</div>
 <div class="t serif" data-in="0.45" style="top:330px;font-size:92px;line-height:1.06">Shtëpia që <em>nuk mbaron kurrë.</em></div>
 {house}{slab}{rebar}
 <div class="t sub" data-in="1.8" style="top:1560px;font-size:44px;right:150px;left:96px">Kati i parë: për ne.</div>
 <div class="t sub" data-in="3.2" style="top:1625px;font-size:44px">Kati i dytë: për djalin.</div>
 <div class="t sub" data-in="4.6" style="top:1690px;font-size:44px">Kati i tretë: <em>për më vonë.</em></div>
 <div class="t sub" data-in="6.0" style="top:560px;font-size:56px;color:#E8B96C;font-weight:600;left:96px">Hekurat mbi çati mbeten.</div>
</div>
<div class="sc cr" data-in="8.4" data-out="12.4">
 <div class="t serif" data-in="8.7" style="top:700px;font-size:100px;line-height:1.08">Ndërtuam për të tjerët, dhe <em>lamë veten për më vonë.</em></div>
 <div class="t sub" data-in="10.2" style="top:1380px;color:#4A443C">Shumë njerëz e njohin këtë ndjenjë.</div>
</div>
<div class="sc gr" data-in="12.2" data-out="15.6">
 <div class="t serif" data-in="12.5" style="top:760px;font-size:108px;line-height:1.06">Shtëpia mbaron një ditë. <em>Ti s’je i pambaruar.</em></div>
</div>
'''+END(15.4,19.4,'Dikush të dëgjon, <em>pa emër.</em>','Anonim, falas dhe në shqip.')
open('v3-shtepia.html','w').write(page(v3))

# ---------- V4: Ke njeri? (16 s) ----------
bub=lambda a,y,side,txt,bg,fg: f'<div class="abs" data-in="{a}" data-dy="30" style="top:{y}px;{side}:96px;max-width:620px;background:{bg};color:{fg};padding:30px 42px;border-radius:34px;font-size:56px;line-height:1.2;font-weight:600">{txt}</div>'
v4=f'''
<div class="sc dk" data-in="0" data-out="6.6">
 <div class="tag" data-in="0.2" style="top:300px">Te dera e zyrës</div>
 <div class="t serif" data-in="0.45" style="top:370px;font-size:120px;line-height:1.04">„Ke <em>njeri</em> aty brenda?“</div>
 {bub(2.0,860,'right','Jo, s’kam.','#3F6259','#FAF7F1')}
 {bub(3.4,1070,'left','Atëherë prit radhën.','#FAF7F1','#221F1C')}
 <div class="t sub" data-in="5.0" style="top:1330px;color:#E8B96C;font-weight:600;font-size:50px">Fjali që e dëgjuam shumë herë.</div>
</div>
<div class="sc cr" data-in="6.4" data-out="10.6">
 <div class="t serif" data-in="6.7" style="top:700px;font-size:100px;line-height:1.08">Pse duhet <em>njeri</em> për gjënë që e meriton çdokush?</div>
 <div class="t sub" data-in="8.4" style="top:1380px;color:#4A443C">Pyetja nuk është për një person. Është për një zakon.</div>
</div>
<div class="sc gr" data-in="10.4" data-out="13.4">
 <div class="t serif" data-in="10.7" style="top:760px;font-size:100px;line-height:1.08">Për të folur, s’të duhet njeri. <em>Vetëm një vend.</em></div>
</div>
'''+END(13.2,17.2,'Pa emër. <em>Pa njeri.</em>','Anonim, falas dhe në shqip. Dikush të dëgjon.')
open('v4-ke-njeri.html','w').write(page(v4))
print('ok')
