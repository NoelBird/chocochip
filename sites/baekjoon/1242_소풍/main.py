from collections import defaultdict

def DFS_picnic(d_relationship: defaultdict, unvisited: list, possible_list: list):
        if unvisited == []:
                return 


def main():
    inp1 = """3
    2 1
    0 1
    4 6
    0 1 1 2 2 3 3 0 0 2 1 3
    6 10
    0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5"""

    inp = inp1.split('\n')
    i_inp = 0

    n_stages = int(input('입력할 세트는 몇 세트입니까? : '))
    for i in range(n_stages):
        p, r = list(map(int, input('인원, 친구관계 수를 입력해주세요 : ').split(' ')))
        l = list(map(int, input('친구관계 리스트를 입력해주세요 : ').split(' ')))

        # 친구 그래프 형성
        d = defaultdict(set)
        for j in range(0, len(l), 2):
                d[l[j]].add(l[j + 1])
                d[l[j+1]].add(l[j])
        
        # DFS
        unvisited = list(range(p))
        ans = DFS_picnic(d, unvisited, [])
        print(len(ans))

if __name__ == "__main__":
    main()