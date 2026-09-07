# Implementation and Fidelity Contract

Use this reference only after the user has selected a concept.

## 1. Output mode

- Existing frontend: preserve framework, routes, APIs, state, components, and build conventions.
- New standalone page: use `index.html`, local assets, and no runtime network dependency unless requested.
- Multiple screens of one app: derive shared components and connect visible navigation.
- Do not rebuild backend behavior that is not visible or requested.

## 2. Measure before coding

Run `scripts/analyze_reference.py` and record exact dimensions, outer frame, major boundaries, content columns, fixed areas, spacing rhythm, dominant colors, borders, radii, shadows, typography, wrapping, state, and overflow.

Machine-read dimensions are authoritative. A different-size browser render fails before scoring.

Create a checklist grouped by:

1. Silhouette: frame, bands, columns, content width.
2. Components: cards, navigation, rails, actions, charts.
3. Typography: hierarchy, wrapping, line-height, density.
4. Assets: photos, portraits, equipment, logos, textures, ornaments.
5. State: selection, loading/empty/error, scroll, fixed placement.

For desktop login, registration, and other short gateway screens, default the outer frame to exactly `100vh`. The page, split columns, and form card must not use vertical scrolling. Compact spacing and remove redundant copy before considering overflow. Mobile may scroll vertically, but must not overflow horizontally.

Use a copy budget during measurement: classify every supporting line as action, state, scope, risk, or required instruction. Remove lines that merely repeat a heading, visible control, role label, process diagram, or another trust statement.

## 3. Asset rules

- Smallest clean crop: use only when a reusable visual is cleanly isolated.
- Code-native: text, standard icons, borders, dividers, gradients, charts, masks, and simple geometry.
- Built-in image generation: salient bitmap-like subjects, missing assets, textures, branded illustration, or concept-specific ornaments.
- Generate one asset family per call, inspect it, copy the selected output into project `assets/`, and record consuming selectors.
- Never leave project dependencies only in a generated-images or temporary directory.
- Do not replace prominent subjects with emoji, generic icons, or CSS circles.
- Never rasterize visible labels, buttons, tables, or the full interface.

## 4. Implementation order

1. Frame and major column/band geometry.
2. Component boxes, fixed/sticky placement, and overflow.
3. Typography and exact wrapping.
4. Selected generated/extracted assets and crop behavior.
5. Icons, borders, radii, shadows, subpixel alignment.
6. Interaction state and responsive behavior.

Do not polish a lower step while a higher step has an obvious mismatch.

For fixed-height gateway screens, verify both login and the tallest registration/error state at common desktop heights. Do not accept an auth card with `overflow-y:auto`; reduce decorative copy, duplicated trust text, spacing, and nonessential helper content while preserving every required field and action.

## 5. Deterministic browser capture

Use the existing browser harness or direct Playwright CLI; do not require another skill package. Required properties:

- source viewport exactly matched;
- device scale factor 1 unless evidence says otherwise;
- `document.fonts.ready` completed;
- animations, transitions, carets, and volatile clocks frozen;
- viewport-only screenshot unless the source is full-page;
- console errors and failed requests recorded;
- desktop plus requested narrow-width render preserved under `evidence/` or `output/`;
- desktop gateway screen has `scrollHeight == innerHeight` and no scrollable page, column, or card;
- narrow/mobile render has no horizontal overflow and uses intentional document scrolling when needed;
- exact local server and browser session stopped after testing.

Direct CLI sequence:

```powershell
npx --version
npx --yes --package @playwright/cli playwright-cli -s=ui-fidelity open '<url>' --headed
npx --yes --package @playwright/cli playwright-cli -s=ui-fidelity snapshot
npx --yes --package @playwright/cli playwright-cli -s=ui-fidelity resize <w> <h>
npx --yes --package @playwright/cli playwright-cli -s=ui-fidelity reload
npx --yes --package @playwright/cli playwright-cli -s=ui-fidelity screenshot
npx --yes --package @playwright/cli playwright-cli -s=ui-fidelity console error
npx --yes --package @playwright/cli playwright-cli -s=ui-fidelity requests
npx --yes --package @playwright/cli playwright-cli -s=ui-fidelity close
```

## 6. Comparison and repair

Store critical regions as `[x, y, width, height]`, then run the bundled comparator. Preserve render, JSON report, amplified diff, overlay, and regions file.

Default gates:

- normalized mean absolute RGB error <= 0.035;
- aggregate pixel similarity >= 0.965;
- at least 90% of pixels within per-channel tolerance 24;
- major boundaries within 3 px;
- no critical-region hotspot.

After every capture, list the five largest mismatches with coordinates and classify them as geometry, typography, asset, color, or state. Fix the highest-area/highest-impact mismatch first. Keep a new version only when metric and visual review both improve.

Completion requires all gates, real DOM text/controls, existing local assets, zero console/failed requests, critical-region review, responsive review, and preserved evidence. If dynamic production data differs from concept placeholders, keep real data and document the exact residual instead of falsifying data.

## 7. Anti-cheat and static checks

- Search source for the reference screenshot filename/path and data URLs.
- No asset may approximate the full reference frame unless the requested deliverable is a static image.
- Search for runtime `http://` or `https://` asset dependencies.
- Confirm visible text exists in source/DOM.
- Resolve every relative asset path and verify it exists.
- Verify generated raster subjects are visible at the intended size and are not stretched, poorly cropped, or substituted.

## 8. Acceptance handoff

Report the selected concept, project files changed, generated assets and prompts, desktop/mobile evidence, comparison metrics, interaction coverage, console/network status, and any residual blockers. Deployment requires separate explicit authorization.
