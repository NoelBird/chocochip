from collections import defaultdict
# 입력 받는 부분 ==================================
H, W, N, h, w = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))


d = defaultdict(int)
for i in range(H):
    for j in range(W):
        d[A[i][j]]+=1

#=========================================
res = len(d.keys()) # 결과 미리 계산

for y_s in range(H-h+1):
    blocked_area = defaultdict(int)
    for y_d in range(h): # 가장 왼쪽 위의 사각형에 대해서 계산
        for x_d in range(w):
            blocked_area[A[y_s+y_d][x_d]] += 1
    
    substract_num = 0 # 유니크한 개 몇 개인지 빼는 부분
    for k in d.keys():
        if k in blocked_area and d[k] == blocked_area[k]:
            substract_num += 1
    print(res - substract_num, end=" ")

    for x_s in range(W-w): # 슬라이딩 윈도우로 왼쪽 열 빼고 오른쪽 열 더하기
        for y_d in range(h):
            blocked_area[A[y_s+y_d][x_s]] -= 1 # 왼쪽 열 빼기
            blocked_area[A[y_s+y_d][x_s+w]] += 1 # 오른쪽 열 추가하기
        
        substract_num = 0
        for k in d.keys():
            if k in blocked_area and d[k] - blocked_area[k] == 0:
                substract_num += 1
        print(res - substract_num, end=" ")
    print()