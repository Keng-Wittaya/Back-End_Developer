import database_connect
mycursor = database_connect.mydb.cursor()

def editdb():
    table = input('เลือกตารางที่ต้องการแก้ไข')
    if table == "student":
        id = int(input('ใส่เลขไอดีที่ต้องการจะเปลี่ยน : '))
        call = input('ใส่คอลัมที่ต้องการจะเปลี่ยน : ')
        vall = input('ใส่ค่าที่ต้องการจะเปลี่ยน : ')
        sql = f'UPDATE {table} SET {call} = %s WHERE studentID = %s'
        val = (vall,id)
        mycursor.execute(sql,val)
        database_connect.mydb.commit()
    elif table == "subject":
        id = int(input('ใส่เลขไอดีที่ต้องการจะเปลี่ยน : '))
        call = input('ใส่คอลัมที่ต้องการจะเปลี่ยน : ')
        vall = input('ใส่ค่าที่ต้องการจะเปลี่ยน : ')
        sql = f'UPDATE {table} SET {call} = %s WHERE id_subject = %s'
        val = (vall,id)
        mycursor.execute(sql,val)
        database_connect.mydb.commit() 
        
def TorF():
    if mycursor.rowcount <= 0 :
        return False,None
    else:
        return True,None


# editdb()

