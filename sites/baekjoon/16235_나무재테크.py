from collections import deque
import sys
input = sys.stdin.readline

############
# 전역 변수 #
############
actions = ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1))

############
# 함수 부분 #
############

############
# 입력 부분 #
############
# 다음 M개의 줄에는 상도가 심은 나무의 정보를 나타내는 세 정수 x, y, z가 주어진다. 처음 두 개의 정수는 나무의 위치 (x, y)를 의미하고, 마지막 정수는 그 나무의 나이를 의미한다.
# 1 1 1
# 1
# 1 1 1
# 계산은 0, 0을 기준으로 계산하기 때문에, 나중에 필요하면 1,1로 변환해 줘야함
N, M, K = map(int, input().split()) # 맵의 크기 N, 나무의 개수 M, K년이 지난 후의 나무의 개수를 구하라
g = [[5 for _ in range(N)] for _ in range(N)] # map
trees = deque([[[] for _ in range(N)] for _ in range(N)]) # 살아 있는 나무의 map. age
dead_trees = deque([[[] for _ in range(N)] for _ in range(N)]) # 죽은 나무의 map. age
A = []
for _ in range(N): # 양분 map
    A.append(list(map(int, input().split())))
for _ in range(M):
    x, y, age = map(int, input().split())
    trees[y-1][x-1].append(age)

for i in range(N): # initialize
    for j in range(N):
        if not trees[i][j]:
            trees[i][j].sort()  # 칸마다 나이 순으로 나무를 정렬

for _ in range(K):
    trees_next = [[[] for _ in range(N)] for _ in range(N)]  # for 가을
    for i in range(N):
        for j in range(N):
            cur_trees = trees[i][j]
            for idx_tree_age in range(len(cur_trees)):  # 봄
                if g[i][j] - cur_trees[idx_tree_age] >= 0:
                    g[i][j] -= cur_trees[idx_tree_age]  # 양분을 먹음
                    cur_trees[idx_tree_age] += 1  # 나이 한살 증가
                else:
                    dead_trees[i][j] += cur_trees[idx_tree_age:]  # 나무 죽음
                    trees[i][j] = cur_trees[:idx_tree_age]
                    break
            for tree_age in dead_trees[i][j]: # 여름
                g[i][j] += tree_age // 2
            for tree_age in trees[i][j]: # 가을
                if tree_age % 5 == 0:
                    for action in actions:
                        x_next = j + action[0]
                        y_next = i + action[1]
                        if 0 <= x_next < N and 0 <= y_next < N:
                            trees_next[y_next][x_next].append(1)
    for i in range(N):
        for j in range(N):
            trees[i][j] = trees_next[i][j] + trees[i][j]
            g[i][j] += A[i][j]


ans = 0
for i in range(N):
    for j in range(N):
        ans += len(trees[i][j])
print(ans)