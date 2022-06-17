import sqlite3

class BD():

    def __init__(self):
        self.conn = sqlite3.connect('database.db')

        c = self.conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS data (ID INTEGER PRIMARY KEY, Name TEXT, Phone INTEGER)""")

        self.conn.commit()
        c.close()

    def create_data(self, id, name, phone):
        c = self.conn.cursor()
        c.execute("INSERT INTO data VALUES (?, ?, ?)", (id, name, phone))
        self.conn.commit()
        c.close()


    def read_data(self):
        c = self.conn.cursor()
        c.execute("""SELECT * FROM data""")
        res = c.fetchall()
        c.close()
        return res

    def update_data(self, id, name, phone):
        c = self.conn.cursor()
        c.execute("""UPDATE data SET id = ?, name = ?, phone = ? WHERE id == ?""", (name, int(phone), int(id)))
        self.conn.commit()
        c.close()

    def delete_data(self, id):
        c = self.conn.cursor()
        c.execute("""DELETE FROM data WHERE id = ?""", (int(id),))
        self.conn.commit()
        c.close()
