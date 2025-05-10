#!/usr/bin/python
from openai import OpenAI
import os

class RunaAI(OpenAI):
    @property
    def auth_headers(self) -> dict[str, str]:
        return {"Subscription-Key": f"{self.api_key}"}

RUNAAI_SUBSCRIPTION_KEY = os.environ.get("RUNAAI_SUBSCRIPTION_KEY")

client = RunaAI(
    api_key=RUNAAI_SUBSCRIPTION_KEY,
    base_url='https://api.runaai.com/v1',
)

#global variables
temperature = 0.7
top_p = 0.7

while True:
    print("Odaberite parametar za promenu ili ENTER za nastavak. :")
    print(f"temperatura - (t)={temperature}")
    print(f"top_p - (p)={top_p}")

    user_input = input("")
    if user_input != "":
        if user_input=="t":
            temperature = float(input("Temperatura:"))
        if user_input=="p":
            top_p = float(input("top_p:"))
    else:
        break


#Global conversation state
all_messages=[{
        "role": "system",
         "content": "Ti si asistent koji uvek hoće da pomogne.",
        }]

def process_prompt():
    chat_completion = client.chat.completions.create(
    model="yugogpt",
    top_p = top_p,temperature = temperature, 
    messages=all_messages,
    max_tokens=512
    )
    
    return chat_completion

print("Pritisnite CTRL+C za izlazak ili upišite reč izađi.")
while True:
    prompt = input(">>>")
    if (prompt == "izađi" or prompt=="exit"):
        quit()
    all_messages.append({"role" : "user", "content" : prompt})
    chat_completion = process_prompt()
    response = chat_completion.choices[0].message.content
    print("YugoGPT>>>"+response)
    all_messages.append({"role" : "assistant", "content" : response})
    
