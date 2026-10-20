from pathlib import Path
import json,html
p=Path(__file__).resolve().parents[1]
timing=json.loads((p/'timing.json').read_text());cues={x['key']:x for s in timing for x in s['phrases']}
css='''@font-face{font-family:Brand;src:url(assets/brand-regular.ttf)}@font-face{font-family:Brand;src:url(assets/brand-bold.ttf);font-weight:700}@font-face{font-family:Data;src:url(assets/data-bold.ttf);font-weight:700}*{box-sizing:border-box;margin:0}html,body{width:1920px;height:1080px;overflow:hidden;background:#031425;color:#f3f8ff;font-family:Brand,Arial,sans-serif}#root{width:1920px;height:1080px;position:relative;perspective:1600px}.scene{position:absolute;inset:0;background:#031425;width:100%;height:100%;overflow:hidden;transform-origin:center center}.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transform-origin:60% 64%}.shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(3,20,37,.37),rgba(3,20,37,0) 72%)}.floor-shade{position:absolute;inset:0;background:linear-gradient(0deg,rgba(3,20,37,.94),rgba(3,20,37,0) 30%)}.scene-content{position:relative;width:100%;height:100%;padding:95px 102px 160px;display:flex;flex-direction:column;gap:24px}.brand-group{display:flex;flex-direction:column;gap:7px;align-items:flex-start}.wordmark{font-size:145px;line-height:1;letter-spacing:4px;font-weight:700;position:relative}.motors{font-size:46px;letter-spacing:22px;line-height:1.25;margin-left:6px}.brand-clip{position:relative;overflow:hidden;padding:10px 3px}.brand-light{position:absolute;inset:0;width:120px;background:linear-gradient(100deg,rgba(255,255,255,0),rgba(255,255,255,.8),rgba(255,255,255,0));transform:skewX(-20deg);mix-blend-mode:screen;left:-180px;pointer-events:none}.accent{height:4px;width:80px;background:#76bfff;margin:8px 0 4px}.tagline{display:flex;flex-direction:column;gap:9px;font-size:34px;line-height:1.15;letter-spacing:2px;font-weight:400;max-width:1100px}.line-mask{overflow:hidden;padding:2px}.services{display:flex;align-items:stretch;gap:0;width:1260px;margin-top:auto;min-height:115px}.service{width:315px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;position:relative}.service:not(:last-child){border-right:1px solid rgba(193,213,234,.28)}.service svg{width:70px;height:58px;overflow:visible}.service span{font-size:25px;letter-spacing:1px;font-weight:700;line-height:1.3}.service-glow{position:absolute;width:220px;height:140px;border-radius:50%;background:radial-gradient(ellipse,rgba(150,211,255,.3),rgba(150,211,255,0) 65%);pointer-events:none}.small-logo{font-size:36px;letter-spacing:2px;font-weight:700;line-height:1.05}.small-logo small{display:block;font-size:15px;letter-spacing:8px;margin-top:5px;font-weight:400}.global-content{padding-top:66px;gap:0}.global-copy{display:flex;flex-direction:column;gap:12px;margin-top:76px;width:620px}.global-copy h2{font-size:98px;line-height:1.08;letter-spacing:-3px;font-weight:700;max-width:680px;perspective:1000px}.global-copy h2 .title-line{display:block;transform-origin:0 90%}.global-copy h2 .blue{color:#96d3ff}.global-copy p{font-size:27px;line-height:1.35;letter-spacing:1px;max-width:580px}.globe-shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(3,20,37,.97),rgba(3,20,37,.6) 28%,rgba(3,20,37,0) 53%)}.data-floor{position:absolute;left:0;right:0;bottom:0;height:390px;background:linear-gradient(0deg,#031425 25%,rgba(3,20,37,.94) 58%,rgba(3,20,37,0))}.stats{margin-top:auto;display:flex;align-items:stretch;width:1716px;height:145px;flex-shrink:0}.stat{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;width:286px}.stat:not(:last-child){border-right:1px solid rgba(150,211,255,.25)}.stat-value{height:72px;display:flex;justify-content:center;align-items:center;color:#96d3ff;font-family:Data,monospace;font-weight:700;font-size:59px;letter-spacing:-4px;line-height:72px;font-variant-numeric:tabular-nums;white-space:nowrap}.stat:last-child .stat-value{font-size:48px;letter-spacing:-4px}.stat-label{font-size:19px;line-height:1.3;letter-spacing:.6px;font-weight:700;text-align:center;max-width:265px}.digit-window{display:inline-block;position:relative;width:.61em;height:72px;overflow:hidden}.digit-strip{display:flex;flex-direction:column;position:relative;will-change:transform}.digit-strip span{display:block;height:72px;line-height:72px;flex-shrink:0;text-align:center}.fixed{display:inline-block}.stat-halo{position:absolute;inset:-25px -10px;background:radial-gradient(ellipse,rgba(150,211,255,.28),rgba(150,211,255,0) 65%);border-radius:50%;pointer-events:none}.routes{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}.route{fill:none;stroke:#f5cba3;stroke-width:2.2;stroke-linecap:round}.route-light{fill:#fff2dc;filter:drop-shadow(0 0 7px #f5cba3)}.node{fill:#f5cba3}.caption{position:absolute;bottom:35px;left:180px;right:180px;height:61px;display:flex;align-items:center;justify-content:center;text-align:center;color:#f3f8ff;font-size:26px;line-height:1.35;z-index:50;background:rgba(3,20,37,.8);border:1px solid rgba(193,213,234,.12);border-radius:10px;padding:7px 25px}.global-sweep{position:absolute;top:15px;bottom:15px;left:-180px;width:100px;background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.5),rgba(255,255,255,0));transform:skewX(-22deg);mix-blend-mode:screen}.title-mask{position:relative;overflow:hidden}.tiny-rule{height:2px;width:55px;background:#76bfff;margin:16px 0 10px}'''
car='<path d="M8 36l6-15h40l8 15M4 36h62v15H4zM18 21l5-10h25l6 10"/><circle cx="17" cy="51" r="5"/><circle cx="54" cy="51" r="5"/><path d="M11 40h9m31 0h9"/>'
used='<path d="M8 36l7-14h39l8 14M4 36h62v15H4zM17 22l6-11h24l7 11"/><circle cx="17" cy="51" r="5"/><circle cx="54" cy="51" r="5"/><path d="M27 40l6 6 12-13"/>'
ev='<rect x="9" y="15" width="49" height="35" rx="4"/><path d="M58 26h6v13h-6M36 18l-8 15h10l-8 15M20 8v7m27-7v7"/>'
gear='<path d="M31 7h10l2 8 7 3 7-4 7 8-5 7 1 7 7 5-4 10-9-1-5 5-1 9H36l-3-8-7-3-8 3-7-8 5-7-1-8-7-5 4-9 9 1 6-5z"/><circle cx="37" cy="35" r="10"/>'
services=[('new','NEW CARS',car),('used','USED CARS',used),('electric','EV & PHEV',ev),('parts','AUTO PARTS',gear)]
parts=[f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=1920,height=1080"><title>UNILAND · Global Vehicle Partner</title><script src="assets/gsap.min.js"></script><style>{css}</style></head><body><div id="root" data-composition-id="main" data-start="0" data-duration="25" data-width="1920" data-height="1080" data-fps="30">']
parts.append('<section id="cover" class="clip scene" data-start="0" data-duration="15.85" data-track-index="1"><img class="bg hero-bg" src="assets/hero-clean.png" alt="Vehicle lineup beside a coastal city skyline, reconstructed from the supplied keyframe"><div class="shade" data-layout-ignore></div><div class="floor-shade" data-layout-ignore></div><div class="scene-content" data-layout-allow-overlap data-layout-allow-occlusion><div class="brand-group"><div class="brand-clip"><h1 class="wordmark">UNILAND</h1><div class="brand-light" data-layout-ignore></div></div><div class="motors">MOTORS</div></div><div class="accent" data-layout-ignore></div><div class="tagline"><div class="line-mask"><div class="tag-line">YOUR GLOBAL VEHICLE</div></div><div class="line-mask"><div class="tag-line">SOURCING &amp; EXPORT PARTNER</div></div></div><div class="services">')
for i,(key,label,svg) in enumerate(services):
    parts.append(f'<div id="service-{key}" class="service"><div class="service-glow" data-layout-ignore></div><svg viewBox="0 0 76 74" fill="none" stroke="#f3f8ff" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true">{svg}</svg><span>{label}</span></div>')
parts.append('</div></div></section>')
parts.append('<section id="global" class="clip scene" data-start="15" data-duration="10" data-track-index="2" style="z-index:2"><img class="bg globe-bg" src="assets/globe-clean.png" alt="Earth at night with global connections"><div class="globe-shade" data-layout-ignore></div><svg class="routes" viewBox="0 0 1920 1080" aria-hidden="true" data-layout-ignore>')
origin=(1620,345); ends=[(780,320),(1250,240),(1230,540),(850,610),(1740,625),(1495,465)]
paths=[]
for i,(x,y) in enumerate(ends):
    cx=(origin[0]+x)/2; cy=min(origin[1],y)-(170 if i in (0,1,3) else 105)
    d=f'M {origin[0]} {origin[1]} Q {cx} {cy} {x} {y}'
    paths.append(d)
    parts.append(f'<path id="route-{i}" class="route" d="{d}"/><circle id="node-{i}" class="node" cx="{x}" cy="{y}" r="4"/><circle id="runner-{i}" class="route-light" r="4"/>')
parts.append(f'<circle class="origin" cx="1620" cy="345" r="8" fill="#fff2dc" style="filter:drop-shadow(0 0 15px #f5cba3)"/></svg><div class="data-floor" data-layout-ignore></div><div class="scene-content global-content" data-layout-allow-overlap data-layout-allow-occlusion><div class="small-logo">UNILAND<small>MOTORS</small></div><div class="global-copy"><div class="title-mask"><h2><span class="title-line">GLOBAL</span><span class="title-line blue">FOOTPRINT</span></h2><div class="global-sweep" data-layout-ignore></div></div><div class="tiny-rule" data-layout-ignore></div><p class="mission">BRING CHINESE VEHICLES<br>TO THE WORLD</p></div><div class="stats">')
stats=[('10,000+','VEHICLES DELIVERED','delivered'),('300+','DEALERS','dealers'),('40+','COUNTRIES','countries'),('30+','BRANDS',None),('5','PORT WAREHOUSES',None),('20,000+','m² WAREHOUSE AREA',None)]
reels=[]
for i,(value,label,key) in enumerate(stats):
    parts.append(f'<div id="stat-{i}" class="stat"><div class="stat-halo" data-layout-ignore></div><div class="stat-value" aria-label="{value}">')
    for j,ch in enumerate(value):
        if ch.isdigit():
            target=10+int(ch);seq=[str(k%10) for k in range(target+1)];id=f'reel-{i}-{j}'
            parts.append(f'<span class="digit-window" data-layout-allow-overflow data-layout-allow-occlusion><span id="{id}" class="digit-strip" data-layout-allow-overflow data-layout-allow-occlusion>'+''.join(f'<span>{x}</span>' for x in seq)+'</span></span>');reels.append((id,target,i,j))
        else:parts.append(f'<span class="fixed">{ch}</span>')
    parts.append(f'</div><div class="stat-label">{label}</div></div>')
parts.append('</div></div></section><audio id="voice" src="assets/narration-master.wav" data-start="0" data-duration="25" data-track-index="4" data-volume="1"></audio>')
an=[]
an.append('tl.from("#cover",{opacity:0,scale:1.025,duration:1.1,ease:"sine.out"},.1);')
an.append('tl.to(".hero-bg",{scale:1.045,x:-12,y:4,duration:15.85,ease:"none"},0);')
an.append('tl.from(".wordmark",{clipPath:"inset(0 100% 0 0)",y:24,opacity:0,duration:1.8,ease:"power3.out"},.35);')
an.append('tl.from(".motors",{x:-22,opacity:0,y:10,duration:1.5,ease:"sine.out"},.8);')
an.append('tl.to(".brand-light",{x:1160,duration:2.1,ease:"sine.inOut"},1.1);')
an.append('tl.from(".accent",{scaleX:0,transformOrigin:"0 50%",duration:.8,ease:"expo.out"},1.8);')
an.append(f'tl.from(".tag-line",{{yPercent:110,opacity:0,stagger:.24,duration:1,ease:"power3.out"}},{cues["partner"]["start"]-.2});')
for i,(key,label,svg) in enumerate(services):
    t=cues[key]['start']-.22
    an.append(f'tl.from("#service-{key}",{{y:28,scale:.87,opacity:0,rotationX:15,duration:.9,ease:"back.out(1.15)"}},{t});')
    an.append(f'tl.from("#service-{key} svg path,#service-{key} svg rect",{{strokeDashoffset:180,strokeDasharray:180,duration:1,ease:"power2.out"}},{t+.1});')
    an.append(f'tl.fromTo("#service-{key} .service-glow",{{opacity:0,scale:.5}},{{opacity:.9,scale:1.15,duration:.7,repeat:1,yoyo:true,ease:"sine.inOut"}},{t+.15});')
an.append('tl.from("#global",{opacity:0,z:230,rotationX:3,x:35,duration:.85,ease:"sine.inOut"},15);')
an.append('tl.to(".globe-bg",{scale:1.035,x:-9,y:5,duration:10,ease:"none"},15);')
an.append('tl.from(".small-logo",{opacity:0,y:10,duration:.6,ease:"power2.out"},15.15);')
an.append('tl.from(".title-line",{rotationX:38,transformOrigin:"0 90%",y:22,opacity:0,stagger:.16,duration:1.1,ease:"expo.out"},15.25);')
an.append('tl.to(".global-sweep",{x:980,duration:1.8,ease:"sine.inOut"},15.8);')
an.append('tl.from(".tiny-rule",{scaleX:0,transformOrigin:"0 50%",duration:.6,ease:"power2.out"},16.2);')
an.append('tl.from(".mission",{opacity:0,y:16,duration:1,ease:"sine.out"},22.1);')
# Flight-path drawing and moving points are deterministic visual SVG transforms.
for i,d in enumerate(paths):
    t=15.6+i*.43
    an.append(f'{{const el=document.querySelector("#route-{i}"),n=el.getTotalLength();tl.fromTo(el,{{strokeDasharray:n,strokeDashoffset:n,opacity:0}},{{strokeDashoffset:0,opacity:.9,duration:1.7,ease:"power2.inOut"}},{t});tl.from("#node-{i}",{{scale:0,opacity:0,transformOrigin:"50% 50%",duration:.6,ease:"back.out(1.2)"}},{t+1.5});const runner=document.querySelector("#runner-{i}");const frames=[];for(let k=0;k<=40;k++){{const pt=el.getPointAtLength(n*k/40);frames.push({{x:pt.x,y:pt.y,duration:1.7/41,ease:"none"}})}}tl.from(runner,{{opacity:0,duration:.1}},{t});tl.to(runner,{{keyframes:frames,ease:"none"}},{t});}}')
an.append('tl.from(".origin",{scale:0,opacity:0,transformOrigin:"50% 50%",duration:.8,ease:"power2.out"},15.4);')
stat_times=[15.55,17.65,19.55,20.45,21.0,21.55]
for i,t in enumerate(stat_times):
    an.append(f'tl.from("#stat-{i}",{{y:26,opacity:0,duration:.65,ease:"power3.out"}},{t});')
    an.append(f'tl.fromTo("#stat-{i} .stat-halo",{{opacity:0,scale:.6}},{{opacity:.9,scale:1.2,duration:.6,repeat:1,yoyo:true,ease:"sine.inOut"}},{t+.75});')
for id,target,i,j in reels:
    t=stat_times[i]+.1+j*.035
    an.append(f'tl.to("#{id}",{{y:{-72*target},duration:1.05,ease:"power3.out"}},{t});')
# Phrase captions use boundaries measured from separately synthesized utterances.
transcript=[]
for si,s in enumerate(timing):
    for j,c in enumerate(s['phrases']):
        id=f'cap-{si}-{j}';a=c['start'];dur=c['end']-a
        parts.append(f'<div id="{id}" class="clip caption" data-start="{a:.4f}" data-duration="{dur:.4f}" data-track-index="5">{html.escape(c["text"])}</div>')
        an.append(f'tl.from("#{id}",{{opacity:0,y:5,duration:.18,ease:"sine.out"}},{a:.4f});')
        transcript.append(c)
parts.append('<audio id="ambience" src="assets/ambience.wav" data-start="0" data-duration="25" data-track-index="6" data-volume="1"></audio>')
parts.append('<script>window.__timelines=window.__timelines||{};const tl=gsap.timeline({paused:true});'+''.join(an)+'window.__timelines.main=tl;</script></div></body></html>')
(p/'index.html').write_text(''.join(parts))
def stamp(v):
    ms=round(v*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(p/'subtitles.srt').write_text('\n\n'.join(f'{i+1}\n{stamp(c["start"])} --> {stamp(c["end"])}\n{c["text"]}' for i,c in enumerate(transcript))+'\n')
(p/'transcript.json').write_text(json.dumps({'alignment':'measured synthesized phrase timing','phrases':transcript},indent=2))
print('Built 25-second cover + footprint composition with narration-linked services and stat odometers.')
