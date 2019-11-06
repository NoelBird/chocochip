/*interpolation search는 
정렬된 배열이 균일하게 분포되어 있을 때,loglog n이 나옵니다.
최악의 경우에는 O(n)입니다.
pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]

1. 위와 같은 공식에 의해서 위치를 반복해서 구하고,
2. 만약 arr[pos]가 x보다 값이 작으면, lo를 +1 해주고,
3. 만약 arr[pos]가 x보다 값이 크면, hi를 -1 해주면서
4. 반복합니다.while (lo <= hi && x >= arr[lo] && x <= arr[hi]) 



*/
#include<iostream> 
using namespace std; 
  
// If x is present in arr[0..n-1], then returns 
// index of it, else returns -1. 
int interpolationSearch(int arr[], int n, int x) 
{ 
    // Find indexes of two corners 
    int lo = 0, hi = (n - 1); 
  
    // Since array is sorted, an element present 
    // in array must be in range defined by corner 
    while (lo <= hi && x >= arr[lo] && x <= arr[hi]) 
    { 
        if (lo == hi) 
        { 
            if (arr[lo] == x) return lo; 
            return -1; 
        } 
        // Probing the position with keeping 
        // uniform distribution in mind. 
        int pos = lo + (((double)(hi - lo) / 
            (arr[hi] - arr[lo])) * (x - arr[lo])); 
  
        // Condition of target found 
        if (arr[pos] == x) 
            return pos; 
  
        // If x is larger, x is in upper part 
        if (arr[pos] < x) 
            lo = pos + 1; 
  
        // If x is smaller, x is in the lower part 
        else
            hi = pos - 1; 
    } 
    return -1; 
} 
  
// Driver Code 
int main() 
{ 
    // Array of items on which search will 
    // be conducted. 
    int arr[] = {10, 12, 13, 16, 18, 19, 20, 21, 
                 22, 23, 24, 33, 35, 42, 47}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
  
    int x = 18; // Element to be searched 
    int index = interpolationSearch(arr, n, x); 
  
    // If element was found 
    if (index != -1) 
        cout << "Element found at index " << index; 
    else
        cout << "Element not found."; 
    return 0; 
} 
  
// This code is contributed by Mukul Singh. 