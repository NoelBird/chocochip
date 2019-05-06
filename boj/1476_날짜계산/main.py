E, S, M = map(int, input().split()) # 15 28 19

Found = False
for i in range(1, 15*28*19):
    n = i-1
    if n%15+1 == E and n%28+1 == S and n%19+1 == M:
        print(i)
        break
