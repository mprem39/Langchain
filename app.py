import os
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import init_chat_model

# Load .env file
load_dotenv(find_dotenv())

# Initialize LLM (Chat Model)
model = init_chat_model("gpt-4.1")

# Send prompt
response = model.invoke("Why do parrots talk?")
print(response.content)
