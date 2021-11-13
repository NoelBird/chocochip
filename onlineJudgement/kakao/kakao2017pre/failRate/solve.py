from collections import Counter

def solution(N, stages):
    answer = []

    # 빈도수 계산하기
    cnt = Counter(stages)
    failRate = {}
    # 실패율 계산하기
    cntSum = 0
    cntSum += cnt[N+1]

    for i in range(N, 0, -1):
        cntSum += cnt[i]
        if cntSum != 0:
            failRate[i] = cnt[i] / cntSum
        else:
            failRate[i] = 0
    
    answer = sorted(failRate.items(), key=lambda x: [-x[1], x[0]])
    answer = [i[0] for i in answer]
        
    # 실패율에 따라 정렬하기 - 인덱스 실패율, 순서

    return answer