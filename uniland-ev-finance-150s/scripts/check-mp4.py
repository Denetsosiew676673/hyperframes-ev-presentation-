"""Measure exported metadata, voice/music alignment and clipping. No rendering."""
from pathlib import Path
import json,subprocess,numpy as np
p=Path(__file__).resolve().parents[1];f=p/'renders/uniland-ev-finance-landscape-150s.mp4';sr=16000
meta=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(f)]))
def read(file):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(file),'-vn','-ac','1','-ar',str(sr),'-f','f32le','-']),dtype='<f4').astype(np.float64)
def probe(a,b,begin,end):
 lo=int(begin*sr);hi=int(end*sr);x=a[lo:hi];margin=2400;y=b[lo-margin:hi+margin];n=1<<(len(x)+len(y)-2).bit_length();cc=np.fft.irfft(np.fft.rfft(y,n)*np.conj(np.fft.rfft(x,n)),n);candidates=np.arange(0,2*margin+1);best=int(candidates[np.argmax(cc[candidates])]);lag=best-margin;z=b[lo+lag:hi+lag];corr=float(np.dot(x,z)/(np.linalg.norm(x)*np.linalg.norm(z)+1e-12));return dict(window=[begin,end],offset_ms=lag/sr*1000,offset_frames_30fps=lag/sr*30,correlation=corr)
y=read(f);v=read(p/'work/voice.mp3');m=read(p/'work/bgm.mp3')
voice=[probe(v,y,a,b) for a,b in [(1,6),(43,49),(101,107),(136,141)]]
# BGM probes in low-voice regions are supplementary; voice is the dominant reference.
n=min(len(v),len(m),len(y));vv=v[:n];mm=m[:n];yy=y[:n]
mat=np.array([[np.dot(vv,vv),np.dot(vv,mm)],[np.dot(vv,mm),np.dot(mm,mm)]])
coef=np.linalg.solve(mat,np.array([np.dot(vv,yy),np.dot(mm,yy)]));residual=y.copy();residual[:n]-=coef[0]*vv
music=[probe(m,residual,a,b) for a,b in [(3,7),(43,49),(101,107),(136,141)]]
r=dict(metadata=meta,voice_alignment=voice,music_alignment_after_voice_subtraction=music,estimated_mix_gains=coef.tolist(),max_decoded_amplitude=float(abs(y).max()),analysis_sample_rate=sr,scope='Rendered MP4 numerical audio alignment, not perceptual listening or original-source factual verification')
(p/'review/MP4-CHECK.json').write_text(json.dumps(r,indent=2));print(json.dumps(dict(duration=meta['format']['duration'],voice_alignment=voice,music_alignment=music,peak=r['max_decoded_amplitude']),indent=2))
