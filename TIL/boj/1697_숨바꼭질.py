from collections import deque
import sys
input = sys.stdin.readline

##########################################################
######################## 전역 변수 ########################
##########################################################
actions = [lambda x: x+1, lambda x: x-1, lambda x: x*2]

##########################################################
######################## 함수 부분 ########################
##########################################################
def bfs(N, K):
    global actions
    vis = [False for _ in range(100001)]
    q = deque([N])
    vis[N] = True

    cnt = 0
    while q:
        for _ in range(len(q)):
            p_subin = q.popleft()
            if p_subin == K:
                return cnt
            for action in actions:
                p_subin_next = action(p_subin)
                if 0 <= p_subin_next < 100001 and not vis[p_subin_next]:
                    vis[p_subin_next] = True
                    q.append(p_subin_next)
        cnt += 1
    return -1 # if fails

##########################################################
######################## 입력 부분 ########################
##########################################################
# 5 17 # 수빈이의 위치 N, 동생의 위치 K
N, K = map(int, input().split())
ans = bfs(N, K)
print(ans)
