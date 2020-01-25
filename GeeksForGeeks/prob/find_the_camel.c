/*
오답노트: 2020-01-19
while(*p){ 부분에서
초기에는 while(p++)로 썼는데, 이렇게 하면
p 값이 0이 안되기 때문에 무한 루프에 빠집니다.

*/

#include <stdio.h>
int main() {
	//code
	int T;
	int n;
	scanf("%d", &T);
	
	for(int i=0;i<T;i++){
        char arr[111];
	    char *p;
	    scanf("%s", arr);
	    p = arr;
	    n = 0;
	    while(*p){
	        if(*p>='A' && *p<='Z'){
	            n++;
	       };
	       p++;
	    }
	    printf("%d\n", n);
	}
	return 0;
}