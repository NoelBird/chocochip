#include<iostream>

using namespace std;

int gcd(int a, int b);

int main() {
	int a, b;
	int k;
	int ans;

	cin >> k;
	for (int i = 0; i < k; i++) {
		cin >> a;
		cin >> b;
		ans = gcd(a, b);
		cout << a * b / ans << endl;
	}
	return 0;
}

int gcd(int a, int b) {
	if (b == 0)
		return a;
	if (a % b == 0)
		return b;
	return gcd(b, a % b);
}