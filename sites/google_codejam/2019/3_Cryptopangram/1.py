T = int(input())

for i in range(1, T+1):
    N, L = map(int, input().split())
    l = list(map(int, input().split()))
    
    ll = [0]*(len(l)+1)
    p_a = 0
    p_b = 0
    for j in range(2, l[0]):
        if l[0]%j == 0:
            p_a = j
            p_b = l[0]//j
            break
    
    ll[0] = p_a
    is_fraction = False
    for j in range(len(l)):
        if l[j]%ll[j] != 0:
            is_fraction = True
            break
        ll[j+1] = l[j]//ll[j]
    if is_fraction:
        ll[0] = p_b
        for j in range(len(l)):
            ll[j+1] = l[j]//ll[j]
    values = sorted(list(set(ll)))
    val_dict = {}
    for j in range(len(values)):
        val_dict[values[j]] = chr(j+ord('A'))
    print(f"Case #{i}: ", end="")
    for j in range(len(ll)):
        print(val_dict[ll[j]], end="")
    print()