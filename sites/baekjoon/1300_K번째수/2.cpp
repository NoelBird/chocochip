// exlucde aria and recursion
// 2-dimensional binary search...? o (but repetitively twice)
// O(N * log_2^N) + O(log_2^N) ~= O(N * log_2^N) = 10^5 * 17 <= 2*10^6
// approximately 0~4ms
// integer overflow....!!!

// much faster

#include<stdio.h>
int main()
{
    int N, t, i;
    scanf("%d %d", &N, &t);
    int l = 1; int r = t;
    int mid, sum;
    while (l<r)
    {
        mid = (r + l) / 2;
        sum = 0;
        for (i = 1; i*i <=mid; ++i)
            sum += mid / i < N ? mid / i : N;
        sum = 2*sum - (i-1)*(i-1);

        if (sum < t) l = mid + 1;
        else r = mid;
    }
    printf("%d\n", l);
    return 0;
}