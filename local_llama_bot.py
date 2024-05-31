### Imports from Langchain, Streamlit for interface, and os for secure API Key storage .env
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv() #Load your environment variable

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY") #pulling langchain api key from environment variable

## Customizable Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Take a step-by-step approach when answering questions to provide more detailed responses."),
        ("user","Question:{question}")
    ]
)

## Using streamlit to create a simple use interface

st.title('Langchain+Ollama Demo with Local Llama3')
input_text=st.text_input("Hello! How can I help you?")

## Using local LLama3 through Ollama
llm=Ollama(model="llama3")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

## Launch in terminal (streamlit run 'name of your script')