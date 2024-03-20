from fastapi import FastAPI

app = FastAPI()
app.title = "Mi applicacion con FastAPI"
app.version = "0.0.1"

@app.get('/', tags=['Home'])
def message():
  return "Hola mundo"