from collections import defaultdict, deque
import math

def mst(d, V):
    """
    Prim MST 방법(가중치가 최소인 정점 우선 탐색)으로 구현하였습니다.
    args:
        d: dict(dict()) 형식입니다.
        d[i][j] 형식을 이용하고자 하였는데, 인접행렬보다 공간활용 측면에서 좋아서 사용했습니다.
        
        V: MST의 종료 조건이 (E == V - 1, E는 현재의 간선 개수, V는 꼭지점 개수) 이기 때문에 인자로 받았습니다.
        
        *시작조건은 0으로 하였기 때문에, 별도로 받지 않았습니다.
    
    comments:
        - 21 ~ 26번째줄 : 값들을 초기화 시킵니다.
        - 27 ~ 40번째줄 : 바깥의 for문 -> 방문된 점들의 index, 안쪽의 for문 -> 방문되지 않은 점들의 index
                          방문된 점들과 방문되지 않은 점들 사이의 가중치의 최소값을 찾고, 이 때의 방문되지 않은 점으로 방문합니다.
        - '간선의 개수(E)'가 '정점의 개수(V) -1'이 될 때 까지 반복
    """
    visited = defaultdict(bool)     # visited = [] 대신에 사용. dict를 쓰면, 탐색을 하지 않아도 됩니다.
    s = 0                           # 시작 지점 설정
    visited[s] = True
    q = deque([0])                  # 큐에 시작 값만 넣고 초기화
    ans = 0
    cur_E = 0                       # 현재 간선의 개수
    while cur_E != V -1:            # MST의 종료 조건
        _min = math.inf             # 최소값을 무한대로 초기화 합니다.
        for dot_visited in q:       # 현재 방문된 점들과 방문되지 않은 점들의 간선에서 최소 가중치를 찾습니다.
            dot_find_target = d[dot_visited]        # d[dot_visited]는 dict입니다. 
            for dot_unvisited in dot_find_target:   # d[dot_visited]의 key값들을 하나씩 가져옵니다.
                if not visited[dot_unvisited]:
                    v_inter = dot_find_target[dot_unvisited]
                    if v_inter < _min:
                        _min = v_inter
                        idx_unvisited = dot_unvisited
        ans += _min
        visited[idx_unvisited] = True
        q.append(idx_unvisited)
        cur_E += 1
    return ans

def main():
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split(' '))
        V += 1      # V : 정점의 개수, E : 간선의 개수
        d = defaultdict(defaultdict)    # 인접행렬과 유사하나 빈 공간 없이 저장공간을 사용할 수 있음
        for _ in range(E):
            a, b, c = map(int, input().split(' '))
            d[a][b] = c
            d[b][a] = c
        print('#%d %d' % (i+1, mst(d, V)))

if __name__ == "__main__":
    main()