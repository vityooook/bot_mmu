import sqlite3


class Database:
    def __init__(self):
        self.db_path = "/Users/work/bot_mmu/bot_mmu/schedule.db"
        # self.db = sqlite3.connect("/Users/work/bot_mmu/bot_mmu/schedule.db")
        # self.cur = self.db.cursor()

    def connect(self):
        return sqlite3.connect(self.db_path)
    def select_all_users(self) -> list[tuple]:
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()






# Database.select_all_users()  # wrong becouse u call to class itself
# Database().select_all_users()  # correct

if __name__ == '__main__':
    print(Database().select_all_users())





