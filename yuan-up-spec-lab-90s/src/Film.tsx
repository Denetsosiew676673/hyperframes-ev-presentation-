import {AbsoluteFill,Audio,Sequence,staticFile,useCurrentFrame} from 'remotion';
import {Scene,SHOTS} from './Scenes';
import {SeriesTitle} from './SeriesTitle';
import {C} from './graphics';
import captions from './captions.json';
export const TOTAL=2700;
export const Fonts=()=> <style>{`@font-face{font-family:Display;src:url('${staticFile('fonts/display-light.ttf')}');font-weight:300}@font-face{font-family:Display;src:url('${staticFile('fonts/display-regular.ttf')}');font-weight:400}@font-face{font-family:Display;src:url('${staticFile('fonts/display-semibold.ttf')}');font-weight:600}@font-face{font-family:Data;src:url('${staticFile('fonts/data-bold.ttf')}');font-weight:700}`}</style>;
export const Header=()=>{const f=useCurrentFrame();return <><Fonts/><SeriesTitle/><div style={{position:'absolute',right:88,top:80,fontFamily:'Display',fontSize:27,letterSpacing:3,color:C.muted}}>MODEL INSIGHTS / 001</div><div style={{position:'absolute',left:88,right:88,top:144,height:1,background:C.line,opacity:.6}}/><div style={{position:'absolute',bottom:12,left:88,fontFamily:'Display',fontSize:24,color:C.muted}}>{f<2310?'CLTC lab figures · Specifications and equipment vary by market and trim.':'Availability and export eligibility subject to configuration and destination checks.'}</div></>};
export const Captions=()=>{const f=useCurrentFrame(),c=captions.find(c=>f/30>=c.start&&f/30<c.end);return c?<div style={{position:'absolute',left:88,right:88,top:897,minHeight:136,display:'flex',alignItems:'center',justifyContent:'center',fontFamily:'Display',fontSize:56,lineHeight:1.22,fontWeight:400,textAlign:'center',color:C.ink,background:C.bg,padding:'0 22px'}}>{c.text}</div>:null};
export const AUDIO=[{id:'voice',src:'audio/voice.wav',volume:1},{id:'keys',src:'audio/keys.wav',volume:1}];
export const Film=({bgm=true}:{bgm?:boolean})=> <AbsoluteFill style={{background:C.bg,color:C.ink,fontFamily:'Display'}}><Fonts/>
 {/* Authored scene nodes preserve independent editing in Studio. Shared data owns the time windows. */}
 <Sequence name="00:00 Opening — spotlight hero" from={SHOTS[0].from} durationInFrames={SHOTS[0].duration+12}><Scene index={0}/></Sequence>
 <Sequence name="00:11 Range and motor" from={SHOTS[1].from} durationInFrames={SHOTS[1].duration+12}><Scene index={1}/></Sequence>
 <Sequence name="00:24 Blade battery" from={SHOTS[2].from} durationInFrames={SHOTS[2].duration+12}><Scene index={2}/></Sequence>
 <Sequence name="00:36 DC charging" from={SHOTS[3].from} durationInFrames={SHOTS[3].duration+12}><Scene index={3}/></Sequence>
 <Sequence name="00:48 Cockpit and assistance" from={SHOTS[4].from} durationInFrames={SHOTS[4].duration+12}><Scene index={4}/></Sequence>
 <Sequence name="01:03 Space and wheelbase" from={SHOTS[5].from} durationInFrames={SHOTS[5].duration+12}><Scene index={5}/></Sequence>
 <Sequence name="01:17 Export and quotation" from={SHOTS[6].from} durationInFrames={SHOTS[6].duration}><Scene index={6}/></Sequence>
 <Header/><Captions/>
 {/* AUDIO PLACEHOLDERS: replace these WAVs for a different narrator or soundtrack. */}
 <Audio src={staticFile('audio/voice.wav')}/><Audio src={staticFile('audio/keys.wav')}/>{bgm&&<Audio src={staticFile('audio/bgm.wav')}/>}
 </AbsoluteFill>;
