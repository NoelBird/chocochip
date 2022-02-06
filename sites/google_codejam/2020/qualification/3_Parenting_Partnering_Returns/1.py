T = int(input())

def solution(N, mat):
    mat2 = sorted(mat, key=lambda x: x[0])

    endC = -1
    endJ = -1
    _result = ""
    for i in range(N):
        if endC <= mat2[i][0]:
            endC = mat2[i][1]
            _result += 'C'
        elif endJ <= mat2[i][0]:
            endJ = mat2[i][1]
            _result += 'J'
        else:
            return "IMPOSSIBLE"
    
    result = [0]*N
    for i in range(N):
        result[mat2[i][2]] = _result[i]
    
    return "".join(result)



for t in range(1, T+1):
    N = int(input())
    mat = []
    for i in range(N):
        mat.append(list(map(int, input().split())) + [i])
    result = solution(N, mat)
    print(f"Case #{t}: {result}")
