import random
print("โปรแกรมเป่ายิงฉุบ")
print("1=ค้อน 2=กรรไกร 3=กระดาษ")
while True :
    a = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    print(a)
    user = input("พิมพ์ ค้อน,กรรไกร,กระดาษ : ")
    if a == user :
        if a == "กรรไกร" :
            print("เสมอ เพราะ กรรไกรเหมือนกัน")
        elif a == "ค้อน" :
            print("เสมอ เพราะ ค้อนเหมือนกัน")
        elif a == "กระดาษ" :
            print("เสมอ เพราะ กระดาษเหมือนกัน")
        break
    elif user == "ค้อน" and a == "กรรไกร":
        print("คุณชนะ")
        break
    elif user == "กรรไกร" and a == "กระดาษ":
        print("คุณชนะ")
        break
    elif user == "กระดาษ" and a == "ค้อน":
        print("คุณชนะ")
        break
    else:
        print("คุณแพ้")
        break
    # elif a == "ค้อน" and user == "กรรไกร":
    #     print("คุณแพ้")
    #     break
    # elif a == "กรรไกร" and user == "กระดาษ":
    #     print("คุณแพ้")
    #     break
    # elif a == "กระดาษ" and user == "ค้อน":
    #     print("คุณแพ้")
    #     break
    # else :
    #     print("ค่าที่ป้อนไม่ถูกต้อง")
    


        

            