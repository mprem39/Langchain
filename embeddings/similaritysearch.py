import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAIEmbeddings
import numpy as np

# Load .env file
load_dotenv(find_dotenv())

# Initialize LLM (Chat Model)
llm=OpenAIEmbeddings()
text1=input("Enter text1 to embed: ")
text2=input("Enter text2 to embed: ")

# Send prompt
response1 = llm.embed_query(text1) 
response2 = llm.embed_query(text2)
similarity = np.dot(response1, response2) / (np.linalg.norm(response1) * np.linalg.norm(response2))
print(similarity)
