import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key here
openai.api_key = "sk-proj-Y7ryjyiNUwrnpk7mtyerT3BlbkFJS4bclMYbbjjI5L02JE56"

# Streamlit app title
st.title("ChatGPT Streamlit Chatbot")

# Instructions
st.write("Ask me anything!")

# Text input box for user prompt
user_input = st.text_input("You:", "")

# Chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Function to get OpenAI response
def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # or 'gpt-4' if available
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.9,
    )
    message = response.choices[0].text.strip()
    return message

# Display chat history and get response
if user_input:
    st.session_state['chat_history'].append(f"You: {user_input}")
    response = get_openai_response(user_input)
    st.session_state['chat_history'].append(f"Bot: {response}")

# Display the conversation
for i, chat in enumerate(st.session_state['chat_history']):
    if i % 2 == 0:
        st.text_area("User", value=chat, key=str(i), height=50, disabled=True)
    else:
        st.text_area("Bot", value=chat, key=str(i), height=50, disabled=True)
