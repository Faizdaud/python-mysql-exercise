# Import mysql.connector library/class
import mysql.connector

# connect to database by making
# MySqlConnection Object
mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    passwd="")

# Create Cursor object using the cursor() method
mycursor = mydb.cursor()

# Create Database SQL Statement
sql = "CREATE DATABASE python_db1"

# Execute SQL Statement on SQL Database
mycursor.execute(sql)

