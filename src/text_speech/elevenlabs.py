from dotenv import find_dotenv, load_dotenv
import requests
from playsound import playsound
import os
# import replicate
# from transformers import GPT2Tokenizer, GPT2LMHeadModel
# import torch
# from transformers import AutoTokenizer, AutoModelForCausalLM
# tokenizer = GPT2Tokenizer.from_pretrained("af1tang/personaGPT", padding_side='left')
# model = GPT2LMHeadModel.from_pretrained("af1tang/personaGPT")

# tokenizer = AutoTokenizer.from_pretrained("PygmalionAI/pygmalion-350m")
# model = AutoModelForCausalLM.from_pretrained("PygmalionAI/pygmalion-350m")
# if torch.cuda.is_available():
#     model = model.cuda()
# ## utility functions ##
# flatten = lambda l: [item for sublist in l for item in sublist]

# def to_data(x):
#     if torch.cuda.is_available():
#         x = x.cpu()
#     return x.data.numpy()

# def to_var(x):
#     if not torch.is_tensor(x):
#         x = torch.Tensor(x)
#     if torch.cuda.is_available():
#         x = x.cuda()
#     return x

# def display_dialog_history(dialog_hx):
#     for j, line in enumerate(dialog_hx):
#         msg = tokenizer.decode(line)
#         if j %2 == 0:
#             print(">> User: "+ msg)
#         else:
#             print("Bot: "+msg)
#             print()

# def generate_next(bot_input_ids, do_sample=True, top_k=10, top_p=.92,
#                   max_length=100000, pad_token=tokenizer.eos_token_id):
#     full_msg = model.generate(bot_input_ids, do_sample=True,
#                                               max_length=max_length, pad_token_id=tokenizer.eos_token_id)
#     msg = to_data(full_msg.detach()[0])[bot_input_ids.shape[-1]:]
#     return msg

load_dotenv(find_dotenv())

def get_vm(message):
    url = "https://api.elevenlabs.io/v1/text-to-speech/7rHqOGmcvKg1uYAm3UwT"
    payload = {
        "text" : message,
        "model_id" : "eleven_monolingual_v1",
        "voice_settings": {
            "stability" : 0,
            "similarity_boost" : 0
        }
    }

    headers = {
        "Accept" : "audio/mpeg",
        "xi-api-key" : os.getenv("ELEVENLABS_API_KEY"),
        "Content-type" : "application/json"
    }

    response = requests.post(url = url, json = payload, headers = headers)

    if response.status_code == 200 and response.content:
        os.remove("audio.mp3")
        with open("audio.mp3", "wb") as f:
            f.write(response.content)
        playsound("audio.mp3")
        return response.content
    else: 
        print(response.status_code)
if __name__ == "__main__":
    user_input = "Greetings, fellow traveler. How may I be of assistance to you?"
    message = get_vm(user_input)
