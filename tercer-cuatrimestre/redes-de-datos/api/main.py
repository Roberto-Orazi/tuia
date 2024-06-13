from fastapi import FastAPI

app = FastAPI()

@app.get('/my-first-api')
def hello():
    return {'hello world'}