import sys
SK = '/home/user/Shprehu-3.5/.claude/skills/shprehu-social-ads'
W = 6480

HEAD = f'''<!doctype html><html lang="sq"><head><meta charset="utf-8"><link rel="stylesheet" href="file://{SK}/assets/brand.css"><style>
html,body{{margin:0;height:1920px;overflow:hidden;width:{W}px!important}}
.pano{{position:absolute;left:0;top:0;width:{W}px;height:1920px;overflow:hidden}}
.sl{{position:absolute;top:0;width:1080px;height:1920px;z-index:5}}
.hd{{position:absolute;left:96px;right:150px;top:250px}}
.k{{font-size:27px;font-weight:700;letter-spacing:.2em;text-transform:uppercase}}
.clock{{font-family:'Fraunces',serif;font-weight:500;font-style:italic;font-size:150px;line-height:1}}
.h{{font-family:'Fraunces',serif;font-weight:600;font-size:88px;line-height:1.06;letter-spacing:-.01em;margin-top:26px}}
.h em{{font-style:italic;font-weight:500}}
.sub{{font-size:40px;line-height:1.42;margin-top:30px}}
.hint{{position:absolute;left:96px;top:1330px;display:flex;gap:18px;align-items:center;font-size:32px;font-weight:600}}
.cta{{margin-top:50px;display:inline-block;background:var(--green);color:#fff;font-weight:800;font-size:44px;padding:30px 52px;border-radius:14px}}
.fine{{font-size:26px;line-height:1.45;margin-top:44px}}
.logo{{width:140px;height:140px;border-radius:36px}}
'''

def arrow(c):
    return f'<svg width="60" height="24" viewBox="0 0 60 24"><path d="M2 12h52M44 3l10 9-10 9" stroke="{c}" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def end_slide(i, theme, h, sub):
    c = 'var(--ink)' if theme == 'l' else '#F5EFE4'
    em = 'var(--green)' if theme == 'l' else 'var(--gold-soft)'
    m = 'var(--ink-2)' if theme == 'l' else 'rgba(250,247,241,.85)'
    ctast = '' if theme == 'l' else 'background:var(--gold);color:var(--ink)'
    return f'''<div class="sl" style="left:{i*1080}px"><div class="hd" style="color:{c}">
<img class="logo" src="file://{SK}/assets/logo-mark.png" alt="">
<div class="h" style="margin-top:50px">{h.replace('<em>', f'<em style="color:{em}">')}</div>
<div class="sub" style="color:{m}">{sub}</div>
<div class="cta" style="{ctast}">shprehu.cc</div>
<div class="fine" style="color:{m}">Shprehu nuk është shërbim urgjence.<br>Në rrezik, telefono 112.</div>
</div></div>'''
