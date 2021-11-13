/* linear search는 index를 0부터 nArr-1까지 1씩 증가하면서 대상 값이 들어있는 index를 찾습니다.*/

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

int search(int arr[], int nArr, int x){
    for(i=0;i<nArr;i++)
        if(arr[i]==x)
            return i;
    return -1;
}