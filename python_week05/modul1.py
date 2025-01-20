def func01(a,b):
    result = []
    for i in range(a,b+1):
        if i %3 != 0:
            result.append(i)
    return result

def func02(num , num_p , num_n):
    num_p = 0
    num_n = 0
    while True:
        if num > 0:
            num_p += num
        elif num < 0:
            num_n += num
        elif num == 0:
            break
    return num,num_n,num_p



