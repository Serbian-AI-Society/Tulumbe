import os
from typing import List

# You will need to install the OpenAI Python package
from openai import APIError, OpenAI


def robot_prompt(
        texts: List[str],
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
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    for line in texts:
        line = line.strip()
        if not line:
            results.append("neutral")
            continue

        prompt = f"""
What is the sentiment of the following sentence, 
which is delimited with triple backticks?

Give your answer as a single word, either "positive", "neutral" \
or "negative".

Sentence: '''{line}'''
"""
        # in case of an error append neutral as the result
        try:
        # (logic + OpenAI API call)
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            # lowercasing the responce
            sentiment = response['choices'][0]['message']['content'].strip().lower()
            results.append(sentiment)
        except APIError as e:
            print(f"Error analyzing sentiment for '{line}': {e}")
            results.append("neutral")
        except (KeyError, IndexError, AttributeError) as e:
            print(f"Error processing API response: {e}")
            try:
                sentiment = response.choices[0].message.content.strip().lower()
                results.append(sentiment)
            except (KeyError, IndexError, AttributeError) as e:
                results.append("neutral")

    return results
