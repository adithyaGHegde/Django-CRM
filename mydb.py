# This is mainly used for the initial set up to just create a database,
# after changing it in our setting.py

import mysql.connector

# establish a connection to the MySQL server.
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Mysql@123'
)

# prepare cursor object: The cursor object allows you to execute SQL queries and retrieve the results.
cursorObject = dataBase.cursor()

# create a database: execute an SQL statement that creates a new database. 
# execute() method is responsible for sending the SQL statement to the MySQL server for execution.
cursorObject.execute("CREATE DATABASE db_crm")

print("Database created")