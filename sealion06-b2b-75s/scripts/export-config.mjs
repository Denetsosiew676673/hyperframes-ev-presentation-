import {mkdirSync,writeFileSync} from 'node:fs';
import {CONFIG,SCENES,DEFAULT_PHOTOS} from '../src/config.ts';
mkdirSync(new URL('../work/',import.meta.url),{recursive:true});
writeFileSync(new URL('../work/config.json',import.meta.url),JSON.stringify({CONFIG,SCENES,DEFAULT_PHOTOS},null,2));
