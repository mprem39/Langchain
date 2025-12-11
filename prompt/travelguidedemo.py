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
    input_variables=["city","month","language","budget"],
    template="""
    Welcome to the {city} travel guide!
    If you're visiting in {month}, here's what you can do:
    1. Must-visit attractions.
    2. Local cuisine you must try.
    3. Useful phrases in {language}.
    4. Tips for traveling on a {budget} budget.
    Enjoy your trip!

    """
)
st. title("Travel guide ") 
city=st.text_input("Enter the city: ")
month=st.text_input("Enter the month of visit: ")
language=st.text_input("Preferred language (e.g., English, Spanish): ", value="English")
budget=st.selectbox("Budget level (e.g., low, medium, high): ", options=["low", "medium", "high"], index=1)

if city and month and language and budget:
    # Send prompt
    response = llm.invoke(prompt_template.format(city=city, month=month, language=language, budget=budget))

    st.write(response.content)
