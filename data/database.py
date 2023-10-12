import sqlite3


class Database:
    def __init__(self):
        # self.db = sqlite3.connect("schedule.db")
        self.db = sqlite3.connect("/Users/work/bot_mmu/bot_mmu/schedule.db")
        self.cur = self.db.cursor()

    # def __enter__(self):
    #     return self.db
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.db.close()
    #     self.cur.close()

    def select_all_users(self) -> list[tuple]:
        with self.db as database:
            with self.cur as cursor:
                cursor.execute("SELECT * FROM users")
                return cursor.fetchall()



    # def close_db(self):
    #     self.cur.close()
    #     self.db.close()


# Database.select_all_users()  # wrong becouse u call to class itself
Database().select_all_users()  # correct

if __name__ == '__main__':

    # db = Database()
    #
    # print(db.select_all_users())
    #
    # db.close_db()

    # print(db.select_all_users())

    with Database() as db:
        db.select_all_users()




