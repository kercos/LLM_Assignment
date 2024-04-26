# Machine Learning Engineer (2024) Assignment

## Installation
- Make sure you have python >= 3.12 (tested with 3.12.1)
- create virtual env with `python -m venv .venv`
- acrivate it with `source .venv/bin/activate`
- install requirements with `pip install -r requirements.txt`

## Gemini API Key
- rename the file `.env.template` to `.env` and add the Gemini API Key (which you can get via https://ai.google.dev/gemini-api/docs/api-key)

## Custom Model
- We have hard coded the model `CarperAI/FIM-NeoX-1.3B` from HuggingFace
- For the first time, as a dry run, run `python custom.py` so that the model is downloaded locally.

## Run the server locally
- run `uvicorn main:app --reload`
- click on the provided link (typically http://127.0.0.1:8000)