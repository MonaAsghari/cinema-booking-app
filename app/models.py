from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    rows = Column(Integer, default=10)
    seats_per_row = Column(Integer, default=8)
    movies = relationship("Movie", back_populates="room")


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    poster_url = Column(String)
    start_time = Column(DateTime)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    room = relationship("Room", back_populates="movies")
    bookings = relationship("Booking", back_populates="movie")


class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, index=True)
    row = Column(Integer)
    seat = Column(Integer)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    movie = relationship("Movie", back_populates="bookings")


