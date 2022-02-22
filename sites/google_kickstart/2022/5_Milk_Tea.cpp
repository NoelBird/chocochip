// 1. find optimal binary values
// 2. make an order-index(by 1 0 difference desc)
// 3. increase a number 1 to K and apply order-index here
// 4. xor to optimal binary values
// 5. check if exists in impossible binaries

#include<bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int tc=1; tc<T+1; ++tc)
    {
        int N, M, P;
        cin >> N>> M >> P;
        
        // find optimal values
        bool mat[100][100] = {0,};
        for(int j=0; j<M; ++j)
        {
            string s;
            cin >> s;
            for(int k=0; k<N; ++k)
            {
                mat[j][k] = s[k] - '0';
            }
        }
        
        int optimal[100] = {0,};
        for(int j=0; j<N; ++j)
        {
            int sum=0;
            for(int k=0; k<M; ++k)
            {
                sum+=mat[k][j];
            }
            optimal[j] = sum;
        }
        
        int idx[100] = {0,};
        int diff[100] = {0,};
        for(int i=0; i<N; ++i)
        {
            diff[i] = N - optimal[i];
        }
        for(int i=0; i<N; ++i)
        {
            idx[i] = i;
        }
        
        // sort by diff desc
        for(int i=0; i<N-1; ++i)
        {
            for(int j=i+1; j<N; ++j)
            {
                if(diff[i] < diff[j])
                {
                    int tmp;
                    tmp = diff[j];
                    diff[j] = diff[i];
                    diff[i] = tmp;
                    
                    tmp = idx[j];
                    idx[j] = idx[i];
                    idx[i] = tmp;
                }
            }
        }
        
        bool base[100] = {0,};
        for(int i=0; i<N; ++i)
        {
            if(optimal[i] >= (N+1)/2)
            {
                base[i] = 1;
            }else
            {
                base[i] = 0;
            }
        }
        
        vector<string> vs;
        for(int i=0; i<P; ++i)
        {
            string tmp;
            cin >> tmp;
            vs.push_back(tmp);
        }
        
        for(int i=0; i<P; ++i)
        {
            
        }
        
        
        
        
        
        cout << "Case #" << tc << ": " << result << "\n";
    }
    return 0;
}