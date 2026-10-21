import re
def split_words(text):
 # Preserve financial quantities as semantic units while keeping captions short.
 pattern=r'((?:eight point four billion yuan|six point six billion|one hundred billion yuan|five hundred|thirty-one Maimai cars|fifteen troubled EV companies)[,.;!?]?|[\S]+)'
 units=re.findall(pattern,text,flags=re.I);groups=[];current=[];count=0
 for unit in units:
  n=len(unit.split())
  if current and count+n>6:groups.append(' '.join(current));current=[];count=0
  current.append(unit);count+=n
 if current:groups.append(' '.join(current))
 return groups
def timed(text,start,end):
 groups=split_words(text);total=sum(len(g) for g in groups);result=[];pos=start
 for group in groups:
  stop=pos+(end-start)*len(group)/total;result.append(dict(start=pos,end=stop,text=group));pos=stop
 return result
if __name__=='__main__':
 from pathlib import Path
 import json,soundfile as sf
 from content import SCRIPTS
 p=Path(__file__).resolve().parents[1];audit=json.loads((p/'review/audio-timing.json').read_text());result=[]
 for i,ss in enumerate(SCRIPTS):
  cursor=0;meta=audit[i]
  for j,text in enumerate(ss):
   info=sf.info(p/f'work/raw-{i}-{j}.wav');dur=info.frames/info.samplerate
   start=meta['start']+cursor/meta['tempo'];end=start+dur/meta['tempo'];result.extend(timed(text,start,end));cursor+=dur+.12
 (p/'work/timing.json').write_text(json.dumps(result,indent=2))
