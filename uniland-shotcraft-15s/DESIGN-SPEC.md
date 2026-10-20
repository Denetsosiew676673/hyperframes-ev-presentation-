# UNILAND MOTORS · World Ready · 15s

## Mode and product brief
User selected autonomous creation: continue through the final MP4 without creative approval gates. Audience: B2B vehicle dealers. Core offer: vehicle sourcing and export, new/used/electrified vehicles and parts. Evidence: user's company keyframes and previously confirmed cumulative delivery interpretation. Do not claim 10,000+ is inventory. No private customer data or invented services.

## Requirement → execution
- 15s: exactly450 frames at30fps, 1920×1080 landscape.
- English voiceover: calm American male, about30 words, measured and aligned to three shots.
- Advanced, nonrepetitive animation: multiplane rail, flyline arc, and group-photo launch; distinct principal technique in each shot.
- Brand: retain navy/white/ice-blue, real source-derived city/vehicle and globe plates, not paper/amber template styling.
- Data: prominently show 10,000+ delivered; 300+ dealers and40+ countries as secondary supplied proof. No need to squeeze all six old25s metrics into15s.
- Delivery: rendered MP4, editable Remotion project, screenshot previews and review report. GitHub delivery as previously requested.

## Direction selection
Considered: cinematic ocean-to-orbit, white editorial, paper/ink. Selected ocean-to-orbit because the supplied keyframes already establish coastal vehicle lineups and a blue orbital network; preserves context rather than importing unrelated software/paper metaphors.

## Tokens
Background #031425; text #F3F8FF; secondary #C1D5EA; emphasis #96D3FF; restrained route light #F5CBA3. Local Brand sans (regular/bold) and Data mono. Brand title140–160px, secondary readable text44–52px, English narration captions76px (actual glyph target≥56px). Main reading layers remain sharp; blur is reserved for near decorative shapes and remote atmosphere.
Spacing:96px safe edges, generous open left/right zones. Surfaces:20px corner radius, low blue-silver edge, tight contact shadow; avoid glass-card slideshow. Brand-mark typography recreated, not an official vector logo.
Motion: professional trust / restrained premium. Continuous rail ease(0.45,0,0.18,1), 0.35/0.7/1.4 layer speed ratios. Flyline22f out-cubic; conditional head removal, settle by86f. Outro flying elements12f with bezier(0.34,1.4,0.44,1), 4° crane over40f, wordmark letters42+i*1.8 with8f press, final hold≥30f.

## Styleframe decision
Skip a new direction-proposal styleframe because the user supplied explicit brand-cover and globe keyframes, and retained plates/tokens were already visually checked in the25s project. New composition stills will validate the new three-shot arrangement before full rendering.

## Function → Gallery card mapping
- Brand + vehicle sourcing: depth-layer-moves / multiplane, demo MultiplaneReal.tsx. Adapt page layers to one vehicle hero plate, spatial service tags and static brand title. Preserve rail timing and late hero lift.
- International reach + cumulative deliveries: glow-flyline-moves / flyline-arc, demo FlylineArc.tsx. Use two sequential cubic arcs on globe,22f growth,100 segments, conditional light head and10f tail settle; settle by86f. Fewer than3 routes, so no relay-style requirement.
- Partner CTA: outro-group-photo-launch / outro-group-photo-launch. Reuse edited brand-representative panels and categories, four-way entry, genuine overshoot,42f wordmark press,4° crane, calibrated cool stage lighting; no reused tagline.
Reference demos and matching Gallery MP4s retained under reference/. These are motion references, not assets inserted into the commercial.

## Frame plan
| Shot | From | Duration | Content / action | QA frames |
|---|---:|---:|---|---|
| Hero |0|177|Brand headline, one coastal vehicle hero panel; three depth speeds, late lift. NEW / USED / EV & PHEV / PARTS labels enter as one spatial service group.|30,100,150|
| Reach |165|152|Globe, two connected luminous paths, sharp10,000+ delivered,300+ dealers,40+ countries; everything settled by local86f.|185,220,285|
| Partner |305|145|Representative image/label elements fly into final slots; crane settles; wordmark press and large URL. Final logo/URL hold≥30f.|320,365,420|

## Voiceover plan
Uniland Motors. Your global vehicle sourcing and export partner. New cars, used vehicles, and electrified models. Over ten thousand vehicles delivered. Connect with our team.

Use short phrase-aligned subtitle groups, not one tiny sentence strip. Closing URL visible rather than spoken to protect delivery pace.

Outgoing hero/reach layers retain12 frozen frames under each incoming12-frame dissolve; logical narrative boundaries remain165 and305. Total remains450 frames.

## Audio direction
Narration-led with sparse cinematic SFX only; no BGM for this version. This consciously departs from the skill's tech-house default to preserve the user's calm premium brief and a clear15s B2B read. Transition whoosh, route arrivals, and a final riser→impact→shimmer phrase. Riser synthesized locally; other SFX have source URLs documented in reference/AUDIO-ATTRIBUTION.md. All SFX relative to SHOTS; output alignment measured after render. BGM prop remains false by default.

## Material boundaries
Existing hero and globe plates were AI-cleaned/reconstructed from user keyframes in the earlier project; exact vehicle details may differ. Do not represent them as original photography or official website screenshots. This project is an independent brand film, not a fabricated website tour. 2.5D layers, not a3D vehicle model. Original website access was blocked; no fresh website claim is made.

## Reference version discrepancy
The downloaded Gallery previews are historical variants: multiplane lacks some current demo text/foreground arrangements; flyline preview is light gray while current TSX is the dark glow version; outro preview uses AI Field Lab while current TSX names video-shotcraft. The selected card's current TSX is used for parameter adaptation. This is not claimed to be an exact recreation of those historical Gallery videos; independent review should mark strict dynamic-preview equivalence unverifiable.

## Final wording and readability decisions
Measured narration: “Uniland Motors. New, used, and electric vehicles. Over ten thousand vehicles delivered. Global reach. Start your next business partnership with Uniland Motors today.” Ten thousand means cumulative delivered vehicles. First shot allows a quiet read hold after speech rather than stretching a short phrase below94% natural tempo. Supporting readable text is at least44px (verified uppercase glyph target32px); narration captions76px. Final group-photo support labels sit in discrete slots around the wordmark, with the lower delivery slot widened to620px to prevent wrapping/clipping.

## Output audio alignment
Raw Remotion4.0.484 / H.264 /48kHz AAC MP4 has measured2048/48000s (42.667ms,1.28f) audio delay. Three separate voice windows correlate to the same delay. scripts/finalize.py performs one render-pipeline compensation on the whole mix, copies video unchanged, and pads/trims audio to exactly15s. Source peak lag is separately accounted for: route impact cues start16/52f, source impact peak16.53f later targets node arrivals32/68f; closing impact starts56f and peaks72.53f, targeting completed wordmark73f; shimmer starts60f and peaks87.79f, targeting URL settle89f. These are relative SHOTS expressions, not output-offset changes to each cue.
