from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database, models
from typing import List

from ..database import get_db

rooms_router = APIRouter()


@rooms_router.post("/rooms/", response_model=schemas.Room)
def create_room(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    return crud.create_room(db, room)


@rooms_router.get("/rooms/", response_model=List[schemas.Room])
def get_rooms(db: Session = Depends(get_db)):
    return db.query(models.Room).all()