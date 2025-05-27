from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, database
from ..database import get_db

movies_router = APIRouter()


@movies_router.post("/movies/", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)


@movies_router.get("/movies/by_room/{room_id}", response_model=List[schemas.Movie])
def get_movies_by_room(room_id: int, db: Session = Depends(get_db)):
    return crud.get_movies_by_room(db, room_id)