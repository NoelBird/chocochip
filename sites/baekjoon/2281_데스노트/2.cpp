// hist(unordered_map => array)
// check success after visited-check

#include<bits/stdc++.h>
#include<unordered_map>

using namespace std;

struct compare {
	bool operator()(pair<int, int> a, pair<int, int> b) {
		return a.second > b.second;
	}
};

int solution(vector<int>& v, int M, int N, int idx, int val)
{
    if (idx >= M) return val; // base condition: success
    int curLen = 0;
	
    int minVal = 1e9;
    while (true)
    {
        if (idx >= M)
        {
            minVal = min(minVal, solution(v, M, N, idx, val));
            break;
        }
        curLen += v[idx]+1;
        if (curLen > N+1) break;
        idx++;
        minVal = min(minVal, solution(v, M, N, idx, val + (N - curLen + 1) * (N - curLen + 1)));
    }
    return minVal;
}

int main()
{
	cin.tie(nullptr); cout.tie(nullptr);
	ios::sync_with_stdio(false);

	int M, N;
	cin >> M >> N;
	vector<int> v;
	int tmp;
	for (int i = 0; i < M; ++i)
	{
		cin >> tmp;
		v.push_back(tmp);
	}

    int minVal = solution(v, M, N);

	cout << minVal << "\n";

	return 0;
}