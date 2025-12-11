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
    input_variables=["title", "Emotion"],
    template="""
                You need to write a powerful {Emotion} speech of 350 words
                for the following title: {title}
                format the output with two keys: 'Title' and 'Speech' and fill them accordingly.
            """    )
   
first_chain = title_prompt | llm | StrOutputParser() | (lambda title: (st.write(title), title)[1])
second_chain = speech_prompt | llm
prompt_template = first_chain | (lambda title: {"title": title, "Emotion": emotion}) |  second_chain

st. title("Speech Generator") 
topic=st.text_input("Enter the speech topic: ")
emotion=st.selectbox("Enter the emotion for the speech: ", ["Happy", "Sad", "Angry", "Inspirational"])

if topic and emotion:
    # Send prompt
    response = prompt_template.invoke({
                                    "topic": topic, "Emotion": emotion      
                                })  
    st.write(response.content)      
