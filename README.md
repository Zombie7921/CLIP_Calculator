# CLIP_Calculator

This repository contains a Python-based project to calculate **CLIP scores** for images using OpenAI's CLIP model, with enhanced visualization and customization options.

---

## Features

- **CLIP Score Calculation**:
  - Evaluate how well target images align with a given text prompt using cosine similarity.
  - Calculates scores for single or batch images automatically.

- **Dynamic Model Selection**:
  - Automatically selects the appropriate CLIP model based on available GPU VRAM.
  - Supports manual model selection from available OpenAI CLIP models.

- **Prompt Management**:
  - Allows specifying prompts in a dedicated folder (`prompts/`) with `.txt` files.
  - Automatically reads the first `.txt` file for processing.

- **Batch Processing**:
  - Organizes results into separate batch folders (`Batch_X`) to prevent overwriting and allow easy tracking.

- **Visualization**:
  - Provides multiple chart types: Line Chart, Histogram, Dot Chart, Scatter Chart, Box Plot, Violin Plot, Area Chart, Pie Chart, Heatmap, and 3D Scatter Plot.
  - Custom color options for charts (using hex codes).
  - Advanced settings for chart customization (e.g., axis labels, figure size).

- **Output Management**:
  - Stores results in structured directories for easy access.
  - Saves scores in both `.csv` and `.json` formats for reporting and integration.

---
## CUDA Toolkit Requirements
Considering this project is written on CUDA Toolkit 11.8, make sure you have installed it before use. If you haven’t installed it yet, click here to download and install the toolkit.


## Requirements

This project is built for Python 3.10 and CUDA 11.8. Below are the required dependencies:

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

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Zombie7921/CLIP_Calculator.git
cd CLIP_Calculator
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Command-Line Options

| Argument         | Description                                                                 | Default Value                     |
|-------------------|-----------------------------------------------------------------------------|-----------------------------------|
| `--model`         | Specify the CLIP model to use (`ViT-B/32`, `RN50`, etc.).                   | Automatically selected by VRAM    |
| `--prompt_dir`    | Specify the directory containing `.txt` prompt files.                      | `prompts/`                        |
| `--batch_output`  | Customize batch output folder name.                                         | Auto-generated (`Batch_X`)        |

### Example Usage

1. Add your images to the `target_images/` folder.
2. Add `.txt` files to the `prompts/` folder (e.g., `description.txt`).
3. Run the script:

```bash
python calculate_clip_score.py
```

### Advanced Usage

Specify a custom model, prompt, and batch output folder:

```bash
python calculate_clip_score.py --model ViT-B/16 --prompt_dir prompts/ --batch_output Custom_Batch
```

---

## Results

1. **Scored Images**: Located in `Batches/Batch_X/scored_images`, renamed based on their CLIP scores (e.g., `0.8543.jpg`).
2. **Charts**:
   - Summary charts saved in `Batches/Batch_X/charts/`.
   - Individual image charts saved in `Batches/Batch_X/images_chart/`.
3. **Results**: Scores saved in `results.csv` and `results.json` within each batch folder.

---

## Folder Structure

```plaintext
CLIP_Calculator/
├── prompts/                # Folder for prompt text files
├── target_images/          # Folder for input images
├── Batches/                # Output folder containing results
│   ├── Batch_X/            # Batch-specific results
│   │   ├── scored_images/  # Processed images with scores
│   │   ├── charts/         # Summary visualization charts
│   │   ├── images_chart/   # Individual image charts
│   │   ├── results/        # CSV and JSON score results
```

---

## Example Results

### Input
- **Target Images**: 5 images in the `target_images/` folder.
- **Prompt**: `"A scenic view of a mountain lake."`

### Output
- `Batch_X/scored_images`: Images renamed based on their scores.
- `Batch_X/charts`: A summary chart of all images in the batch.
- `Batch_X/results`: `results.csv` and `results.json` containing the score data.

---

## Supported Models

This project supports the following OpenAI CLIP models:
- `ViT-B/32`
- `ViT-B/16`
- `ViT-L/14`
- `ViT-L/14@336px`
- `RN50`
- `RN101`
- `RN50x4`
- `RN50x16`
- `RN50x64`

For more model details, visit [OpenAI's CLIP repository](https://github.com/openai/CLIP).

---

## Contribution

We welcome contributions! Please open an issue or submit a pull request for enhancements or bug fixes.

If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

If you find this project useful, or it has inspired you, please cite the original paper "CLIP Score" on arXiv or the original CLIP Score project on GitHub to contribute to their work.

---

## Acknowledgments

- **CLIP by OpenAI**: The foundation of this project is the [CLIP model](https://github.com/openai/CLIP). You can also refer to the [original CLIP paper on arXiv](https://arxiv.org/abs/2103.00020).
- **CLIP Score Paper**: Special thanks to the authors of the ["CLIPScore"](https://arxiv.org/abs/2104.08718) paper for introducing this metric.
- **Community Contributions**: This work builds on open-source contributions to CLIP-related projects.
- **OpenCLIP by MLFoundations**: This repository draws inspiration from [OpenCLIP](https://github.com/mlfoundations/open_clip).
- **Special Thanks**: Special thanks to the authors of the "CLIP Score and CLIP" paper and the developers of the original CLIP Score project. If not based on the current outcomes of their efforts, this project might not have been completed.

---

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.
