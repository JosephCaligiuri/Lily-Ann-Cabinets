import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Neon#epic1",
  database="chat"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)