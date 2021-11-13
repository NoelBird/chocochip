#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
int main() {
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d\n", a * (b % 10));
	printf("%d\n", a * ((b / 10)%10));
	printf("%d\n", a * ((b / 100) % 10));
	printf("%d\n", a * b);
}