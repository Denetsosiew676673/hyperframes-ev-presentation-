"""Compile editable slide content and measured audio timings into HyperFrames HTML."""
from pathlib import Path
import json, html
p=Path(__file__).resolve().parents[1]; slides=json.loads((p/'content.json').read_text()); timing=json.loads((p/'schedule.json').read_text())
esc=html.escape; total=sum(x['duration'] for x in timing)
css='''*{box-sizing:border-box;margin:0}html,body{width:1920px;height:1080px;overflow:hidden;background:#f5f5f7;font-family:Arial,Helvetica,sans-serif;color:#1d1d1f}#root{width:1920px;height:1080px;position:relative;perspective:1800px}.clip.scene{position:absolute;inset:0;width:100%;height:100%;background:#f5f5f7;transform-origin:50% 50%;overflow:hidden}.scene-content{width:100%;height:100%;padding:82px 112px 170px;display:flex;flex-direction:column;gap:32px}.mast{display:flex;justify-content:space-between;align-items:center;font-size:20px;letter-spacing:3px;color:#626773}.brand{font-size:23px;font-weight:700;letter-spacing:5px;color:#245bb2}.eyebrow{font-size:21px;letter-spacing:4px;color:#245bb2;font-weight:700;margin-top:48px}.heading{position:relative;max-width:1660px;overflow:hidden}h1{font-size:102px;line-height:1.04;font-weight:500;letter-spacing:-5px}.sweep{position:absolute;inset:-25% auto -25% -30%;width:160px;transform:skewX(-18deg);background:linear-gradient(90deg,transparent,rgba(255,255,255,.88),transparent);pointer-events:none}.intro{font-size:29px;color:#626773;line-height:1.45;max-width:1400px}.cards{display:flex;gap:25px;flex:1;align-items:stretch;margin-top:22px;min-height:280px;max-height:370px}.card{flex:1;border:1px solid #fff;border-radius:30px;padding:36px;background:rgba(255,255,255,.77);box-shadow:0 22px 55px rgba(49,58,76,.065),inset 0 1px 0 #fff;display:flex;flex-direction:column;gap:20px;backdrop-filter:blur(16px)}.value{font-size:68px;line-height:1.05;letter-spacing:-3px;color:#245bb2;font-variant-numeric:tabular-nums;font-weight:500}.card h2{font-size:27px;line-height:1.25;font-weight:500;max-width:100%}.card p{font-size:23px;line-height:1.45;color:#626773}.hero .value{font-size:88px}.footer{font-size:18px;letter-spacing:2px;color:#626773;display:flex;justify-content:space-between;margin-top:auto;padding-top:16px}.caption{position:absolute;bottom:44px;left:160px;right:160px;height:76px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:27px;line-height:1.35;color:#1d1d1f;z-index:100;background:rgba(255,255,255,.9);border-radius:18px;padding:12px 32px}.orb{position:absolute;width:1100px;height:1100px;right:-450px;top:-570px;border-radius:50%;background:radial-gradient(circle,rgba(130,169,224,.18),rgba(235,239,245,.3) 45%,transparent 68%);pointer-events:none}.line{position:absolute;height:1px;background:#d8dde5;bottom:142px;left:112px;right:112px}.photo{width:100%;height:100%;object-fit:contain}.photo-frame{overflow:hidden;border-radius:24px}'''
parts=['<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=1920,height=1080"><title>Uniland · Global Momentum</title><script src="assets/gsap.min.js"></script><style>'+css+'</style></head><body>',f'<div id="root" data-composition-id="main" data-start="0" data-duration="{total:.3f}" data-width="1920" data-height="1080">']
anim=[];captions=[];srt=[];ci=0
for i,(slide,t) in enumerate(zip(slides,timing)):
    start=t['start'];end=start+t['duration']; sid=f's{i}'; track=i+1
    # Overlap the outgoing frozen layer for the incoming 3D transition.
    duration=t['duration']+(.95 if i<len(slides)-1 else 0)
    parts.append(f'<section id="{sid}" class="clip scene {"hero" if i==0 else ""}" data-start="{start}" data-duration="{duration:.3f}" data-track-index="{track}" style="z-index:{i+1}"><div class="orb" data-layout-ignore></div><div class="scene-content" data-layout-allow-overlap data-layout-allow-occlusion><div class="mast"><span class="brand">UNILAND</span><span>GLOBAL MOMENTUM / {i+1:02d}</span></div><div class="eyebrow">{esc(slide["kicker"])}</div><div class="heading"><h1>{esc(slide["title"])}</h1><div class="sweep" data-layout-ignore></div></div><p class="intro">{esc(slide["sub"])}</p><div class="cards">')
    for c in slide['cards']:
        parts.append('<article class="card"><div class="value">'+esc(c[0])+'</div><h2>'+esc(c[1])+'</h2>'+(''.join('<p>'+esc(x)+'</p>' for x in c[2:]))+'</article>')
    parts.append(f'</div><div class="footer"><span>UNILAND MOTORS GROUP CO., LTD.</span><span>{i+1:02d} / 06</span></div></div><div class="line" data-layout-ignore></div></section>')
    parts.append(f'<audio id="voice{i}" data-start="{start}" data-duration="{t["duration"]}" data-track-index="20" src="assets/voice-{i+1}.wav" data-volume="1"></audio>')
    # Each layer is opaque, so its entrance is the scene transition; outgoing content remains intact.
    anim.append(f'tl.from("#{sid}",{{opacity:0,z:160,rotationY:-3.5,x:55,duration:.95,ease:"power2.inOut",immediateRender:false}},{start+.1});')
    for selector,vars,offset in [(' .mast','y:14,opacity:0,duration:.65,ease:"sine.out"',.28),(' .eyebrow','y:20,opacity:0,duration:.8,ease:"power2.out"',.42),(' h1','y:32,opacity:0,duration:1,ease:"expo.out"',.54),(' .intro','y:18,opacity:0,duration:.85,ease:"sine.out"',.8),(' .card','y:38,rotationX:5,opacity:0,duration:1,stagger:.18,ease:"power3.out"',1.0),(' .footer','opacity:0,duration:.8,ease:"sine.out"',1.4)]:
        anim.append(f'tl.from("#{sid}{selector}",{{{vars},immediateRender:false}},{start+offset});')
    anim.append(f'tl.from("#{sid} .card h2,#{sid} .card p",{{y:12,opacity:0,stagger:.18,duration:.7,ease:"power2.out",immediateRender:false}},{start+1.4});')
    anim.append(f'tl.to("#{sid} .sweep",{{x:2600,duration:2.1,ease:"sine.inOut"}},{start+1});')
    anim.append(f'tl.to("#{sid} .value",{{textShadow:"0 0 22px rgba(36,91,178,.35)",color:"#4179ca",duration:.75,stagger:.17,yoyo:true,repeat:1,ease:"sine.inOut"}},{start+2.5});')
    anim.append(f'tl.to("#{sid} .orb",{{x:-50,y:25,scale:1.08,duration:{t["duration"]},ease:"none"}},{start});')
    for c in t['captions']:
        # Phrase clips use sentence generation boundaries, then even word-weighted subdivision.
        words=c['text'].split(); groups=[words[j:j+9] for j in range(0,len(words),9)]; pos=c['start']; span=c['end']-c['start']
        for g in groups:
            text=' '.join(g); dur=span*len(g)/len(words); cid=f'caption{ci}'; ci+=1
            captions.append(f'<div id="{cid}" class="clip caption" data-start="{pos:.3f}" data-duration="{dur:.3f}" data-track-index="30">{esc(text)}</div>')
            anim.append(f'tl.from("#{cid}",{{opacity:0,y:5,duration:.15,ease:"sine.out",immediateRender:false}},{pos:.3f});')
            srt.append((pos,pos+dur,text));pos+=dur
parts+=captions
parts.append('</div><script>window.__timelines=window.__timelines||{};const tl=gsap.timeline({paused:true});'+''.join(anim)+'window.__timelines.main=tl;</script></body></html>')
(p/'index.html').write_text(''.join(parts))
def stamp(s):
    ms=round(s*1000);return f'{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}'
(p/'subtitles.srt').write_text('\n\n'.join(f'{i+1}\n{stamp(a)} --> {stamp(b)}\n{text}' for i,(a,b,text) in enumerate(srt))+'\n')
print(f'Built {len(slides)} scenes, {len(srt)} captions, {total:.2f} seconds')
