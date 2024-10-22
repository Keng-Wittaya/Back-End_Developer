print("โปรแกรมคำนวณเกรด")
score = int(input("ใส่คะแนนที่ได้"))
if score < 0 or score > 100 :
    print("กรุณากรอกตัวเลข 0 - 100")
elif score >= 80 :
    print("เกรดของคุณคือ 4")
elif score >= 70 :
    print("เกรดของคุณคือ 3")
elif score >= 60 :
    print("เกรดของคุณคือ 2")
elif score >= 50 :
    print("เกรดของคุณคือ 1")
else :
    print("เกรดของคุณไม่ผ่านเกณฑ์")
