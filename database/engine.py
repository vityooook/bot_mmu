from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DB_LINK

# connecting to db and create a session
engine = create_engine(DB_LINK)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
