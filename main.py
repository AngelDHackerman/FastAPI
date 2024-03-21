from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # html response in the endpoints
from utils.movies_list_dic import movies

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

# Get and movie using their ID
@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
  for item in movies_list:
    if item['id'] == id:
      return item
  return []

# Params Query, getting movie by category, by adding a "/" you can set the endpoit to receive query params
@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category:str, year:int):
  return [ item for item in movies if item['category'] == category] # this will return a movie that matches with the movie category in the movies_list_dic.py

