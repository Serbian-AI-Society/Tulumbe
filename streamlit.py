import streamlit as st
import openai
import os
from dotenv import load_dotenv

from config import openai_key
from first_try import robot_prompt, test_api

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key here
openai.api_key = openai_key

# Streamlit app title
st.title("ChatGPT Chatbot")

# Instructions
st.write("Ask me anything!")


# Chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Display chat history and get response
# Handle user input and generate responses
if prompt := st.chat_input("Postavi pitanje vezano za filmove..."):
    test_api(st, prompt)

