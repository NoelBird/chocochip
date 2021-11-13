def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

def solve(N, L, l):
    idx = 0
    _min = l[0]
    for i in range(L):
        if l[i] < _min:
            idx = i
            _min = l[i]
    max_iter = int(_min**0.5)
    l_ans = []
    a, b = 0, 0
    for i in range(2, max_iter+1):
        if l[idx] % i == 0:
            a = i
            b = l[idx] // a
            l_ans += [a, b]
            break
    # forward
    _a, _b = a, b
    for i in range(idx, -1, -1):
        if l[i] % _a == 0:
            l_ans += [l[i] // _a, _a]
            _a, _b = l[i] // _a, _a
        else:
            l_ans += [l[i] // _b, _b]
            _a = l[i] // _b
    # backward
    _a, _b = a, b
    for i in range(idx, L):
        if l[i] % _a == 0:
            l_ans += [l[i] // _a, _a]
            _a, _b = l[i] // _a, _a
        else:
            l_ans += [l[i] // _b, _b]
            _a = l[i] // _b
    l_ans = sorted(list(set(l_ans)))
    d = {}
    for i in range(len(l_ans)):
        d[l_ans[i]] = chr(ord('A') + i)
    
    ans = []
    for i in l_ans:
        if l[0] % i == 0:
            a, b = l[0] // i, i
            break

    if l[1] % a == 0:
        first_prime = b
        first_letter = d[b]
        second_prime = a
        second_letter = d[a]
    else:
        first_prime = a
        first_letter = d[a]
        second_prime = b
        second_letter = d[b]
    ans.append(first_letter)
    ans.append(second_letter)

    idx = 1
    prev_prime = second_prime
    while idx < L:
        cur_prime = l[idx] // prev_prime
        ans.append(d[cur_prime])
        prev_prime = cur_prime
        idx += 1
    return ''.join(map(str, ans))


T =int(input())
for i in range(T):
    N, L = map(int, input().split())
    l = list(map(int, input().split()))
    print("Case #%d: %s" % (i+1, solve(N, L, l)))