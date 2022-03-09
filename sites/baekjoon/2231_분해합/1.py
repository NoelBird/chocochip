N = int(input())

is_found = False
for i in range(1, N+1):
    i_bak = i
    s = i
    while i > 0:
        s += i%10
        i //= 10
    if s == N:
        print(i_bak)
        is_found = True
        break
if not is_found:
    print(0)