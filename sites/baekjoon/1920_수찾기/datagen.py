from random import randint
with open("data.txt", "wt") as f:
    n = randint(1, 100000)
    f.write("%d\n" % n)
    f.write(' '.join(map(str, [randint(1, 10**31) for _ in range(n)])) + '\n')
    m = randint(1, 100000)
    f.write("%d\n" % m)
    f.write(' '.join(map(str, [randint(1, 10**31) for _ in range(m)])) + '\n')
    