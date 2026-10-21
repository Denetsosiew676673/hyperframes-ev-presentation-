from pathlib import Path
import sys,json,subprocess,math
import numpy as np,soundfile as sf,onnxruntime as ort
from kokoro_onnx import Kokoro
from content import BEATS,SCRIPTS
from captions import timed
p=Path(__file__).resolve().parents[1];d=p/'work';d.mkdir(exist_ok=True)
sr=24000;T=60/122;duration=math.ceil(BEATS[-1]*T*30)/30
opts=ort.SessionOptions();opts.intra_op_num_threads=4;opts.inter_op_num_threads=1
k=Kokoro.from_session(ort.InferenceSession('/workspace/ev-tools/models/kokoro.onnx',sess_options=opts,providers=['CPUExecutionProvider']),'/workspace/ev-tools/models/voices.bin')
full=np.zeros(round(duration*sr),np.float32);timing=[];audit=[]
for i,sentences in enumerate(SCRIPTS):
 chunks=[];meta=[];cursor=0
 for j,text in enumerate(sentences):
  fn=d/f'raw-{i}-{j}.wav'
  if fn.exists():a,rate=sf.read(fn,dtype='float32')
  else:
   a,rate=k.create(text,voice='am_michael',speed=1,lang='en-us');sf.write(fn,a,rate)
  assert rate==sr
  meta.append(dict(text=text,start=cursor,duration=len(a)/sr));chunks.extend([a,np.zeros(round(.12*sr),np.float32)]);cursor+=len(a)/sr+.12
 start=BEATS[i]*T+.16;end=BEATS[i+1]*T-.16;available=end-start
 tempo=max(.97,cursor/available)
 sf.write(d/'raw.wav',np.concatenate(chunks),sr)
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(d/'raw.wav'),'-af',f'atempo={tempo}','-ar',str(sr),str(d/'fit.wav')],check=True)
 a,_=sf.read(d/'fit.wav',dtype='float32');n=min(len(a),round(available*sr));full[round(start*sr):round(start*sr)+n]=a[:n]
 for m in meta:
  aa=start+m['start']/tempo;bb=aa+m['duration']/tempo
  timing.extend(timed(m['text'],aa,bb))
 audit.append(dict(scene=i+1,raw_seconds=cursor,available_seconds=available,tempo=tempo,start=start,end=start+n/sr))
 print(json.dumps(audit[-1]),flush=True)
sf.write(d/'voice.wav',full,sr)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(d/'voice.wav'),'-af','loudnorm=I=-17:TP=-2:LRA=7','-ar','48000','-b:a','112k',str(d/'voice.mp3')],check=True)
# Original deterministic restrained percussion / low pad bed. Every downbeat has a transient at exact n*T.
rng=np.random.default_rng(122);music=np.zeros(round(duration*sr),np.float64);hits=[]
for beat in range(212):
 start=round(beat*T*sr);n=min(round(.19*sr),len(music)-start);t=np.arange(n)/sr
 env=np.exp(-t*35);phase=2*np.pi*(52*t+35*(1-np.exp(-t*30))/30)
 kick=.18*np.sin(phase)*env
 # Crisp short noise attack makes exact downbeat identifiable; accent on beats 0 mod 4.
 accent=1.0 if beat%4==0 else .48
 kick+=.035*rng.standard_normal(n)*np.exp(-t*180)
 if beat%4==2:kick+=.025*rng.standard_normal(n)*np.exp(-t*55)
 music[start:start+n]+=accent*kick;hits.append(dict(beat=beat,time=beat*T,frame=round(beat*T*30),downbeat=beat%4==0))
t=np.arange(len(music))/sr;pad=(np.sin(2*np.pi*65.406*t)+.4*np.sin(2*np.pi*98*t))*.007
music+=pad
# Attenuate during narration; no transition/extra SFX required for minimal cards.
for m in audit:
 a=round(m['start']*sr);b=round(m['end']*sr);music[a:b]*=.65
fade=np.minimum(1,np.maximum(0,(duration-t)/1.4));music*=fade
sf.write(d/'bgm.wav',music.astype(np.float32),sr)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(d/'bgm.wav'),'-b:a','96k',str(d/'bgm.mp3')],check=True)
(d/'timing.json').write_text(json.dumps(timing,indent=2))
(p/'review/audio-timing.json').write_text(json.dumps(audit,indent=2))
(p/'review/beat-grid.json').write_text(json.dumps(dict(bpm=122,phase=0,T=T,duration=duration,provenance='original synthesized PCM, deterministic seed 122',anchors=hits),indent=2))
