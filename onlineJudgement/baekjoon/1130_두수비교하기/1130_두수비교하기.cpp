#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
int main() {
	int a, b;
	scanf("%d %d", &a, &b);
	if (a < b) {
		printf("<\n");
	}
	else if (a == b) {
		printf("==\n");
	}
	else {
		printf(">\n");
	}
}