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

void solution(int arr[], int n)
{
	for (int i1 = 0; i1 < n - 5; i1++)
		for (int i2 = i1 + 1; i2 < n - 4; i2++)
			for (int i3 = i2 + 1; i3 < n - 3; i3++)
				for (int i4 = i3 + 1; i4 < n - 2; i4++)
					for (int i5 = i4 + 1; i5 < n - 1; i5++)
						for (int i6 = i5 + 1; i6 < n; i6++)
							printf("%d %d %d %d %d %d\n", arr[i1], arr[i2], arr[i3], arr[i4], arr[i5], arr[i6]);
}

int main()
{
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int arr[MAX_ARR] = { 0, };
	int n;
	while (1)
	{
		scanf("%d", &n);
		if (n == 0) break;

		for (int i = 0; i < n; i++)
			scanf("%d", &arr[i]);
		solution(arr, n);
	}
	return 0;
}