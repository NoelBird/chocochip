#include<bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i=a; i<b; i++)

int solution(char (& mat)[2][50], int N)
{
    int rslt[2][50] = { 0, };

    // # => -1, . => 0
    rslt[0][0] = mat[0][0] == '.' ? 0 : -1;
    rslt[1][0] = mat[1][0] == '.' ? 0 : -1;

    int state[2] = { 0, };
    rep(j, 0, N - 1)
    {
        rep(i, 0, 2)
        {
            if (mat[i][j + 1] == '#')
            {
                rslt[i][j + 1] = -1;
            }
            else
            {

                if (rslt[i][j] != -1)
                {
                    state[i] = rslt[i][j];
                }
                else
                {
                    state[i] = -1;
                }

                if (rslt[!i][j] != -1 && mat[!i][j+1] != '#')
                {
                    state[!i] = rslt[!i][j] + 1;
                }
                else
                {
                    state[!i] = -1;
                }
                rslt[i][j + 1] = state[0] > state[1] ? state[0] : state[1];
            }
        }
    }
    int ans = rslt[0][N - 1] > rslt[1][N - 1] ? rslt[0][N - 1] : rslt[1][N - 1];
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