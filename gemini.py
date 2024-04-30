from dotenv import load_dotenv
import google.generativeai as genai
import os

def generate_code_snippet_gemini(prompt):
    load_dotenv()
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    response = generate_code_snippet_gemini('Write a function in python that returns the sum of two numbers.')
    print(response)