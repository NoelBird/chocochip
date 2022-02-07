# pass only sample cases

T = int(input())

def solution(N, K):
    p = K//N
    l = [i for i in range(1, N+1)]
    m = []
    
    l = l[p-1:] + l[:p-1]
    for i in range(N):
        m.append(l)
        l = l[N-1:] + l[:N-1]
    return m

for i in range(1, T+1):
    N, K = map(int, input().split())
    if K in [N*i for i in range(1, N+1)]:
        print(f"Case #{i}: POSSIBLE")
        mat = solution(N, K)
        for j in range(N):
            for k in range(N):
                print(mat[j][k], end=" ")
            print()
    else:
        print(f"Case #{i}: IMPOSSIBLE")