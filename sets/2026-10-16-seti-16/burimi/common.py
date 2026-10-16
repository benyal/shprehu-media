SK = '/home/user/Shprehu-3.5/.claude/skills/shprehu-social-ads'
CSS = f'''<!doctype html><html lang="sq"><head><meta charset="utf-8"><link rel="stylesheet" href="file://{SK}/assets/brand.css"><style>
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden}}
.sc{{position:absolute;left:96px;right:140px;top:250px;bottom:420px;display:flex;flex-direction:column;justify-content:center;opacity:0;animation:var(--a,show) var(--d,2.6s) ease-out var(--t,0s) both}}
@keyframes show{{0%{{opacity:0;transform:translateY(36px)}}10%,88%{{opacity:1;transform:none}}100%{{opacity:0;transform:translateY(-24px)}}}}
@keyframes hold{{0%{{opacity:0;transform:translateY(36px)}}14%,100%{{opacity:1;transform:none}}}}
@keyframes fade{{0%{{opacity:0}}8%,92%{{opacity:1}}100%{{opacity:0}}}}
.k{{font-size:27px;font-weight:700;letter-spacing:.2em;text-transform:uppercase}}
.big{{font-family:'Fraunces',serif;font-weight:600;font-size:104px;line-height:1.06;letter-spacing:-.02em}}
.big em{{font-style:italic;font-weight:500}}
.mid{{font-family:'Fraunces',serif;font-weight:600;font-size:76px;line-height:1.1;letter-spacing:-.01em}}
.mid em{{font-style:italic;font-weight:500}}
.sub{{font-size:42px;line-height:1.4;margin-top:34px}}
.logo{{width:130px;height:130px;border-radius:34px}}
.cta{{margin-top:46px;display:inline-block;font-weight:800;font-size:44px;padding:30px 52px;border-radius:14px}}
.fine{{font-size:25px;line-height:1.45;margin-top:40px}}
'''
def end_card(t, d, dark, headline, sub):
    c = '#F5EFE4' if dark else 'var(--ink)'
    em = 'var(--gold-soft)' if dark else 'var(--green)'
    m = 'rgba(250,247,241,.85)' if dark else 'var(--ink-2)'
    cta = 'background:var(--gold);color:var(--ink)' if dark else 'background:var(--green);color:#fff'
    return f'''<div class="sc" style="--a:hold;--t:{t}s;--d:{d}s;color:{c}"><img class="logo" src="file://{SK}/assets/logo-mark.png" alt=""><div class="mid" style="margin-top:46px">{headline.replace('<em>', f'<em style="color:{em}">')}</div><div class="sub" style="color:{m}">{sub}</div><div class="cta" style="{cta}">shprehu.cc</div><div class="fine" style="color:{m}">Shprehu nuk është shërbim urgjence.<br>Në rrezik, telefono 112.</div></div>'''
