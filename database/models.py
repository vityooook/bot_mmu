from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from database.engine import Base, engine


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    user_id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[str] = mapped_column(ForeignKey("groups.group_id"))
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column(nullable=False)


class Group(Base):
    __tablename__ = 'groups'
    __table_args__ = {'extend_existing': True}

    group_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    course: Mapped[str] = mapped_column()


class Teacher(Base):
    __tablename__ = 'teachers'
    __table_args__ = {'extend_existing': True}

    teacher_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    subject: Mapped[str] = mapped_column()


class Quality(Base):
    __tablename__ = 'quality'
    __table_args__ = {'extend_existing': True}

    quality_id: Mapped[int] = mapped_column(primary_key=True)
    quality: Mapped[int] = mapped_column(unique=True)


class Rating(Base):
    __tablename__ = 'rating'
    __table_args__ = {'extend_existing': True}

    rating_id: Mapped[int] = mapped_column(primary_key=True)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.teacher_id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    quality_id: Mapped[int] = mapped_column(ForeignKey("quality.quality_id"))
    mark: Mapped[int] = mapped_column()


class Squad(Base):
    __tablename__ = 'squads'
    __table_args__ = {'extend_existing': True}

    chat_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    # time_schedule: Mapped[str] = mapped_column()
#

def register_models_database():
    Base.metadata.create_all(engine)
