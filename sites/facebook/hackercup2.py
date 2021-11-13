import sys
sys.stdin = open("leapfrog_ch__sample_input.txt")

n = int(input())

for i in range(n):
    s = input()
    d = {}
    for k in s:
        if d.get(k):
            d[k] += 1
        else:
            d[k] = 1

    remainedLen = len(s) - 1
    if not d.get('B'):
        print("Case #%d: N" % (i+1))
        continue
    if remainedLen == 1:
        ans = 'N'
    if remainedLen == 2:
        if d.get('B') == 1:
            print("Case #%d: Y" % (i+1))
            continue
        else:
            print("Case #%d: N" % (i+1))
            continue
    if remainedLen == 3:
        if d.get('B') == 2:
            print("Case #%d: Y" % (i+1))
            continue
        else:
            print("Case #%d: N" % (i+1))
            continue

    if remainedLen > 1:
        if remainedLen % 2 == 0: # even number
            if 2 <= d['B'] <= remainedLen-1:
                ans = 'Y'
            else:
                ans = 'N'
        else:
            if 2 <= d['B'] <= remainedLen - 1:
                ans = 'Y'
            else:
                ans = 'N'
    print("Case #%d: %s" % (i + 1, ans))
