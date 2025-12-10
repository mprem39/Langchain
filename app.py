import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI

# Load .env file
load_dotenv(find_dotenv())

# Initialize LLM (Chat Model)
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7
)

# Send prompt
response = llm.invoke("what is the whether in chennai?")
print(response.content)
