from pydantic import BaseModel, field_validator, ValidationError
import requests
from datetime import date

response = requests.get("https://mmu2021:mmu2021@schedule.mi.university/api/schedule/group/211?start=2023.09.11&finish"
                        "=2023.09.17&lng=1")


class Lecturer(BaseModel):
    auditorium: str
    lecturer: str

class Lessons(BaseModel):
    date: date
    dayOfWeekString: str
    beginLesson: str
    endLesson: str
    discipline: str
    kindOfWork: str




    @field_validator("date", mode="before")
    @classmethod
    def date_validatod(cls, value):
        try:
            year, month, day = map(int, value.split("."))
            return date(year, month, day)
        except ValidationError:
            raise ValidationError("Wrong data format")


class IndLesson(Lessons):
    auditorium: str
    lecturer: str


class GroupLesson(Lessons):
    lect: list[Lecturer]


lessons = [IndLesson(**lesson) for lesson in response.json()]
print(lessons)

for i in lessons:
    pass
