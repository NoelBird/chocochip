// 4ms

#include<cstdio>
#include<iostream>
#include<vector>
#include<queue>
#define MAX_ARR 1000

using namespace std;

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    
	int M, N;
	char arr[100][100] = {0,};
	bool visited[100][100] = { 0, };

	int dx[4] = { 0, 1, 0, -1 };
	int dy[4] = { 1, 0, -1, 0 };

	scanf("%d", &M);
	scanf("%d", &N);
	fflush(stdin);

	for (int i = 0; i < M; i++)
	{
		scanf("%s", arr[i]);
	}

	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < N; j++)
		{
			arr[i][j] -= '0';
		}
	}

	queue<vector<int>> q;
	q.push(vector<int>{ 0, 0, 1 });

	while (!q.empty())
	{
		vector<int> cur = q.front();
		q.pop();

		int x = cur[0];
		int y = cur[1];
		if (y == M - 1 && x == N - 1)
		{
			printf("%d\n", cur[2]);
			return 0;
		}
		if (visited[y][x]) continue;
		visited[y][x] = 1;

		for (int i = 0; i < 4; i++)
		{
			if (x + dx[i] < 0 || x + dx[i] >= N) continue;
			if (y + dy[i] < 0 || y + dy[i] >= M) continue;
			if (arr[y+dy[i]][x+dx[i]] == 0) continue;

			q.push(vector<int> {x + dx[i], y + dy[i], cur[2] + 1});
		}
	}
	printf("-1\n");
	return 0;
}