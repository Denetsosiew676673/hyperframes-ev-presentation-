"""Generate sentence-aligned narration with local Kokoro. No API credentials."""
import json, os
from pathlib import Path
import numpy as np
import soundfile as sf
import onnxruntime as ort
from kokoro_onnx import Kokoro
root=Path(__file__).resolve().parents[1]
model=Path(os.environ.get('EV_TTS_MODELS','/workspace/ev-tools/models'))
opts=ort.SessionOptions(); opts.intra_op_num_threads=4; opts.inter_op_num_threads=1
session=ort.InferenceSession(str(model/'kokoro.onnx'),sess_options=opts,providers=['CPUExecutionProvider'])
kokoro=Kokoro.from_session(session,str(model/'voices.bin'))
slides=json.loads((root/'content.json').read_text()); schedule=[]; cursor=0; sr=24000
for i,slide in enumerate(slides):
    chunks=[np.zeros(int(sr*1.6),dtype=np.float32)]; local=1.6; captions=[]
    for text in slide['voice']:
        samples,rate=kokoro.create(text,voice='af_nova',speed=.94,lang='en-us')
        assert rate==sr
        dur=len(samples)/sr
        captions.append(dict(text=text,start=round(cursor+local,3),end=round(cursor+local+dur,3)))
        chunks.extend([samples,np.zeros(int(sr*.65),dtype=np.float32)]);local+=dur+.65
    chunks.append(np.zeros(sr,dtype=np.float32));local+=1
    sf.write(root/f'assets/voice-{i+1}.wav',np.concatenate(chunks),sr)
    schedule.append(dict(start=round(cursor,3),duration=round(local,3),captions=captions));cursor+=local
    print(f'Slide {i+1}: {local:.2f}s',flush=True)
(root/'schedule.json').write_text(json.dumps(schedule,indent=2))
print(f'Total: {cursor:.2f}s')
