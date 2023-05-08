from huggingface_hub import login
import config
login(token = config.token, add_to_git_credential = False)
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
from PIL import Image

experimental_pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float16, use_auth_token=True, add_to_git_credential=True) 
experimental_pipe = experimental_pipe.to("cuda")

def post_images(type, theme, gen_prompt):
    PROMPT = gen_prompt
    with autocast("cuda"):
        img = experimental_pipe(PROMPT).images[0]
    img.save(f"gen_images/{type}/{theme}.jpg")
    return img, f"gen_images/{type}/{theme}.jpg"