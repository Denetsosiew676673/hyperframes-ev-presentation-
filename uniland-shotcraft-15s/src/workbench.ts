import {Hero,Reach,Partner,Caption,Film,SHOTS,CAPTIONS,SFX,TOTAL,HERO_DEFAULTS,REACH_DEFAULTS,PARTNER_DEFAULTS,C,FontReady} from './Film';
const textFields=(defaults:Record<string,string>)=>Object.entries(defaults).map(([key,value])=>({type:key==='color'?'color':'text',key,label:key,default:value}));
export const WORKBENCH={
 name:'UNILAND MOTORS · World Ready · 15s',fps:30,width:1920,height:1080,total:TOTAL,background:C.bg,
 shots:[
  {id:'hero',label:'Vehicle sourcing',...SHOTS.hero,component:Hero,props:HERO_DEFAULTS,schema:textFields(HERO_DEFAULTS)},
  {id:'reach',label:'Global reach',...SHOTS.reach,component:Reach,props:REACH_DEFAULTS,schema:textFields(REACH_DEFAULTS)},
  {id:'partner',label:'Partner invitation',...SHOTS.partner,component:Partner,props:PARTNER_DEFAULTS,schema:textFields(PARTNER_DEFAULTS)},
 ],
 transitions:[],overlays:[{id:"fonts",label:"Local font loading",from:0,duration:TOTAL,component:FontReady}],
 captions:CAPTIONS.map(c=>({id:c.id,label:c.text,from:c.from,duration:c.duration,component:Caption,props:{text:c.text,duration:c.duration},schema:[{type:'textarea',key:'text',label:'English caption',default:c.text}],durationProp:'duration'})),
 sfx:[{id:'voice',from:0,duration:TOTAL,src:'audio/voice-master.wav',volume:1},...SFX],bgm:[],order:['transitions','captions','overlays'],original:Film,
};
