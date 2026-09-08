# concept-to-ui

**See three UI directions. Choose one. Then let Codex build it.**

[简体中文](README.zh-CN.md) · [Quick start](QUICKSTART.md) · [Report an experience](https://github.com/flyingrtx2333/concept-to-ui/issues/new?template=experience-feedback.yml)

`concept-to-ui` is an MIT-licensed Codex skill for concept-first UI redesign. It inspects an existing screen, generates three materially different full-screen concepts, pauses for your choice, implements the selected direction as real interactive UI, and then compares the result with deterministic screenshot tooling.

The selection checkpoint is the point: the agent does not silently commit your product to its first design guess.

## Workflow

1. Inspect the existing screen, route, interactions, and constraints.
2. Generate complete A/B/C design directions.
3. Stop and wait for the user to choose.
4. Implement the chosen direction with real DOM, controls, and product data.
5. Capture the exact viewport and produce a JSON report, diff, and overlay.

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

- A Codex environment with built-in image generation and browser/screenshot access
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
