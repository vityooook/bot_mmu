from pydantic import BaseModel


class Lesson(BaseModel):
    f: int


if __name__ == '__main__':
    l = Lesson(f="qwerty")
    print(l.f)