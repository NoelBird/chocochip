# 220ms
import sys
import heapq
input = sys.stdin.readline

def sol():
    N = int(input())
    ans = [0]*N
    h_small = []
    h_big = []

    for i in range(N):
        a = int(input())
        if i % 2:
            heapq.heappush(h_big, a)
        else:
            heapq.heappush(h_small, -a)
        
        if h_big and -h_small[0] > h_big[0]:
            tmp1 = -heapq.heappop(h_small)
            tmp2 = -heapq.heappop(h_big)
            heapq.heappush(h_small, tmp2)
            heapq.heappush(h_big, tmp1)
        ans[i] = -h_small[0]
    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    sol()