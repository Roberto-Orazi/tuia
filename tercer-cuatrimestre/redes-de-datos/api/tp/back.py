from fastapi import FastAPI, HTTPException, Request, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pathlib import Path
from pydantic import BaseModel
import httpx
import json
from typing import List, Dict, Optional
import os

app = FastAPI()
url = 'https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json'
local_file = 'movies.json'
security = HTTPBasic()

USERS_FILE = Path("users.json")

def load_users() -> List[Dict]:
    '''
    This function loads the users from the json
    '''
    with open(USERS_FILE, "r") as file:
        data = json.load(file)
    return data["users"]

def get_user(username: str) -> Dict:
    '''
    Get user by username
    '''
    users = load_users()
    user = next((user for user in users if user["username"] == username), None)
    return user

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    '''
    authenticate users
    '''
    user = get_user(credentials.username)
    if user and user["password"] == credentials.password:
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Basic"},
    )

def admin_required(user: Dict = Depends(authenticate_user)):
    '''
    permision for admin roles for create, edit, delete
    '''
    if user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )
    return user

# Dependency to check if the user is a viewer
def viewer_required(user: Dict = Depends(authenticate_user)):
    '''
    permision for viewer & admin roles for get method
    '''
    if user["role"] not in ["viewer", "admin"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Viewer access required",
        )
    return user


class Movie(BaseModel):
    title: str
    year: int
    cast: List[str]
    genres: List[str]

async def download_movies_data():
    '''
    This function downloads and save the json localy, only if the file doesnt exist
    '''
    try:
        if not os.path.exists(local_file):
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                response.raise_for_status()
                with open(local_file, 'w', encoding='utf-8') as f:
                    json.dump(response.json(), f, ensure_ascii=False, indent=4)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error downloading data: {str(e)}")

def load_movies_data():
    '''
    This function loads the data into the local file
    '''
    if not os.path.exists(local_file):
        raise HTTPException(status_code=500, detail="Local movies data file not found.")
    with open(local_file, 'r', encoding='utf-8') as f:
        movies = json.load(f)
    return movies

def save_movies_data(movies):
    '''
    This function saves the data into the local file
    '''
    with open(local_file, 'w', encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False, indent=4)

@app.on_event("startup")
async def startup_event():
    '''
    Download a json file
    '''
    await download_movies_data()

@app.get('/movies', dependencies=[Depends(viewer_required)])
async def get_movies():
    try:
        movies = load_movies_data()
        return movies
    except HTTPException as e:
        raise e

@app.get('/movies/by-title', dependencies=[Depends(viewer_required)])
async def get_movies_by_title(title: str):
    try:
        movies = load_movies_data()
        if not isinstance(movies, list):
            raise HTTPException(status_code=500, detail="Movies data is not in expected format")
        filtered_movies = [movie for movie in movies if title.lower() in movie['title'].lower()]
        if not filtered_movies:
            raise HTTPException(status_code=404, detail="No movies found for the given title")
        return filtered_movies
    except HTTPException as e:
        raise e

@app.get('/movies/by-year', dependencies=[Depends(viewer_required)])
async def get_movies_by_year(year: int):
    try:
        movies = load_movies_data()
        filtered_movies = [movie for movie in movies if movie['year'] == year]
        if not filtered_movies:
            raise HTTPException(status_code=404, detail="No movies found for the given year")
        return filtered_movies
    except HTTPException as e:
        raise e

@app.get('/movies/by-cast', dependencies=[Depends(viewer_required)])
async def get_movies_by_cast(cast: str):
    try:
        movies = load_movies_data()
        filtered_movies = [movie for movie in movies if any(cast.lower() in actor.lower() for actor in movie['cast'])]
        if not filtered_movies:
            raise HTTPException(status_code=404, detail="No movies found for the given cast")
        return filtered_movies
    except HTTPException as e:
        raise e

@app.get('/movies/by-genre', dependencies=[Depends(viewer_required)])
async def get_movies_by_genre(genre: str):
    try:
        movies = load_movies_data()
        filtered_movies = [movie for movie in movies if any(genre.lower() in g.lower() for g in movie['genres'])]
        if not filtered_movies:
            raise HTTPException(status_code=404, detail="No movies found for the given genre")
        return filtered_movies
    except HTTPException as e:
        raise e

@app.post('/movies', dependencies=[Depends(admin_required)])
async def create_movie(movie: Movie):
    try:
        movies = load_movies_data()
        new_movie = movie.dict()
        movies.append(new_movie)
        save_movies_data(movies)
        return new_movie
    except HTTPException as e:
        raise e

@app.put('/movies/{title}', dependencies=[Depends(admin_required)])
async def update_movie(title: str, updated_movie: Movie):
    try:
        movies = load_movies_data()
        for i, movie in enumerate(movies):
            if movie['title'].lower() == title.lower():
                movies[i] = updated_movie.dict()
                save_movies_data(movies)
                return updated_movie
        raise HTTPException(status_code=404, detail="Movie not found")
    except HTTPException as e:
        raise e

@app.delete('/movies/{title}', dependencies=[Depends(admin_required)])
async def delete_movie(title: str):
    try:
        movies = load_movies_data()
        movies = [movie for movie in movies if movie['title'].lower() != title.lower()]
        save_movies_data(movies)
        return {"detail": "Movie deleted"}
    except HTTPException as e:
        raise e

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")


    '''
    Ejemplos de los endpoints para despues filtrar en el front o por si queremos probar manualmente:
    GET http://127.0.0.1:8000/movies/by-year?year=1900
    GET http://127.0.0.1:8000/movies/by-cast?cast=Matt%20Damon
    GET http://127.0.0.1:8000/movies/by-genre?genre=Comedy
    '''