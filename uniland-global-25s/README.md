# UNILAND MOTORS — Ocean to Orbit

A 25-second English B2B brand video reconstructed from the user's two keyframes.

- 0–15 seconds: coastal vehicle lineup, editable brand title and light sweep, staggered tagline, four service icons aligned to spoken phrases, slow Ken Burns.
- 15–25 seconds: globe, six independently drawn routes with traveling lights, six rolling odometer statistics, concluding mission text.
- Male English narration, phrase-aligned English subtitles, original quiet synthesized ambience.
- 1920×1080, 30fps, H.264 / AAC MP4.

## Download / watch

- [MP4](renders/uniland-global-25s.mp4)
- [English subtitles](subtitles.srt)
- [Cover preview](previews/cover.jpg)
- [Footprint preview](previews/footprint.jpg)

On GitHub, open the MP4 and choose **Download raw file**. Serve `watch.html` with a static HTTP server for a minimal video player.

## Development

```sh
npm run dev -- --background
npm run check
npm run render -- --output renders/uniland-global-25s.mp4 --fps 30 --quality high --workers 4
```

CLI is pinned. The wrapper selects a writable npm cache and system Chromium when available. Override with EV_NPM_CACHE / HYPERFRAMES_BROWSER_PATH as appropriate.

Edit `scripts/build.py` for composition and choreography; run `python3 scripts/build.py` to regenerate HTML/SRT from measured `timing.json`.

To regenerate voiceover, install `scripts/requirements.txt`, obtain the official Kokoro ONNX v1.0 model and voice pack and place them under `/workspace/ev-tools/models` as `kokoro.onnx` and `voices.bin`; then run `python scripts/narrate.py`. Use the generated narration.wav through loudnorm (-17 LUFS, -1.5dBTP) to update narration-master.wav. `scripts/soundbed.py` synthesizes the original ambience. These files are already included; no model or credentials are needed to render.

## Source fidelity

The user supplied reference images inline in chat. Backgrounds are AI-cleaned/reconstructed interpretations, not extracted pixel-identical source images, so exact vehicle details may differ. Titles, service icons, routes, figures and captions are separate editable animation layers. Typography is recreated, not an official vector logo. No 3D vehicle mesh is used.

The user explicitly confirmed **10,000+ means cumulative deliveries**, not inventory. Other statistics are supplied by the user, not independently audited. Route lines are schematic visual connections, not verified shipping lanes. The second narration was shortened to fit ten seconds at a natural pace; all six figures remain on screen. See SCRIPT.md and STORYBOARD.md.
