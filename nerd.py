from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
)

while True : 
    
    prompt = input("User: ")
    if prompt.lower in ["exit","quit","bye","stop"]:
        break
    
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role":"user",
                "content":"Hello Nerd"
            }
        ]
    )

    print(f"Nerd: {response.choices[0].message.content}")