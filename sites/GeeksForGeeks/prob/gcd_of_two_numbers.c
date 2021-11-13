// 풀이2: 풀이1과 동일하나 구조체 Pair 삭제

#include <stdio.h>

int gcd(int a, int b){
    if(b==0){
        return a;
    }
    return gcd(b, a%b);
}

int main() {
	int T;
	scanf("%d", &T);
	while(T--){
	    int a, b;
	    scanf("%d %d", &a, &b);
	    printf("%d\n", gcd(a, b));
	}
	
	return 0;
}

// 풀이1: return 값을 Pair로 해야할 것 같아서
// 구조체를 선언했으나, 그럴 필요는 없었음

// #include <stdio.h>

// typedef struct _Pair{
//     int a;
//     int b;
// } Pair;

// int gcd(Pair p){
//     if(p.b==0){
//         return p.a;
//     }
//     Pair tmp;
//     tmp.a=p.b;
//     tmp.b=p.a%p.b;
//     return gcd(tmp);
// }

// int main() {
// 	//code
// 	int T;
// 	scanf("%d", &T);
// 	while(T--){
// 	    Pair a;
// 	    scanf("%d %d", &a.a, &a.b);
// 	    printf("%d\n", gcd(a));
// 	}
	
// 	return 0;
// }