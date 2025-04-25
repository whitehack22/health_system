# Install MySQL on your computer
# https://dev.mysql.com/downloads/installer/
# pip install pysql


import pymysql

dataBase =pymysql.connect(
    host='localhost',
    user='root',
    password='MySQL@12345',
    
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE health_system")

print("Database created successfully")