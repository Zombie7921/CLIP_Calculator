import os
import requests

# Define a list of models with their URLs and expected file sizes for verification
MODELS = [
    {
        "name": "RN50",
        "url": "https://openaipublic.blob.core.windows.net/clip/models/clip/RN50.pt",
        "expected_size": 102884236  # File size in bytes
    },
    {
        "name": "RN101",
        "url": "https://openaipublic.blob.core.windows.net/clip/models/clip/RN101.pt",
        "expected_size": 170257303  # File size in bytes
    },
    {
        "name": "RN50x4",
        "url": "https://openaipublic.blob.core.windows.net/clip/models/clip/RN50x4.pt",
        "expected_size": 178604983  # File size in bytes
    },
    {
        "name": "RN50x16",
        "url": "https://openaipublic.blob.core.windows.net/clip/models/clip/RN50x16.pt",
        "expected_size": 329455054  # File size in bytes
    },
    {
        "name": "RN50x64",
        "url": "https://openaipublic.blob.core.windows.net/clip/models/clip/RN50x64.pt",
        "expected_size": 1105943367  # File size in bytes
    },
    {
        "name": "ViT-B/32",
        "url": "https://openaipublic.blob.core.windows.net/clip/models/clip/ViT-B-32.pt",
        "expected_size": 170257303  # File size in bytes
    },
    {
        "name": "ViT-B/16",
        "url": "https://openaipublic.blob.core.windows.net/clip/models/clip/ViT-B-16.pt",
        "expected_size": 344380155  # File size in bytes
    },
    {
        "name": "ViT-L/14",
        "url": "https://openaipublic.blob.core.windows.net/clip/models/clip/ViT-L-14.pt",
        "expected_size": 428531238  # File size in bytes
    },
    {
        "name": "ViT-L/14@336px",
        "url": "https://openaipublic.blob.core.windows.net/clip/models/clip/ViT-L-14-336px.pt",
        "expected_size": 546766937  # File size in bytes
    }
]

# Define the directory where models will be downloaded
MODELS_DIR = "models"


def download_model(model):
    """Download a model file and save it to the models directory."""
    model_path = os.path.join(MODELS_DIR, f"{model['name']}.pt")

    if os.path.exists(model_path):
        print(f"{model['name']} already exists. Skipping download.")
        return True

    print(f"Downloading {model['name']}...")
    try:
        response = requests.get(model["url"], stream=True)
        response.raise_for_status()

        with open(model_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Download completed: {model['name']}")
        return True
    except Exception as e:
        print(f"Failed to download {model['name']}: {e}")
        return False


def verify_model(model):
    """Verify the downloaded model's size and integrity."""
    model_path = os.path.join(MODELS_DIR, f"{model['name']}.pt")

    if not os.path.exists(model_path):
        print(f"{model['name']} is missing.")
        return False

    actual_size = os.path.getsize(model_path)
    if actual_size != model["expected_size"]:
        print(f"{model['name']} size mismatch. Expected {model['expected_size']}, got {actual_size}.")
        return False

    print(f"{model['name']} verified successfully.")
    return True


def main():
    """Main function to download and verify all models."""
    if not os.path.exists(MODELS_DIR):
        os.makedirs(MODELS_DIR)

    print("Starting model downloads...\n")
    for model in MODELS:
        success = download_model(model)
        if success:
            verified = verify_model(model)
            if not verified:
                print(f"Verification failed for {model['name']}. Please re-download.")
        else:
            print(f"Download failed for {model['name']}.")

    print("\nAll models processed.")


if __name__ == "__main__":
    main()
