# TOO EASY
T = int(input())
for _ in range(T):
    lower, upper = map(int, input().split())
    n = int(input())
    # a < num <= b
    for _ in range(n):
        mid = (lower+upper)//2
        print(mid)
        res = input()
        if res == "TOO_SMALL":
            lower = mid + 1
        elif res == "TOO_BIG":
            upper = mid - 1
        else:
            break