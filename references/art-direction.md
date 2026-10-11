# Distinctive art direction across platforms

Read before concept generation. The default ambition is exceptional, high-end visual authorship for every frontend: H5, web, mini-programs, desktop and native apps. Clean spacing and working controls are the foundation, not the aesthetic finish line. Keep required functions and concise copy.

## Research what is visible

Start with the [local case index](design-library/index.md) when its studied references fit the task. Each case includes local visual captures and concrete transfer/avoid decisions. Open the relevant images before using them; a case title or prose summary alone is not a visual reference. Supplement stale, incomplete or poorly matched cases with live research. Load a few useful cases rather than the entire library.

Use a small set of relevant references: a user-supplied site first, a reference with strong expressive identity, and a reference resembling the product's actual task/density. Curated galleries help discover directions; inspect original sites before drawing conclusions about implementation or motion. References need not all look alike.

Open actual pages at useful desktop/mobile sizes. Inspect hierarchy, proportions, typography, whitespace, imagery, material edges, contrast and surface relationships. For motion references, move the pointer, scroll or exercise a relevant control. Distinguish directly observed behavior from an implementation hypothesis. If a site cannot render or motion cannot be inspected, record that limitation and use another source; do not claim to have studied it from snippets alone.

Save a concise `design-research.md` with source URLs and inspection date, inspected viewport/state, two or three concrete observations per reference, which principles transfer, which do not, and any unavailable evidence. Preserve useful local captures when available. Reference sites change: reuse relevant recent observations, but verify the user’s specific current reference. Do not rank a gallery's inclusion as objective proof of quality.

## From references to an original visual idea

Define a composition thesis for each A/B/C before writing image prompts. A useful brief specifies:

- Product task and intended visual character in concrete terms.
- Main visual anchor and its relationship to the primary action/data.
- Composition: grid, asymmetric/symmetric balance, scale contrasts, reading path and spacing rhythm.
- Typography: actual target-size scale, Chinese glyph quality, numeral treatment, weight, line length and baseline alignment.
- Material: light direction, contrast, edge treatment, texture and layering where justified. Flat precision is a valid material language.
- Signature: an identifiable product-specific motif, data graphic, image treatment, typographic composition or spatial interaction. It need not be an added decorative object.
- Motion: trigger, spatial relationship and resting appearance of proposed effects; feasibility in the existing stack.
- Copy whitelist and what changes materially from rejected concepts.

Each direction must have visibly different authorship, not the same dashboard with light/dark skins. “Premium,” “cinematic,” or “Apple-like” without these choices is not a brief. Reference a principle rather than copying another site's logo, wording, entire composition or branding.

## Adapt by product and platform

| Context | What strong art direction can emphasize | What to protect |
| --- | --- | --- |
| Marketing web/H5 | Bold composition, editorial typography, original imagery, particles/light fields, scroll choreography | Clear action, mobile reading path, load cost and touch use |
| Desktop/native workspace | Crafted dense typography, strong spatial hierarchy, exceptional charts, subtle material/light and continuous interaction | Real window size, information density, keyboard/focus and native semantics |
| Mini-program/mobile task flow | Distinctive compact composition, considered shapes/image crops, tactile transitions | Safe areas, touch targets, short flows, runtime/API limits; no pointer-dependent meaning |
| Data-heavy tools | Precise alignment, chart authorship, restrained layers, clear numeric hierarchy | Honest encodings, labels, contrast and comparison accuracy |

Use a brand/ambient effect where it supports the task, for example an introductory area, quiet background or transition. Do not spread a landing-page hero over a working ledger or add a new feature to create spectacle. Conversely, do not prohibit expressive visuals merely because the product is an app. Adapt their location, amplitude and density. Preserve regional redesign boundaries.

## Expressive effects are designed components

Particles, meshes, atmospheric light, depth and refined image treatments are allowed when they serve the direction. Specify density, color, scale, motion field, interaction response, layering and content protection. A sparse directional field with a readable focal area is a different design from uniform confetti. Motion must have a coherent spatial rule; random looping does not supply quality.

Describe feasibility per platform before selection: CSS/SVG or Canvas/WebGL for web as appropriate; available native drawing/animation APIs for Apple apps; supported mini-program canvas/runtime APIs for mini-programs. Avoid adding a rendering engine when simple primitives suffice. A bitmap texture may be generated; actual interactive particles must run as a real effect with accessible controls/text kept separate.

Budget effects for the actual device: pause ambient work offscreen/inactive, avoid expensive per-frame layout, cap particle/render resolution where appropriate, retain a useful static fallback and respect Reduce Motion. Evaluate observed responsiveness before performance claims. Ambient motion can be intentional in expressive areas; it must not compete with reading, alter financial values or delay controls. Include such an effect in every motion variant if it is part of the selected visual idea, with different comparable treatments and the same settled composition.

## Aesthetic review beyond functional compliance

Use selected library captures as craft comparators during review. Compare the clarity of the visual anchor, spacing rhythm, type discipline and effect containment at similar readable scale, not pixel resemblance or copied brand identity. If a result is only a standard panel layout with a decorative light/particle layer added, revise its underlying composition. Preserve a product-specific functional signature even when atmosphere is removed.

Inspect at real target size and compare with the studied references for craft, not screenshot similarity. Alongside the six checks in concept-generation, answer:

1. Can the visual idea be named from the actual image without reading its prompt?
2. Does it have controlled scale, rhythm and focal tension, rather than evenly distributing everything into interchangeable cards?
3. Are typography, artwork/data graphics and material details crafted to the same level?
4. Does the page remain composed when decorative effects are removed or settled?
5. Are A/B/C clearly distinct and credible for this product on this platform?

State observed weaknesses, not promotional adjectives. Reject major failures in authorship as well as usability. “All content is present” and “the palette is restrained” do not establish high-end design. User preference remains decisive; no rubric guarantees subjective approval.

## Studied first-party starting points

Inspected 2026-10-11 in a 1440×1000 browser viewport. These are starting points, not permanent templates or required palettes.

- [Google Antigravity](https://antigravity.google/): a sparse multicolor particle field around a centered black typographic focal point on white; compact top navigation and a clear dark CTA. Browser inspection found a viewport-size canvas; time-separated pointer captures showed changed particle distribution. Exact simulation and pointer causality were not isolated. Transfer the balance of expressive atmosphere and legible foreground; adapt density to a workspace rather than copy the marketing hero.
- [Linear](https://linear.app/): left-aligned large type above a broad product view; black and graphite surfaces, fine borders and tightly controlled secondary contrast. Transfer precision and tonal depth; do not use its English marketing copy or its issue-tracker layout as an unrelated product template.
- [Apple MacBook Pro](https://www.apple.com/macbook-pro/): a dominant product image shaped by directional light on black, with a compact text/action grouping. Transfer focal hierarchy and coherent lighting; the photographed hardware and spacious marketing composition are not a financial workspace pattern. Only the initial rendered frame was inspected, not full scroll choreography.
- [Apple Motion HIG](https://developer.apple.com/design/human-interface-guidelines/motion): use as interaction guidance alongside actual visual references; verify current framework APIs when implementing.

Consult a user-specified gallery such as [recent.design](https://recent.design/?ref=godly&category=web) for broader discovery, then document the specific works actually inspected and their original sources. See [the sampled study](recent-design-study.md) for concrete adaptations and evidence limitations. Do not pretend to inspect every work or adopt its gallery layout as the product design.
