"""Finalize approved landscape MP4 and voice-only alternate, preserving video frames."""
from pathlib import Path
import subprocess
p=Path(__file__).resolve().parents[1];raw=p/'work/landscape-raw-v2.mp4';out=p/'renders';out.mkdir(exist_ok=True)
duration='149.5333333333'
subprocess.run(['ffmpeg','-v','error','-y','-i',str(raw),'-map','0:v:0','-map','0:a:0','-c:v','copy','-af','volume=-3dB','-c:a','aac','-b:a','192k','-t',duration,'-movflags','+faststart',str(out/'uniland-ev-finance-landscape-150s.mp4')],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(raw),'-i',str(p/'work/voice.mp3'),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','192k','-t',duration,'-movflags','+faststart',str(out/'uniland-ev-finance-landscape-150s-voice-only.mp4')],check=True)
print('Finalized both MP4 variants, video copied without re-rendering.')
