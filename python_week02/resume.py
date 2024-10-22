name = input("โปรดกรอกชื่อ\n")
age = input("โปรดกรอกอายุ\n")
stdno = input("โปรดกรอกรหัสประจำตัวนักศึกษา\n")
stdy = input("โปรดกรอกชั้นปี\n")
nickname = input("โปรดกรอกชื่อเล่น\n")
hight = float(input("โปรดกรอกส่วนสูง\n"))
weight = float(input("โปรดกรอกน้ำหนัก\n"))
handw = hight + weight

print("ชื่อ: " + name + " อายุ: " + age + " ปี")
print("รหัสประจำตัวนักเรียน: " + stdno + " ระดับชั้น: " + stdy )
print("ชื่อเล่น: " + nickname)
print("ส่วนสูง: " + str(hight) + " เชนติเมตร " + "น้ำหนัก: " + str(weight) + " กิโลกรัม")
print("ส่วนสูง + น้ำหนัก = " + str(handw))
