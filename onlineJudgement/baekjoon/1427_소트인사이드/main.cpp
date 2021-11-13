#include<iostream>

using namespace std;

void sort(int arr[], int nArr);

int main() {
	int n;
	cin >> n;

	int size_n = 0;
	int tmp = n;
	while (tmp > 0) {
		tmp /= 10;
		size_n++;
	}
	int* arr = new int[size_n];

	tmp = n;
	for (int i = size_n-1;i >=0;i--) {
		arr[i] = tmp % 10;
		tmp /= 10;
	}
	sort(arr, size_n);
	for (int i = 0;i < size_n;i++)
		cout << arr[i];
	cout << endl;

	delete [] arr;

	
	return 0;
}

void sort(int arr[], int nArr) {
	for (int i = 1;i < nArr;i++) {
		int j = i;
		while (j - 1 >= 0 && arr[j] > arr[j - 1]) {
			int tmp = arr[j];
			arr[j] = arr[j - 1];
			arr[j - 1] = tmp;
			j -= 1;
		}

	}
}