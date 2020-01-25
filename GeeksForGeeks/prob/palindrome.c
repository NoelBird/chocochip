// 솔루션2: 루프 제어 변수를 2개 둬서(i, j) 해결

#include <stdio.h>

int main() {
	//code
	int T;
	scanf("%d", &T);
	while(T--){
	    char arr[6];
	    scanf("%s", arr);
	    char *p=arr;
	    int i, j;
	    int len=0;
	    while(*p!=NULL){
	        len++;
	        p++;
	    }
	    i=0;
	    j=len-1;
	    int isPal=1;
	    while(j>=i){
	        if(arr[i]!=arr[j]){
	            isPal=0;
	            break;
	        }
	        j--;
	        i++;
	    }
	    if(isPal){
	        printf("Yes\n");
	    }else{
	        printf("No\n");
	    }
	}
	return 0;
}

// // 솔루션1: 답이 틀림

// #include <stdio.h>

// int main() {
// 	//code
// 	int T;
// 	scanf("%d", &T);
// 	while(T--){
// 	    int N;
// 	    scanf("%d", &N);
// 	    int rev=0;
// 	    int cpy=N;
// 	    int len=0;
// 	    while(cpy){
// 	        rev*=10;
// 	        rev+=N%10;
// 	        cpy/=10;
// 	        len++;
// 	    }
// 	    int isPal=1;
// 	    for(int i=0; i<=len/2; i++){
// 	        if(rev%10 != N%10){
// 	            isPal=0;
// 	            break;
// 	        }
// 	        rev/=10;
// 	        N/=10;
// 	    }
// 	    if(isPal){
// 	        printf("Yes\n");
// 	    }else{
// 	        printf("No\n");
// 	    }
// 	}
// 	return 0;
// }