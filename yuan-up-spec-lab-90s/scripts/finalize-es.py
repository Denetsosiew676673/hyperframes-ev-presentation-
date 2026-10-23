from pathlib import Path
import subprocess
p=Path(__file__).resolve().parents[1]
for music,suffix in [(True,''),(False,'-no-music')]:
 cmd=['ffmpeg','-v','error','-y','-i',str(p/'renders/visual-es.mp4'),'-i',str(p/'public/audio/voice-es.wav'),'-i',str(p/'public/audio/keys.wav')]
 if music:cmd+=['-i',str(p/'public/audio/bgm.wav')]
 inputs='[1:a][2:a][3:a]' if music else '[1:a][2:a]';n=3 if music else 2
 cmd+=['-filter_complex',inputs+f'amix=inputs={n}:normalize=0,alimiter=limit=0.95:level=false:latency=true,apad,atrim=duration=90[a]','-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-t','90','-metadata','language=spa','-metadata:s:a:0','language=spa','-movflags','+faststart',str(p/f'renders/yuan-up-uniland-spec-lab-90s-es{suffix}.mp4')]
 subprocess.run(cmd,check=True)
