import sqlite3


class Students:

    def init(self):
        self.connection = sqlite3.connect('db.sqlite3')
    pass

    def create_table(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('create table students (id integer, name text, surname text);')
        except sqlite3.OperationalError:
            print("Таблица уже существует!")
        self.connection.commit()

    def insert(self, id, name, surname):
        cursor = self.connection.cursor()
        cursor.execute("insert into students values (?, ?, ?)", (id, name, surname))
        self.connection.commit()
        print("Row inserted")

    def update(self, id, name=None, surname=None):
        cursor = self.connection.cursor()
        cursor.execute(f"update students set name = 'Igor' where id = {id}")
        self.connection.commit()
        print("Row updated")

    def delete(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"delete from products where id = {id}")
        self.connection.commit()
        print("Row deleted")


students = Students()
students.insert(1, 'Igor', 'Lee')
students.insert(2, 'Karina', 'Kim')

students.delete(1)