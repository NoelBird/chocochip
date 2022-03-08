# 276ms
import sys
import heapq
input = sys.stdin.readline

def swap_heap_top(h_small, h_big):
    if -h_small[0] > h_big[0]:
        tmp1 = -heapq.heappop(h_small)
        tmp2 = -heapq.heappop(h_big)
        heapq.heappush(h_small, tmp2)
        heapq.heappush(h_big, tmp1)

N = int(input())
if N == 1:
    print(int(input())); exit(0)
h_small = []
h_big = []

# 1
a = int(input())
heapq.heappush(h_small, -a)
print(a)

# 2
a = int(input())
heapq.heappush(h_big, a)
swap_heap_top(h_small, h_big)
print(-h_small[0])

for i in range(N-2):
    a = int(input())
    if i % 2:
        heapq.heappush(h_big, a)
    else:
        heapq.heappush(h_small, -a)
    
    swap_heap_top(h_small, h_big)
    print(-h_small[0])