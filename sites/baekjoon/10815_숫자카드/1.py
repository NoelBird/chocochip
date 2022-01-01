# 솔직히 오늘 공부하기 좀 싫어서 쉬운 문제 대충 골라서 푼 문제...

import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))
for b in B:
    rslt = bisect.bisect_left(A, b)
    if rslt != len(A) and A[rslt] == b:
        print("1", end=" ")
    else:
        print("0", end=" ")