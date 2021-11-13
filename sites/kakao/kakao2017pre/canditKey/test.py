import solution

data = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
res = 2

def test():
    global data
    ans = solution.solution(data)
    assert ans == res