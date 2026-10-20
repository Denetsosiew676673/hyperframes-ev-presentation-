"""Compensate measured Remotion4.0.484 AAC priming uniformly; copy video, remux15s audio."""
from pathlib import Path
import subprocess
p=Path(__file__).resolve().parents[1]
# Measured cross-correlation: raw render is2048/48000sec late (three independent windows).
# Output alignment is a render-pipeline adjustment, not scattered per-cue frame edits.
shift=2048/48000
subprocess.run(['ffmpeg','-hide_banner','-v','error','-y','-i',str(p/'out/uniland-shotcraft-15s-raw.mp4'),'-map','0:v:0','-map','0:a:0','-c:v','copy','-af',f'atrim=start={shift},asetpts=PTS-STARTPTS,apad,atrim=duration=15','-c:a','aac','-ar','48000','-b:a','192k','-t','15','-movflags','+faststart',str(p/'out/uniland-shotcraft-15s.mp4')],check=True)
print('Finalized: copied450 video frames; compensated2048-sample AAC priming;15.000s audio/container.')
