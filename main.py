from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # html response in the endpoints
from movies_list_dic import movies

app = FastAPI()
app.title = "Mi applicacion con FastAPI"
app.version = "0.0.1"

movies_list = movies


@app.get('/', tags=['Home'])
def message():
  return HTMLResponse('<h1>Hola Mundo!</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
  return movies_list