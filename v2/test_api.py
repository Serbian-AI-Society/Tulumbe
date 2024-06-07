import os
import sys

sys.path.append('../')
import openai
from openai import APIError
from prompts import SYSTEM_PROMPT

def test_api(conversation, model: str = "gpt-3.5-turbo"):
    client = openai

    # Assuming OpenAI API key is set elsewhere
    if 'OPENAI_API_KEY' not in os.environ:
        raise ValueError("OpenAI API key not found in environment variables")

    try:
        nana = (f"ovo u uglastim zagradama su prethodni upiti: "
                f"{str(conversation[:-1])} {SYSTEM_PROMPT} '''{conversation[-1]['content']}'''")
        # Generate a response using the LLM and return it
        print(nana)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": nana}
            ]
        )
        # Extract the message content from the response
        print("ODGOVOR", response)
        response_text = response.choices[0].message.content.strip().lower()
        return response_text

    except APIError as e:
        print(f"Error generating response: {e}")
        return "Sorry, there was an error generating the response."

