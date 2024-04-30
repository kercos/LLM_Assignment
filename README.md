# Machine Learning Engineer (2024) Assignment

## Installation
- Make sure you have python >= 3.12 (tested with 3.12.1)
- Create virtual env with `python -m venv .venv`
- Acrivate it with `source .venv/bin/activate`
- Install requirements with `pip install -r requirements.txt`

## OpenAI and Gemini API Keys
- Rename the file `.env.template` to `.env` and add the Gemini and OpenAI API Keys. For Gemini API key, see https://ai.google.dev/gemini-api/docs/api-key. For OpenAI see https://openai.com/blog/openai-api.

## Custom Model
- We have hard coded the model `CarperAI/FIM-NeoX-1.3B` from HuggingFace
- For the first time, as a dry run, run `python custom.py` so that the model is downloaded locally (this may take 5-10 minutes).

## Run the server locally
- run `uvicorn main:app --reload`
- click on the provided link (typically http://127.0.0.1:8000)