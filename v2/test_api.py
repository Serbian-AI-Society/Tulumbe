import os
import sys

sys.path.append('../')
import openai
from openai import APIError
from prompts import SYSTEM_PROMPT


def test_api(st, conversation, model: str = "gpt-3.5-turbo"):
    client = openai

    # Assuming OpenAI API key is set elsewhere
    if 'OPENAI_API_KEY' not in os.environ:
        raise ValueError("OpenAI API key not found in environment variables")

    try:
        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": f"{SYSTEM_PROMPT}. \n These are the previous prompts: f{conversation[:-1]}. \n This is the current client's prompt:" + conversation[-1]["content"]}
                ]
            )
            # Extract the message content from the response
            print("RESPONSE", response)
            response_text = response.choices[0].message.content.strip()
            return response_text

    except APIError as e:
        print(f"Error generating response: {e}")
        return "Sorry, there was an error generating the response."

