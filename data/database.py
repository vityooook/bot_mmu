import sqlite3
from data import config


class Database:
    def __init__(self):
        self.db = sqlite3.connect(config.DB_PATH)
        self.cur = self.db.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.db.close()

    def get_group_id(self, user_id: int):
        group_id = self.cur.execute(
            f"SELECT name_of_groups.id FROM name_of_groups INNER JOIN users ON name_of_groups.name = "
            f"users.user_group WHERE users.user_id=?", (user_id,)
        ).fetchone()[0]
        return group_id

    def id_check(self, user_id: int):
        user_id_checking = self.cur.execute('SELECT user_id FROM users WHERE user_id=?', (user_id,)).fetchone()
        return user_id_checking

    def add_info_user(self, user_id, user_group):
        self.cur.execute('INSERT INTO users (user_id, user_group) VALUES (?, ?)', (user_id, user_group))
        self.db.commit()

    def check_group_by_name(self, name: str) -> bool | None:
        group = self.cur.execute("SELECT * FROM name_of_groups WHERE name = ?", (name,)).fetchone()
        return group







# if __name__ == '__main__':
    # print(Database().check_group_by_name('ЭКН211-1'))
    # with Database() as base:
    #     print(base._try_select())




