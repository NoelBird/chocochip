#include<stdio.h>

int main()
{
    long long N;
    scanf("%lld", &N);

    long long cnt=0;

    for(long long a=1; a<4700; ++a)
    {
        for(long long b=a; b<10000000; ++b)
        {
            if(a*b*b > N)
            {
                break;
            }
            long long dd = N/(a*b)-(b-1);
            if( dd > 0)
            {
                cnt += dd;
            }
        }
    }
    printf("%lld\n", cnt);
    return 0;
}