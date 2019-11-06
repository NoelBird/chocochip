def get_step(dist):
    n = 1
    while True:
        if n % 2 == 0:
            calced_n = (n//2)*((n//2)+1)
        else:
            calced_n = ((n+1)//2)**2
        if calced_n >= dist:
            break
        n += 1
    return n

aa = int(input())
for i in range(aa):
    x, y = list(map(int, input().split()))
    dist = y - x
    print(get_step(dist))
