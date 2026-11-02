"""Generate phrase-aligned narration after configuration evidence has been reconciled.
Optional dependencies: numpy,soundfile,onnxruntime,kokoro-onnx. Pre-generated WAV assets
will be included for normal project use; those packages are not needed by Remotion.
"""
from pathlib import Path
import json,os,subprocess
import numpy as np,soundfile as sf,onnxruntime as ort
from kokoro_onnx import Kokoro
p=Path(__file__).resolve().parents[1];subprocess.run(['node',str(p/'scripts/export-config.mjs')],check=True)
data=json.loads((p/'work/config.json').read_text());config=data['CONFIG'];scenes=data['SCENES']
if not config['specsVerified']:raise RuntimeError('Reconcile the supplied configuration sheet before generating production narration.')
model=os.environ.get('SEALION_KOKORO_MODEL','/workspace/ev-tools/models/kokoro.onnx');voices=os.environ.get('SEALION_KOKORO_VOICES','/workspace/ev-tools/models/voices.bin')
opts=ort.SessionOptions();opts.intra_op_num_threads=4;opts.inter_op_num_threads=1
k=Kokoro.from_session(ort.InferenceSession(model,sess_options=opts,providers=['CPUExecutionProvider']),voices)
sr=24000;duration=config['total']/config['fps'];full=np.zeros(round(duration*sr),np.float32);caps=[];audit=[]
for i,s in enumerate(scenes):
 chunks=[];meta=[];cursor=0
 for j,text in enumerate(s['voice']):
  a,rate=k.create(text,voice='am_michael',speed=.94,lang='en-us');active=np.flatnonzero(np.abs(a)>.004)
  if len(active):a=a[max(0,active[0]-1440):min(len(a),active[-1]+1440)]
  meta.append({'text':text,'offset':cursor,'duration':len(a)/sr});chunks.extend([a,np.zeros(round(.12*sr),np.float32)]);cursor+=len(a)/sr+.12
 start=s['from']/30+.12;available=s['duration']/30-.24
 if cursor>available:raise RuntimeError(f"{s['id']}: {cursor:.2f}s narration exceeds {available:.2f}s; shorten copy instead of accelerating")
 a=np.concatenate(chunks);full[round(start*sr):round(start*sr)+len(a)]=a
 for m in meta:caps.append({'start':start+m['offset'],'end':start+m['offset']+m['duration'],'text':m['text']})
 audit.append({'scene':s['id'],'start':start,'end':start+cursor,'synthesis_speed':.94});print(audit[-1],flush=True)
sf.write(p/'work/voice.wav',full,sr)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(p/'work/voice.wav'),'-af','loudnorm=I=-17:TP=-2:LRA=7','-ar','48000',str(p/'public/audio/voice.wav')],check=True)
(p/'src/captions.json').write_text(json.dumps(caps,indent=2));(p/'review/audio-timing.json').write_text(json.dumps(audit,indent=2))
def stamp(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(p/'subtitles.srt').write_text('\n\n'.join(f"{i+1}\n{stamp(c['start'])} --> {stamp(c['end'])}\n{c['text']}" for i,c in enumerate(caps))+'\n')
