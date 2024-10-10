import requests
import io
from PIL import Image
# import torch
# from diffusers import DiffusionPipeline
# from huggingface_hub import login

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}


def generate_image(prompt_text, path):
    # login(token="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")
    # pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-base", torch_dtype=torch.float16)
    # pipe = pipe.to("cuda")

    # image_bytes = pipe(
        # prompt_text,
        # negative_prompt="",
        # num_inference_steps=30,
        # guidance_scale=8.0,
    # ).images[0]
    # #image = Image.open(io.BytesIO(image_bytes))
    # image_bytes.save(path)
    # return path
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content

    image_bytes = query({"inputs": prompt_text})
    image = Image.open(io.BytesIO(image_bytes))
    image.save(path)
    return path
