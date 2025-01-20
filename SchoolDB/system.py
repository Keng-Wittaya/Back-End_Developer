import database_connect
import function
mycursor = database_connect.mydb.cursor()

def system_all():
    print("โปรแกรมจัดการฐานข้อมูลโรงเรียน")
    print("กด [1]  -->  โปรแกรมดูข้อมูลทั้งหมดในฐานข้อมูล")
    print("กด [2]  -->  โปรแกรมเพิ่มข้อมูลในฐานข้อมูล")
    print("กด [3]  -->  โปรแกรมลบข้อมูลในฐานข้อมูล")
    system = input('กรอกโปรแกรมที่ต้องการ(1,2,3) : ')
    if system == '1':
        function.select()
    elif system == '2':
        function.insert()
    elif system == '3':
        function.delete()
    else :
        print('!!Error!!')

# system_all()

