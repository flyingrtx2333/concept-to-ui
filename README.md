# concept-to-ui

**Choose the look. Try the motion. Then let Codex integrate it.**

[简体中文](README.zh-CN.md) · [Quick start](QUICKSTART.md) · [Report an experience](https://github.com/flyingrtx2333/concept-to-ui/issues/new?template=experience-feedback.yml)

`concept-to-ui` is an MIT-licensed Codex skill for concept-first UI redesign. It inspects an existing screen, generates three materially different full-screen concepts, pauses for your visual choice, builds 2–3 isolated interactive motion prototypes, pauses for your motion choice, and then integrates the selected design with separate static and dynamic verification.

The selection checkpoint is the point: the agent does not silently commit your product to its first design guess.

H5, web, mini-program, desktop and native concepts share a high-end art-direction standard: inspect strong references, then establish original composition, typography, material and a product-specific visual signature. Adapt expressive effects to the task and platform; a clean generic template is not the aesthetic finish line. Static imagery and actual motion receive separate evaluation.

The [local design library](references/design-library/index.md) includes 12 studied cases and 18 saved screenshots with source/date, adaptations and evidence limitations. Retrieve a few relevant cases per task; these are study references, not production assets or fixed templates.

## Workflow

1. Inspect the existing screen, route, interactions, and constraints.
2. Generate complete A/B/C design directions.
3. Stop and wait for the user to choose.
4. Try 2–3 motion variants of the same selected layout and choose one.
5. Integrate both choices using real web or native controls and product data.
6. Capture static fidelity evidence and separately verify interruption, reversal, and Reduce Motion with animations enabled.

The skill preserves existing routes, APIs, authentication, product logic, and information architecture. Concept images are references—not shippable pages or full-screen image backgrounds.

## Install

Install it into a project with the Skills CLI:

```bash
npx skills add flyingrtx2333/concept-to-ui --agent codex --skill concept-to-ui
```

Or clone this repository and copy or link it to:

```text
<CODEX_HOME>/skills/concept-to-ui/
```

On Windows, the default location is:

```text
%USERPROFILE%\.codex\skills\concept-to-ui\
```

Restart or refresh skill discovery if needed, then invoke:

```text
$concept-to-ui
```

For a five-minute walkthrough, see [QUICKSTART.md](QUICKSTART.md).

## Requirements

- A Codex environment with built-in image generation and platform-appropriate preview/capture access
- For native apps, the target platform build/run tools; for web, a local browser preview
- Python 3.10+
- Pillow 10–12 for the bundled image tools
- An existing web or app screen to redesign

Install the script dependency:

```bash
python -m pip install -r requirements.txt
```

## Screenshot tools

Measure a reference image:

```bash
python scripts/analyze_reference.py reference.png \
  --output evidence/reference-analysis.json
```

Compare an implementation with the selected concept:

```bash
python scripts/compare_screenshots.py reference.png render.png \
  --report evidence/report.json \
  --diff evidence/diff.png \
  --overlay evidence/overlay.png
```

For identical inputs and options, both scripts are deterministic. The comparator exits non-zero when configured thresholds fail. Its pixel metrics are evidence of visual difference, not a claim that a design is subjectively good.

## Repository layout

```text
SKILL.md                         Skill entrypoint
agents/openai.yaml               Codex UI metadata
references/                      Phase-specific guidance
scripts/analyze_reference.py     Reference measurement
scripts/compare_screenshots.py   Comparison report and artifacts
tests/                           Helper-script tests
```

## Scope and safety

This skill does not authorize deployment, publishing, backend changes, authentication changes, or production mutation. It guides an agent working inside the target product repository and keeps visible text and controls as real, accessible UI.

## Feedback and contributing

This is an early release. The most useful feedback is a reproducible experience report: whether A/B/C were meaningfully different, whether Codex waited for your choice, whether existing behavior survived implementation, and the exact step where the flow failed.

[Open the experience feedback form](https://github.com/flyingrtx2333/concept-to-ui/issues/new?template=experience-feedback.yml), or read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a code change.

Run these checks before opening a pull request:

```bash
python -m unittest discover -s tests -v
python <path-to-skill-creator>/scripts/quick_validate.py .
```

## License

MIT. See [LICENSE](LICENSE).

Design quality: premium minimal composition and a strict visible-copy budget. Chinese interfaces exclude redundant English, subtitles, and repeated instructions. Motion prototypes cover eligible interaction regions with justified static exclusions, rather than a few isolated animated samples.
