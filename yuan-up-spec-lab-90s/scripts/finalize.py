from pathlib import Path
import subprocess,json
p=Path(__file__).resolve().parents[1]
def run(args):subprocess.run(args,check=True)
# PCM sources share t=0 with the video. FFmpeg handles AAC priming timestamps in mux.
for music,name in [(True,'yuan-up-uniland-spec-lab-90s.mp4'),(False,'yuan-up-uniland-spec-lab-90s-no-music.mp4')]:
 cmd=['ffmpeg','-v','error','-y','-i',str(p/'renders/visual.mp4'),'-i',str(p/'public/audio/voice.wav'),'-i',str(p/'public/audio/keys.wav')]
 if music:cmd+=['-i',str(p/'public/audio/bgm.wav')]
 inputs='[1:a][2:a][3:a]' if music else '[1:a][2:a]';n=3 if music else 2
 cmd+=['-filter_complex',inputs+f'amix=inputs={n}:normalize=0,alimiter=limit=0.95:level=false:latency=true,apad,atrim=duration=90[a]','-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-t','90','-movflags','+faststart',str(p/'renders'/name)]
 run(cmd)
# Sidecar subtitles preserve the exact spoken phrases.
caps=json.loads((p/'src/captions.json').read_text())
def stamp(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(p/'subtitles.srt').write_text('\n\n'.join(f"{i+1}\n{stamp(x['start'])} --> {stamp(x['end'])}\n{x['text']}" for i,x in enumerate(caps))+'\n')
