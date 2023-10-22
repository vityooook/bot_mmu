import sqlite3
from data import config


class Database:
    def __init__(self):
        # self.db_path = "/Users/work/bot_mmu/bot_mmu/schedule.db"
        self.db = sqlite3.connect(config.DB_PATH)
        self.cur = self.db.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.db.close()

    def connect(self):
        # return sqlite3.connect(self.db_path)
        return self

    def id_check(self, user_id):
        # with self.connect() as conn: # connect to cur
        with self.db as db:
            cursor = db.cursor()
            user_id_checking = cursor.execute('SELECT user_id FROM users WHERE user_id=?', (user_id,)).fetchone()
            return user_id_checking

    def add_info_user(self, user_id, user_group):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (user_id, user_group) VALUES (?, ?)', (user_id, user_group))

    def check_group_by_name(self, name) -> bool | None:
        with self.db as db:
            cursor = db.cursor()
            group = cursor.execute("SELECT * FROM name_of_groups WHERE name = ?", (name,)).fetchone()
            return group

    def select_all_users(self) -> list[tuple]:
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()

    def _try_select(self):
        self.cur.execute("SELECT * FROM users")
        return self.cur.fetchall()








if __name__ == '__main__':
    # print(Database().check_group_by_name('ЭКН211-1'))
    with Database() as base:
        print(base._try_select())




