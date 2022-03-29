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

# Query SQL Statement
sql = "SELECT * from employee"

# Execute SQL Statement on SQL Database
mycursor.execute(sql)

# fetchone() method, which fetches first row 
# of table
myresult = mycursor.fetchone()

# Print rows of employee table on cmd
for row in myresult:
    print (row)