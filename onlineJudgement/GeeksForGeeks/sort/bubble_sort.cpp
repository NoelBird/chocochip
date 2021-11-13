/*
bubble sort는 O(n^2)입니다.

best case: n^2
worst case: n^2

[실수한 부분]
1) 바깥쪽 루프는 n-1, 안쪽 루프는 n-1-i인데, 안쪽 루프도 n-1로 짰음. 비효율적.

*/

#include<iostream>

using namespace std;

void sort(int arr[], int nArr);

int main() {
	int arr[] = { 1,2,3,56,76,4,342112,24,4,6,57 };
	int n = sizeof(arr) / sizeof(arr[0]);
	sort(arr, n);
	for (int i = 0;i < n;i++)
		cout << arr[i] << " ";
	cout << endl;
	return 0;
}

void sort(int arr[], int nArr) {
	for(int i=0;i<nArr-1;i++)
		for(int j=0;j<nArr-1-i;j++)
			if (arr[j] > arr[j + 1]) {
				int tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
			}
}