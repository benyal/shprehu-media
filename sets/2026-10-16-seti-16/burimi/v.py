from common import *
lines = ['një ditë që s’mbaroi', 'një mesazh që s’e dërgove', 'një „mirë“ që s’ishte e vërtetë', 'një lodhje që s’ia the askujt']
rows = ''.join(f'<div style="padding:18px 0;border-top:2px solid rgba(250,247,241,.14);font-family:Fraunces,serif;font-style:italic;font-size:54px;color:var(--gold-soft);opacity:0;animation:rowin .6s ease-out {5.9+i*1.25}s both">{t}</div>' for i, t in enumerate(lines))
chat = f'''<div class="sc" style="--a:fade;--t:3.0s;--d:9.4s;color:#F5EFE4">
<div style="opacity:0;animation:rowin .5s ease-out 3.3s both;align-self:flex-start;background:rgba(250,247,241,.12);border-radius:34px 34px 34px 8px;padding:26px 40px;font-size:50px">Çfarë ke?</div>
<div style="opacity:0;animation:rowin .5s ease-out 4.6s both;align-self:flex-end;margin-top:26px;background:var(--gold);color:var(--ink);border-radius:34px 34px 8px 34px;padding:26px 46px;font-size:64px;font-weight:700">Asgjë.</div>
<div class="k" style="margin-top:74px;color:var(--sage);opacity:0;animation:rowin .5s ease-out 5.4s both">Brenda kësaj fjale ka</div>
<div style="margin-top:14px">{rows}</div></div>'''
body = f'''<body style="background:linear-gradient(180deg,#1B2A24,#0F1A16)">
<div class="sc" style="--t:0.2s;--d:2.7s;color:#F5EFE4"><div class="k" style="color:var(--sage)">Një fjalë që e themi shpesh</div><div class="big" style="margin-top:26px">„Asgjë“ është fjala <em style="color:var(--gold-soft)">më e gjatë në shqip.</em></div></div>
{chat}
<div class="sc" style="--t:12.7s;--d:2.4s;color:#F5EFE4"><div class="big" style="font-size:92px">Dhe pyetja zakonisht <em style="color:var(--gold-soft)">nuk përsëritet.</em></div></div>
{end_card(15.0, 4.8, True, 'Në Shprehu mund ta thuash <em>gjithë fjalën.</em>', 'Anonimisht, falas, në shqip.')}
<style>@keyframes rowin{{from{{opacity:0;transform:translateX(-30px)}}to{{opacity:1;transform:none}}}}</style>
</body>'''
open('v.html', 'w').write(CSS + '</style></head>' + body)
