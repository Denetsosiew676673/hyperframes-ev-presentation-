import {Composition} from 'remotion';
import {Film} from './Film';
export const Root=()=> <Composition id="Sealion06" component={Film} width={1920} height={1080} fps={30} durationInFrames={2250} defaultProps={{withAudio:true,bgm:false,photos:{range:'',performance:'',charging:'',assistance:'',comfort:'',safety:''}}}/>;
