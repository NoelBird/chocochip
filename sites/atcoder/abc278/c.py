from collections import defaultdict

N, Q = map(int, input().split())
d = defaultdict(set)

for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        d[A].add(B)
    elif T == 2:
        if B in d[A]:
            d[A].remove(B)
    else:
        if B in d[A] and A in d[B]:
            print("Yes")
        else:
            print("No")