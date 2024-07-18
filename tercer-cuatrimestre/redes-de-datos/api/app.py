from fastapi import FastAPI, HTTPException, Query
import pandas as pd
import httpx
import numpy as np

app = FastAPI()

url = 'https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json'

@app.get('/movies', summary="Get all movies", description="Fetch all movies from the dataset")
async def get_movies():
    """
    Fetches all movies from the dataset.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            movies = response.json()

        df = pd.DataFrame(movies)
        df = df.replace({np.nan: None})

        movies_dict = df.to_dict(orient='records')

        return movies_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/movies/by-year', summary="Get movies by year", description="Fetch movies from a specific year")
async def get_movies_by_year(year: int = Query(..., description="The year of the movies to fetch")):
    """
    Fetches movies released in a specific year.

    - **year**: The year of the movies to fetch
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            movies = response.json()

        df = pd.DataFrame(movies)
        df = df.replace({np.nan: None})

        filtered_df = df[df['year'] == year]
        if filtered_df.empty:
            raise HTTPException(status_code=404, detail="No movies found for the given year")

        movies_dict = filtered_df.to_dict(orient='records')
        return movies_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/movies/by-director', summary="Get movies by director", description="Fetch movies by a specific director")
async def get_movies_by_director(director: str = Query(..., description="The name of the director")):
    """
    Fetches movies directed by a specific director.

    - **director**: The name of the director
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            movies = response.json()

        df = pd.DataFrame(movies)
        df = df.replace({np.nan: None})

        filtered_df = df[df['director'] == director]
        if filtered_df.empty:
            raise HTTPException(status_code=404, detail="No movies found for the given director")

        movies_dict = filtered_df.to_dict(orient='records')
        return movies_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/movies/by-genre', summary="Get movies by genre", description="Fetch movies by a specific genre")
async def get_movies_by_genre(genre: str = Query(..., description="The genre of the movies to fetch")):
    """
    Fetches movies of a specific genre.

    - **genre**: The genre of the movies to fetch
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            movies = response.json()

        df = pd.DataFrame(movies)
        df = df.replace({np.nan: None})

        filtered_df = df[df['genres'].apply(lambda x: genre in x if x else False)]
        if filtered_df.empty:
            raise HTTPException(status_code=404, detail="No movies found for the given genre")

        movies_dict = filtered_df.to_dict(orient='records')
        return movies_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

    '''
    Ejemplos de los endpoints para después filtrar en el front:
    GET http://127.0.0.1:8000/movies/by-year?year=1900
    GET http://127.0.0.1:8000/movies/by-director?director=Christopher%20Nolan
    GET http://127.0.0.1:8000/movies/by-genre?genre=Comedy
    '''
