from sqlalchemy.orm import Session
from app import models, schemas


def create_room(db: Session, room: schemas.RoomCreate):
    db_room = models.Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room


def get_rooms(db: Session):
    return db.query(models.Room).all()


def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def get_movies_by_room(db: Session, room_id: int):
    return db.query(models.Movie).filter(models.Movie.room_id == room_id).all()


def create_booking(db: Session, booking: schemas.BookingCreate):
    existing = db.query(models.Booking).filter_by(
        row=booking.row,
        seat=booking.seat,
        movie_id=booking.movie_id
    ).first()
    if existing:
        raise ValueError("Seat already booked")
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def get_booked_seats(db: Session, movie_id: int):
    return db.query(models.Booking).filter(models.Booking.movie_id == movie_id).all()
