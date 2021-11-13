n = int(input())

for i in range(n):
    print(" "*i, end='')
    print("*"*((n-i)*2-1))
for i in range(n-2, -1, -1):
    print(" "*i, end='')
    print("*"*((n-i)*2-1))