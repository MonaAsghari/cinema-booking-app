import uvicorn
from fastapi import FastAPI

from app.database import Base, engine
from app.routers.bookings import bookings_router
from app.routers.movie import movies_router
from app.routers.rooms import rooms_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(rooms_router)
app.include_router(movies_router)
app.include_router(bookings_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8007)
