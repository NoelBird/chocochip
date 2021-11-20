#include<stdio.h>
#include<vector>
#include<queue>
#define MAX_LEN 300
// constexpr int MAX_LEN=301;

using namespace std;
// TODO: fix check union function

// variables
int _mat[MAX_LEN][MAX_LEN] = {0,};


// functions
void printMat(int M, int N)
{
    for(int i=0; i<M; ++i)
    {
        for(int j=0; j<N; ++j)
        {
            printf("%d ", _mat[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

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
            if(i<MAX_LEN-1 && _mat[i+1][j] == 0 && _mat[i][j] > 0)
                _matUpdate[i][j] += 1;
            if(j>0 && _mat[i][j-1] == 0 && _mat[i][j] > 0)
                _matUpdate[i][j] += 1;
            if(j<MAX_LEN-1 && _mat[i][j+1] == 0 && _mat[i][j] > 0)
                _matUpdate[i][j] += 1;
            _matUpdate[i][j] = _matUpdate[i][j] > _mat[i][j] ? _mat[i][j] : _matUpdate[i][j];
        }
    }
    for(int i=0; i<M; ++i)
    {
        for(int j=0; j<N; ++j)
        {
            _mat[i][j] -= _matUpdate[i][j];
            if(_mat[i][j] > 0) isEnd = false;
        }
    }
    
    printMat(M, N);
    return isEnd;
}

bool checkUnion(int M, int N, int num)
{
    bool _matVisited[MAX_LEN][MAX_LEN] = {false,};
    queue<vector<int> > q;

    int isFound=0;
    for(int i=0; i<M; ++i)
    {
        for(int j=0; j<N; ++j)
        {
            
        }
    }

    while(!q.empty())
    {
        vector<int> cur = q.front();
        q.pop();

        if(_matVisited[cur[0]][cur[1]] == num)
        {

        }
    }
    return true;
}

int solution(int M, int N)
{
    // simulation
    // union find
    // feasibility
    // 300^2x300^2x10
    // rows^2 x columns^2 x max number
    // BFS or DFS
    // 81b => not feasible
    int ans=0;

    for(int curStep=1; curStep<11; ++curStep)
    {
        bool isUnion = checkUnion(M, N, curStep);
        if(!isUnion)
        {
            ans = 0;
            break;
        }
        

        bool isEnd = updateStep(M, N);
        if(isEnd) break;
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

    // printMat(M, N);

    // solve
    solution(M, N);
    // printf("%d\n", solution(M, N));
    return 0;
}