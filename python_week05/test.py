import modul1

while True:
    program = int(input("เลือกโปรแกรม 1 หรือ 2 : "))
    if program == 1:
        print("โปรแกรมที่1")
        a = int(input("ใส่เลขต้น : "))
        b = int(input("ใส่เลขปลาย : "))
        num = modul1.func01(a,b)
        print(num)
    elif program == 2:
        print("โปรแกรมที่2")
        a = int(input("ใส่ตัวเลข : "))
        num = modul1.func02(a)
    else:
        print("ผิดพลาด!!")




