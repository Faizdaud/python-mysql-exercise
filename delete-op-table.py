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

# Delete Table SQL Statement
sql = "DELETE FROM employee WHERE name = 'James'"

# Execute SQL Statement on SQL Database
mycursor.execute(sql)

# Make changes to table
mydb.commit()