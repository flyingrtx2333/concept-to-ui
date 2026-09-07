# concept-to-ui

一个面向 Codex 的概念优先 UI 重设计 skill：先检查和测量现有界面，生成至少三个完整方向，等待用户选择，再把选定方向实现为真实可交互 UI，并用确定性的截图对比进行验收。

> English: A concept-first Codex skill for redesigning web and app screens. It measures the current UI, generates multiple complete directions, pauses for user selection, then guides implementation and deterministic screenshot comparison.

## What it does

- 保留现有路由、API、认证、产品逻辑和中文信息架构。
- 强制执行 A/B/C 概念选择 checkpoint，避免在用户选择前直接改产品 UI。
- 用内置图像生成能力制作概念图和必要的位图素材。
- 使用 `analyze_reference.py` 测量参考图，使用 `compare_screenshots.py` 输出可审计的差异报告、diff 和 overlay。
- 要求真实 DOM 文本和控件、可访问名称、键盘交互、响应式行为以及控制台/网络检查。

## Install as a Codex skill

Clone this repository, then copy or link the repository folder as:

```text
<CODEX_HOME>/skills/concept-to-ui/
```

On Windows, the default location is:

```text
%USERPROFILE%\\.codex\\skills\\concept-to-ui\\
```

Restart or refresh Codex skill discovery if needed. Invoke it explicitly with:

```text
$concept-to-ui
```

The skill intentionally uses Codex's built-in image-generation capability and does not require another skill package.

## Use the bundled scripts

The helper scripts require Python 3.10+ and Pillow:

```powershell
python -m pip install -r requirements.txt
python scripts/analyze_reference.py reference.png --output evidence/reference-analysis.json
python scripts/compare_screenshots.py reference.png render.png `
  --report evidence/report.json `
  --diff evidence/diff.png `
  --overlay evidence/overlay.png
```

Both scripts are deterministic for the same input files and options. The comparator returns a non-zero exit code when its configured thresholds fail.

## Repository layout

```text
SKILL.md                         # Skill entrypoint
agents/openai.yaml               # Codex UI metadata
references/                      # Phase-specific detailed guidance
scripts/analyze_reference.py    # Reference image measurement
scripts/compare_screenshots.py  # Screenshot comparison and artifacts
tests/                           # Lightweight helper-script tests
```

## Design boundaries

This skill does not authorize deployment, publishing, backend changes, authentication changes, or production mutation. It is intended to guide an agent working inside the target product repository; the generated concept image is never a substitute for a real frontend implementation.

## Contributing

Keep the entrypoint concise and self-contained. Put phase-specific detail in `references/`, keep scripts deterministic and dependency-light, and validate changes with the commands below:

```powershell
python -m unittest discover -s tests -v
python <path-to-skill-creator>/scripts/quick_validate.py .
```

Please preserve the phase gate and the distinction between visual concept evidence and real DOM implementation.

## License

MIT. See [LICENSE](LICENSE).
