from pathlib import Path
import numpy as np,subprocess,json
p=Path(__file__).resolve().parents[1];sr=16000
out=p/'out'
def read(file):
    b=subprocess.check_output(['ffmpeg','-v','error','-i',str(file),'-f','f32le','-ac','1','-ar',str(sr),'-'])
    return np.frombuffer(b,dtype='<f4').astype(np.float64)
a=read(out/'uniland-shotcraft-15s.mp4');v=read(p/'public/audio/voice-master.wav');n=1<<(len(a)+len(v)-2).bit_length();c=np.fft.irfft(np.fft.rfft(a,n)*np.conj(np.fft.rfft(v,n)),n)
limit=1600;lags=np.arange(-limit,limit+1);values=np.concatenate([c[-limit:],c[:limit+1]]);lag=int(lags[np.argmax(values)])
result={'pipeline':{'remotion':'4.0.484','container':'mp4','video_codec':'h264','audio_codec':'aac','sample_rate_analysis':sr,'date':'2026-10-20'},'method':'FFT cross-correlation of rendered mixed audio with complete original voiceover, within +/-100ms; source SFX attack peaks separately measured','output_voice_offset_samples':lag,'output_voice_offset_ms':lag/sr*1000,'output_voice_offset_frames_30fps':lag/sr*30,'source_sfx_peak_lag_ms':{},'max_amplitude':float(abs(a).max()),'rms_dbfs':float(20*np.log10(np.sqrt(np.mean(a*a))+1e-12))}
for file in ['transition.mp3','impact.mp3','shimmer.mp3','riser.wav']:
    s=read(p/'public/audio'/file);result['source_sfx_peak_lag_ms'][file]=int(np.argmax(abs(s)))/sr*1000
# Three independent strong voice windows corroborate global lag without assuming codec priming.
windows=[]
for start,end in [(1.4,3.6),(6.0,7.5),(11.5,13.7)]:
    x=v[int(start*sr):int(end*sr)]; scores=[]; ls=range(max(-limit,lag-64),min(limit,lag+64)+1)
    for d in ls:
        y=a[int(start*sr)+d:int(end*sr)+d];scores.append(float(np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y)+1e-12)))
    best=list(ls)[int(np.argmax(scores))];windows.append({'window_seconds':[start,end],'lag_samples':best,'lag_ms':best/sr*1000,'normalized_correlation':max(scores)})
result['corroborating_windows']=windows
# Separate source peak lag and measured output residuals for three sharp effects.
residual=a.copy();nv=min(len(v),len(residual));residual[:nv]-=v[:nv]
probes=[]
for name,frame,duration,source in [('route1',181,30,'impact.mp3'),('route2',217,30,'impact.mp3'),('brand-stamp',361,60,'impact.mp3'),('url-shimmer',365,60,'shimmer.mp3')]:
    x=read(p/'public/audio'/source)[:int(min(duration/30,.85)*sr)]
    at=round(frame/30*sr); ls=range(-1600,1601);scores=[]
    # FFT for local cross-correlation; a pre/post margin allows source-start detection.
    lo=max(0,at-1600);y=residual[lo:min(len(residual),at+len(x)+1600)]
    nf=1<<(len(y)+len(x)-2).bit_length();cc=np.fft.irfft(np.fft.rfft(y,nf)*np.conj(np.fft.rfft(x,nf)),nf)
    candidates=np.arange(max(0,at-lo-1600),min(len(y)-len(x),at-lo+1600)+1)
    best=int(candidates[np.argmax(cc[candidates])]);found=lo+best;delay=found-at
    probes.append({'effect':name,'cue_frame':frame,'source':source,'residual_start_samples':delay,'residual_start_ms':delay/sr*1000,'residual_start_frames':delay/sr*30})
result['sfx_cross_correlation_probes']=probes
result['source_peak_target_residuals_frames']={'route1':16+result['source_sfx_peak_lag_ms']['impact.mp3']*.03-32,'route2':52+result['source_sfx_peak_lag_ms']['impact.mp3']*.03-68,'brand_stamp':56+result['source_sfx_peak_lag_ms']['impact.mp3']*.03-73,'url_settle':60+result['source_sfx_peak_lag_ms']['shimmer.mp3']*.03-89}
(out/'AUDIO-ALIGNMENT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
