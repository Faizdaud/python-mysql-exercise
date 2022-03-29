# Import mysql.connector library/class
import mysql.connector
# connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root", 
    passwd="", database="python_db1")

# Create Cursor object using the cursor() method
mycursor = mydb.cursor()

# Store SQL Command in a variable
sqlform = "INSERT INTO employee(name,salary) values(%s, %s)"

# Store populate data in a variable
employees = [ ("Tom", 30000), ("James", 10000), ("Ahmad", 50000) ]

# Populate many data in table
mycursor.executemany(sqlform, employees)

# Make changes to table
mydb.commit()


