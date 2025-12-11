import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st

# Load .env file
load_dotenv(find_dotenv())

# Initialize LLM (Chat Model)
llm=ChatOpenAI(model="gpt-4o")
st. title("LangChain Chat with GPT-4o") 
question=st.text_input("Ask a question: ")

if question:
    # Send prompt
    response = llm.invoke(question)
    st.write(response.content)
