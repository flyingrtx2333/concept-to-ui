# Implementation and Fidelity Contract

Use this reference for product integration only after visual and motion selections are recorded, or the user explicitly waives the corresponding gate. Carry the selected motion specification from `motion-manifest.json` into this contract.

## 1. Output mode

- Existing frontend: preserve framework, routes, APIs, state, components, and build conventions.
- Native app: preserve its native stack and deployment target; build real native views/controls. Browser/DOM/CSS checks below apply to web only; use native accessibility, window layout, and runtime diagnostics for native apps.
- New standalone page: use `index.html`, local assets, and no runtime network dependency unless requested.
- Multiple screens of one app: derive shared components and connect visible navigation.
- Do not rebuild backend behavior that is not visible or requested.

For a regional redesign, freeze the selected component, screenshot bounds, unchanged surroundings, and permitted shared changes from the concept manifest. Implement only that boundary; choosing a concept does not authorize redesigning the shell or adjacent regions. Prefer component-local styles and assets. Apply content, density, and gateway-layout rules only where the editable scope permits; report outside-scope problems separately.

## 2. Measure before coding

Run `scripts/analyze_reference.py` and record exact dimensions, outer frame, major boundaries, content columns, fixed areas, spacing rhythm, dominant colors, borders, radii, shadows, typography, wrapping, state, and overflow.

Machine-read dimensions are authoritative. A different-size browser render fails before scoring.

For regional work, this size check applies to the concept and region crop. Record the crop's origin within the canonical full-screen viewport and any explicit scaling to the target region. Preserve the unmodified reference and transformation details; never normalize a regional concept to the entire screen. Keep an identical-state full-screen baseline for checking unchanged surroundings.

Create a checklist grouped by:

1. Silhouette: frame, bands, columns, content width.
2. Components: cards, navigation, rails, actions, charts.
3. Typography: hierarchy, wrapping, line-height, density.
4. Assets: photos, portraits, equipment, logos, textures, ornaments.
5. State: selection, loading/empty/error, scroll, fixed placement.

For desktop login, registration, and other short gateway screens, default the outer frame to exactly `100vh`. The page, split columns, and form card must not use vertical scrolling. Compact spacing and remove redundant copy before considering overflow. Mobile may scroll vertically, but must not overflow horizontally.

Default to no redundant subtitles or English in Chinese UI; use the approved copy whitelist from the concept phase. Use a copy budget during measurement: classify every supporting line as action, state, scope, risk, or required instruction. Remove lines that merely repeat a heading, visible control, role label, process diagram, or another trust statement. Record whether suspect copy is static, fixture, cached, API, or model output before editing it.

## 3. Asset rules

- Smallest clean crop: use only when a reusable visual is cleanly isolated.
- Code-native: text, standard icons, borders, dividers, gradients, charts, masks, and simple geometry.
- Built-in image generation: salient bitmap-like subjects, missing assets, textures, branded illustration, or concept-specific ornaments.
- Generate one asset family per call, inspect it, copy the selected output into project `assets/`, and record consuming selectors.
- Never leave project dependencies only in a generated-images or temporary directory.
- Do not replace prominent subjects with emoji, generic icons, or CSS circles.
- Use one consistent non-emoji icon family for controls and status.
- Never rasterize visible labels, buttons, tables, or the full interface.

## 4. Implementation order

1. Frame and major column/band geometry.
2. Component boxes, fixed/sticky placement, and overflow.
3. Typography and exact wrapping.
4. Selected generated/extracted assets and crop behavior.
5. Icons, borders, radii, shadows, subpixel alignment.
6. Selected motion across the agreed coverage inventory, interruption/reversal, Reduce Motion, interaction state, and responsive behavior. Do not silently drop secondary-control feedback during integration.

Do not polish a lower step while a higher step has an obvious mismatch.

For fixed-height gateway screens, verify both login and the tallest registration/error state at common desktop heights. Do not accept an auth card with `overflow-y:auto`; reduce decorative copy, duplicated trust text, spacing, and nonessential helper content while preserving every required field and action.

## 5. Static capture and separate dynamic verification

For native apps, capture the actual window or simulator, recording OS, content bounds, backing scale, and the mapping to reference pixels. Preserve full-resolution originals. Do not silently resize images to pass comparison. Check native accessible text, keyboard/focus, layout, runtime errors, and failed app requests instead of browser-only checks.

For dynamic verification, follow `motion-prototyping.md` with animations enabled. Save the actual sequence, interruption/reversal and Reduce Motion observations, and available recordings in `motion-review.md`. Freeze animation only for the separate static pass below; static metrics cannot certify motion quality.

### Web static capture

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
- affected populated, loading, empty, and error states are inspected with representative data;
- exact local server and browser session stopped after testing.

For regional work, save both the exact-viewport full-screen capture and its editable-region crop. Keep viewport, state, and crop coordinates consistent with the baseline. If responsive layout moves the region, record separate bounds for that viewport and check the requested responsive behavior rather than stretching the desktop crop.

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

For a regional redesign, run fidelity scoring on the selected regional concept and final crop only; critical-region coordinates are relative to that crop. Separately compare the full-screen before/after captures outside the editable bounds and explicitly allowed shared changes. Verify the surrounding geometry, appearance, navigation, and interactions remain intact. Do not include unchanged surrounding pixels in the regional fidelity score. Freeze dynamic content or document unrelated differences instead of treating them as permission to change other regions.

Default gates:

- normalized mean absolute RGB error <= 0.035;
- aggregate pixel similarity >= 0.965;
- at least 90% of pixels within per-channel tolerance 24;
- major boundaries within 3 px;
- no critical-region hotspot.

After every capture, list the five largest mismatches with coordinates and classify them as geometry, typography, asset, color, or state. Fix the highest-area/highest-impact mismatch first. Keep a new version only when metric and visual review both improve.

Completion requires static and dynamic gates, real DOM or native accessible text/controls, existing local assets, zero relevant runtime errors/failed app requests, critical-region review, responsive review, and preserved evidence. Review the final screenshot and DOM for duplicate cards/subtitles, cramped content beside unused space, emoji, AI-sounding promises, unsupported claims, and errors without a next action. If dynamic production data differs from concept placeholders, keep real data and document the exact residual instead of falsifying data. If generated output is poor, identify its source and fix it only when content behavior is in scope; otherwise report it as unresolved rather than declaring the UI finished.

## 7. Anti-cheat and static checks

- Search source for the reference screenshot filename/path and data URLs.
- No asset may approximate the full reference frame unless the requested deliverable is a static image.
- Search for runtime `http://` or `https://` asset dependencies.
- Confirm visible text is implemented as real DOM or native accessible text.
- Resolve every relative asset path and verify it exists.
- Verify generated raster subjects are visible at the intended size and are not stretched, poorly cropped, or substituted.

## 8. Acceptance handoff

Report both visual and motion selections/waivers, runnable prototype and dynamic evidence, project files changed, generated assets and prompts, desktop/mobile evidence, comparison metrics, interaction coverage, console/network status, and any residual blockers. Deployment requires separate explicit authorization.

For regional work, also report the editable bounds, any authorized shared changes, regional fidelity evidence, and the separate unchanged-surroundings check. Reject out-of-scope visual changes even when the regional score passes.
