# fail history: I tried so much because memory limit error(MLE)
# it is better to process a number than a string

T = int(input())

def solution(N):
    A = 0
    B = 0
    if N % 2 == 0:
        A, B = N//2, N//2
    else:
        A, B = N//2+1, (N//2)
    _A = A
    _B = B
    len_N = len(str(N))
    for i in range(len_N):
        if _A % 10 == 4 or _B % 10 == 4:
            A += 2*10**i
            B -= 2*10**i
        _A //= 10
        _B //= 10
    return A, B

for i in range(1, T+1):
    N = int(input())
    A, B = solution(N)
    print(f"Case #{i}: {A} {B}")