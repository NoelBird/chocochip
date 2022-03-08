# 1. 시간초과

import sys
import heapq
input = sys.stdin.readline

N = int(input())
l = []
heapq.heapify(l)
for len_l in range(1, N+1):
    a = int(input())
    heapq.heappush(l, a)
    if len_l % 2:
        print(l[len_l//2])
    else:
        print(min(l[len_l//2], l[len_l//2-1]))