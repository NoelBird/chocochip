T = int(input())

l = []
for _ in range(T):
    l.append(input().split())
l = list(map(lambda x: tuple(x), l))
print(len(set(l)))