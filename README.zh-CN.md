# concept-to-ui

**先选视觉概念，再体验并选择动效，最后接入正式功能。**

[English](README.md) · [快速开始](QUICKSTART.md) · [提交体验反馈](https://github.com/flyingrtx2333/concept-to-ui/issues/new?template=experience-feedback.yml)

`concept-to-ui` 是一个采用 MIT 许可证的 Codex skill，用于“概念优先”的 UI 重设计。它会先检查现有页面，生成三套有实质差异的完整界面方案，等待你选择视觉方向，再提供 2–3 套同布局的可操作动效小样。选定动效后才接入正式功能，并分别验证静态画面和动态交互。

它的核心是“选择关卡”：不让 agent 一收到“优化 UI”就直接按自己的第一个想法改代码。

首次交付前先完成构图推敲、草稿比较和必要修整。三套选择项必须通过展示质量检查，不能把通用模板、粗糙字体或明显错误的图表留给用户筛选，也不能用“实现时修正”绕过检查。“一遍出好图”指首次交付经过筛选的方案；不承诺模型单次生成或主观审美必然命中。流程见[概念质量关卡](references/concept-quality.md)。

H5、网站、小程序、桌面和原生应用统一以有辨识度的高端设计为目标：先实际研究优秀作品，再确定各方向的构图、字体、材质和视觉主题。粒子、光场等表现手法按产品与平台适配，概念图的静态表现和真实动效分别验收；简洁可用的通用模板仍需继续打磨。

内置[设计参考库](references/design-library/index.md)：12 个案例、18 张本地截图，附来源、观察日期、可迁移关系及证据限制。按任务选择少量相关案例查看，参考库只供研究，不作为产品素材或固定模板。

## 工作流程

1. 检查现有页面、路由、交互和约束。
2. 生成完整的 A/B/C 三套设计方向。
3. 停下来，等待用户选择视觉方向。
4. 基于相同布局和示例数据，制作 2–3 套独立动效小样，等待用户体验并选择。
5. 用真实 Web 或原生控件及产品数据，接入选定视觉和动效。
6. 静态截图输出对比证据；开启动画，检查连续操作、中途反向及减少动态效果。

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

- 支持内置图像生成及对应平台预览、截图的 Codex 环境
- 原生 App 需要对应平台的构建运行工具；Web 使用本地浏览器预览
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

设计要求：专业、高级简约；中文界面去掉冗余英文、副标题和重复说明。动效小样须覆盖可交互区域，并记录有理由保持静态的区域，不能只演示少数几个动画。
