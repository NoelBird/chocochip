#include<bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i=a; i<b; i++)
typedef vector<int> vi;

#define BIG_VALUE 1000

int solution(char (& mat)[2][50], int N)
{
    // 1. 최단경로를 찾고, 최단경로를 찾으면
    // 2. 나머지 흰색들은 전부 삭제해도 됨
    int ans=0;
    int minDist[2][50] = {0,};
    memset(minDist, BIG_VALUE, sizeof(int)*2*50);

    queue<vi> q;
    int x, y, cnt;
    if(mat[0][0] == '.') q.push(vi{0, 0, 0}); // x, y, cnt
    if(mat[1][0] == '.') q.push(vi{0, 1, 0}); // x, y, cnt
    while(!q.empty())
    {
        vi cur = q.front();
        q.pop();
        x = cur[0];
        y = cur[1];
        cnt = cur[2];

        if(x==N-1) break;

        if(minDist[y][x] < cnt)
            continue;
        minDist[y][x] = cnt;

        if(mat[!y][x] == '.')
        {
            q.push(vi{x, !y, cnt+1});
        }
        if(mat[y][x+1] == '.')
        {
            q.push(vi{x+1, y, cnt+1});
        }
    }
    int minimal_required_numbers = cnt;

    int num_of_white = 0;
    for(int i=0; i<2; i++)
    {
        for(int j=0; j<N; j++)
        {
            if(mat[i][j] == '.') num_of_white++;
        }
    }

    ans = num_of_white - minimal_required_numbers;
    return ans;
}

int main()
{
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int N;
    char tmp;
    cin >> N;
    
    char mat[2][50] = { 0, };

    // get inputs
    rep(i, 0, 2)
        rep(j, 0, N)
    {
        cin >> tmp;
        mat[i][j] = tmp;
    }

    int ans = solution(mat, N);
    
    cout << ans << '\n';
    return 0;
}