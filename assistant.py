from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

from rich.console import Console
from rich.markdown import Markdown

client = OpenAI(base_url=os.getenv("BASE_URL"),
                api_key=os.getenv("API_KEY"))

print("*" * 40)
print("        My AI Assistant")
print("*" * 40)

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "quit":
        print("\nAI: Goobye! Have a great day.")
        break

    response = client.chat.completions.create(model=os.getenv("MODEL"),
        messages = [
        {
            "role": "user",
            "content": user_input
        }
    ])

    Console().print("\nAI:",Markdown(response.choices[0].message.content))
