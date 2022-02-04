# 7
# 3 5
# 18 9 21
# 3 5
# 18 18 18
# 1 1
# 1
# 5 30
# 1 2 3 4 5
# 6 10
# 99 35 85 46 78 55
# 2 1
# 0 1
# 8 8
# 5 16 42 15 83 65 78 42

t = int(input())
for _ in range(t):
    n, l = map(int, input().split())
    a = list(map(int, input().split()))
    ss = f"{{0:0{l}b}}"
    a = list(map(lambda x: ss.format(x), a))
    tmp = ""
    
    for i in range(l):
        zeros = 0
        ones = 0
        for j in range(n):
            if a[j][i] == "0":
                zeros += 1
            else:
                ones += 1
        if zeros >= ones:
            tmp += "0"
        else:
            tmp += "1"
    print(int(tmp, 2))
