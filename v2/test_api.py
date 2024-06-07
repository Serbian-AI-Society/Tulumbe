import os

import openai
from openai import APIError


def test_api(conversation, model: str = "gpt-3.5-turbo"):
    client = openai

    # Assuming OpenAI API key is set elsewhere
    if 'OPENAI_API_KEY' not in os.environ:
        raise ValueError("OpenAI API key not found in environment variables")

    try:
        nana = "ovo u uglastin zagradama su predhodni upiti: " + str(conversation[:-1]) + "  ovo je poslednji korisnikov upit: " + conversation[-1]['content']
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

