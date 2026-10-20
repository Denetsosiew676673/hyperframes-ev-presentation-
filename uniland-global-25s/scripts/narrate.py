from pathlib import Path
import os,json,subprocess
import numpy as np,soundfile as sf,onnxruntime as ort
from kokoro_onnx import Kokoro
p=Path(__file__).resolve().parents[1]; out=p/'assets';out.mkdir(exist_ok=True)
opts=ort.SessionOptions();opts.intra_op_num_threads=4;opts.inter_op_num_threads=1
base=Path('/workspace/ev-tools/models')
session=ort.InferenceSession(str(base/'kokoro.onnx'),sess_options=opts,providers=['CPUExecutionProvider'])
k=Kokoro.from_session(session,str(base/'voices.bin'));sr=24000
scenes=[(15,[('brand','At Uniland Motors,'),('partner',"we are your global vehicle sourcing and export partner."),('new','We supply new cars,'),('used','used vehicles,'),('electric','electric and plug-in hybrid models,'),('parts','together with a full range of auto parts.')]),(10,[('delivered','Over ten thousand vehicles delivered.'),('dealers','Serving three hundred dealers'),('countries','across more than forty countries.'),('world','Chinese vehicles. Global reach.')])]
schedule=[]; start=0; master=[]
for si,(duration,lines) in enumerate(scenes):
    samples=[];raw=[];cursor=0
    for key,text in lines:
        a,rate=k.create(text,voice='am_michael',speed=1.0,lang='en-us');assert rate==sr
        samples.extend([a,np.zeros(int(sr*.15),np.float32)])
        raw.append(dict(key=key,text=text,start=cursor,duration=len(a)/sr));cursor+=len(a)/sr+.15
    # Leave a short lead and tail; time-fit the whole read without cutting speech.
    lead=.55 if si==0 else .35;tail=.45;target=duration-lead-tail
    tempo=cursor/target
    sf.write(out/f'voice-{si}-raw.wav',np.concatenate(samples),sr)
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(out/f'voice-{si}-raw.wav'),'-af',f'atempo={tempo:.8f}','-ar',str(sr),str(out/f'voice-{si}-fit.wav')],check=True)
    fit,_=sf.read(out/f'voice-{si}-fit.wav',dtype='float32');full=np.zeros(round(duration*sr),np.float32)
    at=round(lead*sr);n=min(len(fit),len(full)-at);full[at:at+n]=fit[:n];master.append(full)
    sf.write(out/f'voice-{si+1}.wav',full,sr)
    for r in raw:
        r['start']=round(start+lead+r['start']/tempo,4);r['end']=round(r['start']+r.pop('duration')/tempo,4)
    schedule.append(dict(scene=si+1,start=start,duration=duration,tempo=tempo,phrases=raw));start+=duration
    print(f'Scene {si+1}: raw {cursor:.2f}s -> {target:.2f}s, tempo {tempo:.3f}',flush=True)
sf.write(out/'narration.wav',np.concatenate(master),sr)
(p/'timing.json').write_text(json.dumps(schedule,indent=2))
for f in out.glob('*-raw.wav'):f.unlink()
for f in out.glob('*-fit.wav'):f.unlink()
