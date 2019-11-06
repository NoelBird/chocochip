cache = []
MAXLEN = 0

def checkUni():
    pass

def bfs(n):
    global MAXLEN
    if n == MAXLEN - 1: # 종료조건 - 마지막 index에 도달
        return 0
    s = 0
    for i in range(n+1, MAXLEN):
        s += bfs(i)
    return s

def solution(relation):
    global MAXLEN
    MAXLEN = len(relation[0])
    answer = 0
    return answer