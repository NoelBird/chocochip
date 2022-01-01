import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))
for b in B:
    if b in A:
        print("1", end=" ")
    else:
        print("0", end=" ")