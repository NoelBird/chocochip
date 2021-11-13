from collections import defaultdict

MAX_N = 1000000
cache1 = defaultdict(int)
cache2 = [True]*(MAX_N+1)
for i in range(3, MAX_N+1, 2):
        j = 1
        while j<=MAX_N:
            cache2[i*j] = False
            j += 1
def solve(n):
    global cache2
    
    



T = int(input())

for i in range(T):
    solve(int(input()))