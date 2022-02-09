#include<bits/stdc++.h>
#define rep(i, a, b) for(int i=(a);i<(b); i++)
using namespace std;

int main()
{
    int T;
    cin >> T;
    
    rep(i, 1, T+1)
    {
        int N;
        cin >> N;
        string s;
        cin >> s;
        cout << "Case #" << i << ": ";
        rep(j, 0, s.size())
        {
            if(s[j]=='S')
            {
                cout << 'E';
            }else
            {
                cout << 'S';
            }
        }
        cout << "\n";
    }
    return 0;
}