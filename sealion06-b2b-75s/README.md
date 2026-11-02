# BYD SEALION 06 EV — B2B product film project

**Status: production draft. No final MP4 has been generated.** The supplied original photo ZIP exceeds the download tool's32MiB transfer limit. Upload individual photos or smaller ZIP parts. The user approved supported-only wording after reconciliation; see sources/RECONCILIATION.md. Do not distribute this draft as a verified vehicle advertisement.

## What is implemented

React19 / TypeScript / Remotion4.0.484. Landscape1920×1080,30fps,2250frames,75seconds. Six independent feature sequences plus an exact120-frame(4second)white CTA. Pearl-white/gray/blue-gray palette, gentle fades, fixed-width rolling-digit columns adapted from video-shotcraft DigitRoll, thin inlineSVG graphics, original photo props with object-fitcontain. No substitute vehicle images, generated car images,3D,bounce,particles or stickers.

## Install / preview / render

```bash
npm install
npm run dev
npm run typecheck
# After photographs and specification reconciliation are complete:
npm run render
npm run finalize
```

The CLI prints the Studio preview address. Select `Sealion06`. Preview deliberately displays photo placeholders until original photographs have been connected. Render is intentionally blocked while inputs are missing; it is not represented as a complete production export.

Chromium is configured at `/usr/bin/chromium` for this cloud workspace. On another computer replace that browser path or remove the browser-executable flag to let Remotion use its managed browser. FFmpeg is needed for finalize.py.

## Configuration / source layout

- `src/config.ts`: all main copy, data, scene frame windows, fonts, colors and animation constants. Data is from the user brief until reconciled. specsVerified=true records the approved reconciliation against the user-supplied sheet, not independent manufacturer verification. Missing original photos still block production export.
- `src/Root.tsx`, `src/index.tsx`: actual2250-frame root composition and registration.
- `src/Film.tsx`: authored scene nodes, synchronized subtitle lookup, header and audio slots.
- `src/Scenes.tsx`: RangeScene,PerformanceScene,ChargingScene,AssistanceScene,ComfortScene,SafetyScene,CTAScene.
- `src/animation.tsx`: reusable RollingNumber,Fade,Stroke,CarOutline,DimensionLine.
- `src/Graphics.tsx`: energy,power,charging,ADAS and safety line diagrams. All are schematic, not measured vehicle geometry or sensor coverage.
- `src/media.tsx`: ProductPhoto; source photos are not repainted/reconstructed. No text overlays cover the pictured vehicle; graphics live in separate margins/panels.
- `scripts/narrate.py`: optional Kokoro am_michael narration generation, fixed slow synthesis rate, exact per-phrase subtitle timing. Requires local model assets plus NumPy,SoundFile,ONNXRuntime,kokoro-onnx. It rejects an overlong voice segment instead of speeding up speech.
- `scripts/check-assets.mjs`: specification,photo,audio and subtitle prerequisites.
- `scripts/finalize.py`: H264picture-copy/AACvoice mux, exact75seconds.

After originals arrive, set the image paths in production-props.json (relative to public/), for example:

```json
{"withAudio":true,"bgm":false,"photos":{"range":"photos/front.jpg","performance":"photos/side.jpg","charging":"photos/charge.jpg","assistance":"photos/cockpit.jpg","comfort":"photos/side.jpg","safety":"photos/rear.jpg"}}
```

Names above are examples, not supplied files. A blank production-props.json is supplied as an integration slot. The photo props are exposed in Studio composition defaults. Actual photographs and captions will be packaged locally so completed preview/render will not need external mediaURLs.

## Current evidence

sources/sealion06-2025-ev605-leading-plus.xlsx is byte-identical to the separately uploaded configuration sheet. extracted-config.json preserves populated specification rows. SOURCE is user-provided; no independent manufacturer authentication is claimed.0.3hours equals18minutes, whereas one row parenthetically says30minutes. Second-generation, branded Yunlian-C,HNOA/AVP names,78.7%steel,explicit7airbag total and tyre-blowout-specific stability are not all stated in the sheet. Relevant passive/active safety and highway/parking features are listed. The user approved supported-only copy; those extra claims have been removed.

Draft runtime validation: TypeScript passes; range layout still rendered successfully; English voice is generated at0.94natural synthesis rate and all phrases fit their windows without acceleration. Finalvideo,photo fidelity and independent finalreview remain pending original photos. Expected exportcheck failure is not recorded as a render pass.
