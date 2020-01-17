#include<cstdio>
int main() {
	int h, m;
	scanf("%d %d", &h, &m);
	if (m >= 45) {
		m -= 45;
	}
	else {
		if (h != 0) {
			h -= 1;
			m = m + 60 - 45;
		}
		else {
			h = 23;
			m = m + 60 - 45;
		}
	}
	printf("%d %d\n", h, m);
}