
T = int(input())

def solve(N, K):
    """
    1. find diagonal
    2. rotate it
    """
    pass

for i in range(1, T+1):
    N, K = map(int, input().split())
    if K == N+1 or K == N*N-1:
        print(f"Case #{i}: IMPOSSIBLE")
    elif N == 3 and (K == 5 or K == 7):
        print(f"Case #{i}: IMPOSSIBLE")
    else:
        print(f"Case #{i}: POSSIBLE")
        solve(N, K)

