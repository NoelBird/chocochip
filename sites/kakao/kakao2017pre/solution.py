from collections import Counter


def solution(N, stages):
    # 개수 세기
    cnt = Counter(stages)
    failRate = {}

    # 실패율 계산
    failRateSum = 0
    for i in range(N+1, 0, -1):
        if not cnt[N+1]:
            continue
        failRateSum += cnt[i]
        if cnt[i] == 0:
            failRate[i] = 0
        else:
            failRate[i] = failRateSum / cnt[i]
    # 실패율에 따라 정렬
    print(sorted(failRate.items(), key=lambda x: x[1]))
    answer = [i[0] for i in sorted(failRate.items(), key=lambda x: x[1])]
    
    # 출력
    # answer = []
    return answer