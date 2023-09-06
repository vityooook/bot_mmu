import sqlite3

dp = sqlite3.connect('schedule.dp')

c = dp.cursor()

# c.execute("""CREATE TABLE экн211_1 (
#     date_subject,
#     dotw_subject,
#     time_subject,
#     subject,
#     type_of_subject,
#     cabinet,
#     teacher
# )
# """)

# print(c.fetchall())
dp.commit()

dp.close()