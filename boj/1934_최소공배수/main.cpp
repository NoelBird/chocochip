#include<iostream>

using namespace std;

int gcd(int a, int b);

int main() {
	int a, b;
	cin >> a;
	cin >> b;

	int ans = gcd(a, b);
	cout<< ans << endl;
	cout << a * b / ans << endl;
	return 0;
}

int gcd(int a, int b) {
	if (b == 0)
		return a;
	if (a % b == 0)
		return b;
	return gcd(b, a % b);
}