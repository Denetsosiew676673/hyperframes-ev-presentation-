import {AbsoluteFill,Audio,Sequence,staticFile,useCurrentFrame} from 'remotion';
import {CONFIG,DEFAULT_PHOTOS,PhotoSet,SCENES} from './config';
import {CTAScene,SceneFrame} from './Scenes';
import captions from './captions.json';
type Caption={start:number;end:number;text:string};
export type FilmProps={photos?:PhotoSet;withAudio?:boolean;bgm?:boolean};
export const Fonts=()=> <style>{`@font-face{font-family:Display;src:url('${staticFile('fonts/display-light.ttf')}');font-weight:300}@font-face{font-family:Display;src:url('${staticFile('fonts/display-regular.ttf')}');font-weight:400}@font-face{font-family:Display;src:url('${staticFile('fonts/display-semibold.ttf')}');font-weight:600}@font-face{font-family:Data;src:url('${staticFile('fonts/data-bold.ttf')}');font-weight:700}`}</style>;
export const SubtitleLayer=()=>{const frame=useCurrentFrame(),c=(captions as Caption[]).find(c=>frame/30>=c.start&&frame/30<c.end);return frame>=SCENES[6].from?null:c?<div style={{position:'absolute',left:88,right:88,top:905,minHeight:132,display:'flex',alignItems:'center',justifyContent:'center',fontFamily:CONFIG.fonts.body,fontSize:CONFIG.typography.subtitle,lineHeight:1.17,color:CONFIG.colors.ink,textAlign:'center',background:CONFIG.colors.background,padding:'0 15px'}}>{c.text}</div>:null};
export const IdentityLayer=()=>{const f=useCurrentFrame();return f<SCENES[6].from?<><div style={{position:'absolute',left:88,top:57,fontSize:36,letterSpacing:1.2,color:CONFIG.colors.ink}}>{CONFIG.model}</div><div style={{position:'absolute',right:88,top:63,fontSize:32,letterSpacing:3,color:CONFIG.colors.muted}}>{CONFIG.series}</div><div style={{position:'absolute',left:88,right:88,top:123,height:1,background:CONFIG.colors.line}}/><div style={{position:'absolute',left:88,bottom:0,lineHeight:1.1,fontSize:CONFIG.typography.metadata,color:CONFIG.colors.muted}}>{CONFIG.notes.general}</div></>:null};
export const DraftFlag=()=> CONFIG.specsVerified?null:<div style={{position:'absolute',right:18,top:10,fontFamily:CONFIG.fonts.body,fontSize:32,color:'#935a3d',background:'#fff5e9',padding:'4px 10px'}}>{CONFIG.copy.draft}</div>;
export const Film=({photos=DEFAULT_PHOTOS,withAudio=false,bgm=false}:FilmProps)=> <AbsoluteFill style={{background:CONFIG.colors.background,fontFamily:CONFIG.fonts.body}}><Fonts/>
 <Sequence name="00:00 Range and Blade battery" from={SCENES[0].from} durationInFrames={SCENES[0].duration}><SceneFrame index={0} photos={photos}/></Sequence>
 <Sequence name="00:14 Rear motor and acceleration" from={SCENES[1].from} durationInFrames={SCENES[1].duration}><SceneFrame index={1} photos={photos}/></Sequence>
 <Sequence name="00:24 DC charging" from={SCENES[2].from} durationInFrames={SCENES[2].duration}><SceneFrame index={2} photos={photos}/></Sequence>
 <Sequence name="00:34 ADAS" from={SCENES[3].from} durationInFrames={SCENES[3].duration}><SceneFrame index={3} photos={photos}/></Sequence>
 <Sequence name="00:46 Wheelbase and suspension" from={SCENES[4].from} durationInFrames={SCENES[4].duration}><SceneFrame index={4} photos={photos}/></Sequence>
 <Sequence name="00:58 Safety" from={SCENES[5].from} durationInFrames={SCENES[5].duration}><SceneFrame index={5} photos={photos}/></Sequence>
 <Sequence name="01:11 White CTA — four-second hold" from={SCENES[6].from} durationInFrames={120}><CTAScene/></Sequence>
 <IdentityLayer/><SubtitleLayer/><DraftFlag/>
 {/* Audio slots: scripts/narrate.py populates WAV and frame-aligned caption entries after configuration verification. */}
 {withAudio&&<Audio src={staticFile('audio/voice.wav')}/>} {bgm&&<Audio src={staticFile('audio/bgm.wav')}/>}
 </AbsoluteFill>;
