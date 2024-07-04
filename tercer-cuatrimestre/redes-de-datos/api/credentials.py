from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import List, Dict
import json
from pathlib import Path

app = FastAPI()
security = HTTPBasic()

USERS_FILE = Path("users.json")

# Load users from JSON file
def load_users() -> List[Dict]:
    with open(USERS_FILE, "r") as file:
        data = json.load(file)
    return data["users"]

# Get user by username
def get_user(username: str) -> Dict:
    users = load_users()
    user = next((user for user in users if user["username"] == username), None)
    return user

# Authenticate user
def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_user(credentials.username)
    if user and user["password"] == credentials.password:
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Basic"},
    )

# Dependency to check if the user is an admin
def admin_required(user: Dict = Depends(authenticate_user)):
    if user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )
    return user

# Dependency to check if the user is a viewer
def viewer_required(user: Dict = Depends(authenticate_user)):
    if user["role"] != "viewer":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Viewer access required",
        )
    return user

# Routes
@app.post("/add_movie", dependencies=[Depends(admin_required)])
async def add_movie():
    return {"message": "Movie added"}

@app.put("/edit_movie", dependencies=[Depends(admin_required)])
async def edit_movie():
    return {"message": "Movie edited"}

@app.delete("/delete_movie", dependencies=[Depends(admin_required)])
async def delete_movie():
    return {"message": "Movie deleted"}

@app.get("/view_movies", dependencies=[Depends(viewer_required)])
async def view_movies():
    return {"message": "Viewing movies"}