from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, database
from ..database import get_db

bookings_router = APIRouter()


@bookings_router.post("/bookings/", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_booking(db, booking)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@bookings_router.get("/bookings/{movie_id}", response_model=List[schemas.Booking])
def get_bookings(movie_id: int, db: Session = Depends(get_db)):
    return crud.get_booked_seats(db, movie_id)