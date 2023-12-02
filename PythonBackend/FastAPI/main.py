from fastapi import FastAPI

app = FastAPI()
# /docs abre swagger
@app.get("/")
async def root():
    return "Hola FastAPI!"

@app.get("/url")
async def url():
    return{"url": 'robertoorazi.com.ar'}

