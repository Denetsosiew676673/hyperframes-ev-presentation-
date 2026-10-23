from pathlib import Path
import json,subprocess
import numpy as np,soundfile as sf,onnxruntime as ort
from kokoro_onnx import Kokoro
p=Path(__file__).resolve().parents[1];work=p/'work/es';work.mkdir(parents=True,exist_ok=True)
texts=[
['El BYD Yuan UP 2027, también conocido como Atto 2,','es un SUV compacto totalmente eléctrico, pensado para la ciudad y el uso diario.'],
['Ofrece cuatrocientos un kilómetros de autonomía CLTC y un motor delantero de setenta kilovatios,','una opción práctica para trayectos urbanos y flotas ligeras.'],
['Su batería Blade LFP de BYD tiene cuarenta y cinco coma doce kilovatios hora.','Está diseñada para ofrecer estabilidad, durabilidad y un rendimiento diario fiable.'],
['La carga rápida en corriente continua pasa del treinta al ochenta por ciento en unos treinta minutos,','en condiciones adecuadas, para reducir el tiempo de espera.'],
['La pantalla de doce coma ocho pulgadas integra DiLink cien.','La cámara de trescientos sesenta grados y DiPilot cien facilitan una conducción inteligente y con confianza.'],
['Con una distancia entre ejes de dos mil seiscientos veinte milímetros, cinco puertas y cinco plazas,','los asientos traseros abatibles por secciones combinan comodidad y espacio de carga flexible.'],
['Hay unidades en stock. UNILAND gestiona el abastecimiento y la verificación de configuración,','la inspección previa al envío, los documentos de exportación y la logística internacional.']]
scenes=json.loads((p/'src/scenes.json').read_text());sr=24000
opts=ort.SessionOptions();opts.intra_op_num_threads=4;opts.inter_op_num_threads=1
k=Kokoro.from_session(ort.InferenceSession('/workspace/ev-tools/models/kokoro.onnx',sess_options=opts,providers=['CPUExecutionProvider']),'/workspace/ev-tools/models/voices.bin')
voice=np.zeros(sr*90,np.float32);caps=[];audit=[]
for i,(s,phrases) in enumerate(zip(scenes,texts)):
 chunks=[];meta=[];cursor=0
 for j,text in enumerate(phrases):
  fn=work/f'raw-{i}-{j}.wav'
  if fn.exists():a,rate=sf.read(fn,dtype='float32')
  else:a,rate=k.create(text,voice='em_alex',speed=1,lang='es');sf.write(fn,a,rate)
  active=np.flatnonzero(np.abs(a)>.004)
  if len(active):a=a[max(0,active[0]-1440):min(len(a),active[-1]+1440)]
  meta.append({'text':text,'offset':cursor,'duration':len(a)/sr});chunks.extend([a,np.zeros(round(.12*sr),np.float32)]);cursor+=len(a)/sr+.12
 start=s['from']/30+.16;available=s['duration']/30-.32;tempo=max(.94,cursor/available)
 print({'scene':s['id'],'raw_seconds':cursor,'tempo':tempo},flush=True)
 if tempo>1.05:raise RuntimeError('Spanish speech too long; revise text or extend timeline instead of rushing.')
 sf.write(work/'raw.wav',np.concatenate(chunks),sr)
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(work/'raw.wav'),'-af',f'atempo={tempo}','-ar',str(sr),str(work/'fit.wav')],check=True)
 a,_=sf.read(work/'fit.wav',dtype='float32');n=min(len(a),round(available*sr));voice[round(start*sr):round(start*sr)+n]=a[:n]
 for m in meta:caps.append({'start':start+m['offset']/tempo,'end':start+(m['offset']+m['duration'])/tempo,'text':m['text']})
 audit.append({'scene':s['id'],'start':start,'end':start+n/sr,'raw_duration':cursor,'tempo':tempo})
sf.write(work/'voice.wav',voice,sr)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(work/'voice.wav'),'-af','loudnorm=I=-17:TP=-2:LRA=7','-ar','48000',str(p/'public/audio/voice-es.wav')],check=True)
(p/'src/captions-es.json').write_text(json.dumps(caps,indent=2,ensure_ascii=False));(p/'review/audio-timing-es.json').write_text(json.dumps(audit,indent=2));(p/'review/script-es.json').write_text(json.dumps(texts,indent=2,ensure_ascii=False))
def stamp(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(p/'subtitles-es.srt').write_text('\n\n'.join(f"{i+1}\n{stamp(x['start'])} --> {stamp(x['end'])}\n{x['text']}" for i,x in enumerate(caps))+'\n')
