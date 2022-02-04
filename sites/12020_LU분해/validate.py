import numpy as np

A = []
tmp = list(map(float, input().split()))
A.append(tmp)
for i in range(len(tmp)-1):
    tmp = list(map(float, input().split()))
    A.append(tmp)
print(A)
B = []
for i in range(len(tmp)):
    tmp = list(map(float, input().split()))
    B.append(tmp)

A = np.array(A)
B = np.array(B)

print(np.matmul(A, B))