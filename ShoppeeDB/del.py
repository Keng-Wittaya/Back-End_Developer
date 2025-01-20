import connectdb
import function
mycursor = connectdb.mydb.cursor()
show = function.select_all()
sql = 'DELETE FROM '