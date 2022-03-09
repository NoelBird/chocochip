# 50 500 100 1
A, B, C, X = map(int, input().split())
if X<= A:
    print(1.0)
elif X > B:
    print(0.0)
else:
    print(C/(B-A))