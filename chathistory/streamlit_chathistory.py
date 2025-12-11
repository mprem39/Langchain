import os
from dotenv import load_dotenv, find_dotenv

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

# Load .env
load_dotenv(find_dotenv())

st.title("Agile Guide")

# Chat History
history = StreamlitChatMessageHistory()

# LLM
llm = ChatOpenAI(model="gpt-4o")

# Prompt template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are an agile coach. Answer any questions related to agile processes."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}")
])

chain = prompt_template | llm

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda state: history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

# Text input
user_input = st.text_input("Ask a question:")

if user_input:
    response = chain_with_history.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": "agile-session"}}
    )

    st.write(response.content)
