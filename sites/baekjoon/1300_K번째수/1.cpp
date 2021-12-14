// exlucde aria and recursion
// 2-dimensional binary search...? o (but repetitively twice)
// O(N * log_2^N) + O(log_2^N) ~= O(N * log_2^N) = 10^5 * 17 <= 2*10^6
// approximately 0~4ms
// integer overflow....!!!

#include<cstdio>

int main()
{
    int N;
    int target;

    scanf("%d", &N);
    scanf("%d", &target);

    long long left = 1;
    long long right = 1000000000;
    long long mid;
    long long sum;
    while (left < right)
    {
        mid = (right + left) / 2;
        sum = 0;
        for (int i = 1; i < N + 1; ++i)
            sum += mid / i < N ? mid / i : N;

        if (sum < target) left = mid + 1;
        else right = mid;
    }
    printf("%lld\n", left);
    

    return 0;
}