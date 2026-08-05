from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"massage": "Kanban API работает"}