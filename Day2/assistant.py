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

messages = []

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "quit":
        print("\nAI: Goobye! Have a great day.")
        break

    # append the user input to the messages list
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(model=os.getenv("MODEL"), messages = messages)
    ai_reply = response.choices[0].message.content
    Console().print("\nAI:",Markdown(ai_reply))

    messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )
