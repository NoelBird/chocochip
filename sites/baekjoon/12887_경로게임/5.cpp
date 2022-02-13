// DP버전 - vector, queue를 include하지 않아도 되기 때문에 메모리 사용이 좀 더 줄었음
#include<stdio.h>
#define rep(i, a, b) for(int i=a; i<b; i++)
#define MAX_VAL 120

int N;

int solution(char(&mat)[2][50], int N)
{
    int ans = 0;

    int x, y, cnt;
    int state[2] = { 0, };
    int nextState[2] = { 0, };
    rep(i, 0, 2)
    {
        if (mat[i][0] == '.') state[i] = 1;
        else state[i] = MAX_VAL;
    }
    rep(j, 1, N)
    {
        rep(i, 0, 2)
        {
            if (state[i] == MAX_VAL)
            {
                nextState[i] = state[!i] + 2;
            }
            else if (state[!i] == MAX_VAL)
            {
                nextState[i] = state[i] + 1;
            }
            else
            {
                if (mat[i][j] == '#') nextState[i] = MAX_VAL;
                else nextState[i] = state[i] + 1 < state[!i] + 2 ? state[i] + 1 : state[!i] + 2;
            }
        }
        rep(i, 0, 2)
        {
            state[i] = nextState[i];
        }
    }
    int minW = state[0];
    if (state[1] < minW)
        minW = state[1];

    int allW = 0;
    rep(i, 0, 2)
        rep(j, 0, N)
        if (mat[i][j] == '.') allW++;

    ans = allW - minW;
    return ans;
}

int main()
{
    scanf("%d", &N);
    char mat[2][50] = { 0, };

    rep(i, 0, 2) scanf("%s", mat[i]);
    printf("%d\n", solution(mat, N));
    return 0;
}