from pathlib import Path
import subprocess
p=Path(__file__).resolve().parents[1];raw=p/'work/avatr-final-raw.mp4';out=p/'renders';out.mkdir(exist_ok=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(raw),'-map','0:v:0','-map','0:a:0','-c:v','copy','-af','volume=-3dB','-c:a','aac','-b:a','192k','-t','90','-movflags','+faststart',str(out/'avatr11-uniland-b2b-90s.mp4')],check=True)
print('Final MP4 ready; video copied, uniform audio headroom applied.')
