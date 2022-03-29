# Import from mysql-connector library
import mysql.connector
# Create MySqlConnection Object
# to connect python file to MySql Server
mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    passwd="")

print(mydb)

# Test connection
if(mydb):
    print("Connection Sucessful")

else:
    print("Conection unsucessful")