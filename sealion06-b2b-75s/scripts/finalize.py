from pathlib import Path
import subprocess
p=Path(__file__).resolve().parents[1]
subprocess.run(['node',str(p/'scripts/check-assets.mjs')],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(p/'renders/visual.mp4'),'-i',str(p/'public/audio/voice.wav'),'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-af','apad,atrim=duration=75','-t','75','-movflags','+faststart',str(p/'renders/sealion06-uniland-b2b-75s.mp4')],check=True)
