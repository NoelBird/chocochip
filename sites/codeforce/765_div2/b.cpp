#include<cstdio>
#include<cstring>
#define MAX_NUM 150001
using namespace std;

int main()
{
    int t;
    int n;
    int tmp;
    int arr[MAX_NUM] = {0,};

    scanf("%d", &t);
    for(int i=0; i<t; i++)
    {
        scanf("%d", &n);
        memset(arr, -1, MAX_NUM*sizeof(int));
        int rslt = -1;

        for(int j=0; j<n; j++)
        {
            scanf("%d", &tmp);
            if(arr[tmp]==-1)
            {
                arr[tmp] = j;
            }else
            {
                if(arr[tmp] + (n-j) > rslt)
                    rslt = arr[tmp] + (n-j);
                arr[tmp] = j;
            }
        }
        printf("%d\n", rslt);
    }
    return 0;
}