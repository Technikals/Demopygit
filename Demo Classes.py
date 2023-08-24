import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = 'Maryam Shahab',
    passwd = '12345678',
    database = 'technikals'
)

mycursor = mydb.cursor()
mycursor.execute('Select * from student')
students = mycursor.fetchall()
for student in students:
    print(student)