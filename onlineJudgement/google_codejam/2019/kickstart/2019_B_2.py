# 3
# 4
# 20 10 1
# 5 30 5
# 100 30 1
# 5 80 60
# 3
# 10 4 1000
# 10 3 1000
# 10 8 1000
# 2
# 12 300 50
# 5 200 0

# Case #1: 105
# Case #2: 8
# Case #3: 500

def eat_stones(l, E, t):
    l.sort(lambda x: )
            

T = int(input())
for i in range(T):
    N = int(input())
    l = [list(map(int, input().split())) for _ in range(N)] # l[i] => S, E, L
    s_E = 0
    ans = eat_stones(l, 0, 0)
    print("Case #%d: %d" % (i+1, ans))

