#include<cstdio>
int main() {
	int a, b;
	scanf("%d", &a);
	if((a % 400 == 0)||(a % 4 == 0 && a % 100 != 0)){
		puts("1");
	}
	else {
		puts("0");
	}
}