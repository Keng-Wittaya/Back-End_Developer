import connectdb 
mycursor = connectdb.mydb.cursor()

def show_table():
    mycursor.execute("SHOW TABLES")
    table = mycursor.fetchall()
    print('ตารางทั้งหมด')
    for i in table:
        print(i)
# show_table()

def select_table(table):
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
# select_table()

def time():
    import datetime
    now = datetime.datetime.today()
    print(now.strftime("%d/%M/%Y %H:%M:%S"))
    return now
# time()

def ins_ctgr():
    print('ฟังค์ชั่นการเพิ่มข้อมูลในตาราง category')
    id = int(input('Input Category ID : '))
    name = input('Input Category Name : ')
    sql = " INSERT INTO categories VALUES ( %s , %s ) "
    val = ( id , name )
    mycursor.execute(sql,val)
    connectdb.mydb.commit()
    print('เพิ่มข้อมูลสำเร็จ')
# ins_ctgr()

def ins_order():
    print('ฟังค์ชั่นการเพิ่มข้อมูลในตาราง order')
    od_id = int(input('Input Oder ID : '))
    usr_id = int(input('Input User ID : '))
    date = time()
    total = float(input('Input Total : '))
    status = input('Input Status (รอดำเนินการ/กำลังจัดส่ง/จัดส่งสำเร็จ/ยกเลิกรายการ) : ')
    pd_id = int(input('Input Product ID : '))
    sql = " INSERT INTO orders VALUES ( %s , %s , %s , %s , %s , %s ) "
    val = ( od_id , usr_id , date , total , status , pd_id )
    mycursor.execute(sql,val)
    connectdb.mydb.commit()
    print('เพิ่มข้อมูลสำเร็จ')
# ins_order()

def ins_product():
    print('ฟังค์ชั่นการเพิ่มข้อมูลในตาราง product')
    pd_id = int(input('Input Product ID : '))
    pd_name = input('Input Product Name : ')
    dct = input('Input Description : ')
    price = float(input('Input Price : '))
    stock = int(input('Input Stock : '))
    ct_id = int(input('Input Category ID : '))
    sql = " INSERT INTO products VALUES ( %s , %s , %s , %s , %s , %s ) "
    val = ( pd_id , pd_name , dct , price , stock , ct_id )
    mycursor.execute(sql,val)
    connectdb.mydb.commit()
    print('เพิ่มข้อมูลสำเร็จ')
# ins_product()

def ins_user():
    print('ฟังค์ชั่นการเพิ่มข้อมูลในตาราง user')
    usr_id = int(input('Input User ID : '))
    usr_name = input('Input User Name : ')
    pw = input('Input Password : ')
    email = input('Input Email : ')
    us_role = input('Input Role (customer/admin) : ')
    sql = " INSERT INTO users VALUES ( %s , %s , %s , %s , %s ) "
    val = ( usr_id , usr_name , pw , email , us_role )
    mycursor.execute(sql,val)
    connectdb.mydb.commit()
    print('เพิ่มข้อมูลสำเร็จ')
# ins_user()

def ins_table():
    print('โปรแกรมเพิ่มข้อมูลลงในตาราง')
    show_table()
    choice = input('เลือกตารางที่จะเพิ่มข้อมูล : ')
    if choice == 'categories':
        ins_ctgr()
    elif choice == 'orders':
        ins_order()
    elif choice == 'products':
        ins_product()
    elif choice == 'users':
        select_table(choice)
        ins_user()
        select_table(choice)
# ins_table()

