# UNILAND SPEC LAB · BYD Yuan UP / Atto 2

90-second English B2B product explainer. 1920×1080 landscape, 30 fps. Produced natively in Remotion 4.0.484. The user authorized extending the original 75-second brief to prioritize an unhurried narrator.

## Deliverables

- `renders/yuan-up-uniland-spec-lab-90s.mp4` — voice, keyboard SFX and quiet original light-tech music.
- `renders/yuan-up-uniland-spec-lab-90s-no-music.mp4` — identical picture and narration/SFX, no music.
- `subtitles.srt` — English text matching the spoken phrases.
- `src/` — reusable series template, separate scenes and inline SVG graphics.

## Preview / render

Node 20.19+ or 22.13+ or 24+, FFmpeg installed. Run `npm install`, `npm run dev`, then open the Studio URL it prints. Select `YuanUp90`. `npm run render` exports the silent picture, and `npm run finalize` muxes the synchronized provided WAV tracks into both final MP4 variants. System Chromium path is configurable in remotion.config.ts and package.json; remove the explicit browser flag to use Remotion's managed browser on another computer.

No external image URLs or APIs are needed during preview/render. Sources in `public/photos/` remain byte-identical to the supplied ZIP. Only their camera presentation gently scales; no repainting, color filtering or generative reconstruction. Authored overlays are inline SVG or text. Original source photographs include Chinese labels/vehicle badges; those are intentionally retained. All authored overlays and narration are English.

## Series template

Edit `src/scenes.json` for timing, title and narration; `src/Scenes.tsx` selects photos and composes graphics. `src/graphics.tsx` exposes Count, GrowingBar, Ring, DrawPath, Dimension, Icon and Reveal. `src/SeriesTitle.tsx` contains the calibrated typewriter-moves/error-retype adaptation. `src/Film.tsx` owns the authored sequence nodes, captions and audio. Each scene has a named independent sequence in Studio. Update the authored nodes and composition duration if changing timing; scene times remain sourced from scenes.json. Replace `public/audio/voice.wav` and `src/captions.json` together when replacing narration.

`src/workbench.ts` supports the video-shotcraft editing workbench with scene headings, timing, audio and caption tracks. Rhythm constants intentionally remain internal. Audio generation is optional: scripts/audio.py requires kokoro-onnx and local model paths; the finished project includes the generated WAVs, so preview/render does not need the model.

## Data and production notes

2027 model year, 401km CLTC,70kW,45.12kWh,12.8-inch,DiPilot100 and2620mm are the user's confirmed stock specification, not independently verified manufacturer claims. Atto2 is an alternate market name; actual destination versions may differ. Charging30–80%≈30min is conditional. In-stock wording and40+ countries reflect the user's explicit statements, not guaranteed current quantity or approval for every country. No specific right-hand-drive destinations are shown; the film does not call out steering position. Route graphic is illustrative, not an exact shipping network or customs-eligibility map. Seat photos demonstrate flexibility without fabricated cargo-volume data.

Gallery sources: video-shotcraft upstream 43bd349. Exact selected TSX examples are archived in reference/. The spotlight card is a deliberate2D adaptation: original3D orbit, elastic bounce, lamp flash and particles are excluded per the user's instructions. Typing preserves2f first pass,16f hesitation,1.5f deletion/retype, fixed slots, final cursor removal and50+ frame hold. Reference MP4 download endpoints returned HTTP403, so no claim of pixel-identical Gallery reproduction is made. See DESIGN-SPEC.md and review/ for checks and limitations.

Narrator: synthetic Kokoro am_michael. Music and keyboard taps: original deterministic synthesis. Fonts: Open Sans and DejaVu, licenses in reference/. Photos: user supplied. No third-party narration cloning.

Validation helpers: `scripts/check.py` requires NumPy, SoundFile and Pillow. Final mux alignment, frame count, photo hashes and video-stream identity are recorded in review/technical-check.json. Keyframe review uses the extracted final MP4 frames, not only Studio stills.
