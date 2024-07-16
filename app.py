from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI

from langchain_openai import OpenAI
from langchain_community.llms import OpenAI
import os
import streamlit as st

### Function to load openai model and get responses 



load_dotenv()  # load environment variables from .env file

# Function to load OpenAI model and get responses
def get_openai_responses(question):
    api_key = os.getenv("OPENAI_API_KEY")  # get API key from environment variables
    llm = OpenAI(api_key=api_key, model_name="gpt-3.5-turbo", temperature=0.5)
    response = llm(question)
    return response

# Streamlit page configuration
st.set_page_config(page_title="Q&A DEMO", page_icon=":robot_face:", layout="centered")

# Page header
st.title("Harry's AI Q&A Demo")
st.markdown("Welcome to the AI-powered Q&A demo. Ask any question and get a response from OpenAI's GPT-3.5-turbo model.")

# Input section
st.sidebar.header("Ask your question")
input_question = st.sidebar.text_input("Input: ", key="input")

# Button to submit the question
submit = st.sidebar.button("Ask away your questions")

# Display response if the button is clicked
if submit:
    with st.spinner("Getting response..."):
        response = get_openai_responses(input_question)
    st.subheader("The response is:")
    st.write(response)

# Footer
st.markdown("---")
st.markdown("Developed by Harry. Powered by [OpenAI](https://www.openai.com) and [Streamlit](https://streamlit.io).")