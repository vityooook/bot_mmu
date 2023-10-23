import sqlite3

from data import config

db = sqlite3.connect(config.DB_PATH)

#
def id_check(user_id):
    user_id_checking = db.execute('SELECT user_id FROM users WHERE user_id=?', (user_id,)).fetchone()
    return user_id_checking


def add_info_user(user_id, user_group):
    db.execute('INSERT INTO users (user_id, user_group) VALUES (?, ?)', (user_id, user_group))
    db.commit()


def check_group_by_name(name: str) -> bool | None:
    group = db.execute("SELECT * FROM name_of_groups WHERE name = ?", (name,)).fetchone()
    return group





