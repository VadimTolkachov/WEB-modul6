import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.commit()
            self.connection.close()

class Students():
    def add_students():
        
        with DatabaseManager('data.db') as cursor:
            
            
            for i in range(1, 31):
                try:
                    random_name = Faker('uk-UA').name()
                    cursor.execute("""INSERT INTO students (id, name, group_id) VALUES (?, ?, ?);""", (i, random_name, random.randint(1, 3)))
                except:
                    pass
            
class Group:

    def add_groups():
        with DatabaseManager('data.db') as cursor:
            name_groups = ['group one', 'group two', 'group three']
            for i in range(1, len(name_groups)+1):
                cursor.execute("""INSERT INTO groups (ID, group_name) VALUES (?, ?);""", (i, name_groups[i-1]))
                
class Teachers():
    def add_teachers():
        
        with DatabaseManager('data.db') as cursor:
            
            
            for i in range(1,6):
                try:
                    random_name = Faker('uk-UA').name()
                    cursor.execute("""INSERT INTO teachers (ID, teacher_name) VALUES (?, ?);""", (i, random_name))
                except:
                    pass

class Subject:
    def create_subject():
        subjects = ['Математика', 'Англійська мова', 'Хімія', 'Історія', 'Фізика', 'Географія', 'Біологія', 'Література', 'Інформатика', 'Фізкультура']

        #достать данние из бд и вернуть их SELECT * FROM contacts
        with DatabaseManager('data.db') as cursor:
            teachers_data = cursor.execute("""SELECT * FROM teachers""").fetchall()
            
            for i in range(1, len(subjects)+1):
                # print(random.choice(subjects))
                cursor.execute("""INSERT INTO subject (ID, subject_name, teacher_id) VALUES (?, ?, ?);""", (i, subjects[i-1], random.choice(teachers_data)[0]))

                
class Raiting:
    def create_raiting():
        with DatabaseManager('data.db') as cursor:
            students_data = cursor.execute("""SELECT * FROM students""").fetchall()
            subjects_data = cursor.execute("""SELECT * FROM subject""").fetchall()
            ID = 1
            


            for id_student, name_student, group in students_data:
                for id_subject, subject, id_teacher in subjects_data:
                    start_date = datetime(2023, 1, 1)  # Початкова дата
                    end_date = datetime(2023, 1, 31)  # Кінцева дата
                    # Розрахунок різниці між початковою і кінцевою датами
                    delta = end_date - start_date
                    # Генерація випадкової дати в заданому діапазоні
                    random_date = str((start_date + timedelta(days=random.randint(0, delta.days))).date())
                    raiting = random.randint(60, 100)
                    cursor.execute("""INSERT INTO raiting (ID, student_id, subject_id, raiting, date) VALUES (?, ?, ?, ?, ?);""", 
                                   (ID, id_student, id_subject, raiting, random_date))

                    ID += 1

            
                



def create_tables():

    with DatabaseManager('data.db') as cursor:
        # create table students
        cursor.execute("""DROP TABLE IF EXISTS students""")
        cursor.execute("""
        CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(60),
        group_id INT REFERENCES [groups] (ID));""")
        # create table groups
        cursor.execute("""DROP TABLE IF EXISTS groups""")
        cursor.execute("""
        CREATE TABLE groups (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        group_name VARCHAR(60))""")
        # create table teachers
        cursor.execute("""DROP TABLE IF EXISTS teachers""")
        cursor.execute("""
        CREATE TABLE teachers (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_name VARCHAR(60))""")

        # create table subjects with teachers
        cursor.execute("""DROP TABLE IF EXISTS subject""")
        cursor.execute("""
        CREATE TABLE subject (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name VARCHAR(60), 
        teacher_id INT)
        """)

        # create table students, subject, rating, data
        cursor.execute("""DROP TABLE IF EXISTS raiting""")
        cursor.execute("""
        CREATE TABLE raiting (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id REFERENCES students (id), 
        subject_id REFERENCES subject (ID),
        raiting INT,
        date VARCHAR (15))
        """)

def main():
    create_tables()
    Students.add_students()
    Group.add_groups()
    Teachers.add_teachers()
    Subject.create_subject()
    Raiting.create_raiting()

if __name__ == '__main__':
    main()