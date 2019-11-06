for i in range(int(input())):
    int(input())
    l = list(map(int, input().split(' ')))
    print('#%d %d' %(i+1, max(l) - min(l)))