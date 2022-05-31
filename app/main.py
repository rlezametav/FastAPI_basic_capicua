from fastapi import FastAPI
from pydantic import Json
from starlette.responses import RedirectResponse


app = FastAPI()

@app.get("/")
def root():
  return RedirectResponse(url="/docs/")

@app.get("/validar/{number}")
def capicua_validator(number: str) -> Json:
  response = "It is not capicua"

  if number == number[::-1]:
    response = "It's capicua"
  
  return {
    "number": number,
    "validation": response
  }