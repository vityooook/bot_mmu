from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Table

from database.engine import Base, engine


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    group: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column(nullable=False)


class Group(Base):
    __tablename__ = 'groups'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    course: Mapped[str] = mapped_column()


def register_models():
    Base.metadata.create_all(engine)
