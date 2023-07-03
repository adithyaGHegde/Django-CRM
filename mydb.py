import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Mysql@123'
)

# prepare cursor object
cursorObject = dataBase.cursor()


# create a database
cursorObject.execute("CREATE DATABASE db_crm")

print("Database created")