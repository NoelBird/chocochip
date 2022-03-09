N, M = map(int, input().split())
a = set()
b = set()
for _ in range(N):
    a.add(input())
for _ in range(M):
    b.add(input())
ans = sorted(list(a.intersection(b)))
print(len(ans))
print("\n".join(ans))