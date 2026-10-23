# Independent Spanish localization review

Reviewed 2026-10-23. Scope: Spanish narration/subtitles, retained English visual cards and English default. No production source edits by reviewer. Inspected audio-es.py, finalize-es.py, Film.tsx, index.tsx, final captions/script/timing JSON, es-space.png, final review/es/contact-sheet.jpg, full-size f1260/f1680/f2130 and review/es/technical-check.json. English visual/design findings remain in independent-review.md.

## Findings

- ES1 ✓ Translation preserves 2027/Yuan UP/Atto 2,401km CLTC,70kW front motor,45.12kWh Blade LFP,30–80%≈30min,12.8-inch/DiLink100,360°/DiPilot100,2620mm, five doors/five seats and export services. Decimal values are correctly expressed with Spanish “coma.” No new numerical claim was introduced.
- ES2 ✓ Revised “conducción inteligente y con confianza” preserves the original confidence claim without strengthening it into a safety guarantee. “Abatibles por secciones” preserves split-folding detail. Both revisions appear in final captions and final frames f1680/f2130.
- ES3 ✓ Charging conditions remain explicit in the following Spanish phrase. Export wording preserves stock, configuration verification, pre-shipment inspection, documents and international logistics. Company40+ country export history remains an English visual card, as authorized. Localization does not introduce named destinations or steering-position emphasis.
- ES4 ✓ locale="es" selects captions-es.json and voice-es.wav together. YuanUp90ES supplies that locale; ordinary Film and Captions default to English, and YuanUp90 retains its original default properties. Shared scene components/photos, English parameter cards, header, disclaimers and CTA remain unchanged.
- ES5 ✓ Source requests Spanish Kokoro em_alex with lang='es'. All seven measured scene tempos are0.94; none speeds speech up. Speech windows end10.219/21.715/35.466/46.264/59.013/75.465/88.827s, fitting their corresponding scene boundaries. This supports unhurried scheduling; perceived naturalness is not a claimed listening result.
- ES6 ✓ Captions derive from separately synthesized, boundary-trimmed phrase durations, adjusted by the applied tempo. Spanish subtitles and narration use the same script strings. Source schedule contains no truncated phrase or overlap with the next scene.
- ES7 ✓ Final frames show accented Spanish characters correctly, with clean one/two-line subtitle wrapping. Long charge/cockpit/space captions remain inside the subtitle area without clipping or overlap with photo/card content (f1260/f1680/f1980/f2130). Independent Open Sans56px font-width check of all14 phrases predicts at most two lines within1700px. Small English metadata retains the previously reported readability limitation; this localization does not worsen its size.
- ES8 ✓ Final ES main/no-music outputs are90.000s,1920×1080,30fps,2700 frames,H.264/AAC48kHz. Their encoded picture hashes match, so only their audio mix differs. ffprobe confirms the Spanish audio stream language tag is spa.
- ES9 ✓ Technical evidence records decoded peak−1.77dBFS and source-to-final audio correlation lags0,0,0,1sample at12/29/50/82s. No clipping or material mux offset is indicated. This is technical timing evidence rather than perceptual lip/word synchronization assessment.
- ES10 ✓ English delivery files retain their previously recorded byte sizes, and the original English main video's encoded picture SHA256 remains80f4798d3a4caa27b62fcc43871e21b8123cc84b02ed34b7ddd6cf745b5d5303. English source defaults are preserved. Whole-file prelocalization SHA256 was not supplied, so byte-for-byte identity of every English audio/container byte is not independently certified.

## Disposition

No blocking translation, subtitle overflow, locale-wiring or rendered-metadata issue found. The two identified translation precision issues were corrected before this final review.

Unable to verify without listening: actual male timbre, Spanish accent/pronunciation (including brand/model names), perceived calmness, speech intelligibility, music balance and keyboard audibility. No actual listening pass is claimed. Every-frame motion between sampled frames and exact subtitle glyph-pixel height were not measured; inherited visual restrictions and reference limitations are covered in the English review.
