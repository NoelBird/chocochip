max_val = 0
max_idx = 0
for i in range(9):
    cur = int(input())
    if cur > max_val:
        max_idx = i
        max_val = cur
print(max_val)
print(max_idx+1)