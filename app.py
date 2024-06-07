import streamlit as st
import openai
import os
from dotenv import load_dotenv
import sys
from config import openai_key
from test_api import test_api


# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key here
openai.api_key = os.getenv('API_KEY')

# Streamlit app title
st.title("TulumbeGPT")

# Instructions
st.write("Nisi siguran koji film da gledaš? Ili si već pogledao sve i ne znaš šta dalje? "
         "Na pravom si mestu! Opiši kako se osećaš ili kakvo osećanje želiš da film probudi u tebi,"
         " a ja ću se potruditi da ti preporučim savršen film!")

# Chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Text input box for user prompt
user_input = st.chat_input("Kakav film želiš da gledaš?")

# Handle user input and generate responses
if user_input:
    st.session_state['chat_history'].append({"role": "user", "content": user_input})

    # Generate a response using the LLM and store it
    response = test_api(st, st.session_state['chat_history'])
    st.session_state['chat_history'].append({"role": "assistant", "content": response})

# Display all chat messages stored in the session state
for message in st.session_state['chat_history']:
    if message["role"] == "user":
        st.chat_message("user").markdown(message["content"])
    else:
        st.chat_message("assistant").markdown(message["content"])
