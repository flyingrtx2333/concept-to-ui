# concept-to-ui

**先看三套方案，选好，再让 Codex 写代码。**

[English](README.md) · [快速开始](QUICKSTART.md) · [提交体验反馈](https://github.com/flyingrtx2333/concept-to-ui/issues/new?template=experience-feedback.yml)

`concept-to-ui` 是一个采用 MIT 许可证的 Codex skill，用于“概念优先”的 UI 重设计。它会先检查现有页面，生成三套有实质差异的完整界面方案，停下来等待你选择，再把选定方向实现成真实可交互 UI，最后用确定性的截图工具进行对比。

它的核心是“选择关卡”：不让 agent 一收到“优化 UI”就直接按自己的第一个想法改代码。

## 工作流程

1. 检查现有页面、路由、交互和约束。
2. 生成完整的 A/B/C 三套设计方向。
3. 停下来，等待用户选择。
4. 用真实 DOM、控件和产品数据实现选定方向。
5. 按准确视口截图，输出 JSON 报告、差异图和叠加图。

skill 会保留现有路由、API、认证、产品逻辑和信息架构。概念图只作为实现参考，不能冒充可交付页面，也不能被整张铺成网页背景。

## 安装

使用 Skills CLI 安装到项目：

```bash
npx skills add flyingrtx2333/concept-to-ui --agent codex --skill concept-to-ui
```

也可以克隆仓库，再把仓库目录复制或链接到：

```text
<CODEX_HOME>/skills/concept-to-ui/
```

Windows 默认位置：

```text
%USERPROFILE%\.codex\skills\concept-to-ui\
```

必要时刷新或重启 Codex 的 skill 发现，然后显式调用：

```text
$concept-to-ui
```

第一次使用建议阅读 [QUICKSTART.md](QUICKSTART.md)，约五分钟即可跑通选择关卡。

## 环境要求

- 支持内置图像生成和浏览器截图的 Codex 环境
- Python 3.10+
- Pillow 10–12（供仓库内图像工具使用）
- 一个需要重设计的现有 Web 或 App 页面

安装脚本依赖：

```bash
python -m pip install -r requirements.txt
```

## 截图工具

测量参考图：

```bash
python scripts/analyze_reference.py reference.png \
  --output evidence/reference-analysis.json
```

把实现结果与选定概念图对比：

```bash
python scripts/compare_screenshots.py reference.png render.png \
  --report evidence/report.json \
  --diff evidence/diff.png \
  --overlay evidence/overlay.png
```

相同输入和参数会得到确定性结果。未达到配置阈值时，对比脚本返回非零退出码。像素指标只能说明视觉差异，不能证明设计本身一定优秀。

## 适用边界

这个 skill 不授权部署、对外发布、后端修改、认证修改或生产环境变更。它只指导 agent 在目标产品仓库内完成设计与前端实现，并要求可见文字和控件是真实、可访问的 UI。

## 反馈与贡献

项目目前处于早期阶段。最有价值的是可复现的真实反馈：A/B/C 是否有实质区别、Codex 是否真的等你选择、实现后是否保住原功能，以及具体卡在哪一步。

[提交体验反馈](https://github.com/flyingrtx2333/concept-to-ui/issues/new?template=experience-feedback.yml)。提交代码前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，并运行：

```bash
python -m unittest discover -s tests -v
python <path-to-skill-creator>/scripts/quick_validate.py .
```

## 许可证

MIT，详见 [LICENSE](LICENSE)。
