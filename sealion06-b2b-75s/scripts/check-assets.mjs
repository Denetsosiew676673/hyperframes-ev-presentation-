import {existsSync,readFileSync} from 'node:fs';
import {resolve} from 'node:path';
const root=resolve(import.meta.dirname,'..');
const config=readFileSync(resolve(root,'src/config.ts'),'utf8');
if(!/specsVerified:\s*true/.test(config))throw new Error('Configuration table has not been read and reconciled. Production export is blocked.');
const required=['range','performance','charging','assistance','comfort','safety'];
const propsPath=resolve(root,'production-props.json');
if(!existsSync(propsPath))throw new Error('production-props.json must map each scene to its original supplied photograph.');
const props=JSON.parse(readFileSync(propsPath,'utf8'));
for(const key of required){const path=props.photos?.[key];if(!path||!existsSync(resolve(root,'public',path)))throw new Error(`Missing supplied photograph: ${key}`);}
if(!existsSync(resolve(root,'public/audio/voice.wav')))throw new Error('Verified, timed English narration has not been generated.');
const captions=JSON.parse(readFileSync(resolve(root,'src/captions.json'),'utf8'));if(!captions.length)throw new Error('Timed subtitles missing.');
console.log('Verified specifications, all six photo slots, narration and caption assets found.');
