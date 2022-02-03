// too slow 456ms - current 1st: 28ms

//5 3 2
//0 0 0 0 0
//0 0 0 0 0
//0 0 0 0 0
//0 0 0 0 0
//0 0 1 0 0
//0 0 0 0 0

#include<cstdio>
#include<iostream>
#include<vector>
#include<queue>

using namespace std;

int dx[] = {1,0,0,-1,0,0};
int dy[] = {0,1,0,0,-1,0};
int dz[] = {0,0,1,0,0,-1};

int main()
{
	cin.tie(0);
	ios::sync_with_stdio(false);

	char arr[101][101][101] = { 0, };
	bool visited[101][101][101] = { 0, };

	int M, N, H;
	scanf("%d %d %d", &M, &N, &H);

	queue<vector<int>> q;
	for (int i = 0; i < H; i++)
	{
		for (int j = 0; j < N; j++)
		{
			for (int k = 0; k < M; k++)
			{
				scanf("%d", &arr[i][j][k]);
				if (arr[i][j][k] == 1)
				{
					q.push(vector<int>{k, j, i}); // x, y, z
				}
			}
		}
	}


	// search
	int day = 0;
	while (!q.empty())
	{
		vector<int> cur;

		int lenQ = q.size();
		for (int i = 0; i < lenQ; i++)
		{
			cur = q.front();
			q.pop();

			if (visited[cur[2]][cur[1]][cur[0]]) continue;

			visited[cur[2]][cur[1]][cur[0]] = 1;
			arr[cur[2]][cur[1]][cur[0]] = 1;
			for (int j = 0; j < 6; j++)
			{
				int nx = cur[0] + dx[j];
				int ny = cur[1] + dy[j];
				int nz = cur[2] + dz[j];
				
				if (nz < 0 || nz >= H) continue;
				if (ny < 0 || ny >= N) continue;
				if (nx < 0 || nx >= M) continue;
				if (arr[nz][ny][nx] == -1) continue;
				
				q.push(vector<int>{nx, ny, nz});
			}
		}
		if (q.empty()) break;
		day++;
	}

	// check finished
	for (int i = 0; i < H; i++)
	{
		for (int j = 0; j < N; j++)
		{
			for (int k = 0; k < M; k++)
			{
				if (arr[i][j][k] == 0)
				{
					printf("-1\n");
					return 0;
				}
			}
		}
	}
	printf("%d\n", day-1);

	return 0;
}