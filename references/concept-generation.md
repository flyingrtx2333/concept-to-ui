# Concept Generation

Use this reference only during the concept phase.

## Direction design

Generate at least three directions that differ in composition, not merely color:

- **A — calm clinical clarity:** light, reassuring, evidence-led, generous whitespace, restrained teal/blue, human care imagery.
- **B — intelligent monitoring cockpit:** darker or high-contrast, live evidence flow, precise data visualization, strong operational hierarchy.
- **C — guided recovery journey:** warm, approachable, role-based paths, milestone storytelling, rich but controlled illustration.

Adapt the directions to the product; do not force these palettes if the supplied brand requires another system. Each concept must retain every required product role and primary action.

## Built-in ImageGen prompt template

Issue one `image_gen.imagegen` call per direction. When a local screenshot is supplied, inspect it first and pass it as a reference image.

```text
Use case: ui-mockup
Asset type: complete desktop web application landing/index screen concept
Primary request: redesign the supplied interface while preserving its product roles and actions
Input images: Image 1 is the current product reference; use its information architecture, not its styling
Viewport: <exact width>x<exact height>, landscape, full screen visible
Product: <what the application does>
Required sections: <real sections/actions from the product>
Direction: <A/B/C design thesis>
Style/medium: polished production UI concept with project-appropriate raster illustration
Composition/framing: complete browser viewport, clear hierarchy, no device mockup, no browser chrome
Color palette: <direction palette>
Typography: modern Chinese UI hierarchy; concise labels; avoid dense tiny text
Constraints: preserve all required roles; no external brand logos; no watermark; no lorem ipsum; no fake browser frame
Avoid: emoji as primary icons; generic template grid; excessive pills; full-screen decorative art that obscures controls
```

## Inspection checklist

For each output verify:

- complete viewport and all edges are visible;
- product identity and required sections are recognizable;
- concepts differ in frame, hierarchy, and imagery;
- no impossible interaction or missing role;
- no illegible text block dominates the design;
- generated imagery has a plausible path to project-bound assets;
- final HTML can reconstruct text and controls without rasterizing the page.

## Manifest schema

Save `concept-manifest.json` beside the concepts:

```json
{
  "screen": "index",
  "reference": "absolute-or-project-relative-path",
  "viewport": [1536, 1024],
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
  "selected": null
}
```

Update `selected` only after the user chooses. Do not delete non-selected previews until implementation is accepted.
