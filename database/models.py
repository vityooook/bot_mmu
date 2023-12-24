import asyncio

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from database.engine import Base


class User(Base):
    #здесь прописываем настоящее имя таблицы к которой подключаемся
    __tablename__ = "users"
    # обозначаем сталбцы
    user_id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.group_id"))
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column()


class Group(Base):
    __tablename__ = 'groups'

    group_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    course: Mapped[str] = mapped_column()


class Teacher(Base):
    __tablename__ = 'teachers'

    teacher_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    subject: Mapped[str] = mapped_column()


class Quality(Base):
    __tablename__ = 'quality'

    quality_id: Mapped[int] = mapped_column(primary_key=True)
    quality: Mapped[str] = mapped_column(unique=True)


class Rating(Base):
    __tablename__ = 'rating'

    rating_id: Mapped[int] = mapped_column(primary_key=True)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.teacher_id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    quality_id: Mapped[int] = mapped_column(ForeignKey("quality.quality_id"))
    mark: Mapped[int] = mapped_column()


class Squad(Base):
    __tablename__ = 'squads'

    chat_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    # time_schedule: Mapped[str] = mapped_column()

