N, M = map(int, input().split())

ones = []
l =[]
direcs = ((-1, 0), (1, 0), (0, -1), (0, 1))

def init(M, N):
    global l
    global ones
    for i in range(M):
        cur_line = list(map(int, input().split()))
        for j in range(N):
            if cur_line[j] == 1:
                ones.append((j, i)) # 1이 들어있는 셀 찾기
        l.append(cur_line)

def search(l, ones):
    q = ones

    cnt = 0

    while q:
        next_q = []

        for v in q:
            cur_x, cur_y = v[0], v[1]

            for cur_direc in direcs:
                next_x, next_y = cur_x + cur_direc[0], cur_y + cur_direc[1]
                if (0 <= next_x <= N-1) and (0 <= next_y <= M-1) and (l[next_y][next_x] == 0):
                    l[next_y][next_x] = 1
                    next_q.append((next_x,next_y))

        q = next_q
        cnt += 1
    for row in l:
        if row.count(0) != 0:
            return -1
    return cnt - 1

if __name__ == "__main__":
    init(M, N) # 입력 받고, 1들이 들어있는 곳 찾기
    print(search(l,ones))