import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAIEmbeddings

# Load .env file
load_dotenv(find_dotenv())

# Initialize LLM (Chat Model)
llm=OpenAIEmbeddings()
text=input("Enter text to embed: ")

# Send prompt
response = llm.embed_query(text) 
print(response)
