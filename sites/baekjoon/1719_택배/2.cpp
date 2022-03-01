// 16 -> 12 ms로 가려면 stdout에서 시간이 많이 걸리기 때문에
// 바로 systemcall을 하는 것이 필요할 듯

#include<stdio.h>

constexpr int MAX_SIZE = 201;
constexpr int INF = 987654321;

int main()
{
    // init
    int n, m;
    scanf("%d %d", &n, &m);

    int distanceMat[MAX_SIZE][MAX_SIZE] = { 0, };
    int firstNodeMat[MAX_SIZE][MAX_SIZE] = { 0, };

    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j)
            distanceMat[i][j] = INF;

    // get input
    for (int i = 0; i < m; ++i)
    {
        int a, b, dist;
        scanf("%d %d %d", &a, &b, &dist);
        distanceMat[a][b] = dist;
        distanceMat[b][a] = dist;
        firstNodeMat[a][b] = b;
        firstNodeMat[b][a] = a;
    }

    // calc(floyd warshall)
    for (int k = 1; k <= n; ++k)
    {
        for (int i = 1; i <= n; ++i)
        {
            if (distanceMat[i][k] == INF) continue;
            for (int j = 1; j <= n; ++j)
            {
                if (distanceMat[i][k] + distanceMat[k][j] < distanceMat[i][j])
                {
                    distanceMat[i][j] = distanceMat[i][k] + distanceMat[k][j];
                    firstNodeMat[i][j] = firstNodeMat[i][k];
                }
            }
        }
    }

		// print result
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= n; ++j)
            if (i == j) printf("- ");
            else printf("%d ", firstNodeMat[i][j]);
        printf("\n");
    }
    return 0;
}