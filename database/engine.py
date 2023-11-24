from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# connecting to db and create a session
engine = create_engine("sqlite:////Users/work/bot_mmu/bot_mmu/schedule.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
