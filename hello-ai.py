from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

from rich.console import Console
from rich.markdown import Markdown

client = OpenAI(base_url=os.getenv("BASE_URL"),
                api_key=os.getenv("API_KEY"))

response = client.chat.completions.create(model=os.getenv("MODEL"),
    messages = [
    {
        "role": "user",
        "content": "who is Jensen Huang?"
    }
])

Console().print(Markdown(response.choices[0].message.content))
