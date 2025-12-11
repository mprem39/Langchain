import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI

# Load .env file
load_dotenv(find_dotenv())

# Initialize LLM (Chat Model)
llm=ChatOpenAI(model="gpt-4o")
question=input("Ask a question: ")

# Send prompt
response = llm.invoke(question)
print(response.content)
