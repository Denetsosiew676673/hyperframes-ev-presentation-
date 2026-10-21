"""Convert the offline HTML to CLI-compatible files. Does not render video."""
from pathlib import Path
import re,base64,sys
p=Path(__file__).resolve().parents[1];out=Path(sys.argv[1]) if len(sys.argv)>1 else p/'work/hyperframes-ready';(out/'assets').mkdir(parents=True,exist_ok=True)
s=(p/'index.html').read_text()
for media in ['voice','music']:
 pattern=rf'(<audio id="{media}"[^>]*src=")data:audio/mpeg;base64,([^"]+)'
 m=re.search(pattern,s);(out/f'assets/{media}.mp3').write_bytes(base64.b64decode(m[2]));s=s[:m.start(2)-len('data:audio/mpeg;base64,')]+f'assets/{media}.mp3'+s[m.end(2):]
# Keep deterministic composition; exclude browser-only playback UI controller.
s=re.sub(r"const voice=document.getElementById\('voice'\).*?</script>","window.FILM.seek(0);</script>",s,flags=re.S)
s=re.sub(r'<div id="controls">.*?</div></div><details', '<details',s,flags=re.S)
s=re.sub(r'<details.*?</details>','',s,flags=re.S)
# Externalize vendor GSAP to avoid false-positive lint on vendor RNG/ticker functions.
m=re.search(r'<script>(/\*!.*?GSAP.*?)(?:</script>)',s,re.S)
assert m
(out/'assets/gsap.min.js').write_text(m[1]);s=s[:m.start()]+'<script src="assets/gsap.min.js"></script>'+s[m.end():]
s=s.replace('class="scene clip"','class="scene clip"')
s += '<style>body{padding:0;display:block}#frame{width:1920px;height:1080px}#composition{transform:none}</style>'
(out/'index.html').write_text(s);(out/'hyperframes.json').write_text((p/'hyperframes.json').read_text())
print(out)
