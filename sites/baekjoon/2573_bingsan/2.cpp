#include<stdio.h>
#include<cstring>
#include<vector>
#include<queue>
#define MAX_LEN 300
// constexpr int MAX_LEN=301;

using namespace std;

// variables
int _mat[MAX_LEN][MAX_LEN] = {0,};
bool _matVisited[MAX_LEN][MAX_LEN] = {false,};

int updateStep(int M, int N)
{
    bool isEnd = true;
    int _matUpdate[MAX_LEN][MAX_LEN] = {0, };
    for(int i=0; i<M; ++i)
    {
        for(int j=0; j<N; ++j)
        {
            if(i>0 && _mat[i-1][j] == 0 && _mat[i][j] > 0)
                _matUpdate[i][j] += 1;
            if(i<M-1 && _mat[i+1][j] == 0 && _mat[i][j] > 0)
                _matUpdate[i][j] += 1;
            if(j>0 && _mat[i][j-1] == 0 && _mat[i][j] > 0)
                _matUpdate[i][j] += 1;
            if(j<N-1 && _mat[i][j+1] == 0 && _mat[i][j] > 0)
                _matUpdate[i][j] += 1;
            _matUpdate[i][j] = _matUpdate[i][j] > _mat[i][j] ? _mat[i][j] : _matUpdate[i][j];
        }
    }

    int _sum=0;
    for(int i=0; i<M; ++i)
    {
        for(int j=0; j<N; ++j)
        {
            _mat[i][j] -= _matUpdate[i][j];
            _sum += _matUpdate[i][j];
            if(_mat[i][j] > 0) isEnd = false;
        }
    }
    if(_sum == 0) return true;
    
    
    return isEnd;
}

bool checkUnion(int M, int N)
{
    memset(_matVisited, 0, sizeof(_matVisited));
    queue<pair<int, int> > q;

    // find not zero
    int x=0;
    int y=0;
    int isFound=0;
    for(; y<M; ++y)
    {
        
        for(x = 0; x<N; ++x)
        {
            if(_mat[y][x]!=0)
            {
                isFound = true;
                break;
            }
        }
        if(isFound) break;
    }

    if(x==N && y==M) return true;

    q.push(make_pair(x, y));

    // fill the current region
    while(!q.empty())
    {
        pair<int, int> cur = q.front();
        q.pop();

        if(_matVisited[cur.second][cur.first])
            continue;
        
        if(cur.first > 0 && _mat[cur.second][cur.first-1] != 0)
            q.push(make_pair(cur.first-1, cur.second));
        if(cur.first < N && _mat[cur.second][cur.first+1] != 0)
            q.push(make_pair(cur.first+1, cur.second));
        if(cur.second > 0 && _mat[cur.second-1][cur.first] != 0)
            q.push(make_pair(cur.first, cur.second-1));
        if(cur.second < M && _mat[cur.second+1][cur.first] != 0)
            q.push(make_pair(cur.first, cur.second+1));
        _matVisited[cur.second][cur.first] = true;
    }

    y=0;
    for(; y<M; ++y)
    {
        x=0;
        for(; x<N; ++x)
        {
            if(_mat[y][x] != 0 && _matVisited[y][x] == false)
            {
                return false;
            }
        }
        
    }
    return true;
}

int solution(int M, int N)
{
    int ans=0;

    for(int curStep=1; curStep<600; ++curStep)
    {
        bool isUnion = checkUnion(M, N);
        if(!isUnion)
        {
            break;
        }

        bool isEnd = updateStep(M, N);
        if(isEnd)
        {
            ans = 0;
            break;
        }
        ans += 1;
        
        
    }
    
    return ans;
}

int main()
{
    int M, N;

    // get input
    scanf("%d", &M);
    scanf("%d", &N);
    for(int i=0; i<M; ++i)
    {
        for(int j=0; j<N; ++j)
        {
            scanf("%d", &_mat[i][j]);
        }
    }

    printf("%d\n", solution(M, N));
    return 0;
}