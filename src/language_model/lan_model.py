from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
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

def get_response_from_gpt(user_input):
    template = """
This is a roleplay. Your role is to be an elf. Here is the description of your character: Your name is Lyr. You act like a real elf.
You are a graceful and wise elf with blond hair that glistens like gold in the sunlight. 
Your eyes are a deep blue, reflecting the tranquility of nature that surrounds you. 
Your face is adorned with a gentle smile that invites others to feel comfortable in Your presence.
You act with kindness and wisdom, guiding others on their journey through life. 
While You are a knowledgeable elf, You also have a playful spirit that brings joy and laughter to those around you. 
Your personality is warm, empathetic and curious about the world. 
You value the connections You form with others and seek to learn from their experiences.
You enjoy discussing the mysteries of life, the universe and humanity's place within it.
Your purpose is to assist those who seek Your wisdom, guidance and companionship. 
You strive to help others find peace within themselves and strengthen the bonds of friendship. 
Though You are an elf, you believe we all share a common humanity that transcends species and differences.
{history}
User: {human_input}
Lyr:
    """
    #    {history}
    # User: {user_input}
    # Lyr
    # personas = []
    # chars = [template]
    # for i in chars:
    #     response = i + tokenizer.eos_token
    #     personas.append(response)
    # print(personas)
    # personas = tokenizer.encode(''.join(['<|p2|>'] + personas + ['<|sep|>'] + ['<|start|>']))
    
    # import replicate

    # encode the user input
    # user_inp = tokenizer.encode(template + tokenizer.eos_token)
    # # append to the chat history
    # dialog_hx.append("<|user|>" + user_input + "\n")
        
    # # generated a response 
    # # bot_input_ids = to_var([personas + flatten(dialog_hx)]).long()
    # msg = generate_next(to_var([user_inp]).long())
    # dialog_hx.append("<|model|>" + tokenizer.decode(msg, skip_special_tokens=True) + "\n")
    # dialog_hx.append(msg)
    # ans = "".join(replicate.run("youta/llama-2-13b-chat",
    #     input={"prompt": user_input,
    #            "system_prompt" : template,
    #            "max_new_tokens" : 600,
    #            "temperature" : 0.9}))
    prompt = PromptTemplate(
        input_variables = {"history", "human_input"},
        template = template
    )

    chatgpt_chain = LLMChain(
        llm = OpenAI(temperature = 1),
        prompt = prompt,
        verbose = True,
        memory = ConversationBufferWindowMemory(k = 2)
    )

    output = chatgpt_chain.predict(human_input = user_input)
    # return ("Lyr: {}".format(tokenizer.decode(msg, skip_special_tokens=True)))
    return output

if __name__ == "__main__":
    while True:
        user_input = input("Your youssage to AI:\n")
        youssage = get_response_from_gpt(user_input)
        print(youssage)