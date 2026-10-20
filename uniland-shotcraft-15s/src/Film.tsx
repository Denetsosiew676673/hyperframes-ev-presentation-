import React, {useEffect, useState} from 'react';
import {AbsoluteFill, Audio, Img, Sequence, staticFile, useCurrentFrame, useVideoConfig, interpolate, Easing, delayRender, continueRender} from 'remotion';
import {DigitRoll} from './lib/DigitRoll';
import voiceTiming from './timing.json';

export const TOTAL=450;
export const SHOTS={hero:{from:0,duration:177},reach:{from:165,duration:152},partner:{from:305,duration:145}} as const;
export const C={bg:'#031425',white:'#F3F8FF',blue:'#96D3FF',muted:'#C1D5EA',warm:'#F5CBA3'};
const clamp={extrapolateLeft:'clamp' as const,extrapolateRight:'clamp' as const};
const ramp=(f:number,a:number,d:number,easing=Easing.bezier(.2,.75,.3,1))=>interpolate(f,[a,a+d],[0,1],{...clamp,easing});
const railEase=Easing.bezier(.45,0,.18,1);
const easeOut=Easing.out(Easing.cubic);
const imgStyle:React.CSSProperties={width:'100%',height:'100%',objectFit:'cover',display:'block'};
export const HERO_DEFAULTS={brand:'UNILAND',subbrand:'MOTORS',line1:'YOUR GLOBAL VEHICLE',line2:'SOURCING & EXPORT PARTNER',color:C.white};
export const REACH_DEFAULTS={headline:'GLOBAL REACH',value:'10,000+',label:'VEHICLES DELIVERED',color:C.blue};
export const PARTNER_DEFAULTS={brand:'UNILAND MOTORS',cta:'LET’S BUILD YOUR NEXT PARTNERSHIP',url:'www.uniland-motors.com',color:C.white};

export const FontReady:React.FC=()=>{
 const [handle]=useState(()=>delayRender('Local brand fonts'));
 useEffect(()=>{Promise.all([new FontFace('Brand',`url(${staticFile('fonts/brand-regular.ttf')})`).load(),new FontFace('Brand',`url(${staticFile('fonts/brand-bold.ttf')})`,{weight:'700'}).load(),new FontFace('Data',`url(${staticFile('fonts/data-bold.ttf')})`,{weight:'700'}).load()]).then(fonts=>{fonts.forEach(f=>document.fonts.add(f));continueRender(handle)}).catch(()=>continueRender(handle));},[handle]);
 return null;
};

export const Hero:React.FC<Partial<typeof HERO_DEFAULTS>>=(props)=>{
 const d={...HERO_DEFAULTS,...props},f=useCurrentFrame();
 const drive=300*ramp(f,6,130,railEase)+4*ramp(f,136,29,Easing.inOut(Easing.cubic));
 const lift=ramp(f,122,22,easeOut);const h=ramp(f,4,32);
 return <AbsoluteFill style={{background:C.bg,overflow:'hidden',fontFamily:'Brand'}}>
  <AbsoluteFill style={{opacity:.48,transform:`translateX(${-drive*.35}px)`,filter:'blur(5px) saturate(.7)'}}><Img src={staticFile('images/hero.png')} style={{position:'absolute',left:-50,top:-80,width:2280,height:1283,objectFit:'cover'}}/></AbsoluteFill>
  <AbsoluteFill style={{background:'linear-gradient(90deg,rgba(3,20,37,.98),rgba(3,20,37,.83) 32%,rgba(3,20,37,.2) 80%)'}}/>
  <div style={{position:'absolute',left:900-drive*.7,top:165-14*lift,width:1100,height:619,transform:`scale(${1+.035*lift})`,borderRadius:22,overflow:'hidden',border:`1px solid rgba(150,211,255,${.24+.4*lift})`,boxShadow:`0 ${20+15*lift}px ${60+20*lift}px rgba(0,0,0,.45)`,opacity:ramp(f,0,25)}}><Img src={staticFile('images/hero.png')} style={imgStyle}/><div style={{position:'absolute',inset:0,borderRadius:22,boxShadow:'inset 0 1px 0 rgba(255,255,255,.35)'}}/></div>
  <div style={{position:'absolute',left:1910-drive*1.4,top:55,width:190,height:900,background:'linear-gradient(90deg,rgba(150,211,255,0),rgba(150,211,255,.15),rgba(150,211,255,0))',filter:'blur(7px)',transform:'rotate(-15deg)'}}/>
  <div style={{position:'absolute',left:96,top:85,fontSize:44,letterSpacing:5,color:C.blue,opacity:h}}>GLOBAL VEHICLE PARTNER</div>
  <div style={{position:'absolute',left:91,top:240,color:d.color,opacity:h,transform:`translateY(${24*(1-h)}px)`}}>
   <div style={{fontSize:100,fontWeight:700,letterSpacing:-3,lineHeight:1.08}}>{d.brand}</div><div style={{fontSize:55,letterSpacing:20,marginTop:8}}>{d.subbrand}</div>
   <div style={{height:3,width:96,background:C.blue,marginTop:36,transform:`scaleX(${ramp(f,26,24)})`,transformOrigin:'left'}}/>
   <div style={{fontSize:44,lineHeight:1.45,letterSpacing:.2,marginTop:28,maxWidth:550,opacity:ramp(f,28,24)}}>{d.line1}<div>{d.line2}</div></div>
  </div>
  <div style={{position:'absolute',left:96,right:96,top:847,display:'flex',gap:18,opacity:ramp(f,40,24),transform:`translateY(${18*(1-ramp(f,40,24))}px)`}}>
   {['NEW CARS','USED CARS','EV & PHEV','AUTO PARTS'].map((s)=><div key={s} style={{flex:1,fontSize:44,fontWeight:700,letterSpacing:.4,padding:'20px 18px',whiteSpace:'nowrap',borderTop:'1px solid #96d3ff66',color:C.white}}>{s}</div>)}
  </div>
 </AbsoluteFill>
};

type Pt={x:number;y:number};
const bez=(a:Pt,b:Pt,c:Pt,d:Pt,t:number):Pt=>{const u=1-t;return{x:u*u*u*a.x+3*u*u*t*b.x+3*u*t*t*c.x+t*t*t*d.x,y:u*u*u*a.y+3*u*u*t*b.y+3*u*t*t*c.y+t*t*t*d.y}};
const Flight:React.FC<{frame:number;start:number;points:[Pt,Pt,Pt,Pt];id:string}>=({frame,start,points,id})=>{
 if(frame<start)return null;
 const progress=ramp(frame,start,22,easeOut),settle=ramp(frame,start+22,10,Easing.out(Easing.quad));
 const growing=frame<start+22,n=Math.max(2,Math.ceil(progress*100)+1);
 const pts=Array.from({length:n},(_,i)=>bez(...points,Math.min(i/100,progress)));pts[n-1]=bez(...points,progress);
 const head=pts[n-1],poly=pts.map(p=>`${p.x},${p.y}`).join(' ');const end=points[3];const pulse=frame<start+22?0:frame<=start+28?ramp(frame,start+22,6,easeOut):1-.75*ramp(frame,start+28,12,Easing.out(Easing.quad));
 return <g><defs><radialGradient id={id}><stop offset="0" stopColor="#fff" stopOpacity=".8"/><stop offset=".3" stopColor={C.blue} stopOpacity=".5"/><stop offset="1" stopColor={C.blue} stopOpacity="0"/></radialGradient></defs>
  <polyline points={poly} fill="none" stroke={C.blue} strokeWidth={18} strokeOpacity={.1+.04*settle}/><polyline points={poly} fill="none" stroke={C.blue} strokeWidth={7} strokeOpacity={.24}/>
  {pts.slice(0,-1).map((p,i)=><line key={i} x1={p.x} y1={p.y} x2={pts[i+1].x} y2={pts[i+1].y} stroke={C.white} strokeWidth={3.5} strokeLinecap="butt" opacity={.3+.7*(i/Math.max(1,pts.length-2))**2+(1-(.3+.7*(i/Math.max(1,pts.length-2))**2))*settle}/>)}
  <circle cx={points[0].x} cy={points[0].y} r={5} fill={C.white}/>
  {growing?<g><polyline points={pts.slice(-9).map(p=>`${p.x},${p.y}`).join(' ')} fill="none" stroke="white" strokeWidth={6}/><circle cx={head.x} cy={head.y} r={40} fill={`url(#${id})`}/><circle cx={head.x} cy={head.y} r={7} fill="white"/></g>:<g><circle cx={end.x} cy={end.y} r={13} fill={C.blue} fillOpacity={.2}/><circle cx={end.x} cy={end.y} r={5} fill="white"/>{frame<start+36?<circle cx={end.x} cy={end.y} r={12+65*ramp(frame,start+22,14,easeOut)} fill="none" stroke={C.blue} strokeWidth={2} opacity={.6*(1-ramp(frame,start+22,14,easeOut))}/>:null}<circle cx={end.x} cy={end.y} r={20} fill={C.blue} opacity={.12*pulse}/></g>}
 </g>;
};
export const Reach:React.FC<Partial<typeof REACH_DEFAULTS>>=(props)=>{
 const d={...REACH_DEFAULTS,...props},f=useCurrentFrame();
 const enter=ramp(f,0,20);return <AbsoluteFill style={{background:C.bg,overflow:'hidden',fontFamily:'Brand',opacity:ramp(f,0,12)}}>
 <Img src={staticFile('images/globe.png')} style={{...imgStyle,position:'absolute',inset:0}}/>
 <AbsoluteFill style={{background:'linear-gradient(90deg,rgba(3,20,37,.98),rgba(3,20,37,.85) 32%,rgba(3,20,37,.04) 80%)'}}/>
 <svg viewBox="0 0 1920 1080" style={{position:'absolute',inset:0,width:1920,height:1080}}><Flight frame={f} start={10} id="route-a" points={[{x:1620,y:345},{x:1440,y:110},{x:980,y:120},{x:785,y:320}]}/><Flight frame={f} start={46} id="route-b" points={[{x:1620,y:345},{x:1500,y:130},{x:1340,y:150},{x:1250,y:240}]}/></svg>
 <div style={{position:'absolute',left:96,top:85,fontSize:44,letterSpacing:4,color:C.muted,opacity:enter}}>{d.headline}</div>
 <div style={{position:'absolute',left:90,top:250,color:d.color,opacity:enter,transform:`translateY(${28*(1-enter)}px)`}}>
  <div style={{fontFamily:'Data',fontSize:164,fontWeight:700,letterSpacing:-10}}><DigitRoll value={d.value} delay={6} fontSize={164} color={d.color}/></div>
  <div style={{fontSize:44,fontWeight:700,letterSpacing:2,marginTop:12,color:C.white}}>{d.label}</div>
 </div>
 <div style={{position:'absolute',left:100,top:630,display:'flex',gap:80,color:C.white,opacity:ramp(f,42,24)}}>{[['300+','DEALERS'],['40+','COUNTRIES']].map(([value,label])=><div key={label}><div style={{fontFamily:'Data',fontWeight:700,fontSize:77,color:C.blue}}>{value}</div><div style={{fontSize:44,marginTop:10,letterSpacing:2}}>{label}</div></div>)}</div>
 </AbsoluteFill>
};

const finaleItems=[
 {text:'NEW CARS',image:'hero',x:180,y:110,w:480,h:230,dx:-500,dy:-220,rot:-4,cue:4},
 {text:'USED VEHICLES',image:'hero',x:1260,y:110,w:470,h:230,dx:500,dy:-210,rot:4,cue:7},
 {text:'EV & PHEV',image:'hero',x:100,y:740,w:430,h:180,dx:-400,dy:300,rot:3,cue:10},
 {text:'AUTO PARTS',image:null,x:1320,y:760,w:470,h:130,dx:450,dy:280,rot:-3,cue:13},
 {text:'GLOBAL NETWORK',image:'globe',x:720,y:70,w:500,h:190,dx:0,dy:-300,rot:1.5,cue:16},
 {text:'10,000+ DELIVERED',image:null,x:650,y:800,w:620,h:100,dx:0,dy:320,rot:-1,cue:19},
] as const;
export const Partner:React.FC<Partial<typeof PARTNER_DEFAULTS>>=(props)=>{
 const d={...PARTNER_DEFAULTS,...props},f=useCurrentFrame();const crane=ramp(f,0,40,Easing.bezier(.3,0,.2,1)),push=ramp(f,36,109,Easing.inOut(Easing.cubic));const recede=ramp(f,42,8);const stage=interpolate(f,[42,50,58],[0,.5,.28],clamp);
 return <AbsoluteFill style={{background:C.bg,overflow:'hidden',fontFamily:'Brand',opacity:ramp(f,0,12)}}>
  <Img src={staticFile('images/hero.png')} style={{...imgStyle,opacity:.12,filter:'blur(14px)'}}/>
  <AbsoluteFill style={{transform:`perspective(1400px) rotateX(${4*(1-crane)}deg) scale(${1.06-.06*crane+.035*push})`,transformOrigin:'50% 45%'}}>
   {finaleItems.map(el=>{if(f<el.cue)return null;const t=ramp(f,el.cue,12,Easing.bezier(.34,1.4,.44,1)),landing=interpolate(f,[el.cue+9,el.cue+12,el.cue+16],[0,1,0],clamp);const x=el.dx*(1-t),y=el.dy*(1-t);const prev=ramp(f-1,el.cue,12,Easing.bezier(.34,1.4,.44,1));const speed=Math.hypot(el.dx*(t-prev),el.dy*(t-prev));return <div key={el.text} style={{position:'absolute',left:el.x,top:el.y,width:el.w,height:el.h,borderRadius:20,overflow:'hidden',background:'#0c2941',border:'1px solid #96d3ff55',boxShadow:`0 ${10+26*Math.max(0,1-t)-5*landing}px ${24+46*Math.max(0,1-t)}px rgba(0,0,0,.45)`,transform:`translate(${x}px,${y}px) rotate(${el.rot*(2-t)}deg) scale(${(1.12-.12*t)*(1-.015*landing)})`,opacity:ramp(f,el.cue,3)*(1-.12*recede),filter:`saturate(${1-.08*recede}) blur(${Math.min(22,speed*.1)}px)`}}>
    {el.image?<Img src={staticFile(`images/${el.image}.png`)} style={{...imgStyle,opacity:.75}}/>:null}<div style={{position:'absolute',inset:0,background:el.image?'linear-gradient(0deg,rgba(3,20,37,.95),rgba(3,20,37,0) 80%)':'none'}}/><div style={{position:'absolute',left:24,right:20,bottom:23,fontSize:44,fontWeight:700,letterSpacing:1,color:C.white}}>{el.text}</div>
   </div>})}
  </AbsoluteFill>
  <AbsoluteFill style={{background:'radial-gradient(ellipse 740px 260px at 50% 49%,rgba(150,211,255,.85),rgba(150,211,255,0) 75%)',opacity:stage}}/>
  {Array.from({length:20},(_,i)=>{const y=(((i*613+271-f*(.3+(i%5)*.11))%1080)+1080)%1080;return <div key={i} style={{position:'absolute',left:(i*439+137)%1920+Math.sin(f*(.022+(i%3)*.008)+i*.83)*(9+i%4*5),top:y,width:2.4+i%3*.9,height:2.4+i%3*.9,borderRadius:'50%',background:C.blue,boxShadow:`0 0 10px ${C.blue}`,opacity:.35+((i*7)%5)*.07}}/>})}
  <div style={{position:'absolute',left:100,right:100,top:420,textAlign:'center',color:d.color}}>
   <div style={{fontSize:113,fontWeight:700,letterSpacing:-3,lineHeight:1.15,display:'flex',justifyContent:'center',whiteSpace:'pre',textShadow:'0 8px 30px #031425'}}>{d.brand.split('').map((ch,i)=>{const t=ramp(f,Math.round(42+i*1.8),8);return <span key={i} style={{display:'inline-block',opacity:t,transform:`translateY(${(1-t)*28}px) scale(${1.35-.35*t})`,filter:`blur(${(1-t)*8}px)`}}>{ch}</span>})}</div>
   <div style={{width:280,height:4,background:C.blue,margin:'26px auto',transform:`scaleX(${ramp(f,58,12,Easing.bezier(.3,0,.2,1))})`}}/>
   <div style={{fontSize:46,letterSpacing:1.2,color:C.muted,opacity:ramp(f,68,12)}}>{d.cta}</div>
   <div style={{fontSize:58,fontWeight:700,marginTop:23,color:C.white,opacity:ramp(f,75,14)}}>{d.url}</div>
  </div>
 </AbsoluteFill>
};

export const Caption:React.FC<{text:string;duration?:number}>=({text,duration=60})=>{const f=useCurrentFrame();return <AbsoluteFill style={{justifyContent:'flex-end',alignItems:'center',paddingBottom:24,pointerEvents:'none'}}><div style={{fontFamily:'Brand',fontSize:76,lineHeight:1.13,color:C.white,textAlign:'center',padding:'10px 28px',maxWidth:1760,background:'rgba(3,20,37,.93)',borderRadius:12,opacity:ramp(f,0,5)*(1-ramp(f,duration-5,5))}}>{text}</div></AbsoluteFill>};
// Split captions into measured phrase windows; short groups remain readable at76px.
const phraseGroups:Record<string,string[]>={brand:['Uniland Motors.'],offer:['New, used, and electric vehicles.'],proof:['Over ten thousand','vehicles delivered.'],reach:['Global reach.'],cta:['Start your next business partnership','with Uniland Motors today.']};
export const CAPTIONS=voiceTiming.flatMap((p)=>{const groups=phraseGroups[p.key]??[p.text];return groups.map((text,i)=>({id:`${p.key}-${i}`,from:Math.round((p.start+(p.end-p.start)*i/groups.length)*30),duration:Math.round((p.end-p.start)/groups.length*30),text}));});
export const SFX=[
 {id:'enter',from:SHOTS.hero.from+5,duration:38,src:'audio/transition.mp3',volume:.11},
 {id:'reach',from:SHOTS.reach.from,duration:38,src:'audio/transition.mp3',volume:.13},
 {id:'node1',from:SHOTS.reach.from+16,duration:30,src:'audio/impact.mp3',volume:.045},
 {id:'node2',from:SHOTS.reach.from+52,duration:30,src:'audio/impact.mp3',volume:.035},
 {id:'riser',from:SHOTS.partner.from+1,duration:47,src:'audio/riser.wav',volume:.3},
 {id:'stamp',from:SHOTS.partner.from+56,duration:60,src:'audio/impact.mp3',volume:.18},
 {id:'rule',from:SHOTS.partner.from+60,duration:60,src:'audio/shimmer.mp3',volume:.07},
];
export const Film:React.FC=()=>{const {fps}=useVideoConfig();return <AbsoluteFill style={{background:C.bg}}><FontReady/>
 <Sequence from={SHOTS.hero.from} durationInFrames={SHOTS.hero.duration} premountFor={fps}><Hero/></Sequence>
 <Sequence from={SHOTS.reach.from} durationInFrames={SHOTS.reach.duration} premountFor={fps}><Reach/></Sequence>
 <Sequence from={SHOTS.partner.from} durationInFrames={SHOTS.partner.duration} premountFor={fps}><Partner/></Sequence>
 {CAPTIONS.map(c=><Sequence key={c.id} from={c.from} durationInFrames={c.duration} premountFor={fps}><Caption text={c.text} duration={c.duration}/></Sequence>)}
 <Audio src={staticFile('audio/voice-master.wav')} volume={1}/>
 {SFX.map(s=><Sequence key={s.id} from={s.from} durationInFrames={s.duration} premountFor={fps}><Audio src={staticFile(s.src)} volume={s.volume}/></Sequence>)}
 </AbsoluteFill>};
