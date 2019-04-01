#include<stdio.h>
#include<string.h>

int numO(char ch);

int main(){
    int T;      // the number of test case
    int i;      // the variable for 'for loop'
    char s1[11], s2[11];    // 문자열들
    char *pCh1, *pCh2;     // 문자열 포인터들
    int isSame;     // 같은지 비교 플래그

    scanf("%d", &T);

    for(i=0;i<T;i++){   // 테스트 케이스 반복
        isSame = 1;
        scanf("%s %s", s1, s2);
        if(strlen(s1) != strlen(s2)){   // 문자열의 길이가 다른 경우
            printf("#%d DIFF\n", i+1);
        }else{
            pCh1 = s1;
            pCh2 = s2;
            while(*pCh1!='\0'){     // 문자열의 길이는 같지만, 다른 문자가 있는지 반복 검사
                if(numO(*pCh1) != numO(*pCh2)){
                    isSame = 0;
                    break;
                }
                pCh1++;
                pCh2++;
            }

            if(isSame){     // 검사 결과 같다고 판정되는지
                printf("#%d SAME\n", i+1);
            }else{
                printf("#%d DIFF\n", i+1);
            }
        }
    }
    return 0;
}

int numO(char ch){  // o의 개수를 찾는 함수
    int i;      // for loop
    int n=0;    // o의 개수
    char chs[] = {'A', 'D', 'O', 'P', 'Q', 'R'};

    if(ch == 'B'){
        n = 2;
    }else{    
        for(i=0;i<strlen(chs);i++){
            if(chs[i] == ch){
                n = 1;
                break;
            }
        }
    }

    return n;
}