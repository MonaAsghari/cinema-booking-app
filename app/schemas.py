from pydantic import BaseModel
from datetime import datetime
from typing import List


class RoomBase(BaseModel):
    name: str


class RoomCreate(RoomBase):
    rows: int = 10
    seats_per_row: int = 8


class Room(RoomBase):
    id: int

    class Config:
        orm_mode = True


class MovieBase(BaseModel):
    title: str
    poster_url: str
    start_time: datetime


class MovieCreate(MovieBase):
    room_id: int


class Movie(MovieBase):
    id: int
    room_id: int

    class Config:
        orm_mode = True


class BookingCreate(BaseModel):
    row: int
    seat: int
    movie_id: int


class Booking(BaseModel):
    id: int
    row: int
    seat: int
    movie_id: int
    class Config:
        orm_mode = True