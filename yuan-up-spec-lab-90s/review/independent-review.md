# Independent final review

Reviewed 2026-10-23. Independent reviewer did not modify production source. Baseline: latest user constraints in requirements.json; DESIGN-SPEC.md (90-second revision supersedes its initial 75-second table); README; exact archived TypewriterErrorRetype.tsx and SpotlightHeroCard.tsx; final-review.md and aesthetic-rules.md. Reviewed source, captions, audio-generation/mux code, final MP4 metadata, technical-check.json, contact-sheet.jpg and full-size final frames. Added reviewer-f1200.jpg from the final MP4 because the contact sheet's f1080 samples the charging transition rather than its settled state.

Final outputs: yuan-up-uniland-spec-lab-90s.mp4 and yuan-up-uniland-spec-lab-90s-no-music.mp4. Both are 90.000 seconds, 1920×1080, 30fps, 2700 frames, H.264/AAC 48kHz. Their encoded video stream hashes match. This is a visual/source/technical review, not a claimed listening pass.

## Product and completeness

- P1 ✓ Compact urban EV positioning and B2B export proposition are clear: f180, f450, f2490.
- P2 ✓ User-prioritized range, motor, battery, charging, cockpit, space and export support each receive a distinct scene.
- P3 ✓ Specifications and stock language match the recorded user-confirmed brief. CLTC/charging/market disclaimers appear. 40+ countries is explicitly company export experience, not model certification (f2490). Manufacturer accuracy remains unverified independently.
- P4 ✓ Requirements map to implemented photographs, restrained SVG overlays, subtitles, scene windows and narrator audio generation.
- F1 ✓ All required information visible: f180 identity; f450 range/motor; f825 battery; reviewer-f1200 charging; f1530/f1680 cockpit; f1980/f2130 wheelbase/seats; f2490 export/CTA.
- F2 ✓ Scenes introduce distinct information. Stock appears in the opening and export scene as introductory availability and final commercial CTA, not a duplicate scene.
- F3 ✓ Range/charge indicators, battery schematic, photographed camera display and upright/folded cargo comparison convey their subjects. Seat schematic is countable and does not invent cargo-volume data (f2130).

## Visual and reference fidelity

- V1 ✓ Charcoal/cyan, restrained sans typography, open spacing and large specification hierarchy are consistent across final frames.
- V2 ✓ Source uses bounded ease-out translations, slow contained 1.5% photo scale and 12-frame crossfades. No bounce, 3D, camera shake, particles or flashes found in implemented source or sampled frames.
- V3 ✓ No unrelated visual-style drift found.
- V4 ✓ User prohibitions are respected in the inspected source. Source photo hashes match the 23-file manifest; photographs are not repainted or filtered. Opening has a temporary spotlight darkening overlay, as documented by the selected 2D adaptation.
- S1 ✓ Both selected recipes appear: error/retype series header and opening single spotlight photo card.
- S2 △ Exact TSX variants are archived and identified. Gallery reference MP4/contact-sheet inputs are unavailable; dynamic Gallery equivalence cannot be verified.
- S3 ✓ Source preserves typewriter 2f first pass, 16f hesitation, 1.5f deletion/retype, fixed character slots and cursor removal. Opening preserves spotlight lock34, push40–58, rise56–66, scans68–82/88–108 and reseat124–142. Original perspective, overshoot and flicker are deliberately overridden by explicit user restrictions.
- S4 ✓ Fixed-left typing does not recenter; final header is stable after completion. Photo remains a single coherent hero, and card motion settles before hold.
- S5 ✓ Brand/photo adaptation is visually coherent (f95/f180). No sampled badge, wheel or screen obstruction from authored graphics found.
- S6 △ This is explicitly a custom 2D adaptation, not pixel-identical reference reproduction. Missing preview assets prevent comparison to actual reference playback.

## Storyboard, assets and technical quality

- B1 ✓ Source scene windows are 0–11, 11–24, 24–36, 36–48, 48–63, 63–77 and 77–90 seconds, matching the authorized revision.
- B2 ✓ Photographs, captions and scene information match the final scene data. Final range frames no longer contain the earlier clipped small label (f450/f615).
- B3 ✓ Series header completes near f95 and remains visible for the rest of the film. Opening hero reseats at142, then holds. Other schematic motions settle well before scene ends. Final CTA remains present through f2699.
- B4 ✓ No unexplained additional or removed major scene found against the revised timeline.
- D1 ✓ User-confirmed stock specifications are distinguished from independent manufacturer verification in project documentation.
- D2 ✓ No keys, personal records or internal addresses found in inspected source/frames.
- D3 ✓ Actual supplied car and cockpit photographs are used; no fabricated product interface replaces the photographed screen.
- D4 ✓ Sampled final frames show loaded photos/fonts and clean masks. Both final video streams are identical; deterministic source uses frame-derived animation.
- D5 △ Export stock/spec truth relies on user confirmation; no manufacturer or customs certification evidence was supplied. Route map is illustrative and names no right-hand-drive destinations.

## Audio and timing evidence

- A1 △ Source mix provides low-amplitude original music under narration; perceptual music balance and voice intelligibility are unverified without listening.
- A2 ✓ Keyboard events share exact frame formulas with visual character events in source. Rendered mux cross-correlation probes report 0,0,0 and1 sample lag at12/29/50/82s. Audible tap prominence remains unverified.
- A3/A4 N/A No strong music-beat cutting or riser/impact/sparkle ending is specified; calm narration and restrained motion supersede those recipes.
- A5 ✓ No long external SFX samples are used; generated key taps are30ms with immediate decay.
- A6 △ Decoded final peak is -1.60dBFS (technical-check.json), so no clipping is indicated. Whether every tap is perceptually audible was not verified.
- A7 △ Short generated taps combine noise and a damped sinusoid. Whether they read as keyboard texture rather than synthetic UI tones needs listening; no claim of verified physical timbre is made.
- A8 ✓ Music/no-music files exist and have identical encoded video hashes. Mux code retains the same narration and keys in both.
- A9 ✓ Technical-check.json records output correlation probes, and check.py describes the measurement. Film is not SFX/beat dense; no universal AAC offset was guessed.
- A10 ✓ audio.py synthesizes phrases independently, trims only boundary silence with safety margins, then derives captions from measured phrase duration and tempo. First six scenes use tempo0.94; final uses0.9848, with no tempo above1.0. All speech fits the corresponding window. Male am_michael identity is configured; perceived gender, pace and pronunciation remain unverified without listening.

## Aesthetic checklist

- R1 ✓ Opening brand/header and information hold exceed1s; final CTA has extended hold.
- R2 ✓ Count/bar/cell/line animations use non-linear easing and settle; no mass flood sequence requires accelerating deal rhythm.
- R3 ✓ Opening arc runs through142f (4.73s); scene lengths11–15s support reading and speech.
- R4 ✓ No full-frame beat pumping or impact flashes found in source.
- Q1 ✓ Real photographs/photographed screen; custom graphics are clearly schematics, not simulated product UI.
- Q2 N/A No3D textures or perspective magnification.
- Q3 ✓ No handheld/shake code; inspected frames are stable in composition.
- Q4 ✓ Only the opening hero receives restrained two-pass outline scans, following its selected reference timing; no mass glints. Reference's two scans are documented rather than treated as repeated hero treatments.
- Q5 ✓ One primary vehicle-photo hero in opening.
- Q6 ✓ Information remains frontal, with no perspective compression.
- Q7 N/A The skill's 3D orbit formula conflicts with explicit2D-only user direction.
- Q8 N/A Particle/crane launch-style finale conflicts with the calm restrained direction; export CTA is the appropriate finish.
- Q9 N/A No flying UI elements seeking page slots.
- Q10 N/A No mock document/report scene.
- Q11 ✗ Minor readability exception: footer metadata24px, icon labels24–29px and several subordinate labels are below the skill's32px auxiliary target (f1530/f2130/f2490). Captions are56px CSS, but actual glyph-pixel minimum has not been measured; they look clear at full1920px and substantially denser in a480px player. Essential specs are large. This is a small-player readability limitation, not a missing content issue.
- S1 △ Quiet music direction correctly follows the user rather than the skill's generic high-energy recommendation. Timbre judgment needs listening.
- S2 ✓ Taps are explicitly frame scheduled; randomized deterministic noise varies each tap. Same-level repeated typing is intentional reference behavior; no accelerating card flood is present.
- S3 ✓ Final source shares typewriter event formulas with audio generator; current timing fits the90s revision.
- S4 △ Typing has corresponding short taps; perceived physical quality unverified.
- S5 ✓ Mux alignment is measured in technical-check.json; peak attack perceptual alignment is not claimed from listening.
- C1 ✓ Each content scene has aligned narration/captions, with only short breathing gaps.
- C2 ✓ Copy names concrete features and business services; some restrained benefit headings remain, supported by specific adjacent values.
- C3 N/A No3D annotations.
- P1 ✓ Fresh final frames and contact sheet inspected; additional charge frame extracted independently.
- P2 ✓ Exact reference timing/adaptation choices are documented; no claim of missing reference video inspection.
- P3 N/A No ambiguous feedback implementation decision was part of this independent review.
- P4 ✓ Distinct feature-to-scene mapping, with only opening using the selected hero treatment.

## Disposition

Must fix: No critical product omission, source prohibition violation or visible overlap found in the inspected final frames. The earlier range clipping is absent in final f450/f615.

Suggested optimization: Increase subordinate labels/footer size for small embedded playback, or explicitly document the Q11 metadata exception. Current essential specifications and narration captions remain prominent.

Unable to verify: Actual listening quality (male timbre, calm delivery, pronunciation, music balance, keyboard realism/audibility); every-frame playback quality between sampled frames; pixel-level actual subtitle glyph height; Gallery playback fidelity without reference video; independent manufacturer/spec/stock/export accuracy. Do not describe these as verified passes.
