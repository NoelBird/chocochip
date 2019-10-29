from collections import deque
############
# 입력 부분 #
############

############
# 입력 부분 #
############

############
# 입력 부분 #
############
import sys
input = sys.stdin.readline
N = int(input())
l_s = [0]*(N+2)
v_max = 0
for i in range(1, N+1):
    t, p = map(int, input().split(" "))
    l_s[i] = max(l_s[i], l_s[i-1])
    if t+i > N+1:
        continue
    l_s[i+t] = max(l_s[i+t], l_s[i] + p)
    v_max = max(v_max, l_s[i+t])

print(v_max)