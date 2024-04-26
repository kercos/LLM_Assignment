from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse
from gemini import generate_code_snippet
app = FastAPI()

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.post("/solve/")
def solve_problem(description: str = Form(...)):
    # Here you can implement logic to generate a code snippet based on the description
    # For demonstration purposes, let's just return a dummy code snippet
    code_snippet = generate_code_snippet(description)
    return {"code_snippet": code_snippet}
