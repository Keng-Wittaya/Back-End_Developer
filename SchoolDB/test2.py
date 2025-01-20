import database_connect
mycursor = database_connect.mydb.cursor()

def ins_subject():
    print('ฟังค์ชั่นการเพิ่มข้อมูลในตาราง subject')
    a = input('ใส่ id : ')
    b = input('ใส่ name : ')
    sql = " INSERT INTO subject VALUES ( %s , %s ) "
    val = (a,b)
    mycursor.execute(sql,val)
    database_connect.mydb.commit()
    print('เพิ่มข้อมูลสำเร็จ')

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

def show_table():
    mycursor.execute("SHOW TABLES")
    table = mycursor.fetchall()
    print('หัวข้อทั้งหมด')
    for i in table:
        print(i)

def select_table(table):
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
# select_table('subject')

def insert():
    show_table()
    ch = input('เลือกตารางที่จะแก้ไข : ')
    if ch == 'student':
        ins_student()
        select_table(ch)
    elif ch == 'subject':
        ins_subject()
        select_table(ch)
# insert()

