from collections import deque
##############################
######### 함수 부분 ###########
##############################
def bfs(F, S, G, acts):
    vis = [False for _ in range(F+1)]

    q = deque([S])

    cnt = 0
    while q:
        for _ in range(len(q)):
            s = q.popleft()
            if s == G: # found
                return cnt
            for act in acts:
                s_next = s + act
                if 1<= s_next < F+1 and not vis[s_next]:
                    vis[s_next] = True
                    q.append(s_next)
        cnt += 1
    return -1 # not found

##############################
######### 입력 부분 ###########
##############################
# 10 1 10 2 1
F, S, G, U, D = map(int, input().split()) # 층수, 현재 위치, 목적지, 행동 +U, 행동 -D
if S == G:
    print(0)
else:
    ans = bfs(F, S, G, (U, -D))
    if ans == -1:
        print("use the stairs")
    else:
        print(ans)