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

#Global conversation state
all_messages=[{
        "role": "system",
         "content": "Ti si asistent koji uvek hoće da pomogne.",
        }]

def process_prompt():
    chat_completion = client.chat.completions.create(
    messages=all_messages,
    model="yugogpt",
    max_tokens=512
    )
    
    return chat_completion

print("Pritisnite CTRL+C za izlazak.")
while True:
    prompt = input(">>>")
    all_messages.append({"role" : "user", "content" : prompt})
    chat_completion = process_prompt()
    response = chat_completion.choices[0].message.content
    print("YugoGPT>>>"+response)
    all_messages.append({"role" : "assistant", "content" : response})
    
