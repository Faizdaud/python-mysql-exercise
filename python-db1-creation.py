# Import mysql.connector library/class
import mysql.connector
# connect to database
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="python_db1")

# Create Cursor object using the cursor() method
mycursor = mydb.cursor()

# Create table in the database
mycursor.execute("CREATE TABLE employee(name varchar(200), salary int(201))")

# for db in mycursor:
#     print(db)



# To create a database in MySQL, use the "CREATE DATABASE" statement
# mycursor.execute("CREATE DATABASE python_db1")

# show available databases in sql server 
# mycursor.execute("SHOW DATABASES")