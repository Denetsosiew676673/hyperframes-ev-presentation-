from pathlib import Path
import json,math,subprocess
import numpy as np,soundfile as sf,onnxruntime as ort
from kokoro_onnx import Kokoro
p=Path(__file__).resolve().parents[1];work=p/'work';work.mkdir(exist_ok=True)
scenes=json.loads((p/'src/scenes.json').read_text());sr=24000;duration=sum(s["duration"] for s in scenes)/30;total=round(sr*duration)
opts=ort.SessionOptions();opts.intra_op_num_threads=4;opts.inter_op_num_threads=1
k=Kokoro.from_session(ort.InferenceSession('/workspace/ev-tools/models/kokoro.onnx',sess_options=opts,providers=['CPUExecutionProvider']),'/workspace/ev-tools/models/voices.bin')
voice=np.zeros(total,np.float32);caps=[];audit=[]
for i,s in enumerate(scenes):
 chunks=[];meta=[];cursor=0
 for j,text in enumerate(s['voice']):
  path=work/f'voice-{i}-{j}.wav'
  if path.exists():a,rate=sf.read(path,dtype='float32')
  else:a,rate=k.create(text,voice='am_michael',speed=1,lang='en-us');sf.write(path,a,rate)
  # Trim only leading/trailing synthesis silence; keep 60ms safety margins.
  active=np.flatnonzero(np.abs(a)>.004)
  if len(active):a=a[max(0,active[0]-1440):min(len(a),active[-1]+1440)]
  meta.append({'text':text,'offset':cursor,'duration':len(a)/sr});chunks.extend([a,np.zeros(round(.10*sr),np.float32)]);cursor+=len(a)/sr+.10
 start=s['from']/30+.16;available=s['duration']/30-.32
 tempo=max(.94,cursor/available)
 sf.write(work/'raw.wav',np.concatenate(chunks),sr)
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(work/'raw.wav'),'-af',f'atempo={tempo}','-ar',str(sr),str(work/'fit.wav')],check=True)
 a,_=sf.read(work/'fit.wav',dtype='float32')
 assert len(a)<=round(available*sr)+sr*.05
 n=min(len(a),round(available*sr));voice[round(start*sr):round(start*sr)+n]=a[:n]
 for m in meta:
  caps.append({'start':start+m['offset']/tempo,'end':start+(m['offset']+m['duration'])/tempo,'text':m['text']})
 audit.append({'scene':s['id'],'start':start,'end':start+n/sr,'raw_duration':cursor,'tempo':tempo})
 print(audit[-1],flush=True)
sf.write(work/'voice.wav',voice,sr)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(work/'voice.wav'),'-af','loudnorm=I=-17:TP=-2:LRA=7','-ar','48000',str(p/'public/audio/voice.wav')],check=True)
(p/'src/captions.json').write_text(json.dumps(caps,indent=2));(p/'review/audio-timing.json').write_text(json.dumps(audit,indent=2))
# Original understated 100 BPM technological bed: evolving minor chords and soft low percussion.
rng=np.random.default_rng(2701);t=np.arange(total)/sr;music=np.zeros(total,np.float64)
chords=[(65.406,77.782,98.0),(58.27,73.416,87.307),(51.913,65.406,77.782),(58.27,73.416,98.)]
for j in range(math.ceil(duration/9.6)):
 st=j*9.6;en=min(duration,st+10.2);a=int(st*sr);b=int(en*sr);tt=np.arange(b-a)/sr
 env=np.minimum(1,tt/.6)*np.minimum(1,(en-st-tt)/.6)
 freqs=chords[j%4]
 pad=sum(np.sin(2*np.pi*f*tt)+.15*np.sin(2*np.pi*f*2*tt) for f in freqs)*.006
 music[a:b]+=pad*env
for beat in range(math.ceil(duration/.6)):
 a=round(beat*.6*sr);n=min(int(.19*sr),total-a);tt=np.arange(n)/sr
 music[a:a+n]+=.042*np.sin(2*np.pi*(49*tt+24*(1-np.exp(-tt*25))/25))*np.exp(-tt*30)
 if beat%2:music[a:a+n]+=.004*rng.standard_normal(n)*np.exp(-tt*110)
music*=np.minimum(1,t/1.5)*np.minimum(1,np.maximum(0,(duration-t)/1.5))
sf.write(p/'public/audio/bgm.wav',music.astype(np.float32),sr)
# Frame-accurate typewriter SFX, lower backspace pitch. Synthetic original taps, no external license.
keys=np.zeros(total,np.float32);first='UNILAND AUTO SPECS';keep=8;ds=2+(len(first)-1)*2+16;rs=ds+(len(first)-keep)*1.5+4
events=[(2+i*2,False) for i in range(len(first))]+[(math.ceil(ds+i*1.5),True) for i in range(len(first)-keep)]+[(math.ceil(rs+i*1.5),False) for i in range(8)]
for f,back in events:
 a=round(f/30*sr);tt=np.arange(720)/sr
 click=(rng.standard_normal(len(tt))*.25+np.sin(2*np.pi*(800 if back else 1700)*tt)*.3)*np.exp(-tt*180)*.08
 keys[a:a+len(click)]+=click
sf.write(p/'public/audio/keys.wav',keys,sr)
