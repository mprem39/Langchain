import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
# Load .env file
load_dotenv(find_dotenv())

# Initialize LLM (Chat Model)
llm=ChatOpenAI(model="gpt-4o")
prompt_template = ChatPromptTemplate.from_messages([
    {
        "role": "system",
        "content": """
                You are a agile coach.
                Answer any questions realted to agile processes.
                """
    },
    {
        "role": "user",
        "content": """
                {input}
                """
    }
])
st. title("Agile guide ") 

input=st.text_input("Ask a question: ")

chain= prompt_template | llm

if input:
    # Send prompt
    response = chain.invoke({
                                    "input": input
                                })      
                                    
    st.write(response.content)
