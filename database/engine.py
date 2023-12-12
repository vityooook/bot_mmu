from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DB_LINK

# подключаем к дб и создаем сессию
engine = create_engine(DB_LINK)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
