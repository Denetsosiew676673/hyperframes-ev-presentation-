from pathlib import Path
import subprocess
import soundfile as sf,onnxruntime as ort
from kokoro_onnx import Kokoro
p=Path(__file__).resolve().parent
text='Welcome to UNILAND Spec Lab. We help importers and dealers explore Chinese electric vehicles, verify configurations, and arrange export support. Contact UNILAND to discuss your next order.'
opts=ort.SessionOptions();opts.intra_op_num_threads=4;opts.inter_op_num_threads=1
k=Kokoro.from_session(ort.InferenceSession('/workspace/ev-tools/models/kokoro.onnx',sess_options=opts,providers=['CPUExecutionProvider']),'/workspace/ev-tools/models/voices.bin')
a,sr=k.create(text,voice='am_michael',speed=.94,lang='en-us');sf.write(p/'uniland-host-test.wav',a,sr)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(p/'uniland-host-test.wav'),'-af','loudnorm=I=-17:TP=-2:LRA=7','-ar','48000','-b:a','192k',str(p/'uniland-host-test.mp3')],check=True)
(p/'script.txt').write_text(text+'\n');print('Voice prepared:',round(len(a)/sr,2),'seconds. No talking-head inference performed.')
