M, N = map(int, input().split())
    
def fac(n):
    if n == 1:
        return 1
    return n*fac(n-1)

print(fac(M)//(fac(N)*fac(M-N)))