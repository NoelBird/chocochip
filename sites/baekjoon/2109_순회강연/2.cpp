#include<iostream>
#include<vector>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<pair<int, int> > v;

    int maxDate = 0;
    for(int i=0; i<N; ++i)
    {
        int p, d;
        cin >> p >> d;
        if(d > maxDate)
            maxDate = d;
        v.push_back(make_pair(p, d));
    }

    int result = 0;
    for(int i=maxDate; i>=1; --i)
    {
        int maxPay = 0;
        int maxIdx = -1;
        for(int j=0;j<v.size(); ++j)
        {
            if(v[j].first > maxPay && v[j].second >= i)
            {
                maxPay = v[j].first;
                maxIdx = j;
            }
        }
        if(maxIdx >=0)
        {
            result += maxPay;
            v.erase(v.begin()+maxIdx, v.begin()+maxIdx+1);
        }
    }
    cout << result << endl;
    return 0;
}