# Quick start / 快速开始

This walkthrough tests the most important behavior: three real directions appear before any product UI is edited, and implementation starts only after you choose.

本指南验证最重要的行为：先出现三套真正不同的方向，选择前不修改产品 UI，选择后才进入实现。

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

Reply with `A`, `B`, `C`, or describe an exact hybrid. If you choose a hybrid, the agent should restate which elements come from each direction before implementation.

回复 `A`、`B`、`C`，或明确说明混合方案。若选择混合方案，agent 应先复述各部分来源，再开始实现。

## 4. Review the implementation / 检查实现

After implementation, verify that:

- existing routes, APIs, authentication, and key interactions still work;
- text and controls are real DOM with keyboard and focus behavior;
- the concept image was not used as a full-page background;
- the evidence folder contains an exact-viewport render, JSON report, diff, overlay, and residual note.

实现后请确认：

- 原有路由、API、认证和关键交互仍能工作；
- 文字和控件是真实 DOM，支持键盘和焦点状态；
- 概念图没有被当作整页背景；
- 证据目录包含准确视口截图、JSON 报告、差异图、叠加图和残差说明。

## 5. Share useful feedback / 提交有效反馈

Use the [experience feedback form](https://github.com/flyingrtx2333/concept-to-ui/issues/new?template=experience-feedback.yml). Include the exact failed step and a minimal reproduction. Remove private URLs, credentials, and product data before posting.

请使用[体验反馈表](https://github.com/flyingrtx2333/concept-to-ui/issues/new?template=experience-feedback.yml)，写明具体失败步骤和最小复现方式。提交前请移除内部链接、凭据和产品数据。
