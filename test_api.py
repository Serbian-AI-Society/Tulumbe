import openai
from openai import APIError
from prompts import SYSTEM_PROMPT
import os


def test_api(st, conversation, model: str = "gpt-3.5-turbo"):
    client = openai

    # Assuming OpenAI API key is set elsewhere
    if 'OPENAI_API_KEY' not in os.environ:
        raise ValueError("OpenAI API key not found in environment variables")

    try:
        with st.chat_message("assistant"):
            # Initiate the streaming response
            response_stream = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    *conversation
                ],
                stream=True
            )

            response = st.write_stream(response_stream)
            return response

    except APIError as e:
        print(f"Error generating response: {e}")
        return "Sorry, there was an error generating the response."
