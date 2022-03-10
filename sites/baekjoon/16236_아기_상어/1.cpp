// 알고리즘: BFS에서 한꺼번에 같은 거리를 전부 탐색하고 그 중에서 가장 최선의 후보를 선택함
// 개선 가능 부분: queue => circular queue로 변경하면, 메모리 사용량 줄일 수 있음


#include<iostream>
#include<queue>
#include<vector>
#include<cstring>
using namespace std;

int dx[] = {0, -1, 1, 0};
int dy[] = {-1, 0, 0, 1};

int mat[21][21] = { 0, };

int main()
{
  // 1. get input
	cin.tie(nullptr); cout.tie(nullptr);
	ios::sync_with_stdio(false);

	int N;
	cin >> N;

	int x, y;
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			int tmp;
			cin >> tmp;
			if (tmp == 9)
			{
				x = j;
				y = i;
				tmp = 0;
			}
			mat[i][j] = tmp;
		}
	}

	bool isFinished = false;
	int time = 0;
	int sharkSize = 2;
	int eatingCnt = 0;
	bool visited[21][21] = { 0, };
	while (!isFinished)
	{
		isFinished = true;
		queue<vector<int>> q;
		q.push(vector<int>{x, y});
		int candidateX = -1;
		int candidateY = -1;
		memset(visited, 0, 21 * 21);
		int timeDelta = 0;
		while (!q.empty())
		{
			int qSize = q.size();
			for (int i = 0; i < qSize; ++i)
			{
				vector<int> cur = q.front();
				q.pop();
				int curX = cur[0];
				int curY = cur[1];

				if (visited[curY][curX]) continue;
				visited[curY][curX] = 1;

				if (mat[curY][curX] != 0 && mat[curY][curX] < sharkSize) // eatable
				{
					bool willbeUpdated = false;
					if (candidateX == -1) willbeUpdated = true;
					else if (curY < candidateY) willbeUpdated = true;
					else if (curY == candidateY && curX < candidateX) willbeUpdated = true;

					if (willbeUpdated)
					{
						candidateX = curX;
						candidateY = curY;
					}
				}

				for (int j = 0; j < 4; ++j)
				{
					int nextX = curX + dx[j];
					int nextY = curY + dy[j];

					if (nextX < 0 || nextX >= N) continue;
					if (nextY < 0 || nextY >= N) continue;
					if (mat[nextY][nextX] > sharkSize) continue;
					q.push(vector<int>{nextX, nextY});
				}
			}
			if (candidateX != -1)
			{
				time += timeDelta;
				mat[candidateY][candidateX] = 0;
				eatingCnt++;
				if (eatingCnt == sharkSize)
				{
					sharkSize++;
					eatingCnt = 0;
				}
				x = candidateX;
				y = candidateY;

				isFinished = false;

				break;
			}
			timeDelta++;
		}
	}

	cout << time << "\n";

	return 0;
}