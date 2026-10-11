# Concept Generation

Use this reference only during the concept phase.

Apply [concept-quality.md](concept-quality.md) before the selection checkpoint. An initial generated file is a draft, not automatically a selectable concept.

## Whole-screen or regional scope

Follow the boundary recorded during inspection. For a regional redesign, generate only that region at its crop dimensions/aspect ratio and preserve its controls and states. Supply the region crop as the primary reference; label a wider screenshot as style context whose shell, navigation, and neighboring components must not appear in the generated output. Distinguish directions using geometry, density, emphasis, or imagery inside the permitted region rather than changing the surrounding design system.

Inspect every output for scope violations. Present regional previews directly, or paste them into the original full-screen screenshot using deterministic compositing; preserve the original surrounding pixels. A composed preview is presentation evidence, not a full-screen redesign target or runtime page asset.

## Direction design

Read [art-direction.md](art-direction.md) first. Use inspected references to develop a product-specific visual identity across any frontend platform. Include the visual anchor, signature, typography, material and motion intent in every direction; clean generic layout alone does not meet the default standard. A signature may be exceptional typography or data graphics rather than an extra decorative effect.

Use the [case library](design-library/index.md) selectively. In the brief, name the chosen cases and the concrete relationship being adapted (for example, baseline rhythm, localized light, contrast ladder or functional geometry), then explain its product-specific transformation. Do not merely append brand names to a prompt. A/B/C must differ in composition and visual logic, not share the same template with three reference-site names.

Plan three directions by default, or the user-requested count, that differ in composition and interaction emphasis rather than color. Resolve their reading paths and visual grammar before generation. Derive them from the actual product and brand; do not carry a fixed industry's palette, imagery or terminology into unrelated work. Each final concept retains required product roles and actions and passes draft review.

## Premium minimal design and copy budget

Before writing prompts, establish a visible-copy whitelist from required controls, data labels, states, and notices. Use one language by default. For Chinese UI, forbid decorative English, repeated currency codes, bilingual headings, slogans, and redundant subtitles. Do not copy clutter from the reference merely because it exists. Keep legal/risk notices and necessary data provenance concise, never conceal them for aesthetics.

Design each direction with a distinct composition thesis, numeric/type scale, alignment grid, proportion, and material treatment. Professional simplicity comes from precise relationships, not generic KPI cards or embellishment. Keep the main task readable at the real application window size. Create hierarchy without repeating titles; preserve necessary information and actions. Inspect all generated lettering against the whitelist and reject prominent extra copy. Any small generation artifact must be identified explicitly and removed in implementation.

Generated fixture data must be internally coherent. Chart shapes, percentages, and monetary totals are design examples, never evidence of real performance. Derive or label sample values; never change actual product data to match a concept.

## Art direction and revision quality gate

Translate adjectives such as professional, premium, spacious, and minimal into measurable design choices before generation. Record the intended hierarchy, alignment grid, type sizes in logical pixels, sidebar/content proportions, spacing rhythm, line weights, palette, and chart styling. Keep these tailored to the actual platform and product, not a universal theme.

At a compact native desktop size, start from realistic 11–13 pt body text, 14–18 pt section titles, and 24–36 pt primary values where appropriate; these are calibration examples, not fixed requirements. Avoid the oversized mockup lettering that makes a desktop interface look like a poster. Use alignment, weight and proportion to create presence. Do not equate spaciousness with wasted columns, or minimalism with hiding core functions.

Limit visual competition: one clear primary emphasis, restrained secondary values, quiet axes, coherent grid, deliberate chart domains, and a small coordinated palette. Avoid candy-colored default charts, heavy pills, shiny gold gradients, inconsistent border/shadow styles, or repeated boxed metrics. Use necessary labels and source-appropriate symbols; never ornamental icons to fill space.

Review each output at target window size against these six questions, recording specific visible evidence rather than praise:

1. Hierarchy: is the main task clear without several equally loud titles or enormous values?
2. Typography: are sizes, weights, baseline alignment, numerals and density coherent and platform-appropriate?
3. Composition: does the spacing/grid feel deliberate, with useful content balance and no accidental empty areas?
4. Restraint: are colors, surfaces, borders, icons and emphasis controlled rather than decorative?
5. Data graphics: are axes/labels readable, proportion encodings plausible, and competing series identifiable?
6. Product realism: do controls and information form a feasible usable app instead of a marketing comp or generic dashboard template?

Block presentation for a major defect. Apply the responsible repair and bounded retry rules in concept-quality; keep discarded drafts and reasons separate. Subjective preference remains the user's choice among finished directions, not a reason to submit a plainly weak draft. A rubric does not guarantee subjective approval.

After a rejected round, summarize the concrete recurring failure and propose materially different composition/art directions. Do not resubmit near-identical concepts with new names. Keep prior evidence separate and restart the visual choice; previous acceptance does not apply to a replacement direction.

## Built-in ImageGen prompt template

Issue one initial `image_gen.imagegen` call per planned direction and inspect it before justified repairs. Inspect any supplied local screenshot first; attach it only when it helps preserve the requested product/style without anchoring to a rejected layout. Otherwise carry audited functions in text. This template is a writing aid: combine/remove redundant fields to keep composition dominant, rather than append a long generic constraint wall.

```text
Use case: ui-mockup
Asset type: <complete application screen or specified region> UI concept
Primary request: redesign <screen or editable region> while preserving its product roles and actions
Input images, when used: <product/scope reference role>; <limited style-reference role and exact relationship to adapt>. No copied source branding/copy or inherited rejected geometry.
Output bounds: <exact width>x<exact height>; match the screen or region aspect ratio
Product: <what the application does>
Required sections: <real sections/actions from the product>
Direction: <A/B/C design thesis>
Style/medium: polished production UI concept with project-appropriate raster illustration
Studied principles: <chosen case IDs, observed spatial/type/material relationships and product-specific transformation; original adaptation, not copied branding>
Visual anchor and signature: <distinctive composition/type/data/imagery idea, clearly visible>
Material and lighting: <coherent surface/edge/light treatment or deliberate flat precision>
Motion intent: <resting appearance, spatial rule and input trigger; still image is not animation evidence>
Composition/framing: <complete viewport or region-only output>, clear hierarchy, no device mockup, no browser chrome; do not redraw unchanged surroundings
Color palette: <direction palette>
Typography: refined Chinese-only UI hierarchy and precise tabular numerals; concise approved labels; no redundant English or subtitles; avoid dense tiny text
Visible-copy whitelist: <exact headings, labels, values, states, notices allowed>
Constraints: preserve all required roles; no external brand logos; no watermark; no lorem ipsum; no fake browser frame
Avoid: redundant English; bilingual labels; slogans; redundant subtitles; generic default dashboard styling; emoji icons; generic template grid; repeated heading/subtitle pairs; decorative card stacks; unsupported claims or invented metrics; excessive pills; accidental blank columns; full-screen art that obscures controls
```

## Inspection checklist

For each output verify:

- complete requested screen/region and all its edges are visible;
- product identity and required sections are recognizable;
- concepts differ in frame, hierarchy, and imagery;
- each concept visibly expresses its art-direction thesis; it is not an interchangeable template with a different palette;
- no impossible interaction or missing role;
- no illegible text block dominates the design;
- generated imagery has a plausible path to project-bound assets;
- the target UI framework can reconstruct text and controls without rasterizing the page;
- regional outputs contain only the editable region and respect the surrounding design system;
- the main task uses the available space and every card or subtitle has a distinct purpose;
- illustrative copy does not introduce AI self-praise, invented evidence, or product features absent from the source.

## Manifest schema

Save `concept-manifest.json` beside the concepts:

```json
{
  "screen": "index",
  "reference": "absolute-or-project-relative-path",
  "viewport": [1536, 1024],
  "scope": "screen",
  "editable_component": null,
  "editable_bounds": null,
  "unchanged_regions": [],
  "authorized_shared_changes": [],
  "review": "concept-review.md",
  "drafts": [],
  "concepts": [
    {
      "id": "A",
      "title": "Calm clinical clarity",
      "path": "concept-a.png",
      "prompt_direction": "short direction summary",
      "strength": "primary benefit",
      "tradeoff": "primary cost"
    }
  ],
  "selected": null,
  "visual_waiver": null,
  "motion_manifest": "motion-manifest.json"
}
```

Update `selected` only after the user chooses the visual direction. This selection permits isolated motion prototypes, not final product integration; the separate motion choice is recorded in `motion-manifest.json`. Do not delete non-selected previews until implementation is accepted.

Before presentation, `concepts` contains only ready candidates. Record each failed/replaced attempt in `drafts` with its ID, path, blocking reason and replacement; tie final IDs to actual review decisions. Do not use an implementation residual list to excuse a blocked draft.

For regional work, set `scope` to `region`, retain the full-screen `viewport`, and record `editable_component`, `editable_bounds` as `[x, y, width, height]`, unchanged regions, and authorized shared changes. Record crop/preview paths and any crop scaling alongside the concept paths so implementation uses the regional reference rather than the composed full-screen preview.
