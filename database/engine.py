from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


class Database:
    Base = declarative_base()

    def __init__(self):
        self._engine = create_engine("sqlite:///./schedule.db", echo=True)
        Session = sessionmaker(bind=self.engine)
        self._session = Session()

    @property
    def session(self):
        return self._session

    @property
    def engine(self):
        return self._engine