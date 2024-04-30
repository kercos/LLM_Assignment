from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from chatgpt import generate_code_snippet_chatgpt
from gemini import generate_code_snippet_gemini
from custom import generate_code_snippet_custom

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

@app.post("/solve/")
def solve_problem(description: str = Form(...), model: str = Form(...)):
    if model=='custom':
        code_snippet = generate_code_snippet_custom(description)
    elif model=='gemini':
        code_snippet = generate_code_snippet_gemini(description)
    else: # chatgpt
        code_snippet = generate_code_snippet_chatgpt(description)
    return {"code_snippet": code_snippet}
