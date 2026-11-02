# Independent prepared-draft review

2026-11-02. Scope: source, reconciliation, narration metadata, seven rendered layout stills (frames 200, 600, 900, 1250, 1600, 1930, 2190). This is **not final-film approval**. No final MP4 or original vehicle photographs exist in the reviewed project. No audio listening was performed. Reviewed against parent video-shotcraft final-review.md and aesthetic-rules.md; user minimal/muted direction supersedes high-energy defaults.

## Updated still reinspection

The producer revised typography and replaced the power curve after the initial findings. I reopened all seven updated frame files. Frame 600 now shows a simple drive/axle schematic with no measured-looking ascending curve: that concern is resolved. Labels and footnotes are visibly larger, subtitles now nominally 56px, auxiliary labels mostly 32px. No overlap or clipping appeared in these revised stills; frame 200/1250 two-line captions fit above the footer. Strict Q11 effective glyph-height measurement remains unverified: nominal CSS size is not rendered ink height. The typography findings below describe the initial revision and should not be treated as current nominal-size failures. Original-photo and final-MP4 limitations remain unchanged.

## Required fixes / blockers

- D4 / F1 ✗ Frames 200–1930: six obvious ORIGINAL PHOTOGRAPH PENDING panels. Real Sealion06 identity, source-photo preservation, feature relevance, annotation accuracy, vehicle visibility and photo integration cannot pass until actual supplied assets arrive. Export guard intentionally rejects missing photographs; this is correct blocking behavior, not successful rendering.
- Q11 initial finding, subsequently mitigated (effective-pixel verification pending): All narrated scenes: SubtitleLayer uses fontSize 54, below the rule’s 56px minimum even before measuring glyph height. Qualifiers are 26–27px (frames 200, 900, 1250), metadata 25px, eyebrows 24px and several graphic labels 25–29px, below auxiliary 32px requirement. Increase effective rendered readability and recheck lower-panel fit. Several letters have effective ink heights smaller than nominal sizes; do not treat CSS size alone as proof. CTA text is large and unobstructed at frame 2190.
- D1 / P3 initial concern, subsequently resolved in updated frame 600: PowerArc is an arbitrary ascending Bézier curve next to acceleration/power figures, without plotted variables or source samples. README calls all graphics schematic, but that qualification is not visible in the film. The graphic risks reading as measured power/acceleration data. Replace with an unmistakable nonquantitative drive schematic or remove; do not invent a measured curve.
- A / P1 unable to verify: no final exported audio/video, no listening test, no actual subtitle-vs-speech review, no rendered mux synchronization, clipping or transitions review. Kokoro am_michael selection and metadata support male synthetic English intent only, not verified perceived calmness or pronunciation.

## Product, function, direction and timeline

- P1 ✓ Model and bulk-order intent are clear in header and CTA (200, 2190).
- P2 / P4 / F1 ✓ at draft level: six separate feature windows map to range/battery, motor/acceleration, charging, assistance, space/suspension, occupant safety. Final photo-based demonstration remains blocked.
- P3 / D1 ✓ textual reconciliation: current config omits second-generation, Yunlian-C, HNOA/AVP brand names, 78.7% steel, explicit seven-airbag tally and blowout-control claims. Reviewed extracted sheet rows support 605km, 78.72kWh, 180kW, 7.7s, 2820mm, five seats, Blade LFP and generic assistance/safety wording. Supplied spreadsheet is the evidence boundary, not manufacturer authentication.
- D1 ✓ conditional approved charge treatment: 0.3h × 60 = 18min; source row 8 conflicts with its parenthetical 30min, while rows 57–58 state 0.3h / 30–80%. RECONCILIATION records explicit supported-only approval and conditions. Frame 900 includes charge conditions; keep that qualification readable.
- F2 △ Main scenes provide different information, but range repeats 605km on a decorative scale; comfort repeats 2820mm on dimension rail. Acceptable reinforcement, not new evidence. Generic rolling/fading vocabulary repeats by the explicit restrained user brief; document exception to P4’s unique-technique default.
- F3 △ Schematic ADAS lane/parking and safety silhouettes communicate categories, not measured coverage or confirmed vehicle geometry. Four safety dots must not be presented as an airbag tally/location map. Actual feature-photo relevance remains unverified.
- V1 / V3 / V4 ✓ Seven stills use pearl, gray, graphite and muted blue with ample whitespace and no neon/ink/cyber drift.
- V2 / S3 ✓ source-level only: cubic ease-out and fixed-width digit strips; no elastic/spring/bounce override, handheld motion or random animation found.
- S1–S6 △ DigitRoll reference source is archived and implementation explicitly adapted. No exact Gallery variant is claimed; no sample-equivalence judgment is possible or required. Code retains fixed slots, full digit strip and 4-frame stagger; slows roll to 32f without overshoot.
- B1 ✓ Source windows total 2250 frames = 75s at 30fps; dimensions 1920×1080. Six windows 0–14/14–24/24–34/34–46/46–58/58–71, CTA 71–75.
- B2 ✓ code/metadata alignment: all narration windows fit; latest assistance end 45.758s leaves ~0.242s before next scene. Phrase timings derive synthesis samples rather than word counts. Auditory synchronization still unverified.
- B3 ✓ source-level: all core metrics settle well before cuts; fixed header remains. CTA is wholly static for frames 2130–2249 (120 frames, 4s); frame 2190 confirms white, centered two-line CTA.
- B4 △ No final approved storyboard/change-history artifact was available beyond DESIGN-SPEC and reconciliation; cannot establish historical compliance.
- D2 ✓ No exposed personal data, secrets or internal addresses observed in visible stills.
- D3 N/A: not a product-software UI reconstruction.
- D5 ✓ user-provided configuration source is identified and frozen locally; no live data feed.

## Aesthetic checklist

- R1 ✓ source-level settled information and static CTA hold; R2 ✓ nonlinear easing, no batch flood; R3 △ long readable scene holds, but the default ≥3s opening action arc is intentionally superseded by minimal user direction; R4 ✓ no beat pumps/whole-frame impacts.
- Q1 N/A software UI; Q2 N/A no 3D textures; Q3 ✓ code contains no shake; Q4 ✓ no glints; Q5 △ opening has two metrics and a photo slot rather than a single animated object, consistent with six-scene minimal information brief; Q6 ✓ frontal typography.
- Q7 / Q8 N/A user requested restrained flat photos and static white CTA, superseding orbit/material/family-photo energy defaults; Q9 N/A no flying UI; Q10 N/A no document replica; Q11 △ updated nominal sizes meet the numeric font-size targets, but effective glyph-height verification remains pending.
- S1 △ voice-only is documented; no BGM supplied or required, so strong electronic music default does not apply. S2–S5 N/A no SFX or beat synchronization. Audio output quality remains unverified.
- C1 ✓ text/narration match scene topics; no unexplained animated scenes. CTA narration is represented by its clean static CTA, with subtitles intentionally hidden there. C2 ✓ concrete specs/functions support claims, although titles are generic benefits. C3 N/A no 3D.
- P1 ✓ seven draft stills inspected, with no unintended overlaps or clipped text seen; not a full-frame/transition/final render check. P2 △ no reference-video breakdown available or claimed. P3 △ no ambiguous-feedback history assessed. P4 △ six functions mapped, restrained recurring motion exception as above.

## Validation and limitations

Independent npm run typecheck passed. Studio registration defaults to withAudio:true with blank photos and obvious placeholders; still rendering demonstrates core composition execution, but I did not separately launch interactive Studio. README incorrectly says a draft badge remains until photos are connected: DraftFlag depends only on specsVerified, now true; placeholders carry missing-photo status. This documentation mismatch is minor and should be corrected.

Final disposition: prepared editable draft, blocked for production delivery by missing originals. Typography was enlarged and the ambiguous power curve removed in the rechecked revision. Integrate original photos, render final MP4, inspect transitions and actual pixels, listen to voice/pronunciation, verify encoded audio/subtitle sync, and perform a fresh independent final review. No final-video/photo fidelity claim is supported by this review.
