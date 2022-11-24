H, M = map(int, input().split())

founded = False
for i in range(24):
    for j in range(60):
        H2, M2 = (H//10)*10 + M//10, (H%10)*10 + M%10
        if 0 <= H2 <= 23 and 0<= M2 <= 59:
            founded = True
            break

        M += 1
        if M >= 60:
            H += 1
            M = 0
        if H >= 24:
            H = 0
        if founded:
            break
    if founded:
        break
print(H, M)