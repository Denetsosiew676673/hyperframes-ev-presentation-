from pathlib import Path
import numpy as np,soundfile as sf,onnxruntime as ort,json,subprocess
from kokoro_onnx import Kokoro
p=Path(__file__).resolve().parents[1];opts=ort.SessionOptions();opts.intra_op_num_threads=4;opts.inter_op_num_threads=1
k=Kokoro.from_session(ort.InferenceSession('/workspace/ev-tools/models/kokoro.onnx',sess_options=opts,providers=['CPUExecutionProvider']),'/workspace/ev-tools/models/voices.bin')
sr=24000;full=np.zeros(sr*15,np.float32);result=[]
scenes=[(0.25,5.1,[('brand','Uniland Motors.'),('offer','New, used, and electric vehicles.')]),(5.75,9.9,[('proof','Over ten thousand vehicles delivered.'),('reach','Global reach.')]),(10.55,14.35,[('cta','Start your next business partnership with Uniland Motors today.')])]
for i,(a,b,phrases) in enumerate(scenes):
    chunks=[];meta=[];cursor=0
    for key,text in phrases:
        samples,rate=k.create(text,voice='am_michael',speed=1,lang='en-us');assert rate==sr
        chunks.extend([samples,np.zeros(int(.12*sr),np.float32)]);meta.append({'key':key,'text':text,'start':cursor,'duration':len(samples)/sr});cursor+=len(samples)/sr+.12
    tempo=max(.94,cursor/(b-a));sf.write(p/f'public/audio/raw-{i}.wav',np.concatenate(chunks),sr)
    subprocess.run(['ffmpeg','-hide_banner','-v','error','-y','-i',str(p/f'public/audio/raw-{i}.wav'),'-af',f'atempo={tempo}','-ar',str(sr),str(p/f'public/audio/fit-{i}.wav')],check=True)
    fit,_=sf.read(p/f'public/audio/fit-{i}.wav',dtype='float32');n=min(len(fit),int((b-a)*sr));full[round(a*sr):round(a*sr)+n]=fit[:n]
    for x in meta:
        x['start']=a+x['start']/tempo;x['end']=x['start']+x.pop('duration')/tempo
    result.extend(meta);print('Scene',i+1,'tempo',round(tempo,3),flush=True)
sf.write(p/'public/audio/voice.wav',full,sr)
subprocess.run(['ffmpeg','-hide_banner','-v','error','-y','-i',str(p/'public/audio/voice.wav'),'-af','loudnorm=I=-17:TP=-2:LRA=7','-ar','48000',str(p/'public/audio/voice-master.wav')],check=True)
(p/'timing.json').write_text(json.dumps(result,indent=2))
(p/'src/timing.json').write_text(json.dumps(result,indent=2))
for f in (p/'public/audio').glob('raw-*.wav'):f.unlink()
for f in (p/'public/audio').glob('fit-*.wav'):f.unlink()
# Original rising noise/air bed for the final build, tapered attack and ending.
rng=np.random.default_rng(2701);dur=1.55;t=np.arange(round(sr*dur))/sr;noise=rng.standard_normal(len(t));noise=np.convolve(noise,np.ones(6)/6,mode='same');env=np.sin(np.pi*t/dur)**2*(.2+.8*t/dur)
a=.07*noise*env+.009*np.sin(2*np.pi*(180*t+120*t*t))*env
sf.write(p/'public/audio/riser.wav',a.astype(np.float32),sr)
