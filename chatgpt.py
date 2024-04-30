from dotenv import load_dotenv
from openai import OpenAI
import os

def generate_code_snippet_chatgpt(prompt):
    load_dotenv()
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.getenv('CHATGPT_API_KEY')
    )
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="gpt-3.5-turbo",
    )
    result = response.choices[0].message.content
    return result

if __name__ == "__main__":
    response = generate_code_snippet_chatgpt('Write a function in python that returns the sum of two numbers.')
    print(response)