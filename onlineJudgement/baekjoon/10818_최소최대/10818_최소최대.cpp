/*
제출 이력

2020-01-17. 최소 값이 - 값이 될 수 있는 것을 문제를 잘 못 봤음

*/

#include<cstdio>
int main() {
	int n, nn;
	int max= -1000000, min= 1000000;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &nn);
		if (nn > max) {
			max = nn;
		}
		if (nn < min) {
			min = nn;
		}
	}
	printf("%d %d\n", min, max);
}