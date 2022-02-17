// wrong
// because I ignored integer range

#include<bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

enum Direction {
    VERTICAL = 0,
    HORIZONTAL = 1
};

bool checkCrossed(const vi& l1, const vi& l2)
{
    bool isCrossed = false;
    if(l1[4] == Direction::VERTICAL && l2[4] == Direction::HORIZONTAL && l1[0] == l2[0])
    {
        if((l2[1] - l1[1])*(l2[3] - l1[1]) <= 0)
        {
            isCrossed = true;
        }else if((l2[1] - l1[3])*(l2[3] - l1[1]) <= 0)
        {
            isCrossed = true;
        }
    }else if(l1[4] == Direction::VERTICAL && l2[4] == Direction::HORIZONTAL)
    {
        if(l2[0] <= l1[0] && l1[0] <= l2[2] && l1[1] <= l2[1] && l2[1] <= l1[3])
            isCrossed = true;
    }else if(l1[4] == Direction::HORIZONTAL && l2[4] == Direction::VERTICAL)
    {
        if(l2[1] <= l1[1] && l1[1] <= l2[3] && l1[0] <= l2[0] && l2[0] <= l1[2])
            isCrossed = true;
    }else if(l1[4] == Direction::HORIZONTAL && l2[4] == Direction::HORIZONTAL)
    {
        if((l2[0] - l1[0])*(l2[2] - l1[0]) <= 0)
            isCrossed = true;
        if((l2[0] - l1[2])*(l2[2] - l1[2]) <= 0)
            isCrossed = true;
    }

    return isCrossed;
}

bool checkCrossedWithPoint(const vi& l, int x, int y)
{
    bool isCrossed = false;
    if(l[4] == Direction::VERTICAL && x == l[0])
    {
        if((l[1] - y)*(l[3] - y) <= 0)
            isCrossed = true;
    }else if(l[4] == Direction::HORIZONTAL && y == l[1])
    {
        if((l[0] - x)*(l[2] - x) <= 0)
            isCrossed = true;
    }
    return isCrossed;
}
    


int main()
{
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int M, N;
    scanf("%d %d", &M, &N);
    int K;
    scanf("%d", K);

    vvi buses(K);
    for(int i=0; i<K; ++i)
    {
        int _b, _x1, _y1, _x2, _y2;
        scanf("%d %d %d %d %d", &_b, _x1, _y1, _x2, _y2);
        int _type;
        if(_x1 == _x2)
            _type = Direction::VERTICAL;
            if(_y1 > _y2)
            {
                int tmp;
                tmp = _y2;
                _y2 = _y1;
                _y1 = tmp;
            }
        else
            _type = Direction::HORIZONTAL;
            if(_x1 > _x2)
            {
                int tmp;
                tmp = _x2;
                _x2 = _x1;
                _x1 = tmp;
            }
        buses[_b] = vi{_x1, _y1, _x2, _y2, _type};
    }

    bool g[5010][5010] = {0,};

    vector<int> a{1,2,3,4};



    int x_start, y_start, x_end, y_end;
    scanf("%d %d %d %d", &x_start, &y_start, &x_end, &y_end);

    for(int i=1; i<K+1; ++i)
    {
        for(int j=i+1; j<K+1; ++j)
        {
            if(checkCrossed(buses[i], buses[j]))
            {
                g[i][j] = true;
                g[j][i] = true;
            }
        }
        if(checkCrossedWithPoint(buses[i], x_start, y_start))
        {
            g[0][i] = true;
            g[i][0] = true;
        }
        if(checkCrossedWithPoint(buses[i], x_end, y_end))
        {
            g[K+1][i] = true;
            g[i][K+1] = true;
        }
    }

    // BFS
    queue<int> q;
    q.push(0);
    bool visited[5010] = {0,};
    int cnt = 0;
    while(!q.empty())
    {
        int lenQ = q.size();
        for(int _lq=0; _lq<lenQ; ++_lq)
        {
            int cur = q.front();
            q.pop();

            if(visited[cur]) continue;
            if(cur == K+1)
            {
                printf("%d\n", cnt-1);
                return 0;
            }

            visited[cur] = true;
            for(int i=0; i<K+2; ++i)
            {
                if(g[cur][i] && cur!=i)
                {
                    q.push(i);
                }
            }
        }
        cnt++;
    }
    printf("-1\n");
    return 0;
}
