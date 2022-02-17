# 1. calculate joint points
# 2. search by BFS

# 7 6
# 8
# 1 2 1 2 2
# 2 1 1 5 1
# 6 7 3 7 6
# 7 2 1 2 6
# 3 3 2 6 2
# 4 5 6 5 1
# 5 1 5 7 5
# 8 3 5 6 5
# 2 1 7 4

# get input
from collections import defaultdict, namedtuple
import sys

input = sys.stdin.readline

M, N = map(int ,input().split()) # 수직선의 수 m - 열의 수(x), 수평선의 수 n행의 수(y)
K = int(input())



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bus:
    def __init__(self, x1, y1, x2, y2, _type):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        if _type == 'v':
            if self.p1.y > self.p2.y:
                self.p1, self.p2 = self.p2, self.p1
        if _type == 'h':
            if self.p1.x > self.p2.x:
                self.p1, self.p2 = self.p2, self.p1
        self._type = _type
    
    def check_crossed(self, l2):
        is_crossed = False
        if self._type == 'v' and l2._type == 'v' and self.p1.x == l2.p1.x:
            if (l2.p1.y - self.p1.y)*(l2.p2.y - self.p1.y) <= 0:
                is_crossed = True
            elif (l2.p1.y - self.p2.y)*(l2.p2.y - self.p2.y) <= 0:
                is_crossed = True
        elif self._type == 'v' and l2._type == 'h':
            if l2.p1.x <= self.p1.x <= l2.p2.x and self.p1.y <= l2.p1.y <= self.p2.y:
                is_crossed = True
        elif self._type == 'h' and l2._type == 'v':
            if l2.p1.y <= self.p1.y <= l2.p2.y and self.p1.x <= l2.p1.x <= self.p2.x:
                is_crossed = True
        elif self._type == 'h' and l2._type == 'h' and self.p1.y == l2.p1.y:
            if (l2.p1.x - self.p1.x)*(l2.p2.x - self.p1.x) <= 0:
                is_crossed = True
            elif (l2.p1.x - self.p2.x)*(l2.p2.x - self.p2.x) <= 0:
                is_crossed = True
        
        return is_crossed
    
    def check_crossed_with_point(self, p):
        is_crossed = False
        if self._type == 'v' and p.x == self.p1.x:
            if (self.p1.y - p.y)*(self.p2.y - p.y) <= 0:
                is_crossed = True
        elif self._type == 'h' and p.y == self.p1.y:
            if (self.p1.x - p.x)*(self.p2.x - p.x) <= 0:
                is_crossed = True
        return is_crossed

buses = [0]*(K+1)
for _ in range(K):
    l = list(map(int, input().split()))
    b_num = l[0]
    _type = ''
    if l[1] == l[3]:
        _type = 'v'
    else:
        _type = 'h'
    buses[b_num] = Bus(l[1], l[2], l[3], l[4], _type)

g = [[False]*5010 for _ in range(5010)]

tmp_l = list(map(int, input().split()))
p_s = Point(tmp_l[0], tmp_l[1])
p_e = Point(tmp_l[2], tmp_l[3])

def solution(p_s, p_e, buses):
    # find joint points
    d = defaultdict(list)
    for i in range(1, len(buses)):
        for j in range(i+1, len(buses)):
            is_crossed  = buses[i].check_crossed(buses[j])
            if is_crossed:
                d[i].append(j)
                d[j].append(i)
            
        if buses[i].check_crossed_with_point(p_s):
            d[0].append(i)
            d[i].append(0)
        
        if buses[i].check_crossed_with_point(p_e):
            d[K+1].append(i)
            d[i].append(K+1)
    
    q = [0]

    visited = [False]*5010
    cnt = 0
    while q:
        len_q = len(q)
        for _ in range(len_q):
            cur = q.pop(0)
            if visited[cur]:
                continue

            if cur == K+1:
                return cnt - 1

            visited[cur] = True
            for i in range(len(d[cur])):
                q.append(d[cur][i])
        cnt += 1
    return -1


print(solution(p_s, p_e, buses))