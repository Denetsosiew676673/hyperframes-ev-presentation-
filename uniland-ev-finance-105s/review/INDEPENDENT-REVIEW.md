# Independent HTML review — 2026-10-21

Result: no release-blocking issue found in the reviewed HTML scope. No product files modified and no video rendered.

Basis: DESIGN.md, approved storyboard.json, scripts/content.py, scripts/build.py, review/browser-check.json, review/audio-timing.json, review/beat-grid.json, ten browser PNGs, and video-shotcraft references/final-review.md and aesthetic-rules.md. This is an HTML delivery review, not an MP4 review. The user's explicit HTML-only, restrained typography instructions take precedence over skill defaults for Remotion, Gallery recreation, dramatic finales and MP4 variants.

1. P1/F1/B1 ✓ Ten scenes follow the approved market-history → funding → execution → outcomes → procurement → UNILAND sequence. Duration 104.2667 seconds, nominal 1080×1920 / 30fps, under 105 seconds. Examples: scene 2 at 15.443s / f463 (previews/02.png), scene 6 at 68.105s / f2043 (06.png), procurement at 98.518s / f2956 (09.png).
2. P3/D1/C1 ✓ Revised wording retained: Byton funding and Saleen state-backed investment distinguished; 31 cars described as sold; >¥100bn explicitly a reported sample of 15 troubled firms. Broad profitability and RMB1.6bn assertions omitted. Scene 7 says delivery scale differs from sustainable profit, without claiming the listed brands are profitable. Source notes disclose all supplied pages were inaccessible through proxy 403; this is attribution review, not independent fact verification.
3. V1–V4/Q3/Q4/Q6 ✓ Solid charcoal, muted blue rules, frontal type, restrained 18px entry lift/fade, tabular counting and exactly two inline vehicle SVGs. No image assets, 3D, icons, screen pumping, glow or dramatic effects. Car outline has a small horizontal motion separately from the text lift, consistent with the approved outline exception.
4. Q11/P1 ✓ Inspected all ten scene PNGs as a contact sheet, plus scene 3 full resolution. No clipping or collision visible at the sampled settled states. Browser report additionally finds no out-of-bounds text or caption intersection in these states. Typography follows the approved 76px captions / 44px sources; these explicit project sizes supersede a literal percentage-of-portrait-height interpretation of the skill's general landscape guidance. At 390×844, the scene 2 main numbers and captions remain readable, controls fit without horizontal scrolling (document width 390), and sources/notes remain accessible below.
5. B3/R1/R2 ✓ Final wordmark and CTA have a static hold; explicit beat offsets leave the CTA settled well over one second before the end. No batch flood or collection motion requiring a physical metaphor. R3/R4 ✓ No rushed interaction simulation or whole-screen beat impulses; scene holds are 3.93–13.77 seconds.
6. Q9/determinism ✓ Browser report: byte-identical screenshots after seek 12s → 97s → 12s. Independent current-build check at every scene start +0.1s: zero future-offset reveal elements visible. End seek leaves scene 10 opacity 1 and empty finished captions. Latest year display is 2014, without thousands separator (previews/03.png, 28.308s / f849).
7. A3/S2/S3 ✓ Beat grid is deterministic 122 BPM / phase 0. Scene boundaries and visual entry offsets are multiples of four beats. Nominal frame rounding ≤0.5 frame is within the three-frame guidance. Caption phrase subdivisions are the disclosed intelligibility exception. Audio timing report shows all measured generated phrases end within their scenes; most accelerated sections reach approximately 1.65× and 1.70×, so perceptual naturalness remains a listening limitation.
8. Offline/security ✓ Embedded fonts, GSAP and both audio tracks; no runtime fetch, eval or external dependency found in authored code. Source links are explicit user-clicked references with noopener/noreferrer. Browser report records no external network requests or JavaScript errors. Independent browser opened with ordinary autoplay policy: both audio elements initially paused; a Play click starts voice and music. No autoplay. File itself contains executable presentation JavaScript as expected; no suspicious exfiltration or dynamic-code path found.
9. Playback ✓ Independent 390×844 browser run confirms user-click playback progresses (voice 0.534s, music 0.556s after short start); existing browser report confirms timeline advancement, mute, BGM-off and paused/resume controls. Playback timeline uses voice time with BGM drift correction. Public FILM.seek is a visual review hook; user seek slider separately synchronizes media and clock.
10. S/Q not applicable: existing product UI screenshot fidelity, 3D rasterization/orbits, document mocks, rounded texture masks, UI click foley and cinematic finale. No such shot is claimed or required by the approved minimal composition.

## Must fix

None established from the reviewed evidence.

## Optional refinement

None outstanding. Numeric phrases and trailing punctuation are now kept together by scripts/captions.py; no current chunk begins with stray punctuation.

## Unverified

- Human listening quality, male/business delivery naturalness, music balance and perceptual caption sync; reports and browser progression cannot establish these.
- Direct file:// launch: managed Chromium policy blocks that protocol. The review used the existing local HTTP server, did not circumvent that policy, and found no remote runtime dependency.
- Human continuous viewing and every transition frame. Separately produced continuous-playback.json confirms uninterrupted browser progression and clean automatic stop over the full duration on the prior identical audio/player version; the current visual timing/caption refinement received targeted regression checks.
- MP4 render, output codec/audio priming and render-derived beat offset: intentionally not performed because user requested no video rendering.
- Original source-page facts independently: supplied URLs were proxy-blocked, as disclosed in the artifact.
- ZIP contents/final packaging were not part of this independent review; ensure the final ZIP contains the current self-contained index.html.

## Targeted final refinement recheck

Latest enlarged 31-car count (88px) and 15-firm count (100px) inspected in regenerated previews/02.png and previews/06.png: both clear, fully visible and separated from captions. Independently swept midpoint of all 55 current caption chunks in Chromium: zero caption-bound overflow and zero intersection with currently visible body reveal/source elements. Financial phrase preservation is improved; narration windows unchanged. The separately produced continuous-playback.json was reviewed: no runtime errors, voice/music progressed throughout ten 10-second samples, music led voice by approximately 21ms, both stopped at the end and Play label restored. That run used the prior identical audio/player version.

Final timing/punctuation regression: current HTML loads and exposes working FILM API; repeated all 55 caption midpoint checks with no bounds/collision failures, and all ten scene-start checks with zero premature future reveals. Current code quantizes FILM.seek and beat entrances to 30fps. Caption data contains no leading comma/semicolon/colon/period chunks. No new release-blocking issue found.
