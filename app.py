import streamlit as st
import openai
import os
from dotenv import load_dotenv
from test_api import test_api

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key here
openai.api_key = os.environ['OPENAI_API_KEY']

logo_path = "images/logo3.png"
# Streamlit app title
st.set_page_config(page_title="TulumbeGPT", page_icon=logo_path)
st.image(logo_path, width=100)
st.title("TulumbeGPT")

# Instructions
st.write("Nisi siguran koji film da gledaš? Ili si već pogledao sve i ne znaš šta dalje? "
         "Na pravom si mestu! Opiši kako se osećaš ili kakvo osećanje želiš da film probudi u tebi,"
         " a ja ću se potruditi da ti preporučim savršen film!")

# Frequently Asked Questions
with st.expander("❓Kako koristiti TulumbeGPT"):
    st.write("""
        **Kako funkcioniše TulumbeGPT?**
        TulumbeGPT koristi napredne alate za analizu vaših osećanja i preferencija
        kako bi vam preporučio najbolje filmove.

        **Koje filmove može TulumbeGPT da preporuči?**
        Naša baza podataka sadrži hiljade filmova različitih žanrova, uključujući najnovije
        hitove i bezvremenske klasike.

        **Kako korisnik može da dobije preporuku filma?**
        Samo unesite kako se osećate ili kakvo osećanje želite da film izazove i mi ćemo vam
        preporučiti savršen film.
    """)

with st.expander("❓Često postavljana pitanja"):
    st.write("""
        **Osecam se tuzno, preporuci mi neki film da me oraspolozi**

        **Zelim da gledam neki film sa dinosaurusima**

        **Preporuci mi nekoliko avanturisticnih filmove koji bi mogli da me odvedu u neku drugaciju realnost**

    """)

# Display some popular movie images
st.subheader("Popularni filmovi")
cols = st.columns(4)
images = ["images/image1.jpg", "images/image2.jpg", "images/image3.jpg", "images/image4.jpg"]

for col, img in zip(cols, images):
    col.image(img, use_column_width=True)


# Chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Display all chat messages stored in the session state
for message in st.session_state['chat_history']:
    if message["role"] == "user":
        st.chat_message("user").markdown(message["content"])
    else:
        st.chat_message("assistant").markdown(message["content"])

# Text input box for user prompt
user_input = st.chat_input("Kakav film želiš da gledaš?")

# Handle user input and generate responses
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state['chat_history'].append({"role": "user", "content": user_input})

    # Generate a response using the LLM and store it
    response = test_api(st, st.session_state['chat_history'])
    st.session_state['chat_history'].append({"role": "assistant", "content": response})

# JavaScript code to scroll to the bottom of the chat container
scroll_script = """
<script>
window.scrollTo(0, document.body.scrollHeight);
</script>
"""
st.write(scroll_script, unsafe_allow_html=True)
