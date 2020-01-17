# 4의 배수이면서, 100의 배수가 아닐 때 또는 400
a = int(input())
print(1 if a%400 == 0 or (a%4==0 and a%100!=0) else 0)