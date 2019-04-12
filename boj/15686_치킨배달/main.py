import sys
from itertools import combinations
rdl = sys.stdin.readline

def get_chic_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def get_total_chic_dist(l_chic_stores, l_houses):
    s = 0
    for house in l_houses:
        dist_min = 9999999
        for chic_store in l_chic_stores:
            cur_dist = get_chic_dist(chic_store, house)
            if cur_dist < dist_min:
                dist_min = cur_dist
        s += dist_min
    return s

N, M = map(int, input().split())
l = [[0]*N for _ in range(N)]
for i in range(N):
    l[i] = list(map(int, rdl().split()))

l_houses = []
l_chic_stores = []
for y in range(N):
    for x in range(N):
        if l[y][x] == 1:
            l_houses.append((x, y))
        elif l[y][x] == 2:
            l_chic_stores.append((x, y))

comb_dist_min = 999999
for cur_comb in combinations(l_chic_stores, M):
    cur_dist = get_total_chic_dist(cur_comb, l_houses)
    if cur_dist < comb_dist_min:
        comb_dist_min = cur_dist
print(comb_dist_min)




