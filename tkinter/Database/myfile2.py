import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="Tkinter"
)
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE Registration(username VARCHAR(255),passsword VARCHAR(255),firstname VARCHAR(255),lastname VARCHAR(255))"
)
