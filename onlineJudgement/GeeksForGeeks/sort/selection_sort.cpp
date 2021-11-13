/*
selection sorting은 이중루프를 반복해서 돌면서, 최소값들만 찾아서 하나씩 붙여나가는 과정을 수행합니다.

best case: O(n^2)
worst case: O(n^2)

바깥쪽의 루프에서는 마지막 항목은 비교할 필요가 없기 때문에, i< nArr-1까지 돌아도 괜찮고

안쪽의 루프는 첫 번째 요소는 idx_min 으로 저장하기 때문에 j=i+1부터 시작해서, nArr까지 루프를 돕니다.

*/

#include<iostream>

using namespace std;

void swap(int* a, int* b);
int sort(int arr[], int nArr);

int main() {
	int arr[] = { 1,5,7,8,21,34,78, };
	sort(arr, sizeof(arr)/sizeof(arr[0]));
	for (int i = 0;i < sizeof(arr) / sizeof(arr[0]);i++)
		cout << arr[i] << " ";
	cout << endl;
	return 0;
}

void swap(int* a, int* b) {
	int tmp;
	tmp = *a;
	*a = *b;
	*b = tmp;
}

int sort(int arr[], int nArr) {
	for (int i = 0;i < nArr - 1; i++) {
		int idx_min = i;
		int val_min = arr[i];
		for (int j = i + 1;j < nArr;j++) {
			int val_cur = arr[j];
			if (val_cur < val_min) {
				idx_min = j;
				val_min = val_cur;
			}
		}
		swap(arr[idx_min], arr[i]);
	}
	return -1;
}