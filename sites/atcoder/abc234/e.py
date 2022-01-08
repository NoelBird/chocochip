N = input()

if len(N) == 1:
    print(N)
    exit(0)

is_answer = False
a = int(N[0])
b = int(N[1])
diff = 0
new_val = 0
while(a*10+b < 100):
    diff = b - a
    fin_val = a+(len(N)-1)*diff
    if fin_val >= 10 or fin_val < 0:
        is_answer = False
    else:
        new_val = int("".join(map(str, [a+i*diff for i in range(0, len(N))])))
        if new_val >= int(N):
            is_answer = True
            break

    s = str(a*10+b+1)
    a = int(s[0])
    b = int(s[1])

print(new_val)