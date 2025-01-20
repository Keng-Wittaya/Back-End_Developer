import connectdb 
mycursor = connectdb.mydb.cursor()

def show_table():
    mycursor.execute("SHOW TABLES")
    table = mycursor.fetchall()
    print('หัวข้อทั้งหมด')
    for i in table:
        print(i)
# show_table()

def select_all():
    show_table()
    table = input("ใส่หัวข้อที่ต้องการจะค้นหา : ")
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
# select_all()

def select_category():
    name = input('ป้อนชื่อคับน้อง : ')
    mycursor.execute(f"SELECT * FROM categories where category_name like '%{name}%' ")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
# select_category()

def select_order():
    id = int(input('ป้อนไอดีคับน้อง : '))
    mycursor.execute(f"SELECT * FROM orders where order_id like '%{id}%' ")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
# select_order()

def select_product():
    name = input('ป้อนชื่อคับน้อง : ')
    mycursor.execute(f"SELECT * FROM products where product_name like '%{name}%' ")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
# select_product()

def select_user():
    name = input('ป้อนชื่อคับน้อง : ')
    mycursor.execute(f"SELECT * FROM users where username like '%{name}%' ")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
# select_user()



# def select_choice():
#     show_table()
#     table = input("ใส่หัวข้อที่ต้องการจะค้นหา : ")
#     if table == 'categories':
#         select_category()
#     elif table == 'orders':
#         select_order()
#     elif table == 'products':
#         select_product()
#     elif table == 'users':
#         select_user()

# # select_choice()
