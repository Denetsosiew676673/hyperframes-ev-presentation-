import React from 'react';
import {Composition} from 'remotion';
import {Film,TOTAL,Hero,Reach,Partner} from './Film';
export const RemotionRoot:React.FC=()=> <>
 <Composition id="Uniland15" component={Film} durationInFrames={TOTAL} fps={30} width={1920} height={1080}/>
 <Composition id="BrandHero" component={Hero} durationInFrames={165} fps={30} width={1920} height={1080}/>
 <Composition id="GlobalReach" component={Reach} durationInFrames={140} fps={30} width={1920} height={1080}/>
 <Composition id="PartnerCTA" component={Partner} durationInFrames={145} fps={30} width={1920} height={1080}/>
</>;
