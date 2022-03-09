#include<bits/stdc++.h>

using namespace std;

int main()
{
    cin.tie(nullptr); cout.tie(nullptr);
    ios::sync_with_stdio(false);
    
    int T;
    scanf("%d", &T);
    for(int tc=1; tc<=T; ++tc)
    {
        double result;
        int N, dest;
        scanf("%d %d", &dest, &N);
        double maxTime = 0.0;
        int pos, v;
        for(int i=0; i<N; ++i)
        {
            scanf("%d %d", &pos, &v);
            if(((double)dest - pos)/v > maxTime)
                maxTime = ((double)dest - pos)/v;
        }
        result = dest/maxTime;
        printf("Case #%d: %lf\n", tc, result);
    }
    return 0;
}