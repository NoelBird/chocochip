from collections import defaultdict, deque

def init():
    N, M = map(int, input().split())
    l = []
    balls = []
    for y in range(N):
        l.append(list(input().strip()))
        for x in range(M):
            if l[y][x] == 'R':
                balls.append((x, y, 'R'))
            elif l[y][x] == 'B':
                balls.append((x, y, 'B'))
    return N, M, l, balls

def roll_one(l, N, M, ball, to):
    ans = 0
    if to == (1, 0):    # right
        tmp_x = ball[0]
        for i in range(ball[0]+1, M):
            if l[ball[1]][i] == 'O':
                if ball[2] == 'R':
                    ans = 1
                else:
                    ans = -1
                break
            elif l[ball[1]][i] != '.':
                break
            else:
                tmp_x = i
        return ans, (tmp_x, ball[1], ball[2])
    elif to == (-1, 0):     # left
        tmp_x = ball[0]
        for i in range(ball[0]-1, 0, -1):
            if l[ball[1]][i] == 'O':
                if ball[2] == 'R':
                    ans = 1
                else:
                    ans = -1
                break
            elif l[ball[1]][i] != '.':
                break
            else:
                tmp_x = i
        return ans, (tmp_x, ball[1], ball[2])
    elif to == (0, -1):     # up
        tmp_y = ball[1]
        for i in range(ball[1]-1, 0, -1):
            if l[i][ball[0]] == 'O':
                if ball[2] == 'R':
                    ans = 1
                else:
                    ans = -1
                break
            elif l[i][ball[0]] != '.':
                break
            else:
                tmp_y = i
        return ans, (ball[0], tmp_y, ball[2])
    elif to == (0, 1):     # down
        tmp_y = ball[1]
        for i in range(ball[1]+1, N):
            if l[i][ball[0]] == 'O':
                if ball[2] == 'R':
                    ans = 1
                else:
                    ans = -1
                break
            elif l[i][ball[0]] != '.':
                break
            else:
                tmp_y = i
        return ans, (ball[0], tmp_y, ball[2])
    else:
        print("잘못된 입력입니다.")
        exit(0)

def transfer_points(l, before_balls, after_balls):
    b0, b1 = before_balls[0], before_balls[1]
    a0, a1 = after_balls[0], after_balls[1]
    l[b0[1]][b0[0]] = '.'
    l[b1[1]][b1[0]] = '.'
    l[a0[1]][a0[0]] = 'B'
    l[a1[1]][a1[0]] = 'R'

def swap(l, p1, p2):
    l[p1[1]][p1[0]], l[p2[1]][p2[0]] = l[p2[1]][p2[0]], l[p1[1]][p1[0]]

def bfs(l, M, N, balls):
    balls = tuple(balls)
    visited = defaultdict(bool)
    q = deque([balls])
    q_cnt = deque([1])
    cnt = 1
    while q:
        if cnt > 10:
            break
        i_loop = q_cnt.popleft()
        cur_i_loop = 0
        for _ in range(i_loop):
            cur_balls = q.popleft()
            if visited[cur_balls]:
                continue
            else:
                visited[cur_balls] = True
                transfer_points(l, balls, cur_balls)
            # right
            next_balls = []
            b = cur_balls[0]
            r = cur_balls[1]
            if b[0] >= r[0]:
                ans1, next_ball1 = roll_one(l, N, M, b, (1, 0))
                if ans1 == 1:
                    l[b[1]][b[0]] = '.'
                swap(l, b, next_ball1)
                ans2, next_ball2 = roll_one(l, N, M, r, (1, 0))
                swap(l, r, next_ball2)
            else:
                ans1, next_ball1 = roll_one(l, N, M, cur_balls[1], (1, 0))
                if ans1 == 1:
                    l[r[1]][r[0]] = '.'
                swap(l, r, next_ball1)
                ans2, next_ball2 = roll_one(l, N, M, b, (1, 0))
                swap(l, b, next_ball2)
            next_balls = sorted([next_ball1, next_ball2], key=lambda x: x[2])
            transfer_points(l, next_balls, cur_balls)
            if (ans1 == 1 and ans2 != -1) or (ans2 == 1 and ans1 != -1):
                return cnt
            if ans1 != -1 and ans2 != -1:
                q.append(tuple(next_balls))
                cur_i_loop += 1
            # left
            next_balls = []
            if b[0] <= r[0]:
                ans1, next_ball1 = roll_one(l, N, M, b, (-1, 0))
                if ans1 == 1:
                    l[b[1]][b[0]] = '.'
                swap(l, b, next_ball1)
                ans2, next_ball2 = roll_one(l, N, M, r, (-1, 0))
                swap(l, r, next_ball2)
            else:
                ans1, next_ball1 = roll_one(l, N, M, r, (-1, 0))
                if ans1 == 1:
                    l[r[1]][r[0]] = '.'
                swap(l, r, next_ball1)
                ans2, next_ball2 = roll_one(l, N, M, b, (-1, 0))
                swap(l, b, next_ball2)
            next_balls = sorted([next_ball1, next_ball2], key=lambda x: x[2])
            transfer_points(l, next_balls, cur_balls)
            if (ans1 == 1 and ans2 != -1) or (ans2 == 1 and ans1 != -1):
                return cnt
            if ans1 != -1 and ans2 != -1:
                q.append(tuple(next_balls))
                cur_i_loop += 1
            # up
            next_balls = []
            if b[1] <= r[1]:
                ans1, next_ball1 = roll_one(l, N, M, b, (0, -1))
                if ans1 == 1:
                    l[b[1]][b[0]] = '.'
                swap(l, b, next_ball1)
                ans2, next_ball2 = roll_one(l, N, M, r, (0, -1))
                swap(l, r, next_ball2)
            else:
                ans1, next_ball1 = roll_one(l, N, M, r, (0, -1))
                if ans1 == 1:
                    l[r[1]][r[0]] = '.'
                swap(l, r, next_ball1)
                ans2, next_ball2 = roll_one(l, N, M, b, (0, -1))
                swap(l, b, next_ball2)
            next_balls = sorted([next_ball1, next_ball2], key=lambda x: x[2])
            transfer_points(l, next_balls, cur_balls)
            if (ans1 == 1 and ans2 != -1) or (ans2 == 1 and ans1 != -1):
                return cnt
            if ans1 != -1 and ans2 != -1:
                q.append(tuple(next_balls))
                cur_i_loop += 1
            # down
            next_balls = []
            if b[1] >= r[1]:
                ans1, next_ball1 = roll_one(l, N, M, b, (0, 1))
                if ans1 == 1:
                    l[b[1]][b[0]] = '.'
                swap(l, b, next_ball1)
                ans2, next_ball2 = roll_one(l, N, M, r, (0, 1))
                swap(l, r, next_ball2)
            else:
                ans1, next_ball1 = roll_one(l, N, M, r, (0, 1))
                if ans1 == 1:
                    l[r[1]][r[0]] = '.'
                swap(l, r, next_ball1)
                ans2, next_ball2 = roll_one(l, N, M, b, (0, 1))
                swap(l, b, next_ball2)
            next_balls = sorted([next_ball1, next_ball2], key=lambda x: x[2])
            transfer_points(l, next_balls, cur_balls)
            if (ans1 == 1 and ans2 != -1) or (ans2 == 1 and ans1 != -1):
                return cnt
            if ans1 != -1 and ans2 != -1:
                q.append(tuple(next_balls))
                cur_i_loop += 1
            transfer_points(l, cur_balls, balls)
        cnt += 1
        q_cnt.append(cur_i_loop)
    return -1

N, M, l, balls = init()
balls.sort(key=lambda x:x[2])
print(bfs(l, M, N, balls))
