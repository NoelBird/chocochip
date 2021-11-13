import sys
from itertools import combinations
from collections import defaultdict
rdl = sys.stdin.readline

# cache = defaultdict(int)

@profile
def get_total_chic_dist(l_chic_stores, l_houses):
    # global cache
    s = 0
    for house in l_houses:
        dist_min = 9999999
        for chic_store in l_chic_stores:
            cur_dist = abs(chic_store[0] - house[0]) + abs(chic_store[1] - house[1])
            if cur_dist < dist_min:
                dist_min = cur_dist
        s += dist_min
    return s

N, M = map(int, input().split())
l = [[0]*N for _ in range(N)]
l_houses = []
l_chic_stores = []
for y in range(N):
    l[y] = list(map(int, rdl().split()))
    for x in range(N):
        if l[y][x] == 1:
            l_houses.append((x, y))
        elif l[y][x] == 2:
            l_chic_stores.append((x, y))

def main():
    comb_dist_min = 999999
    for cur_comb in combinations(l_chic_stores, M):
        cur_dist = get_total_chic_dist(cur_comb, l_houses)
        if cur_dist < comb_dist_min:
            comb_dist_min = cur_dist
    sys.stdout.write("%d " % comb_dist_min)


if __name__ == "__main__":
    main()