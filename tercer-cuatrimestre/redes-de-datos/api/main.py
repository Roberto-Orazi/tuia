from fastapi import FastAPI, HTTPException
import pandas as pd
import httpx
import numpy as np

app = FastAPI()
url = 'https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json'

@app.get('/movies')
async def get_movies():
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

@app.get('/movies/by-year')
async def get_movies_by_year(year: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            movies = response.json()

        df = pd.DataFrame(movies)
        df = df.replace({np.nan: None})

        # Filter by year
        filtered_df = df[df['year'] == year]
        if filtered_df.empty:
            raise HTTPException(status_code=404, detail="No movies found for the given year")

        movies_dict = filtered_df.to_dict(orient='records')
        return movies_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/movies/by-director')
async def get_movies_by_director(director: str):
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

@app.get('/movies/by-genre')
async def get_movies_by_genre(genre: str):
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
    Ejemplos de los endpoints para despues filtrar en el front:
    GET http://127.0.0.1:8000/movies/by-year?year=1900
    GET http://127.0.0.1:8000/movies/by-director?director=Christopher%20Nolan
    GET http://127.0.0.1:8000/movies/by-genre?genre=Comedy
    '''