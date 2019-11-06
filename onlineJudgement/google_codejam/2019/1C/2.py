T, F = map(int, input().split())

for i in range(T):
    A = []
    B = []
    C = []
    D = []
    E = []
    l = [j for j in range(119)]
    ans = ''
    for i1 in range(119):
        cur = i1*5+1
        print(cur)
        cur_ans = input()
        if cur_ans == 'A':
            A += [i1]
        elif cur_ans == 'B':
            B += [i1]
        elif cur_ans == 'C':
            C += [i1]
        elif cur_ans == 'D':
            D += [i1]
        elif cur_ans == 'E':
            E += [i1]
    if len(A) == 23:
        ans += 'A'
        l = A[:]
    elif len(B) == 23:
        ans += 'B'
        l = B[:]
    elif len(C) == 23:
        ans += 'C'
        l = C[:]
    elif len(D) == 23:
        ans += 'D'
        l = D[:]
    elif len(E) == 23:
        ans += 'E'
        l = E[:]
    A = []
    B = []
    C = []
    D = []
    E = []
    for i1 in range(23):
        cur = l[i1]*5+2
        print(cur)
        cur_ans = input()
        if cur_ans == 'A':
            A += [i1]
        elif cur_ans == 'B':
            B += [i1]
        elif cur_ans == 'C':
            C += [i1]
        elif cur_ans == 'D':
            D += [i1]
        elif cur_ans == 'E':
            E += [i1]
    if len(A) == 5:
        ans += 'A'
        l = A[:]
    elif len(B) == 5:
        ans += 'B'
        l = B[:]
    elif len(C) == 5:
        ans += 'C'
        l = C[:]
    elif len(D) == 5:
        ans += 'D'
        l = D[:]
    elif len(E) == 5:
        ans += 'E'
        l = E[:]
    A = []
    B = []
    C = []
    D = []
    E = []
    for i1 in range(5):
        cur = l[i1]*5+3
        print(cur)
        cur_ans = input()
        if cur_ans == 'A':
            A += [i1]
        elif cur_ans == 'B':
            B += [i1]
        elif cur_ans == 'C':
            C += [i1]
        elif cur_ans == 'D':
            D += [i1]
        elif cur_ans == 'E':
            E += [i1]
    if len(A) == 1:
        ans += ''.join(set(list('ABCDE')) - set(list(ans)))
        ans += 'A'
        print(ans)
        break
    elif len(B) == 1:
        ans += ''.join(set(list('ABCDE')) - set(list(ans)))
        ans += 'B'
        print(ans)
        break
    elif len(C) == 1:
        ans += ''.join(set(list('ABCDE')) - set(list(ans)))
        ans += 'C'
        print(ans)
        break
    elif len(D) == 1:
        ans += ''.join(set(list('ABCDE')) - set(list(ans)))
        ans += 'D'
        print(ans)
        break
    elif len(E) == 1:
        ans += ''.join(set(list('ABCDE')) - set(list(ans)))
        ans += 'E'
        print(ans)
        break