import database_connect 
mycursor = database_connect.mydb.cursor()

# ---------------------------------------------------------------------------------------------
# ฟังก์ชันนี้ใช้แสดงชื่อของทุกตารางในฐานข้อมูล
def show_table():
    mycursor.execute("SHOW TABLES")
    table = mycursor.fetchall()
    print('หัวข้อทั้งหมด')
    for i in table:
        print(i)

# ---------------------------------------------------------------------------------------------
# ฟังก์ชันนี้ใช้เลือกและแสดงข้อมูลทั้งหมดจากตารางที่ผู้ใช้กำหนด
def select():
    show_table()
    table = input("ใส่หัวข้อที่ต้องการจะค้นหา : ")
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)

# ---------------------------------------------------------------------------------------------
# ฟังก์ชันนี้ใช้แสดงข้อมูลทั้งหมดจากตารางที่ส่งเข้ามาในพารามิเตอร์
def select_all(table):
    # show_table()
    # table = input("ใส่หัวข้อที่ต้องการจะค้นหา : ")
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
    return table

# ---------------------------------------------------------------------------------------------
# ฟังก์ชันนี้ใช้แสดงชื่อคอลัมน์ทั้งหมดของตารางที่ส่งเข้ามาในพารามิเตอร์
def colum(table):
    mycursor.execute(f"SHOW COLUMNS FROM {table};")
    table = mycursor.fetchall()
    print('ชื่อคอลัมน์ทั้งหมด')
    for i in table:
        print(i)
# colum('student')

# ---------------------------------------------------------------------------------------------
# ฟังก์ชันนี้ใช้ค้นหาและแสดงข้อมูลของนักเรียนในตาราง 'student'
# โดยค้นหาตามชื่อที่ผู้ใช้กรอก
def select_nametable():
    # show_table()
    # table = input('ใส่หัวข้อที่ต้องการจะค้นหา : ')
    name = input('ป้อนชื่อนักเรียน : ')
    mycursor.execute(f"SELECT * FROM student where name like '%{name}%' ")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)

# ---------------------------------------------------------------------------------------------
# ฟังก์ชันนี้ใช้เพิ่มข้อมูลในตาราง 'subject'
# โดยรับค่าจากผู้ใช้เป็น id และ name
def ins_subject():
    print('ฟังค์ชั่นการเพิ่มข้อมูลในตาราง subject')
    a = input('ใส่ id : ')
    b = input('ใส่ name : ')
    sql = " INSERT INTO subject VALUES ( %s , %s ) "
    val = (a,b)
    mycursor.execute(sql,val)
    database_connect.mydb.commit()
    print('เพิ่มข้อมูลสำเร็จ')

# ---------------------------------------------------------------------------------------------
# ฟังก์ชันนี้ใช้เพิ่มข้อมูลในตาราง 'student'
# โดยรับค่าจากผู้ใช้เป็น studentID, name และ grade
def ins_student():
    print('ฟังค์ชั่นการเพิ่มข้อมูลในตาราง student')
    a = input('ใส่ studentID : ')
    b = input('ใส่ name : ')
    c = float(input('ใส่ grade : '))
    sql = " INSERT INTO student VALUES ( %s , %s , %s ) "
    val = (a,b,c)
    mycursor.execute(sql,val)
    database_connect.mydb.commit()
    print('เพิ่มข้อมูลสำเร็จ')

# ---------------------------------------------------------------------------------------------
# ฟังก์ชันนี้ใช้แสดงข้อมูลทั้งหมดจากตารางที่ส่งเข้ามาในพารามิเตอร์
def select_table(table):
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
# select_table('subject')

# ---------------------------------------------------------------------------------------------
# ฟังก์ชันนี้ใช้เพิ่มข้อมูลในตาราง 'student' หรือ 'subject'
# โดยให้ผู้ใช้เลือกตารางที่ต้องการเพิ่มข้อมูล
def insert():
    show_table()
    ch = input('เลือกตารางที่จะเพิ่มข้อมูล : ')
    if ch == 'student':
        ins_student()
        select_table(ch)
    elif ch == 'subject':
        ins_subject()
        select_table(ch)
# insert()

# ---------------------------------------------------------------------------------------------
# เพิ่มข้อมูลใหม่ในตาราง subject โดยใส่ id และ name
def ins_subject():
    print('ฟังค์ชั่นการเพิ่มข้อมูลในตาราง subject')
    a = input('ใส่ id : ')
    b = input('ใส่ name : ')
    sql = " INSERT INTO subject VALUES ( %s , %s ) "
    val = (a,b)
    mycursor.execute(sql,val)
    database_connect.mydb.commit()
    print('เพิ่มข้อมูลสำเร็จ')

# ---------------------------------------------------------------------------------------------
# เพิ่มข้อมูลใหม่ในตาราง student โดยใส่ studentID, name และ grade
def ins_student():
    print('ฟังค์ชั่นการเพิ่มข้อมูลในตาราง student')
    a = input('ใส่ studentID : ')
    b = input('ใส่ name : ')
    c = float(input('ใส่ grade : '))
    sql = " INSERT INTO student VALUES ( %s , %s , %s ) "
    val = (a,b,c)
    mycursor.execute(sql,val)
    database_connect.mydb.commit()
    print('เพิ่มข้อมูลสำเร็จ')

# ---------------------------------------------------------------------------------------------
# แสดงข้อมูลทั้งหมดจากตารางที่ระบุ
def select_table(table):
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
# select_table('subject')

# ---------------------------------------------------------------------------------------------
# เลือกตารางที่ต้องการเพิ่มข้อมูล (student หรือ subject) 
# แล้วเพิ่มข้อมูลใหม่ในตารางและแสดงข้อมูลทั้งหมดในตารางนั้น
def insert_all():
    show_table()
    ch = input('เลือกตารางที่จะแก้ไข : ')
    if ch == 'student':
        ins_student()
        select_table(ch)
    elif ch == 'subject':
        ins_subject()
        select_table(ch)
# insert_all()

# ---------------------------------------------------------------------------------------------
# ลบข้อมูลจากตารางที่ระบุ โดยเลือกตาราง คอลัมน์ และค่าที่ต้องการลบ
# จากนั้นแสดงข้อมูลที่เหลือหลังการลบ
def delete():
    print('ฟังค์ชั่นการลบข้อมูลในตาราง')
    show_table()
    a = input('ใส่ชื่อตารางที่จะลบ: ')
    colum(a)
    b = input('ใส่ชื่อคอลัมที่จะลบ : ')
    select_all(a)
    c = input('ใส่ข้อมูลที่จะลบ : ')
    sql = f" DELETE FROM {a} WHERE {b} = {c} "
    mycursor.execute(sql)
    database_connect.mydb.commit()
    print('ลบข้อมูลสำเร็จ')
    select_all(a)
# delete()