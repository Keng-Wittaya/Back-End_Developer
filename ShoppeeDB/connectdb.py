import mysql.connector as mysqlcon
mydb = mysqlcon.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "onlineshop")
mycursor = mydb.cursor()
print(mydb)
print(type(mydb))