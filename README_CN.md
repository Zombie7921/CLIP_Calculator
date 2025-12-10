# CLIP 计算器 (CLIP_Calculator)

[English](README.md)

本项目包含一个基于 Python 的项目，用于使用 OpenAI 的 CLIP 模型计算图像的 **CLIP 分数**，并提供增强的可视化和自定义选项。

---

## 功能特性

- **CLIP 分数计算**:
  - 基于余弦相似度评估目标图像与给定提示词的匹配程度。
  - 自动计算单张或批量图像的分数。

- **动态模型选择**:
  - 根据可用的 GPU 显存自动选择合适的 CLIP 模型。
  - 支持手动选择 OpenAI CLIP 模型。

- **提示词管理**:
  - 允许在专用文件夹 (`prompts/`) 中使用 `.txt` 文件指定提示词。
  - 自动读取第一个 `.txt` 文件进行处理。

- **批量处理**:
  - 将结果组织到单独的批次文件夹 (`Batch_X`) 中，以防止覆盖并方便追踪。

- **可视化**:
  - 提供多种图表类型：折线图、直方图、点图、散点图、箱线图、小提琴图、面积图、饼图、热力图和 3D 散点图。
  - 自定义图表颜色（使用十六进制代码）。
  - 高级图表自定义设置（例如，轴标签、图表尺寸）。

- **输出管理**:
  - 将结果存储在结构化目录中以便访问。
  - 将分数保存为 `.csv` 和 `.json` 格式，便于报告和集成。

---

## CUDA 工具包要求

鉴于本项目是基于 CUDA Toolkit 11.8 编写的，请确保在使用前安装它。如果您尚未安装，请点击此处下载并安装工具包。

## 环境要求

本项目基于 Python 3.10 和 CUDA 11.8 构建。以下是所需的依赖项：

```bash
torch==2.0.0+cu118
torchvision==0.15.1+cu118
torchaudio==2.0.0+cu118
clip-by-openai
pillow>=9.5.0
matplotlib>=3.10.0
seaborn>=0.11.2
numpy>=1.24.4
GPUtil>=1.4.0
tqdm
```

---

## 安装指南

### 1. 克隆仓库

```bash
git clone https://github.com/Zombie7921/CLIP_Calculator.git
cd CLIP_Calculator
```

### 2. 创建虚拟环境

```bash
python -m venv .venv
source .venv/bin/activate
# Windows 用户请使用: .venv\Scripts\activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

---

## 使用方法

### 命令行选项

| 参数 | 描述 | 默认值 |
|---|---|---|
| `--model` | 指定使用的 CLIP 模型（`ViT-B/32`, `RN50` 等）。 | 根据显存自动选择 |
| `--prompt_dir` | 指定包含 `.txt` 提示词文件的目录。 | `prompts/` |
| `--batch_output` | 自定义批次输出文件夹名称。 | 自动生成 (`Batch_X`) |

### 示例用法

1. 将您的图像添加到 `target_images/` 文件夹。
2. 将 `.txt` 文件添加到 `prompts/` 文件夹（例如 `description.txt`）。
3. 运行脚本：

```bash
python main.py
```

### 高级用法

指定自定义模型、提示词和批次输出文件夹：

```bash
python main.py --model ViT-B/16 --prompt_dir prompts/ --batch_output Custom_Batch
```

### Windows 快捷方式

直接双击 `run.bat` 即可运行。

---

## 结果说明

1. **已评分图像**：位于 `Batches/Batch_X/scored_images`，根据其 CLIP 分数重命名（例如 `0.8543.jpg`）。
2. **图表**：
   - 汇总图表保存在 `Batches/Batch_X/charts/` 中。
   - 单张图像图表保存在 `Batches/Batch_X/images_chart/` 中。
3. **结果数据**：分数保存在每个批次文件夹内的 `results.csv` 和 `results.json` 中。

---

## 文件夹结构

```plaintext
CLIP_Calculator/
├── prompts/                # 提示词文件文件夹
├── target_images/          # 输入图像文件夹
├── Batches/                # 包含结果的输出文件夹
│   ├── Batch_X/            # 特定批次的结果
│   │   ├── scored_images/  # 带有分数的处理后图像
│   │   ├── charts/         # 汇总可视化图表
│   │   ├── images_chart/   # 单张图像图表
│   │   ├── results/        # CSV 和 JSON 格式的分数结果
```

---

## 支持的模型

本项目支持以下 OpenAI CLIP 模型：

- `ViT-B/32`
- `ViT-B/16`
- `ViT-L/14`
- `ViT-L/14@336px`
- `RN50`
- `RN101`
- `RN50x4`
- `RN50x16`
- `RN50x64`

有关更多模型详情，请访问 [OpenAI 的 CLIP 仓库](https://github.com/openai/CLIP)。

---

## 贡献指南

我们欢迎您的贡献！如有增强功能或错误修复，请提交 issue 或 pull request。
如果您发现任何问题或有改进建议，请随时提交 issue 或 pull request。

如果您觉得本项目有用，或从中获得了灵感，请为了支持原作者的工作引用 arXiv 上的原论文 "CLIP Score" 或 GitHub 上的原 CLIP Score 项目。

---

## 致谢

- **CLIP by OpenAI**: 本项目的基础是 [CLIP 模型](https://github.com/openai/CLIP)。您也可以参考 [arXiv 上的原 CLIP 论文](https://arxiv.org/abs/2103.00020)。
- **CLIP Score Paper**: 特别感谢 ["CLIPScore"](https://arxiv.org/abs/2104.08718) 论文的作者提出了这一指标。
- **Community Contributions**: 本项目建立在 CLIP 相关项目的开源贡献之上。
- **OpenCLIP by MLFoundations**: 本仓库从 [OpenCLIP](https://github.com/mlfoundations/open_clip) 中汲取了灵感。
- **Special Thanks**: 特别感谢 "CLIP Score and CLIP" 论文的作者以及原 CLIP Score 项目的开发者。如果没有他们目前的工作成果，本项目可能无法完成。

---

## 许可证

本项目根据 Apache License 2.0 许可证授权。详情请参阅 [LICENSE](LICENSE) 文件。
