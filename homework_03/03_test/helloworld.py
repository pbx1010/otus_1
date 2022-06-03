print("Hello World")

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/{pk}')
def get_item(pk: int):
    return {"key": pk}