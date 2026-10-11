# Quick start / 快速开始

This walkthrough tests the most important behavior: three real directions appear before any product UI is edited, then isolated motion prototypes appear after visual selection, and product integration starts only after motion selection.

本指南验证最重要的行为：先出现三套真正不同的方向，选择视觉后制作独立动效小样，选择动效后才接入产品 UI。

首次展示的三套应是内部审查与必要修整后的成稿；初次生成的图片只是草稿。不要把同一面板的换色版本或已知明显缺陷交给用户选择。出图工具可能自动显示草稿，但选择关卡只展示通过检查的最终方案。

Before generation, inspect relevant design references and record a distinct art-direction brief for each concept. High-end visual authorship applies to H5, web, mini-programs and native apps alike; adapt typography, composition and expressive effects to the actual task and platform.

出图前先实际查看设计参考，并为每套方案确定独立的美术方向。H5、网站、小程序和原生应用都以有辨识度的高端设计为目标；字体、构图与表现性动效按实际任务和平台适配。

## 1. Install / 安装

Run this in the project you want to redesign:

在需要重设计的项目中运行：

```bash
npx skills add flyingrtx2333/concept-to-ui --agent codex --skill concept-to-ui
```

Make sure the target project can already start locally and that you know the route of one screen to test.

请先确认目标项目能在本地启动，并选定一个可访问的测试页面。

## 2. Start with one screen / 从一个页面开始

Attach a screenshot or provide a local route, then use a prompt like:

附上截图或提供本地页面地址，然后输入：

```text
Use $concept-to-ui to redesign this dashboard. Preserve its routes, APIs,
data, and interactions. Show me three complete directions and wait for my
choice before editing the product UI.
```

中文示例：

```text
使用 $concept-to-ui 重设计这个控制台。保留现有路由、API、数据和交互。
先给我三套完整方案，并在修改产品 UI 前等待我选择。
```

## 3. Check the selection gate / 检查选择关卡

Before choosing, verify that:

- A/B/C are complete screens, not the same layout with different colors.
- Each direction has a short, understandable tradeoff.
- No product UI file has been edited yet.

选择前请确认：

- A/B/C 是完整界面，不是同一布局只换颜色。
- 每套方向都有简短、清楚的取舍说明。
- 产品 UI 文件还没有被修改。

Reply with `A`, `B`, `C`, or describe an exact hybrid. If you choose a hybrid, the agent should restate which elements come from each direction before motion prototyping.

回复 `A`、`B`、`C`，或明确说明混合方案。若选择混合方案，agent 应先复述各部分来源，再制作动效小样。

## 4. Try and choose motion / 体验并选择动效

Try M1/M2/M3 (2–3 alternatives) in the runnable preview. Layout, sample data, and the demonstrated interaction sequence must match. Compare rapid repeated input, reversal during a transition, and dragging/release where relevant. Use the native preview for a native app; a web approximation must be labeled. Short clips supplement the hands-on preview.

在可运行预览中体验 M1/M2/M3（2–3 套）。它们使用相同布局、示例数据和操作路径，便于比较连续点击、中途返回和拖动松手。原生 App 优先用原生小样；Web 近似演示必须注明。短视频辅助比较，不能代替亲手操作。

Choose a motion alternative or specify an exact hybrid. The agent waits for this choice before product integration. You may explicitly waive either selection gate.

选定动效或明确混合行为后，agent 才接入正式功能；你也可以明确跳过其中一个选择节点。

## 5. Review the implementation / 检查实现

After implementation, verify that:

- existing routes, APIs, authentication, and key interactions still work;
- text and controls are real DOM or native accessible UI with keyboard and focus behavior;
- the concept image was not used as a full-page background;
- the evidence folder contains an exact-viewport render, JSON report, diff, overlay, and residual note;
- `motion-manifest.json` records your selection, and `motion-review.md` records enabled-animation checks including interruption and Reduce Motion, with recordings when available.

实现后请确认：

- 原有路由、API、认证和关键交互仍能工作；
- 文字和控件是真实 DOM 或原生可访问控件，支持键盘和焦点状态；
- 概念图没有被当作整页背景；
- 证据目录包含准确视口截图、JSON 报告、差异图、叠加图和残差说明；
- `motion-manifest.json` 记录动效选择，`motion-review.md` 记录开启动画后的打断、减少动态效果等检查，并保留可用录屏。

## 6. Share useful feedback / 提交有效反馈

Use the [experience feedback form](https://github.com/flyingrtx2333/concept-to-ui/issues/new?template=experience-feedback.yml). Include the exact failed step and a minimal reproduction. Remove private URLs, credentials, and product data before posting.

请使用[体验反馈表](https://github.com/flyingrtx2333/concept-to-ui/issues/new?template=experience-feedback.yml)，写明具体失败步骤和最小复现方式。提交前请移除内部链接、凭据和产品数据。

设计要求：专业、高级简约；中文界面去掉冗余英文、副标题和重复说明。动效小样须覆盖可交互区域，并记录有理由保持静态的区域，不能只演示少数几个动画。
