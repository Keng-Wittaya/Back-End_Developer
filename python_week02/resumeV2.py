name = input("โปรดกรอกชื่อ\n")
age = input("โปรดกรอกอายุ\n")
stdno = input("โปรดกรอกรหัสประจำตัวนักศึกษา\n")
stdy = input("โปรดกรอกชั้นปี\n")
nickname = input("โปรดกรอกชื่อเล่น\n")
hight = float(input("โปรดกรอกส่วนสูง\n"))
weight = float(input("โปรดกรอกน้ำหนัก\n"))
handw = hight + weight

print(f"ชื่อ: {name} อายุ: {age} ปี")
print(f"รหัสประจำตัวนักเรียน: {stdno} ระดับชั้น: {stdy}")
print(f"ชื่อเล่น: {nickname}")
print(f"ส่วนสูง: {hight} เชนติเมตร  น้ำหนัก: {weight} กิโลกรัม")
print(f"ส่วนสูง + น้ำหนัก = {handw}")