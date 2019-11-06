# @profile
def main():
    from collections import Counter
    rdl = sys.stdin.readline
    rdl()
    cnt_n = Counter(map(int ,rdl().split(' ')))
    m = int(rdl())
    l_m = list(map(int ,rdl().split(' ')))
    for i in l_m:
        if cnt_n[i] > 0:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")

if __name__ == "__main__":
    import sys
    sys.stdin = open("data.txt", "rt")
    main()