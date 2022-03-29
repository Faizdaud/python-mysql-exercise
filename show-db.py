# Import mysql.connector library/class
import mysql.connector
# connect to database
mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    passwd="", 
    database="python_db1")

# Create Cursor object using the cursor() method
mycursor = mydb.cursor()

# Show Database SQL Statement
sql = "SHOW DATABASES"

# Execute SQL Statement on SQL Database
mycursor.execute(sql)

# Print databases on sql server on cmd
for db in mycursor:
    print(db)