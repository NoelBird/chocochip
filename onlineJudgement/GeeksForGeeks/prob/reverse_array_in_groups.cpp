// https://practice.geeksforgeeks.org/problems/reverse-array-in-groups/0/


#include <stdio.h>

long arr[10000001];

int main() {
	//code
	int T;
	int N;
	int K;
	int K_sum;
	scanf("%d", &T);
	for(int t=0; t<T; t++){
	    scanf("%d %d", &N, &K);
	    K_sum=0;
	    while(1){
	        for(int i=0; (i<K) && (i+K_sum<N); i++){
    	        scanf("%ld", &arr[i]);
    	    }
    	    if(K_sum + K<=N){
    	        for(int i=K-1; i>=0; i--){
    	            printf("%ld ", arr[i]);
    	        }
    	    }else{
    	        for(int i=K - (K_sum + K - N) - 1; i>=0; i--){
    	            printf("%ld ", arr[i]);
    	        }
    	        printf("\n");
    	        break;
    	    }
	        K_sum += K;
	    }
	}
	return 0;
}