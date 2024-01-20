import datetime

from pydantic import BaseModel, field_validator, ValidationError


class Lessons(BaseModel):
    date: datetime.date
    dayOfWeekString: str
    beginLesson: str
    endLesson: str
    discipline: str
    kindOfWork: str
    auditorium: str
    lecturer: str


    @field_validator("date", mode="before")
    @classmethod
    def date_validator(cls, value):
        try:
            year, month, day = map(int, value.split("."))
            return datetime.date(year, month, day)

        except ValidationError:
            raise ValidationError("Wrong data format")

    def __str__(self):

        return f"""
{self.beginLesson} - {self.endLesson}
<b>{self.discipline}</b>({self.kindOfWork})
{self.auditorium} {self.lecturer}
        """

# lessons = [Lessons(**lesson) for lesson in response.json()]
# print(lessons)


# merged_lessons = {}
#
# for lesson_data in response.json():
#     lesson = Lessons(**lesson_data)
#     key = (
#     lesson.date, lesson.dayOfWeekString, lesson.beginLesson, lesson.endLesson, lesson.discipline, lesson.kindOfWork)
#
#     if key not in merged_lessons:
#         merged_lessons[key] = lesson
#     else:
#         merged_lessons[key].auditorium += f", {lesson.auditorium}"
#         merged_lessons[key].lecturer += f", {lesson.lecturer}"
#
# merged_lessons_list = list(merged_lessons.values())


# class Lecturer(BaseModel):
#     auditorium: str
#     lecturer: str
#
# class Lessons(BaseModel):
#     date: date
#     dayOfWeekString: str
#     beginLesson: str
#     endLesson: str
#     discipline: str
#     kindOfWork: str
#
#
#
#
#     @field_validator("date", mode="before")
#     @classmethod
#     def date_validatod(cls, value):
#         try:
#             year, month, day = map(int, value.split("."))
#             return date(year, month, day)
#         except ValidationError:
#             raise ValidationError("Wrong data format")
#
#
# class IndLesson(Lessons):
#     auditorium: str
#     lecturer: str
#
#
# class GroupLesson(Lessons):
#     lect: list[Lecturer]
#
#
# lessons = [IndLesson(**lesson) for lesson in response.json()]
# print(lessons)
#
# for i in lessons:
#     pass
