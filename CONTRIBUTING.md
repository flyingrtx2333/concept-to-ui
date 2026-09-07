# Contributing

感谢贡献。请保持这个 skill 的核心行为稳定：

1. 在概念选择前不修改目标产品 UI。
2. 每个方向都必须是完整界面概念，而不是只有换色。
3. 参考图测量和截图对比必须使用仓库内的确定性脚本。
4. 不把真实产品数据、内部路径、凭据或生产环境信息写进 skill。
5. 让 visible text、控件和交互保持真实 DOM，而不是把整页栅格化。

提交前请运行：

```powershell
python -m unittest discover -s tests -v
```

如果修改了 skill 结构或元数据，还请运行 Codex 的 `quick_validate.py`。
