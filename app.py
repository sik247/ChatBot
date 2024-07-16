from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI

from langchain_openai import OpenAI
from langchain_community.llms import OpenAI
import os
import streamlit as st



import streamlit as st

### Function to load openai model and get responses 



load_dotenv()  # load environment variables from .env file

def get_openai_responses(question):
    api_key = os.getenv("OPENAI_API_KEY")  # get API key from environment variables
    llm = OpenAI(api_key=api_key, model_name="gpt-3.5-turbo", temperature=0.5)
    response = llm(question)
    return response
    
    
st.set_page_config(page_title="Q&A DEMO")

st.header("Harry's AI Q&A Demo")

input = st.text_input("Input: ", key = "input")
response = get_openai_responses(input)
submit = st.button("Ask away your questions")


## IF "ask" button is clicked 


if submit: 
    st.subheader("The response is:")
    st.write(response)  # Pass the "response" variable as an argument to the function
