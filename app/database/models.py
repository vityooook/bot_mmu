from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, BigInteger
# * import Base to declare tables
from database.engine import Base


# * create a table in database
class User(Base):
    # * real table's name for connection
    __tablename__ = "users"
    # * create columns
    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.group_id"))
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=True)


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
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.user_id"))
    quality_id: Mapped[int] = mapped_column(ForeignKey("quality.quality_id"))
    mark: Mapped[int] = mapped_column()


class Squad(Base):
    __tablename__ = 'squads'

    chat_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    title: Mapped[str] = mapped_column()
    # time_schedule: Mapped[str] = mapped_column()
