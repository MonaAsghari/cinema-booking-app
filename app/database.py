from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from database_configs import settings

load_dotenv()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DATABASE_URL = (
    f"postgresql://{settings.POSTGRESQL_USER}:"
    f"{settings.POSTGRESQL_PASS}@"
    f"{settings.POSTGRESQL_HOST}:"
    f"{settings.POSTGRESQL_PORT}/"
    f"{settings.POSTGRESQL_NAME}"
)
Base = declarative_base()

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

