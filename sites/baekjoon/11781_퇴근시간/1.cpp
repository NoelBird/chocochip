#include<bits/stdc++.h>

using namespace std;

// 7 6 5 13
// 1 2 8 1 0
// 3 2 4 0 1
// 1 5 5 0 0
// 1 4 10 0 0
// 1 6 10 0 0
// 6 7 5 0 0

// 5000*5000
// map의 사이즈가 작다면 cache hit rate를 높여서
// 원래 시간에 들어오는 게 불가능한(O(N^3)) floyd-warshall을 도전해봤을 듯
int main()
{
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    
    return 0;
}
// void Floyd_Warshall() {
//   for(m=1; m<=N; m++)
//     for(s=1; s<=N; s++)
//       for(e=1; e<=N; e++)
//         if (d[s][e] > d[s][m] + d[m][e])
// 			d[s][e] = d[s][m] + d[m][e];
// }