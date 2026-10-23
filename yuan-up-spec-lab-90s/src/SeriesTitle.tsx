import {useCurrentFrame} from 'remotion';
import {C,progress} from './graphics';
// Faithful error-retype timing, remapped to series identity. Never re-centre the growing string.
export const SeriesTitle=()=>{const f=useCurrentFrame(),a='UNILAND AUTO SPECS',keep=8,b='SPEC LAB',ds=2+(a.length-1)*2+16,rs=ds+(a.length-keep)*1.5+4,end=rs+(b.length-1)*1.5;
 const n=f<2?0:Math.min(a.length,Math.floor((f-2)/2)+1),del=f<ds?0:Math.min(a.length-keep,Math.floor((f-ds)/1.5)+1),n2=f<rs?0:Math.min(b.length,Math.floor((f-rs)/1.5)+1);
 const text=f>=160?'UNILAND SPEC LAB':a.slice(0,Math.max(keep,n-del)).slice(0,n)+b.slice(0,n2);
 const cursor=f<end+20&&(f>=end?Math.floor((f-end)/5)%2===0:f>=ds?true:f>=ds-16?Math.floor((f-(ds-16))/4)%2===0:true);
 return <div style={{position:'absolute',left:88,top:62,height:60,color:C.ink,display:'flex',alignItems:'center'}}>
 <div style={{position:'absolute',left:8*29-3,top:38,width:8*29*progress(f,Math.ceil(end)+1,14),height:14,background:C.line}}/>
 {text.split('').map((c,i)=><span key={i} style={{position:'relative',width:29,fontSize:44,fontFamily:'Data,monospace',textAlign:'center',fontWeight:700}}>{c===' '?'\u00a0':c}</span>)}
 {cursor&&<span style={{width:3,height:42,marginLeft:3,background:C.accent}}/>}</div>};
