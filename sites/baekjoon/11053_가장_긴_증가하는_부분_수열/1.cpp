// 6
// 10 20 10 30 20 50

// 어려움…

// 가장 긴 증가하는 부분 수열

// 언제 분기가 되느냐…?
// 모든 값들이 다 증가하고 있다면, 분기가 될 가능성이 없음
// 내려 가는 값이 있을 때 분기가 됨

// 어떻게 저장할 지..?

// 1. 무식하게 전부 다 저장

// 어떻게 다 저장..?
// 분기를 만날 때마다 다 저장..?
// 그러면 최대 N개만큼 저장해야 함

// 분기를 만나면, 새로운 cache에다가 분기해서 저장
// 분기가 없으면 모든 cache값들을 순회하면서 +1씩 함

// 이중 포문…?
// => 이중 포문이 생성됨. 시간 안에는 못 들어옴

// 2. NlogN이 되어야 시간 안에 들어옴.  Binary Search..?


// 바깥의 부분이 binary search, 안쪽 부분이 N으로 순회하는 방법이 없을까…?
// 긴 수열이라면 작은 수열을 포함하기 때문에, 돌 수 있음

// DP...?
// A(i) = max(A(j) for j in range(0, i) if A(j) < A(i)) + 1 

#include<cstdio>
#define MAXLEN 1000000

int cache[MAXLEN] = {0,};
int vals[MAXLEN] = {0,};

int main()
{
    int N;
    scanf("%d", &N);

    // get inputs
    for(int i=0; i<N; ++i)
    {
        scanf("%d", &vals[i]);
    }
    
    for(int i=0; i<N; ++i)
    {
        for(int j=0; j<i; ++j)
        {
            if(vals[j] < vals[i] && cache[j] > cache[i])
                cache[i] = cache[j];
        }
        cache[i]++;
    }

    int max=0;
    for(int i=0; i<N; ++i)
    {
        if(cache[i] > max)
            max = cache[i];
    }
    printf("%d\n", max);
    return 0;
}