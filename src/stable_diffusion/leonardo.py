import requests
import json
import os
from PIL import Image
from dotenv import find_dotenv, load_dotenv
def image_from_text(user_message):
    load_dotenv(find_dotenv())
    user_message = "Anime styled 8K " + user_message
    url = "https://stablediffusionapi.com/api/v4/dreambooth"
    payload = json.dumps({
    "key": os.getenv("STABLEDIFFUSION_API_KEY"),
    "model_id": "midjourney",
    "prompt": user_message,
    "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",
  "width": "512",
  "height": "512",
  "samples": "1",
  "num_inference_steps": "30",
  "seed": None,
  "guidance_scale": 7.5,
  "webhook": None,
  "track_id": None
    })

    headers = {
    "Content-type" : "application/json"
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())
    if response.status_code == 200 and response.content:
        if os.path.isfile("image.png"):
            os.remove("image.png")
        with open("image.png", "wb") as f:
            image_link = requests.get(response.json()['future_links'][0])
            while image_link.status_code != 200:
                image_link = requests.get(response.json()['future_links'][0])
            f.write(image_link.content)
        img = Image.open("image.png")
        img.show()
        return response.content
    else: 
        print(response.status_code)

if __name__ == "__main__":
    image_from_text("Blonde Elven mage fight her enemies")
