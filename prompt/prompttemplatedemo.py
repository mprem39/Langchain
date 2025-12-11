import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import PromptTemplate
# Load .env file
load_dotenv(find_dotenv())

# Initialize LLM (Chat Model)
llm=ChatOpenAI(model="gpt-4o")
prompt_template = PromptTemplate(
    input_variables=["country","no_of_paragraphs","language"],
    template="""
    You are an expert in traditional cuisines.
    You provide information about a specific dish from a specific country.
    Avoid giving information about fictional places. If the country is fictional
    or non-existent answer: I don't know.
    Answer the question: What is the traditional cuisine of {country}?
    Answer in {no_of_paragraphs} paragraphs in {language}.
    """
)
st. title("Cuisine Info") 
country=st.text_input("Enter the country: ")
no_of_paragraphs=st.number_input("Number of paragraphs:", min_value=1, max_value=5, value=2)
language=st.text_input("Language (e.g., English, Spanish): ", value="English")

if country:
    # Send prompt
    response = llm.invoke(prompt_template.format(country=country, no_of_paragraphs=no_of_paragraphs, language=language))    
    st.write(response.content)
