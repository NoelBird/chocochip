# dp 알고리즘 - 문제는 ㅗ가 구현이 안됨

vis = []
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 4 방향
def find_max(x, y, r, s): # x, y, remained_block, sum
    global mat # map
    global vis # visited ?
    global direction

    if r <= 0: # 블록 4개 다 사용했다면 return
        return s
    max_v = 0
    for direc in direction:
        new_x = x + direc[0]
        new_y = y + direc[1]
        if new_x < 0 or new_x >= M: # 방문하지 않을 조건 1 - 틀을 넘어간 곳
            continue
        if new_y < 0 or new_y >= N: # 방문하지 않을 조건 2 - 틀을 넘어간 곳
            continue
        if (new_x, new_y) in vis: # 방문하지 않을 조건 3 - 이미 방문한 곳
            continue
        vis.append((new_x, new_y))
        cur_v = find_max(new_x, new_y, r-1, s + mat[y][x])
        if cur_v > max_v:
            max_v = cur_v
        vis.pop()
    return max_v

N, M = map(int, input().split()) # N: 행의 개수, M: 열의 개수
mat = [] # create matrix

for _ in range(N):
    tmp = list(map(int, input().split()))
    mat.append(tmp)

max_v = 0
for j in range(N):
    for i in range(M):
        cur_v = find_max(i, j, 4, 0) # x, y, remained_block
        if cur_v > max_v:
            max_v = cur_v

print(max_v)

