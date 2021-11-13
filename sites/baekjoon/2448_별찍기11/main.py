"""
소원 얻어냈던 문제 :D

기본 패턴을 설정한 다음
k가 커질때마다 삼각형을 3개 배치하여 크기를 키운다.
"""

pattern = ["  *  ",
" * * ",
"*****"]

def expand(patt):
    # print(patt)
    res = [" "*((len(i)+1)//2) + i + " "*((len(i)+1)//2) for i in patt]
    res += [i +' ' + i for i in patt]
    return res

def main():
    # k를 추출한다.
    n_pre = int(input('숫자를 입력해주세요 : ')) / 3
    n = 0
    while n_pre != 1:
        n_pre /= 2
        # print(n_pre)
        n += 1
    
    global pattern
    # k만큼 패턴의 사이즈를 키운다.
    for i in range(n):
        pattern = expand(pattern)
    print(len(pattern))
    print('\n'.join(pattern))


if __name__ == '__main__':
    main()