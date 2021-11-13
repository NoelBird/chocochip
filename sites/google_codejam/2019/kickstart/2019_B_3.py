# 4
# 6 2
# 1 1 4 1 4 4
# 8 1
# 1 2 500 3 4 500 6 7
# 10 1
# 100 200 8 8 8 8 8 300 400 100
# 12 2
# 40 50 1 1 1 60 70 2 2 2 80 90

# Case #1: 4
# Case #2: 6
# Case #3: 4
# Case #4: 6

from collections import Counter, defaultdict
T = int(input())
for i in range(T):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0
    for l in range(len(lst)):
        cnt = Counter() # counter
        d = defaultdict(int) # banned dict
        _max = 0
        __max = 0
        for r in range(l, len(lst)):
            cur = lst[r]
            if d[cur]:
                continue
            if cnt[cur] + 1 > S:
                if _max > __max:
                    __max = _max
                _max -= S
                d[cur] += 1
                continue
            _max += 1
            cnt[cur] += 1
        __max = max(_max, __max)
        if __max > ans:
            ans = __max
        
    print("Case #%d: %d" % (i+1, ans))