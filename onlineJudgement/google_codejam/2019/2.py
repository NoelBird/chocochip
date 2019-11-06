def solve(n, s):
    ans = ""
    for i in range(len(s)):
        if s[i] == 'E':
            ans += 'S'
        else:
            ans += 'E'
    return ans

T = int(input())

for i in range(T):
    n = int(input())
    s = input()
    print("Case #%d: %s" % (i+1, solve(n, s)))