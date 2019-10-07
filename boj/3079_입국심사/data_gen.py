from random import *

with open("data.txt", "wt") as f:
    n = randint(1, 100000)
    m = randint(1, 1000000)
    f.write("%d %d\n" % (n, m))
    for i in range(n):
        f.write("%d\n" % randint(1, 10**9))