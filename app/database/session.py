from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


database_url = settings.DATABASE_URL


# engine create

engine = create_engine(database_url)


#session local create

SessionLocal =  sessionmaker(bind=engine)