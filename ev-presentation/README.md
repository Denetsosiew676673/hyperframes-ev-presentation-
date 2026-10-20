# Uniland · Global Momentum

Six-scene, 1920 × 1080 HyperFrames presentation with local English narration and subtitles. White / pearl / glass visual system, 3D layer entrances, title sweeps, line reveals and numerical glow.

**Status:** typography/data review draft. Original slide image files are required for image-faithful completion. See SOURCE-NOTES.md.

## Preview and export

```sh
npm run dev -- --background
npm run check
npm run render -- --output renders/uniland-review.mp4 --fps 30 --quality high --workers 2
```

Open the project in HyperFrames Studio to scrub or play the timeline. `presentation.html` provides a video player with six chapter buttons and keyboard navigation after export; serve this directory with a static HTTP server. MP4 export includes narration and burned-in subtitles. `subtitles.srt` is also supplied separately.

## Edit

- `content.json`: editable copy, facts, and narration.
- `schedule.json`: measured audio timings.
- `scripts/build.py`: compiles HTML and SRT from content and timings.
- `assets/voice-*.wav`: generated English Nova voice, speed 0.94.
- `DESIGN.md`: palette, typography and motion rules.

Run `python3 scripts/build.py` after edits that do not alter narration duration. To regenerate narration, use a Python environment with kokoro-onnx and soundfile, and set EV_TTS_MODELS to a directory containing `kokoro.onnx` and `voices.bin` from the official Kokoro v1.0 model release. Then run `python scripts/voiceover.py` followed by `python scripts/build.py`. This task's tools are in `/workspace/ev-tools/venv`; models in `/workspace/ev-tools/models`.

The CLI wrapper selects a writable temporary npm cache and uses system Chromium when available. Override with EV_NPM_CACHE or HYPERFRAMES_BROWSER_PATH if needed. No API key is required. CLI is pinned in package.json.
