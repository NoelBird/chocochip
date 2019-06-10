#include<iostream>
#define NIL -1

using namespace std;

void _init(int arr[], int n); // 초기화

int fib(int arr[], int n);	// dp적용된 피보나치 수

int main() {
	int arr[100];
	_init(arr, sizeof(arr) / sizeof(arr[0]));
	int ans = fib(arr, 40); // 40정도까지밖에 구현이 안 됩니다.
	cout << ans << endl;
	return 0;
}

void _init(int arr[], int n) {
	for (int i = 0; i < n; i++)
		arr[i] = NIL;
}

int fib(int arr[], int n) {
	int cur = arr[n];
	if (cur == NIL) {
		if (n == 1 | n == 2)
			arr[n] = 1;
		else
			arr[n] = fib(arr, n - 1) + fib(arr, n - 2);
	}
	return arr[n];
}