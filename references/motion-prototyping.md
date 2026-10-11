# Motion prototyping and dynamic acceptance

Read after the visual choice, before product integration. The purpose is to compare the feel of the same interface, not to reopen its visual design.

## Small, comparable prototypes

Inventory all eligible interactions within the agreed boundary first. Choose representative sequences to exercise that inventory: for example, list-to-detail and back, disclosure, or timeline dragging and release. Use identical layout, copy, sample data, window size, initial state, and action sequence across M1/M2/M3. Identify sample values as fixtures in the evidence; do not imply live financial results or model output.

## Coverage before choreography

Create `motion-coverage.json` or an equivalent maintained table. For each visible interactive component or state-changing region record its trigger, feedback, transition, interruption behavior, reduced-motion fallback, demo step, and verification status. Mark truly static content with a specific reason. Prefer broad purposeful coverage with restrained amplitude; more coverage does not mean slower or more theatrical motion.

Consider the actual product's eligible regions:

- Buttons/icons: pointer hover, press/release, keyboard focus, enabled/disabled and busy feedback.
- Navigation, segmented controls and chips: moving selection, content handoff, retargeting.
- Data views: legitimate changing numeric values, chart range/data transitions, chart focus marker/readout, composition selection/legend feedback. Animate actual state changes; do not fabricate changes in static numbers or loop chart drawing.
- Rows and disclosures: hover/selection, existing detail expansion, collapse, and panel dismissal.
- Overlays and forms: origin-aware presentation, focus movement, validation/status change and dismissal.
- Loading, empty, success and error states when those states are affected by the redesigned interactions.

Apply only interactions the product has or the user explicitly authorizes. Do not invent clickable rows, drill-down, filtering, trading controls, or new features just to increase animation count. For an otherwise static composition chart, modest hover emphasis may be offered as local feedback without changing business behavior. Static axes, labels, and settled numbers need no idle animation. Avoid unsolicited autoplay decoration in working data regions and blocking staggered entrance for every row; deliberately selected ambient art follows the separate expressive-effects guidance below.

Every motion variant must cover the same eligible inventory. A restrained variant still provides purposeful feedback; do not present it as an intentionally unfinished/no-motion option. Presentation must identify coverage and deliberate exclusions so the user can judge completeness, rather than showing only a handful of animated examples.

Build one isolated harness with a variant switch and reset/replay controls outside the evaluated region. Keep the prototypes small: no backend integration, authentication rewrite, or whole-app duplication. Reuse approved layout code where safe, without activating changes in the shipped app. Do not load the full concept as a background or animate a screenshot in place of real controls.

Offer materially different motion treatments appropriate to the product. Possible directions are restrained native transitions, stronger spatial continuity, or a slightly more tactile spring response. These are examples, not mandatory presets. Do not exaggerate bounce to make alternatives look different or change only animation duration. Frequent operations must stay quick.

For each interaction record:

- trigger and input method;
- start/end state and spatial origin;
- moving properties, timing/spring settings, and sequencing;
- interruption, reversal, and gesture-release behavior;
- focus/selection behavior and Reduce Motion fallback.

## Platform fit

- Expressive effects: read [art-direction.md](art-direction.md). If particles, atmospheric light or another ambient signature were selected, prototype their actual rendering and response as part of the same motion inventory. Keep real controls/text accessible above the effect, pause inactive/offscreen work, and provide a settled Reduce Motion fallback. Purposeful ambient motion is allowed; do not apply a blanket ban to a selected expressive area or turn every data region into idle animation.
- Native Apple apps: use the existing SwiftUI/AppKit/UIKit stack and system controls first. For macOS, prefer a separate local preview app/window or existing preview target. Retain keyboard, pointer, and trackpad behavior. Check API availability against the deployment target before using newer animation APIs.
- Web: use the existing stack and an isolated preview page. Prefer compositor-friendly transforms/opacity when appropriate; avoid a heavy animation dependency for a few transitions. Respect `prefers-reduced-motion`.
- Native reduced motion: observe the platform accessibility setting, such as SwiftUI's `accessibilityReduceMotion`. Replace large movement/zoom with a restrained fade or immediate update while preserving meaning and usability.
- If only a web approximation of native motion can run, label that limitation. Do not silently switch the product framework or represent it as a native performance test.

## Motion quality

Prioritize response and continuity. New input should retarget or reverse the current motion without resetting position, queueing obsolete actions, or disabling controls until playback ends. Where supported, preserve velocity across gesture release and interrupted springs. A spring can be non-bouncy; use bounce only when it fits the interaction.

Transitions should communicate a real relationship between source and destination. Keep a clear return path and avoid arbitrary shared-element morphs. System motion is often sufficient; do not add decorative animation to every action. Pointer interactions on macOS generally need more restrained feedback than direct touch.

## Present and stop

Present M1/M2/M3 with a runnable launch path/link and one concise tradeoff each. Capture short clips of the same action sequence when available, using the real prototype. Video is supplementary: let the user try rapid input, reversal, and dragging. Do not use generated video as runtime evidence. If capture is unavailable, provide the working preview and say that recording is unavailable. If execution itself is unavailable, report the blocker rather than claiming the alternatives are ready.

Ask for the motion choice, then stop. A visual choice does not count as a motion choice. Record any explicit waiver or exact hybrid behavior before final integration.

## Evidence

Save beside `concept-manifest.json`:

```json
{
  "visual_selection": "B",
  "platform": "macOS SwiftUI",
  "preview_path": "motion-preview/",
  "launch_instructions": "Exact project-specific launch command or steps",
  "viewport": [1440, 900],
  "fixture": "fixtures/preview-data.json",
  "sequence": ["Open item", "Expand details", "Return"],
  "variants": [
    {
      "id": "M1",
      "tradeoff": "Project-specific benefit and cost",
      "interaction_specs": "motion-m1.md",
      "recording": null
    }
  ],
  "selected": null,
  "hybrid": null,
  "waiver": null
}
```

Use actual project values and existing paths; omit a fixture path if data is inline and record its source instead. Include every built variant. Selection fields change only on user choice or explicit waiver. Preserve the selected motion specification as the implementation contract.

## Focused dynamic verification

Check the coverage inventory for omissions before presentation. Verify each interaction family once, then exercise rapid interruption/reversal on the consequential transitions. Avoid redundant tests per identical repeated row. Static fidelity and content gates remain separate.

For prototypes, verify the representative sequence works before presenting it. After integration, run the same sequence against real product state plus the affected edge cases:

1. Ordinary use: prompt feedback, understandable transition, stable end state and focus.
2. Rapid retargeting: repeated selection or open/close before completion; no snap, stale destination, duplicate view, or blocked input.
3. Gesture release/reversal where applicable: continuous handoff and correct final state.
4. Reduce Motion: all actions and status remain understandable and usable.

Run with animations enabled. Keep the separate frozen/settled screenshot pass for static comparison. Record environment, sequence, observations, available clips, and unresolved issues in `motion-review.md`. Check affected data-arrival/loading states when they alter the animation; do not add unrelated regression checks.

Do not infer frame rate from appearance, recording FPS, build success, or screenshots. If stutter is observed, investigate with platform profiling and record actual measurements before claiming a performance result. A smooth recording alone does not prove interruption or gesture responsiveness.

## Design references

These sources explain the principles; verify current API availability when implementing:

- [Apple Motion HIG](https://developer.apple.com/design/human-interface-guidelines/motion): purposeful, brief, cancellable motion and input-aware feedback.
- [Designing Fluid Interfaces, WWDC18](https://developer.apple.com/videos/play/wwdc2018/803/): responsive and interruptible interaction.
- [Animate with springs, WWDC23](https://developer.apple.com/videos/play/wwdc2023/10158/): position/velocity continuity, including springs without bounce.
- [Enhance your UI animations and transitions, WWDC24](https://developer.apple.com/videos/play/wwdc2024/10145/): spatial transitions and gesture-to-spring continuity.
