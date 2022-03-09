N = int(input())
l = []
for _ in range(N):
    l.append(input())
l = list(set(l))
print('\n'.join(sorted(l, key=lambda x: (len(x), x))))