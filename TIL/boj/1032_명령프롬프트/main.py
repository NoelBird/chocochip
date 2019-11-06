import sys
rdl = sys.stdin.readline

n = int(rdl())
l = []
for _ in range(n):
    l.append(rdl())

ans = []
for i in range(len(l[0])):
    tmp = l[0][i]
    for j in range(n):
        isSame = True
        if l[j][i]!= tmp:
            isSame = False
            break
    if isSame:
        ans.append(tmp)
    else:
        ans.append('?')

print(''.join(map(str, ans)))