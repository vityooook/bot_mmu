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


class Test(Base):
    __tablename__ = 'test'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    test: Mapped[str] = mapped_column(default="hello")


def register_models():
    Base.metadata.create_all(engine)

# if __name__ == '__main__':
#     from database.crud import user, group
#     register_models()
#     # s = group.get_group_id(1)
#     # sss = group.verify_group(1)
#     # s = group.verify_group(1)
#     s = group.test()
#     print(s)

# def register_models():
#     Database.Base.metadata.create_all(Database().engine)
