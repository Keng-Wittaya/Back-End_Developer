num_positive = 0
num_negative = 0
while True:
    num = int(input("ใส่ตัวเลข : "))
    if num > 0:
        num_positive += num
    elif num < 0:
        num_negative += num
    elif num == 0:
        break