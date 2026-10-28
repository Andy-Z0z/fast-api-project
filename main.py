from fastapi import FastAPI

app = FastAPI()

@app.get("/00")
def read_root():
    return {"message": "Hello World"}