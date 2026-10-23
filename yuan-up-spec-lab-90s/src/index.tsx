import {AbsoluteFill,Composition,registerRoot} from 'remotion';
import {Film,Header} from './Film';
import {Scene} from './Scenes';
import {C} from './graphics';
registerRoot(()=> <><Composition id="YuanUp90" component={Film} width={1920} height={1080} fps={30} durationInFrames={2700} defaultProps={{bgm:true}}/><Composition id="YuanUp90ES" component={Film} width={1920} height={1080} fps={30} durationInFrames={2700} defaultProps={{bgm:true,locale:"es"}}/><Composition id="Opening" component={()=> <AbsoluteFill style={{color:C.ink,fontFamily:'Display'}}><Scene index={0}/><Header/></AbsoluteFill>} width={1920} height={1080} fps={30} durationInFrames={330}/></>);
