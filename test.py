import torch
import clip

model, preprocess = clip.load("ViT-B/32", device="cuda" if torch.cuda.is_available() else "cpu")
print("CLIP model loaded successfully!")
