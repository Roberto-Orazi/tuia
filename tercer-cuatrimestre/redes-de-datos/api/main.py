from fastapi import FastAPI, HTTPException
import pandas as pd
import httpx
import numpy as np

app = FastAPI()
url = 'https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json'

@app.get('/get-movies')
async def getMovies():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # Raise an error for bad status
            movies = response.json()
        
        # Convert to pandas DataFrame
        df = pd.DataFrame(movies)
        
        # Handle NaN values: replace them with None
        df = df.replace({np.nan: None})
        
        # Convert DataFrame to dictionary
        movies_dict = df.to_dict(orient='records')
        
        return movies_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
