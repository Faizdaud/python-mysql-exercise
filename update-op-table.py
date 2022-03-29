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

# Update Table SQL Statement
sql = "UPDATE employee SET salary=70000 WHERE name = 'Ahmad'"

# Execute SQL Statement on SQL Database
mycursor.execute(sql)

# Make changes to table
mydb.commit()