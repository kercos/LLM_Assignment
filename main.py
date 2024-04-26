from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse
from gemini import generate_code_snippet
from custom import generate_code_snippet_custom
app = FastAPI()

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.post("/solve/")
def solve_problem(description: str = Form(...), custom: bool = Form(...)):
    if custom:
        code_snippet = generate_code_snippet_custom(description)
    else:
        code_snippet = generate_code_snippet(description)
    return {"code_snippet": code_snippet}
