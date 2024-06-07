import os
from typing import List

# You will need to install the OpenAI Python package
from openai import APIError, OpenAI

from config import openai_key


def robot_prompt(
        text: List[str],
        model: str = "gpt-3.5-turbo"    # This is just a suggestion
) -> List[str]:
    """
    Analyze the sentiment of given texts and return a list of sentiment labels.

    Args:
    texts (List[str]): A list of texts for sentiment analysis.

    Returns:
    List[str]: A list of sentiment labels ('positive', 'negative', 'neutral')
    corresponding to the input texts.
    """
    results = []
    client = OpenAI(
        api_key=openai_key,
    )

    prompt = f"""
        What is the sentiment of the following sentence, 
        which is delimited with triple backticks?
        
        Give your answer as a single word, either "positive", "neutral" \
        or "negative".
        
        Sentence: '''{text}'''
        """

    # (logic + OpenAI API call)
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # lowercasing the responce
        sentiment = response.choices[0].message.content.strip().lower()
        results.append(sentiment)

    except APIError as e:
        print(f"Error analyzing sentiment for '{text}': {e}")
        results.append("neutral")

    return results


def test_api(st, prompt, model: str = "gpt-3.5-turbo"):
    client = OpenAI(api_key=openai_key)

    # Initialize or update the session state for storing chat messages.
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Ja sam to i to, pitaj me sta god da zelis!"}]

    # Display all chat messages stored in the session state.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Append user message to session state.
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in chat container.
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Generate a response using the LLM and display it.
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        # Extract the message content from the response
        response_text = response.choices[0].message.content.strip().lower()
        st.markdown(response_text)

        # Append assistant's response to session state.
        st.session_state.messages.append({"role": "assistant", "content": response_text})
