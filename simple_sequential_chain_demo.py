import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser  
# Load .env file
load_dotenv(find_dotenv())

# Initialize LLM (Chat Model)
llm=ChatOpenAI(model="gpt-4o")
title_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
                You are an experienced speech writer.
                You need to craft an impactful title for a speech
                on the following topic: {topic}
                Answer exactly with one title. 
            """
)

speech_prompt = PromptTemplate(
    input_variables=["title"],
    template="""
                You need to write a powerful speech of 350 words
                for the following title: {title}
            """    )
   
first_chain = title_prompt | llm | StrOutputParser() | (lambda title: (st.write(title), title)[1])
second_chain = speech_prompt | llm
prompt_template = first_chain | second_chain

st. title("Speech Generator") 
topic=st.text_input("Enter the speech topic: ")

if topic:
    # Send prompt
    response = prompt_template.invoke({
                                    "topic": topic
                                })  
    st.write(response.content)
