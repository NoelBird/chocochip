// 처음에 틀린 이유는 i->j->k로 순회하도록 floyd warshall을 썼는데,
// k->i->j로 순회하도록 변경하니까 맞았음 거쳐가는 노드 => 출발 노드 => 도착 노드 순으로 해야 함

// 6 10
// 1 2 2
// 1 3 1
// 2 4 5
// 2 5 3
// 2 6 7
// 3 4 4
// 3 5 6
// 3 6 7
// 4 6 4
// 5 6 2

// - 2 3 3 2 2
// 1 - 1 4 5 5
// 1 1 - 4 5 6
// 3 2 3 - 6 6
// 2 2 3 6 - 6
// 5 5 3 4 5 -
#include<bits/stdc++.h>
using namespace std;
constexpr int MAX_SIZE = 200;
constexpr int INF = 10000000;


int main()
{
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    // init
    int n, m;
    cin >> n >> m;

    vector<vector<pair<int, int>>> mat; // shortest dist, first node

    for(int i=0; i<n; ++i)
    {
        mat.push_back(vector<pair<int, int>>{});
        for(int j=0; j<n; ++j)
        {
            mat[i].push_back(pair<int, int>{INF, INF});
        }
    }

    // get input
    for(int i=0; i<m; ++i)
    {
        int a, int b, int dist;
        cin >> a >> b >> dist;
        mat[a-1][b-1].first = dist;
        mat[b-1][a-1].first = dist;
    }
    
    // calc
    for(int i=0; i<n; ++i)
    {
        for(int j=0; j<n; ++j)
        {
            for(int k=0; k<n; ++k)
            {
                if(mat[i][k].first + mat[k][j].first < mat[i][j].first)
                {
                    if(mat[i][j].second == INF)
                    {
                        mat[i][j].second = k;
                    }else
                    {
                        mat[i][j].second = mat[i][k].second;
                    }
                    mat[i][j].first = mat[i][k].first + mat[k][j].first;
                }
            }
        }
    }

    return 0;
}