# 4 4
# 1 2
# 1 3
# 1 4
# 3 4
# 1 3
# 1 4
# 2 3
# 3 4
from itertools import permutations
N, M = map(int, input().split())

A = [[0]]
B = [[0]]
for i in range(M):
    A.append(sorted(list(map(int, input().split()))))
for i in range(M):
    B.append(list(map(int, input().split())))

B_range = [0] + list(range(1, N+1))

for per in permutations(B_range[1:], N):
    new_B = [0]+[B_range[i] for i in per]
    B_corrected = []
    for i in range(1, M+1):
        B_corrected.append(sorted([new_B[B[i][0]], new_B[B[i][1]]]))
    if sorted(A[1:]) == sorted(B_corrected):
        print("Yes")
        exit(0)
print("No")