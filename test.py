from faker import Faker
from random import randint
import sqlite3

def add_students():
        
        
        with sqlite3.connect('data.db') as cursor:
            for i  in range(1, 31):
                random_name = Faker('uk-UA').name()
                cursor.execute(f"""INSERT INTO students VALUES(?, ?, ?);""", (i, random_name, randint(1,5)))
                
            cursor.commit()
                


add_students()