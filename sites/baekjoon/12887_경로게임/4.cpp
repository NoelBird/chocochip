// 완전 탐색 - 0ms이긴 한데 메모리 사용이 좀 큼
#define _CRT_SECURE_NO_WARNINGS
#include<vector>
#include<queue>
#include<cstdio>
using namespace std;
#define rep(i, a, b) for(int i=a; i<b; i++)
typedef vector<int> vi;

#define BIG_VALUE 120

int solution(char(&mat)[2][50], int N)
{
    // 1. 최단경로를 찾고, 최단경로를 찾으면
    // 2. 나머지 흰색들은 전부 삭제해도 됨
    int ans = 0;
    char minDist[2][50] = { 0, };
    rep(i, 0, 2)
        rep(j, 0, N)
        minDist[i][j] = BIG_VALUE;

    queue<vi> q;
    int x, y, cnt;
    rep(i, 0, 2)
        if (mat[i][0] == '.') q.push(vi{ 0, i, 1 }); // x, y, cnt

    while (!q.empty())
    {
        vi cur = q.front();
        q.pop();
        x = cur[0];
        y = cur[1];
        cnt = cur[2];

        if (x > N - 1) continue; // terminal condition 1: x > N-1
        if (minDist[y][x] < cnt) // terminal condition 2: already visited
            continue;
        if (mat[y][x] == '#') // terminal condition 3: impossible block
            continue;

        minDist[y][x] = cnt;

        q.push(vi{ x, !y, cnt + 1 });
        q.push(vi{ x + 1, y, cnt + 1 });
    }
    int minW = minDist[0][N - 1];
    if (minDist[1][N - 1] < minDist[0][N - 1])
        minW = minDist[1][N - 1];

    int allW = 0;
    rep(i, 0, 2)
        rep(j, 0, N)
        if (mat[i][j] == '.') allW++;

    ans = allW - minW;
    return ans;
}

int main()
{

    int N;
    char tmp;
    scanf("%d", &N);

    char mat[2][50] = { 0, };

    // get inputs
    rep(i, 0, 2)
        scanf("%s", mat[i]);

    int ans = solution(mat, N);

    printf("%d\n", ans);
    return 0;
}