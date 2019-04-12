import sys
r=sys.stdin.readline
while 1:
    M,A,B=map(int,r().split())
    if not(M|A|B):
        break
    s=round((M/A-M/B)*3600)
    print("%01d:%02d:%02d"%(s//3600,(s% 3600)//60,s%60))