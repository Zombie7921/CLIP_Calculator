import argparse
import csv
import json
import os
import clip
import torch
from PIL import Image

from chart_selection import select_chart_type, select_color
from dynamic_model_loader import load_model, select_model_based_on_vram
from prompt_selection import get_prompt_from_folder
from visualization_options import visualize


# Function to create output directory
def create_output_dir(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

# Function to find the next batch folder
def get_next_batch_folder(base_dir):
    """
    Determines the next available batch folder name.
    """
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        return os.path.join(base_dir, "Batch_1")

    batch_folders = [folder for folder in os.listdir(base_dir) if folder.startswith("Batch_")]
    batch_numbers = [int(folder.split("_")[1]) for folder in batch_folders if folder.split("_")[1].isdigit()]
    next_batch_number = max(batch_numbers) + 1 if batch_numbers else 1
    return os.path.join(base_dir, f"Batch_{next_batch_number}")

# Function to calculate CLIP scores and save images, charts, and results
def calculate_clip_scores_and_save(target_dir, prompt, output_dir, model, preprocess, device):
    """
    Calculates CLIP scores for images, saves processed images, results, and prepares folders for charts.
    """
    if not os.path.exists(target_dir):
        raise FileNotFoundError(f"Target directory '{target_dir}' does not exist.")

    # Create necessary subdirectories
    scored_images_dir = os.path.join(output_dir, "scored_images")
    charts_dir = os.path.join(output_dir, "charts")
    images_chart_dir = os.path.join(output_dir, "images_chart")
    results_dir = os.path.join(output_dir, "results")

    os.makedirs(scored_images_dir, exist_ok=True)
    os.makedirs(charts_dir, exist_ok=True)
    os.makedirs(images_chart_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)

    # Process images and calculate scores
    results = []
    for image_name in os.listdir(target_dir):
        image_path = os.path.join(target_dir, image_name)
        if not os.path.isfile(image_path):  # Skip non-files
            print(f"Skipping non-file: {image_name}")
            continue

        try:
            # Preprocess the image
            print(f"Processing: {image_name}")
            image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
            text = clip.tokenize([prompt]).to(device)

            # Calculate features
            with torch.no_grad():
                image_features = model.encode_image(image)
                text_features = model.encode_text(text)

            # Normalize and calculate similarity
            image_features /= image_features.norm(dim=-1, keepdim=True)
            text_features /= text_features.norm(dim=-1, keepdim=True)
            score = (image_features @ text_features.T).item()
            print(f"Score for {image_name}: {score}")

            # Save scored image
            scored_image_name = f"{score:.4f}.jpg"
            scored_image_path = os.path.join(scored_images_dir, scored_image_name)
            Image.open(image_path).save(scored_image_path)
            print(f"Saved scored image to: {scored_image_path}")

            # Store results
            results.append({
                "image_index": len(results) + 1,
                "image_name": image_name,
                "clip_score": score,
                "scored_image_path": scored_image_name
            })

        except Exception as e:
            print(f"Error processing {image_name}: {e}")

    # Save results to CSV and JSON
    results_csv_path = os.path.join(results_dir, "results.csv")
    results_json_path = os.path.join(results_dir, "results.json")
    with open(results_csv_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["image_index", "image_name", "clip_score", "scored_image_path"])
        writer.writeheader()
        writer.writerows(results)
    with open(results_json_path, "w") as jsonfile:
        json.dump(results, jsonfile, indent=4)

    print(f"Results saved to: {results_csv_path} and {results_json_path}")
    return results, charts_dir, images_chart_dir

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Calculate CLIP scores for target images.")
    parser.add_argument("--model", type=str, default=None, help="CLIP model to use. If not specified, it will be selected based on VRAM.")
    parser.add_argument("--prompt_dir", type=str, default="prompts", help="Directory containing prompts .txt files.")
    args = parser.parse_args()

    # Load the prompts using the new `prompt_selection.py` module
    try:
        prompt = get_prompt_from_folder(args.prompt_dir)
    except FileNotFoundError as e:
        print(e)
        exit(1)

    # Determine the model to use
    model_name = args.model if args.model else select_model_based_on_vram()
    print(f"Selected model: {model_name}")
    model, preprocess, device = load_model(model_name)

    # Determine the batch folder for this run
    batch_folder = get_next_batch_folder("Batches")
    create_output_dir(batch_folder)
    print(f"Running Batch: {os.path.basename(batch_folder)}")

    # Calculate CLIP scores and save images, charts, and results
    scores, charts_dir, images_chart_dir = calculate_clip_scores_and_save("target_images", prompt, batch_folder, model, preprocess, "cuda" if torch.cuda.is_available() else "cpu")

    # Prompt user for visualization settings
    print("Select visualization settings:")

    # Summary chart options
    summary_chart_type = select_chart_type("summary chart")
    summary_chart_color = select_color("summary chart")

    # Single-image chart options
    single_chart_type = select_chart_type("single-image chart")
    single_chart_color = select_color("single-image chart")

    advanced_settings = {
        "figsize": (12, 6),
        "xlabel": "Images",
        "ylabel": "CLIP Scores"
    }

    # Visualize results
    visualize(
        scores,
        summary_chart_type,
        summary_chart_color,
        advanced_settings,
        charts_dir,
        images_chart_dir,
        single_chart_type=single_chart_type,
        single_chart_color=single_chart_color
    )
