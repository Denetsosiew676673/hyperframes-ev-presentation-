import {Film,Header,Captions,AUDIO,TOTAL} from './Film';
import {Scene,SHOTS} from './Scenes';
export const WORKBENCH={name:'UNILAND SPEC LAB · Yuan UP',fps:30,width:1920,height:1080,total:TOTAL,background:'#111619',revision:'1',
 shots:SHOTS.map((s,i)=>({id:s.id,label:s.title,from:s.from,duration:s.duration+(i===6?0:12),component:Scene,props:{index:i,title:s.title,duration:s.duration},schema:[{type:'textarea',key:'title',label:'Scene heading',default:s.title}],cardId:s.id})),
 overlays:[{id:'header',label:'Series identity',from:0,duration:TOTAL,component:Header}],
 captions:[{id:'captions',label:'English narration captions',from:0,duration:TOTAL,component:Captions}],
 transitions:[],sfx:AUDIO.map(a=>({from:0,duration:TOTAL,src:a.src,volume:a.volume})),bgm:[{from:0,duration:TOTAL,src:'audio/bgm.wav',volume:1}],order:['captions','overlays'],original:Film};
