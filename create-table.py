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

# Create Table SQL Statement
sql = "CREATE TABLE employee(name varchar(200), salary int(20))"


# Execute SQL Statement on SQL Database
mycursor.execute(sql)

# Save Changes in Database
mydb.commit()