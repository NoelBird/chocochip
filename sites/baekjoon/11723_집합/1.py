import sys
input = sys.stdin.readline

N = int(input())

st = [0]*3000001

for _ in range(N):
    s = input().split()
    cmd = s[0]
    val = None
    if len(s) == 2:
        val = int(s[1])
    if cmd == "add":
        st[val] = 1
    elif cmd == "remove":
        st[val] = 0
    elif cmd == "check":
        print(st[val])
    elif cmd == "toggle":
        st[val] = int(not st[val])
    elif cmd == "all":
        st = [0]*3000001
        for i in range(1, 21):
            st[i] = 1
    elif cmd == "empty":
        st = [0]*3000001