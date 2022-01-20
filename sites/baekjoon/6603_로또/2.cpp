// 7 1 2 3 4 5 6 7
// 8 1 2 3 5 8 13 21 34
// 0

// 처음 여섯 개 고름
// 전략 - 백트랙킹

#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<iostream>
#define MAX_ARR 50

using namespace std;

int arr[MAX_ARR] = { 0, };
int arrIdx[6] = {0, };
int n;

void solution(int idx)
{
	// base condition 2 - success
	if(idx==6)
	{
		for(int i=0; i<n; i++)
		{
			printf("%d ", arr[i]);
		}
		printf("\n");
	}

	int bak = arrIdx[idx];
	for(int i=arrIdx[idx]; i<6; i++)
	{
		arrIdx[idx] = i;
		solution(idx+1);
		arrIdx[idx] = bak;
	}

	
}

int main()
{
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	while (1)
	{
		scanf("%d", &n);
		if (n == 0) break;

		for(int i=0; i<6; i++)
			arrIdx[i] = i;

		for (int i = 0; i < n; i++)
			scanf("%d", &arr[i]);
		solution(0);
	}
	return 0;
}