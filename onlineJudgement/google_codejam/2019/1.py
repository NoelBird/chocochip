def solve(n):
    l = list(map(int, list(n)))[::-1]
    a, b = [], []
    for i in range(len(l)):
        if l[i] != 4:
            a.append(l[i])
            b.append(0)
        else:
            a.append(2)
            b.append(2)
    return ''.join(map(str, a))[::-1], ''.join(map(str, b))[::-1]



    return a, b

T = int(input())

for i in range(T):
    a, b = solve(input())
    print("Case #%d: %s %s" % (i+1, int(a), int(b)))
