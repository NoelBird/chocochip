class Node:
    def __init__(self, val):
        self.val = val
        self.parent = 0

    def connect(self, parent):
        self.parent = parent


n = int(input()) # 전체 사람의 수
a, b = map(int, input().split())
m = int(input()) # 부모와 자식 간의 관계 개수

g = []
for i in range(1, n+2): # 노드 생성
    g.append(Node(i))
for _ in range(m): # 그래프 연결
    p_parent, p_child = map(int, input().split())
    g[p_child].connect(p_parent)

# a로부터 루트까지의 거리 계산
cnt1 = 0
l_a = [a]
while True:
    if g[a].parent == 0:
        break
    parent_a = g[a].parent
    l_a.append(parent_a)
    a = parent_a
    cnt1 += 1

cnt2 = 0
l_b = [b]
while True:
    if g[b].parent == 0:
        break
    parent_b = g[b].parent
    l_b.append(parent_b)
    b = parent_b
    cnt2 += 1

# 루트가 다른 경우 불가능
if l_a[-1] != l_b[-1]:
    print(-1)

# 루트가 공통되는 경우 공통되는 부분만 답으로 출력
set_a = set(l_a)
set_b = set(l_b)
if len(set_a.intersection(set_b)):
    set_c = set_a.difference(set_b)
    set_c.update(set_b.difference(set_a))
    print(len(set_c))