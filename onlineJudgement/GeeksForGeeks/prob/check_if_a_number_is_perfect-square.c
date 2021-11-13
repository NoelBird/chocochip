// 풀이1: 쉽지만 비효율적인 풀이입니다.

#include <stdio.h>

int main() {
	//code
	int T;
	scanf("%d", &T);
	while(T--){
	    int N;
	    scanf("%d", &N);
	    int isTrue=0;
	    for(int i=2; i<=N/2; i++){
	        if(N==i*i){
	            printf("1\n");
	            isTrue=1;
	            break;
	        }
	    }
	    if(!isTrue){
	        printf("0\n");
	    }
	}
	return 0;
}