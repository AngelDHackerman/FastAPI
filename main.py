from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse  # html response in the endpoints
from utils.movies_list_dic import movies
from pydantic import BaseModel, Field # Utilizar Pydantic en FastAPI para la definición y validación de modelos de datos
from typing import Optional

app = FastAPI()
app.title = "Mi applicacion con FastAPI"
app.version = "0.0.1"
movies_list = movies

class Movie(BaseModel):
  id: Optional[int] = None # if there is not id, the id will be automatically "None"
  title: str = Field(min_length=5, max_length=15) # validate that title has no more than 15 chars and no less than 5 chars
  overview: str = Field(min_length=15, max_length=50)
  year: int = Field(le=2025)
  rating: float
  category: str

  # Adding new method for add extra data in the JSON schema in Fast API:
  model_config = { 
    "json_schema_extra": {
      "example": [{
        "id": 1,
        "title": "Mi Pelicula X",
        "overview": "Descripcion de la pelicula",
        "year": 2024,
        "rating": 9.9,
        "category": "Accion"
      }]
    }
  }


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

# POST endpoint with the values of the movie in the body request.
@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
  movies_list.append(movie)
  return movies_list

# PUT endpoint for update a movie
@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
  for item in movies_list:
    if item['id'] == id:
      # Here we update the values of the movie selected by id
      item['title'] = movie.title
      item['overview'] = movie.overview
      item['year'] = movie.year
      item['rating'] = movie.rating
      item['category'] = movie.category
      return movies_list

# DELETE endpoint for delete the movies by using their id
@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
  for item in movies_list:
    if item['id'] == id:
      movies_list.remove(item)
      return movies_list