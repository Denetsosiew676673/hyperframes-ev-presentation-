# UNILAND MOTORS · World Ready ·15seconds

A narration-led B2B vehicle-sourcing brand film built with **video-shotcraft + Remotion** in autonomous creation mode.1920×1080 /30fps /450frames. Final video, audio and container duration are all exactly15seconds.

## Watch / download

- [Final MP4](renders/uniland-shotcraft-15s.mp4)
- [Brand preview](previews/01-brand.jpg)
- [Global reach preview](previews/02-global.jpg)
- [Partner invitation preview](previews/03-partner.jpg)
- [Design and frame plan](DESIGN-SPEC.md)
- [Independent review](review/INDEPENDENT-REVIEW.md)
- [Audio alignment measurements](review/AUDIO-ALIGNMENT.json)

On GitHub, open the MP4 and choose **Download raw file**.

## Content and motion

1. Vehicle sourcing: a crisp coastal vehicle hero,0.35/0.7/1.4multiplane depth, a late lift and bold brand typography.
2. Global reach: two independently drawn100-segment cubic light paths,10,000+ cumulative deliveries,300+ dealers,40+ countries.
3. Partnership: representative business elements assemble around the wordmark;4°crane, letterpress reveal, stage light, large website URL.

Male English narration, readable phrase-aligned English captions, sparse cinematic sound design. No background-music recording in this edition. Narration text and sample-derived phrase boundaries are in timing.json; generated copy src/timing.json is used by the workbench.

The source hero/globe plates were reconstructed from the user's keyframes in the earlier project, so exact original vehicle details may differ. These are not claimed to be untouched photographs or official website screenshots. Brand typography is recreated text. The effect is2.5D, not a3D vehicle mesh. The user confirmed10,000+ means cumulative deliveries, not current stock; other numbers were supplied by the user.

## Run and edit

```sh
npm ci
npm run dev
npm run typecheck
npm run render
```

Remotion CLI and runtime pinned to4.0.484. System Chromium is configured at/usr/bin/chromium; set a suitable executable for another machine. In this cloud machine, set npm_config_cache=/tmp/ev-npm-cache if the default npm cache is unwritable.

- src/Film.tsx: scenes, editable defaults, shared SHOTS / CAPTIONS / SFX tables.
- src/workbench.ts: editable shot/typography/color and multitrack manifest, importing the same tables.
- scripts/narrate.py: optional voice regeneration using local Kokoro-ONNX and soundfile; voice files already included for rendering.
- scripts/finalize.py: uniform render-pipeline audio compensation. It copies video unchanged and corrects this measured Remotion/AAC pipeline's2048-sample priming delay, padding/trimming final audio to15seconds.
- scripts/check-audio.py: verifies finalized mix delay and individual SFX probes. Re-measure after changing renderer/codec/sample rate; do not blindly transfer this pipeline constant.
- scripts/parity.mjs: project-adapted skill parity check (portable fs copy instead of unavailable rsync; explicit system Chromium).

## Editing workbench

When video-shotcraft is installed at../.agents/skills/video-shotcraft:

```sh
node ../.agents/skills/video-shotcraft/workbench/scripts/open.mjs "$PWD" --no-open
node scripts/parity.mjs --frames 150,285,420
```

Use `--frames 150,285,420` with a space when invoking the parity script. The local workbench opens on port5198 and imports the film as shots, captions, narration and sound effects. Three inspected frames match the original composition with zero differing pixels.

## References and attribution

Shot recipes: depth-layer-moves /multiplane; glow-flyline-moves /flyline-arc; outro-group-photo-launch. Current demo code was used for motion parameters; downloaded historical Gallery previews differ from current demos. Exact Gallery-video equivalence is not claimed. See DESIGN-SPEC.md and the independent report.

Audio sources are mapped in reference/USED-AUDIO.md. Retained reference/TSX and Gallery movies are verification references, not footage in the final video. Brand imagery came from this user's project context.

## Optional follow-up

The film belongs to the user. When publishing, credit to the skill author is optional: [X @VincentWei93](https://x.com/VincentWei93), [Douyin @Vincent](https://www.douyin.com/user/MS4wLjABAAAAK1pkjBxilk2Oi_9h_vFyD-lTAu9CTlvhmOtkosDvvxg), [Xiaohongshu @Vincent](https://xhslink.cn/m/At9iP2d5C1V).

You may optionally submit the film to the [video-shotcraft showcase](https://vincentwei1021.github.io/video-shotcraft/showcase.html) using its [submission form](https://github.com/Vincentwei1021/video-shotcraft/issues/new?template=showcase.yml); the form lets you include your social profile so viewers can find you.

A Jianying/CapCut project export can also be prepared on request, for editing captions, shot order/speed and audio in that editor.
