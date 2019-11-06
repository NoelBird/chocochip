/*
insertion sort는 배열의 왼쪽에다 정렬된 부분을 만들어가면서, 새로운 항목들을 정렬된 부분에 끼워넣는 정렬입니다.
바깥쪽 for loop에서는 1부터 n-1까지 루프를 돕니다. (두 번째 항목부터 시작하면 됨)
안쪽의 while loop의 조건은 j-1>=0이면서, j번째 항목이 j-1번째 항목보다 더 작은 경우에만 돕니다.

worst case: O(n^2) - 반대방향으로 정렬되어 있는 경우에 가장 느립니다.
best case: O(n)

input array가 대부분 정렬되어 있을 때, insertion sort를 쓰는 것이 효율적입니다.

개량된 방법으로 worst case
*/

#include<iostream>

using namespace std;

void swap(int* a, int* b);
void sort(int arr[], int nArr);

int main() {
	int arr[] = { 12,11,13,5,6, };
	int n = sizeof(arr) / sizeof(arr[0]);
	sort(arr, n);
	for (int i = 0;i < n;i++)
		cout << arr[i] << " ";
	cout << endl;
	return 0;
}

void swap(int* a, int* b) {
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void sort(int arr[], int nArr) {
	for (int i = 1;i < nArr;i++) {
		int j = i;
		while (j - 1 >= 0 && arr[j] < arr[j - 1]) {
			swap(&arr[j], &arr[j - 1]);
			j -= 1;
		}
	}
}