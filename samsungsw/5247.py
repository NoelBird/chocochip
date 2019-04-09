from collections import defaultdict, deque

funcs = []

funcs.append(lambda x:x+1)
funcs.append(lambda x:x-1)
funcs.append(lambda x:x*2)
funcs.append(lambda x:x-10)

# @profile
def bfs(funcs, start, end):
    idx = 0
    q = deque([start])
    visited = defaultdict(int)

    while q:
        len_q = len(q)
        for i in range(len_q):
            cur = q.popleft()
            if not visited[cur]:
                visited[cur] = True
                if cur == end:
                    return idx
                for j in range(len(funcs)):
                    tmp = funcs[j](cur)
                    if tmp >= 1 and tmp <= 1000000:
                        q.append(tmp)
        idx += 1
    return -1

for i in range(int(input())):
   n, m = map(int, input().split(' '))
   print("#%d %d" % (i+1, bfs(funcs, n, m)))
   