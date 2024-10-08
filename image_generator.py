import requests
import io
from PIL import Image
import torch
from diffusers import StableDiffusion3Pipeline

# API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
# headers = {"Authorization": "Bearer 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"}


def generate_image(prompt_text, path):
    pipe = StableDiffusion3Pipeline.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers", torch_dtype=torch.float16)
    pipe = pipe.to("cuda")

    image_bytes = pipe(
        "A cat holding a sign that says hello world",
        negative_prompt="",
        num_inference_steps=15,
        guidance_scale=2.0,
    ).images[0]
    image = Image.open(io.BytesIO(image_bytes))
    image.save(path)
    return path
