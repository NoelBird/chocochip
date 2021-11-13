// 솔루션1: len을 측정하기 위해 cpy로 둔 변수가 long long 형이 아니어서 긴 문자열에서
// 오류가 났습니다.

#include <stdio.h>

int main() {
	//code
	int T;
	scanf("%d", &T);
	while(T--){
	    long long a, res;
	    scanf("%ld", &a);
	    res=0;
	    int len=0;
	    long long cpy=a;
	    while(cpy){
	        len++;
	        cpy/=10;
	    }
	    
	    for(int i=0; i<len; i++){
	        int sum=a%10;
	        for(int j=0; j<i; j++){
	            sum*=2;
	        }
	        res += sum;
	        a/=10;
	    }
	    
	    printf("%ld\n", res);
	}
	return 0;
}