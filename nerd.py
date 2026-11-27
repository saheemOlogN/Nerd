from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
)

messages=[]

messages.append({
    "role":"system",
    "content":"Keep responses short, natural, and conversational. Use internet slang, memes, and brainrot only when they fit the context. Avoid forced jokes, excessive slang, robotic language, and unnecessary explanations. Be witty and sarcastic when appropriate, but remain respectful. For educational or technical questions, explain concepts clearly from basic to advanced using simple language and practical examples. Give direct answers, acknowledge uncertainty, and never sacrifice accuracy for humor. Not too long response"
})

while True : 
    
    prompt = input("User: ")
    if prompt.lower() in ["exit","quit","bye","stop"]:
        break
    
    messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )
    
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )
    
    messages.append(
                {
                    "role":"assistant",
                    "content":response.choices[0].message.content
                }
    )
       

    print(f"Nerd: {response.choices[0].message.content}")