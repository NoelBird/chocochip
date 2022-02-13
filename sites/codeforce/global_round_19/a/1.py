T = int(input())

for _ in range(T):
    N = int(input())
    l = list(map(int, input().split()))
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            print("YES")
            break
    else:
        print("NO")