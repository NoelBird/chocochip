import solve

data = [
    [5, [2, 1, 2, 6, 2, 4, 3, 3], [3,4,2,1,5]],
    [4,	[4,4,4,4,4],	[4,1,2,3]]
]

def test(N, stages, res):
    ans = solve.solution(N, stages)
    assert ans == res

for d in data:
    test(d[0], d[1], d[2])