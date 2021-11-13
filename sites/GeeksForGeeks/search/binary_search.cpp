/* 
binary search는 arr를 반씩 쪼개가면서, 하한값, 상한값을 변경해가면서, 가운데의 값이 target value와 같으면 탐색을 종료합니다.

1) 오름차순 정렬 되어있는 경우에,

middle point의 값이 target value보다 작으면, 원하는 index가 middle point보다 큰 곳에 있기 때문에 lower bound를 middle point +1로,
middle point의 값이 target value보다 크면, 원하는 index가 middle point보다 작은 곳에 있기 때문에 upper bound를 middler point -1로.
*/

#include<iostream>

using namespace std;

int search(int arr[], int nArr, int x);

void main(){
    int arr[]={1,3,5,6,7,9,};
    int x=5;
    int ans=search(arr, sizeof(arr)/sizeof(arr[0]), x);
    if(ans!=-1){
        cout<<"the index of target is: "<<ans<<endl;
    }else{
        cout<<"there's no target value in arr"<<endl;
    }
}

int search(int arr[], int nArr, int x){ // 찾으면 arr의 index를 반환, 못 찾으면 -1 반환
    int idx_l, idx_h, idx_m, val_m;
    idx_l = 0;
    idx_h = nArr-1;
    while(idx_h>=idx_l){
        idx_m = idx_l + (idx_h - idx_l)/2;
        val_m = arr[idx_m];
        if(val_m == x){     //found
            return idx_m;
        }else if(val_m < x){
            idx_l = idx_m + 1;
        }else{
            idx_h = idx_m - 1;
        }
    }
    return -1;
}