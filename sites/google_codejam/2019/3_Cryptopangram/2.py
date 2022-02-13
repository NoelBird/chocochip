# Runtime Error
# there is an corner case that occurs when first and second values are equal

T = int(input())

def gcd(p, q):
    while p != q:
        if p > q:
            p -= q
        else:
            q -= p
    return p

for i in range(1, T+1):
    N, L = map(int, input().split())
    encrypted = list(map(int, input().split()))

    decrypted = [0]*(L+1)
    decrypted[1] = gcd(encrypted[0], encrypted[1])
    decrypted[0] = encrypted[0]//decrypted[1]
    for j in range(2, L+1):
        decrypted[j] = encrypted[j-1]//decrypted[j-1]
    
    value_set = sorted(list(set(decrypted)))
    char_dict = {}
    for j in range(0, 26):
        char_dict[value_set[j]] = chr(65 + j)
    
    print(f"Case #{i}: ", end="")
    for j in range(L+1):
        print(char_dict[decrypted[j]], end="")
    print()

    
