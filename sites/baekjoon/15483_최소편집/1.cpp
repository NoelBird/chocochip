#include<stdio.h>
#include<string.h>
#include<stdlib.h>

using namespace std;

char a[1002] = {0,};
char b[1002] = {0,};
int buf[1002][1002];

int sol(int n, int m)
{
    if(n<0) return m+1;
    if(m<0) return n+1;
    if(buf[n][m] != -1) return buf[n][m];

    int ret=0;
    if(a[n] == b[m])
        ret = sol(n-1, m-1);
    else
    {
        int val1 = sol(n, m-1)+1;
        int val2 = sol(n-1, m)+1;
        int val3 = sol(n-1, m-1)+1;
        int min_val = val1;
        if(val2 < min_val) min_val = val2;
        if(val3 < min_val) min_val = val3;
        ret = min_val;
    }
    buf[n][m] = ret;
    return ret;
}

int main()
{
    scanf("%s", a);
    scanf("%s", b);
    memset(buf, -1, sizeof(buf));
    printf("%d\n", sol(strlen(a)-1, strlen(b)-1));
    return 0;
}