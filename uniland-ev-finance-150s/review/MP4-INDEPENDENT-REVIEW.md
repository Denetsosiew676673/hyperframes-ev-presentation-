# Independent final MP4 technical review

2026-10-21. Reviewed actual `renders/uniland-ev-finance-landscape-150s.mp4`, voice-only alternate, MP4-CHECK.json, all12 decoded scene JPEGs and4 transition JPEGs in review/mp4-frames. No product edits or rerender.

1. **Metadata PASS, independently probed:** H.2641920×1080,16:9,30/1fps,4486frames,149.533333s; AAC48kHz stereo. Within150s limit. Voice-only alternate has identical dimensions/fps/frame count/duration.
2. **Decode PASS, independently run:** full FFmpeg video/audio decode completed exit0 without reported errors.
3. **Alternate picture equality PASS:** compressed video-stream SHA256 matches both MP4s: `2176dd59ce2cd4617fb4461d82416ba5e62b7f069b16823896410aeefbee0b54`.
4. **Actual scene frames PASS:** inspected01–12.jpg. All three chart values/order/qualifiers/units remain correct against reviewed chart-data.json. Tick/grid alignment and note/source separation fixes survive encoding. No new truncation, collision, blank scene, unexpected chart raster replacement or obvious compression damage observed in these samples. Small attribution remains the previously accepted limitation.
5. **Actual transition samples PASS:** inspected transition-0–3.jpg. Page-plane perspective/push states are visible; partial outgoing text at moving page boundaries is intentional occlusion. Incoming chart bars/numbers do not appear before their cue in the sampled entrance. No unexpected black flash or unrelated layer appears in these four samples. These stills cannot certify every transition frame or motion smoothness.
6. **Numerical audio evidence reviewed:** MP4-CHECK.json reports four voice windows and four voice-subtracted music windows at0ms offset, correlations≈0.998 voice/0.923–0.945 music, decoded peak0.7836. This supports synchronization and headroom for the measured samples; calculations were reviewed, not independently recomputed here.
7. **Scope limits:** no subjective listening claim. Voice naturalness, perceived slower pace, intelligibility, music character/122BPM perception and caption/word alignment remain outside this technical review. Original source factual claims remain user-provided and not independently verified. Frame inspection is sampled, not continuous playback.

**MUSTFIX status: none found within the independent technical and sampled visual review.** Previous axis/overlap issues remain resolved in actual MP4. This report supplements INDEPENDENT-REVIEW.md; final metadata/decode checks are now complete, while subjective audio/continuous-playback limitations remain explicit.
