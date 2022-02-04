// quick and dirty
// approach: sort each rows and columns

// trial1 failed: because I printed 'Case 1' instead of 'Case #1'

// more fast way is to index chaining..? using data structure like hash table...
// it should be solved in 5 minutes to win

#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include <vector>
#include<algorithm>

using namespace std;

int main()
{
	cin.tie(0);
	ios::sync_with_stdio(false);

	// input T
	int T;
	scanf("%d", &T);

	
	for (int i = 0; i < T; i++)
	{
		// input matrix
		int N;
		scanf("%d", &N);
		vector<vector<int>> mat;
		for (int j = 0; j < N; j++)
		{
			mat.push_back(vector<int>{});
			for (int k = 0; k < N; k++)
			{
				int tmp;
				scanf("%d", &tmp);
				mat[j].push_back(tmp);
			}
		}

		// k
		int k = 0;
		for (int j = 0; j < N; j++)
		{
			k += mat[j][j];
		}

		int r = 0;
		for (int j = 0; j < N; j++)
		{
			vector<int> n(mat[j]);
			sort(n.begin(), n.end());
			int isDup = false;
			for (int k = 0; k < N-1; k++)
			{
				if (n[k] == n[k + 1])
				{
					isDup = true;
					break;
				}
			}
			if (isDup) r++;
		}

		int c = 0;
		for (int j = 0; j < N; j++)
		{
			vector<int> n;
			for (int k = 0; k < N; k++)
			{
				n.push_back(mat[k][j]);
			}
			sort(n.begin(), n.end());
			int isDup = false;
			for (int k = 0; k < N - 1; k++)
			{
				if (n[k] == n[k + 1])
				{
					isDup = true;
					break;
				}
			}
			if (isDup) c++;
		}

		printf("Case #%d: %d %d %d\n", i+1, k, r, c);
	}
	return 0;
}