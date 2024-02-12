import psycopg2 as psql
import dotenv
import os

class Database:
     @staticmethod
     def connect(query):
         baza = psql.connect(
             database=('darslar'),
             host=('localhost'),
             user=os.getenv('postgres'),
             password=os.getenv('DB_PASSWORD')
        )
         boshqaruv = baza.cursor()
         boshqaruv.execute(query)
         return boshqaruv.fetchall()

if __name__ == '__main__':
    buyruq = """select * from author"""
    yugur = Database.connect(buyruq)
    for i in yugur:
        print(i)

