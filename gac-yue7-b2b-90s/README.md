# GAC YUE7 — Global Export Presentation

A 90-second, 1920 × 1080, 30 fps English automotive presentation made with HyperFrames.

- `GAC-YUE7-90s.mp4`: finished H.264/AAC video, including the full British male narration and understated original instrumental music.
- `index.html`: one HyperFrames composition HTML with inline GSAP, CSS, vector diagrams and photographs. Audio files use absolute HTTPS links to this repository; internet access is required for audio in this portable HTML.
- `GAC-YUE7-HyperFrames-project.zip`: complete local project, including local audio and image assets, for previewing and rendering without remote media links.
- `timing.json`: exact chapter and narration phrase timing.
- `DESIGN.md`: palette, typography and motion direction.

## Preview or render

Extract the project ZIP, open its folder in a terminal, then run:

```sh
npx --yes hyperframes@0.9.37 preview
npx --yes hyperframes@0.9.37 render --output GAC-YUE7-90s.mp4 --fps 30 --quality high
```

If the CLI does not discover an already installed Chrome, set `HYPERFRAMES_BROWSER_PATH` to its executable path.

## Chapters

- 0.00–6.71s: Opening
- 6.71–25.60s: Off-road performance
- 25.60–44.40s: Power & fast charging
- 44.40–67.05s: Space & camping
- 67.05–84.34s: Body & safety
- 84.34–90.00s: Wholesale & export CTA

## Production notes

Vehicle photography was supplied in `GAC Yue7.zip`. Product specifications and English narration are based on the provided brief. The chapter timing was expanded to 90 seconds at the requester’s direction. The voice is locally synthesized with Kokoro `bm_george` (British male). The accompanying instrumental bed is an original synthesized composition. Technical vector drawings are schematics.

All narration is retained. Numeric callouts use a short upward fade, a two-second hold, then a soft fade out. Scenes dissolve and photographs move slowly. No Chinese captions, neon flashes or rapid cuts are used.
