// 0ms

#include<cstdio>
#include<iostream>
#include<vector>
#include<queue>

using namespace std;

int main()
{
	cin.tie(0);
	ios::sync_with_stdio(false);
	bool arr[101][101] = { 0, };
	bool visited[101] = { 0, };
	int N;
	int M;
	int tmp1, tmp2;
	scanf("%d", &N);
	scanf("%d", &M);

	for (int i = 0; i < M; i++)
	{
		scanf("%d %d", &tmp1, &tmp2);
		arr[tmp1][tmp2] = 1;
		arr[tmp2][tmp1] = 1;
	}

	queue<int> q;
	q.push(1);
	int cnt = 0;

	while (!q.empty())
	{
		int cur = q.front();
		q.pop();

		if (visited[cur]) continue;

		visited[cur] = 1;
		cnt++;

		for (int i = 0; i < 101; i++)
		{
			if (arr[cur][i])
			{
				q.push(i);
			}
		}
	}

	printf("%d\n", cnt-1);
	return 0;
}