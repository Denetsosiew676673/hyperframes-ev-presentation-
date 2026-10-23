from pathlib import Path
import json,subprocess,hashlib
import numpy as np,soundfile as sf
from PIL import Image,ImageDraw
p=Path(__file__).resolve().parents[1];main=p/'renders/yuan-up-uniland-spec-lab-90s.mp4';other=p/'renders/yuan-up-uniland-spec-lab-90s-no-music.mp4'
report={}
for f in [main,other]:
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(f)]));v=next(s for s in probe['streams'] if s['codec_type']=='video');a=next(s for s in probe['streams'] if s['codec_type']=='audio')
 assert (v['width'],v['height'],v['r_frame_rate'],int(v['nb_frames']))==(1920,1080,'30/1',2700)
 assert abs(float(probe['format']['duration'])-90)<.02
 report[f.name]={'duration':probe['format']['duration'],'width':v['width'],'height':v['height'],'frames':v['nb_frames'],'fps':v['r_frame_rate'],'audio':a['codec_name'],'audio_rate':a['sample_rate'],'bytes':f.stat().st_size}
 h=subprocess.check_output(['ffmpeg','-v','error','-i',str(f),'-map','0:v:0','-c','copy','-f','streamhash','-hash','sha256','-']).decode().strip();report[f.name]['video_stream_hash']=h
assert report[main.name]['video_stream_hash']==report[other.name]['video_stream_hash']
report['photo_hashes']=all(hashlib.sha256((p/'public/photos'/x['file']).read_bytes()).hexdigest()==x['sha256'] for x in json.loads((p/'review/asset-manifest.json').read_text()))
subprocess.run(['ffmpeg','-v','error','-y','-i',str(main),'-vn','-ac','1','-ar','48000',str(p/'work/decoded.wav')],check=True)
a,sr=sf.read(p/'work/decoded.wav',dtype='float32');v,_=sf.read(p/'public/audio/voice.wav',dtype='float32');lags=[]
for t in [12,29,50,82]:
 x=v[int(t*sr):int((t+2)*sr)];y=a[int((t-.15)*sr):int((t+2.15)*sr)]
 size=1<<(len(y)+len(x)-2).bit_length();corr=np.fft.irfft(np.fft.rfft(y,size)*np.conj(np.fft.rfft(x,size)),size);idx=int(np.argmax(corr));lag=(idx if idx<len(y) else idx-size)-.15*sr
 lags.append({'probe_seconds':t,'lag_samples':float(lag),'lag_ms':float(lag/sr*1000)})
assert max(abs(x['lag_ms']) for x in lags)<1000/30
report['mux_audio_alignment']=lags;report['decoded_peak_dbfs']=float(20*np.log10(max(abs(a))));assert max(abs(a))<1
frames=[10,36,60,95,180,450,615,825,1080,1530,1680,1980,2130,2490,2630,2699]
canvas=Image.new('RGB',(1920,4*300),'#111619');draw=ImageDraw.Draw(canvas)
for i,f in enumerate(frames):
 fn=p/f'review/f{f:04}.jpg';subprocess.run(['ffmpeg','-v','error','-y','-ss',str(f/30),'-i',str(main),'-frames:v','1','-q:v','2',str(fn)],check=True)
 im=Image.open(fn);im.thumbnail((480,270));canvas.paste(im,((i%4)*480,(i//4)*300));draw.text(((i%4)*480+12,(i//4)*300+275),f'f{f} / {f/30:.2f}s',fill='white')
canvas.save(p/'review/contact-sheet.jpg',quality=94)
(p/'review/technical-check.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
