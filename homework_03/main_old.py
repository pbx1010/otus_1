from fastapi import FastAPI
from pydantic import constr

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
async def hello_view(name: constr(min_length=3) = "Kracken"):
    return {"message": f"Hello {name}"}


@app.get("/ping")
async def view():
    return {"message": f"pong"}



@app.get("/add")
async def add(a: int, b: int):
    return {"a": a, "b": b, "sum": a+b}