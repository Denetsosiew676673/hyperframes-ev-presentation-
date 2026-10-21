import {chromium} from '/opt/codex/runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs';
import {resolve} from 'node:path';import {writeFileSync,mkdirSync} from 'node:fs';
const root=resolve(import.meta.dirname,'..');const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox','--autoplay-policy=no-user-gesture-required']});
const page=await browser.newPage({viewport:{width:1120,height:2160},deviceScaleFactor:1});const errors=[],requests=[];page.on('pageerror',e=>errors.push(e.message));page.on('request',r=>{if(/^https?:/.test(r.url())&&!r.url().startsWith('http://127.0.0.1:3035/'))requests.push(r.url());});
await page.goto('http://127.0.0.1:3035/index.html');await page.evaluate(()=>document.fonts.ready);await page.waitForFunction(()=>window.FILM&&document.getElementById('voice').readyState>=2);
// use full-resolution canvas while keeping standalone controls outside the capture
await page.evaluate(()=>{document.getElementById('composition').style.transform='none';Object.assign(document.getElementById('frame').style,{width:'1080px',height:'1920px'});});
const spec=await page.evaluate(()=>FILM.spec);let issues=[];const shots=[];
for(let i=0;i<10;i++){
 const start=spec.beats[i]*60/122,end=spec.beats[i+1]*60/122;
 const t=Math.min(end-.4,start+(i===9?2.8:Math.max(5,(end-start)*.77)));
 await page.evaluate(t=>FILM.seek(t),t);await page.waitForTimeout(30);
 const data=await page.evaluate(i=>{const s=document.getElementById('scene-'+i);const cap=document.getElementById('captions');const a=s.getBoundingClientRect(),c=cap.getBoundingClientRect();let out=[];for(const el of s.querySelectorAll('h1,.kicker,.label,.figure,.mega,.stack,.fund,.step,.brands,.lesson,.cta,.web,.source')){const b=el.getBoundingClientRect();if(b.left<a.left-1||b.right>a.right+1||b.bottom>a.bottom+1||el.scrollWidth>el.clientWidth+2)out.push({text:el.textContent,bbox:{x:b.x-a.x,y:b.y-a.y,w:b.width,h:b.height},scroll:el.scrollWidth,client:el.clientWidth});if(!el.classList.contains('source')&&b.bottom>c.top&&b.top<c.bottom)out.push({captionOverlap:el.textContent,bottom:b.bottom-a.y,captionTop:c.top-a.y});}return out;},i);
 issues.push(...data.map(x=>({scene:i+1,...x})));
 await page.locator('#composition').screenshot({path:root+`/previews/${String(i+1).padStart(2,'0')}.png`});shots.push({scene:i+1,time:t,frame:Math.round(t*30)});
}
// seeking backwards must exactly restore counters/captions/scene visibility
await page.evaluate(()=>FILM.seek(12));const a=await page.locator('#composition').screenshot();await page.evaluate(()=>FILM.seek(97));await page.evaluate(()=>FILM.seek(12));const b=await page.locator('#composition').screenshot();const deterministic=a.equals(b);
await page.locator('#play').click();await page.waitForTimeout(1300);const playback=await page.evaluate(()=>({voice:voice.currentTime,music:music.currentTime,timeline:__timelines['uniland-ev-finance'].time(),paused:voice.paused,musicPaused:music.paused}));await page.locator('#play').click();
await page.locator('#bgm').click();const noBgm=await page.evaluate(()=>music.volume===0);await page.locator('#mute').click();const muted=await page.evaluate(()=>voice.muted&&music.muted);
writeFileSync(root+'/review/browser-check.json',JSON.stringify({spec,errors,networkRequests:requests,issues,shots,deterministic,playback,noBgm,muted},null,2));console.log(JSON.stringify({errors,networkRequests:requests,issues,deterministic,playback,noBgm,muted},null,2));await browser.close();
