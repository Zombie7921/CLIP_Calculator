import os
import clip
import torch
import requests
import GPUtil

# Directory to store downloaded models
MODEL_DIR = "models"

# CLIP model URLs from the OpenAI project
CLIP_MODEL_URLS = {
    "RN50": "https://openaipublic.azureedge.net/clip/models/afeb0e10f9e5a86da6080e35cf09123aca3b358a0c3e3b6c78a7b63bc04b6762/RN50.pt",
    "RN101": "https://openaipublic.azureedge.net/clip/models/8fa8567bab74a42d41c5915025a8e4538c3bdbe8804a470a72f30b0d94fab599/RN101.pt",
    "RN50x4": "https://openaipublic.azureedge.net/clip/models/7e526bd135e493cef0776de27d5f42653e6b4c8bf9e0f653bb11773263205fdd/RN50x4.pt",
    "RN50x16": "https://openaipublic.azureedge.net/clip/models/52378b407f34354e150460fe41077663dd5b39c54cd0bfd2b27167a4a06ec9aa/RN50x16.pt",
    "RN50x64": "https://openaipublic.azureedge.net/clip/models/be1cfb55d75a9666199fb2206c106743da0f6468c9d327f3e0d0a543a9919d9c/RN50x64.pt",
    "ViT-B/32": "https://openaipublic.azureedge.net/clip/models/40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af/ViT-B-32.pt",
    "ViT-B/16": "https://openaipublic.azureedge.net/clip/models/5806e77cd80f8b59890b7e101eabd078d9fb84e6937f9e85e4ecb61988df416f/ViT-B-16.pt",
    "ViT-L/14": "https://openaipublic.azureedge.net/clip/models/b8cca3fd41ae0c99ba7e8951adf17d267cdb84cd88be6f7c2e0eca1737a03836/ViT-L-14.pt",
    "ViT-L/14@336px": "https://openaipublic.azureedge.net/clip/models/3035c92b350959924f9f00213499208652fc7ea050643e8b385c2dac08641f02/ViT-L-14-336px.pt",
}

# Function to download a model if it's not already downloaded
def download_model(model_name):
    if model_name not in CLIP_MODEL_URLS:
        raise ValueError(f"Model {model_name} is not available. Choose from: {list(CLIP_MODEL_URLS.keys())}")

    url = CLIP_MODEL_URLS[model_name]
    sanitized_model_name = model_name.replace("/", "_")  # Replace forward slash with underscore
    model_path = os.path.join(MODEL_DIR, f"{sanitized_model_name}.pt")
    os.makedirs(MODEL_DIR, exist_ok=True)

    if not os.path.exists(model_path):
        print(f"Downloading {model_name} from {url}...")
        response = requests.get(url, stream=True)
        with open(model_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"{model_name} downloaded successfully!")
    else:
        print(f"{model_name} is already downloaded.")
    return model_path


# Function to load the CLIP model and preprocess function
def load_model(model_name):
    """
    Load a CLIP model from a pre-downloaded file or URL.
    """
    model_path = download_model(model_name)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load(model_path, device=device)
    return model, preprocess, device

# Function to select a model based on VRAM
def select_model_based_on_vram():
    gpus = GPUtil.getGPUs()
    if not gpus:
        print("No GPU found. Defaulting to the smallest model (RN50).")
        return "RN50"

    available_vram = max(gpu.memoryFree for gpu in gpus)  # Get the largest available VRAM
    print(f"Available VRAM: {available_vram} MB")

    if available_vram >= 16000:
        return "ViT-L/14@336px"
    elif available_vram >= 12000:
        return "ViT-L/14"
    elif available_vram >= 8000:
        return "ViT-B/16"
    elif available_vram >= 4000:
        return "ViT-B/32"
    else:
        return "RN50"

if __name__ == "__main__":
    import argparse

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Download and load CLIP models dynamically.")
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="CLIP model to use. Options: RN50, RN101, RN50x4, RN50x16, RN50x64, ViT-B/32, ViT-B/16, ViT-L/14, ViT-L/14@336px. If not specified, the model will be selected based on available VRAM.",
    )
    args = parser.parse_args()

    # Determine the model to use
    model_name = args.model if args.model else select_model_based_on_vram()
    print(f"Selected model: {model_name}")

    # Load the selected model
    model, preprocess, device = load_model(model_name)
    print(f"Using CLIP model: {model_name}")
