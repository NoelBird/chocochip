from collections import Counter
a = Counter(list(input()))
b = (a['6'] + a['9'] + 1)//2
a['6'], a['9'] = b, b
_max = 0
for i in a:
    if a[i] > _max:
        _max = a[i]
print(_max)
