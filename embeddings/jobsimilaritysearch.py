import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma


# Load .env file
load_dotenv(find_dotenv())

# Initialize LLM (Chat Model)
llm=OpenAIEmbeddings()

document_loader = TextLoader("C:/langchain/embeddings/job_listings.txt").load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=10)  
chunks = text_splitter.split_documents(document_loader)
db = Chroma.from_documents(chunks, llm)

text=input("Enter the query: ")
embed_query = llm.embed_query(text)
docs = db.similarity_search_by_vector(embed_query)
for doc in docs:
    print(doc.page_content)

