import database_connect
mycursor = database_connect.mydb.cursor()

def edit(table,call,vall,id):
    sql = f'UPDATE {table} SET {call} = %s WHERE studentID = %s'
    val = (vall,id)
    mycursor.execute(sql,val)
    database_connect.mydb.commit()

table = input('เลือกตารางที่ต้องการแก้ไข')
id = int(input('ใส่เลขไอดีที่ต้องการจะเปลี่ยน : '))
call = input('ใส่คอลัมที่ต้องการจะเปลี่ยน : ')
vall = input('ใส่ค่าที่ต้องการจะเปลี่ยน : ')
edittable = edit(table,call,vall,id)
print(edittable)