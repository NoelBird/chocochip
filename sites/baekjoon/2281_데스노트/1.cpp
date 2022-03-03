// 1. dp에서 상태를 정의하는 것에 시간이 좀 걸렸음
// 2. 맨 마지막 줄은 추가하지 않는 다는 것을 깜빡했음
// 3. priority_queue를 second 기준으로 정렬
// 4. 최적화가 필요함

#include<bits/stdc++.h>
#include<unordered_map>

using namespace std;

struct compare {
	bool operator()(pair<int, int> a, pair<int, int> b) {
		return a.second > b.second;
	}
};

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

	unordered_map<int, int> hist;
	priority_queue<pair<int, int>, vector<pair<int, int>>, compare> q; // curIdx, squaredSum

	q.push(pair<int, int>{0, 0});

	vector<int> results;
	while (!q.empty())
	{
		pair<int, int> cur = q.top();
		q.pop();

		if (cur.first >= M) // base condition: success
		{
			results.push_back(cur.second);
			continue;
		}
		if(hist.count(cur.first))
			if (hist[cur.first] < cur.second) continue; // base condition: fail
		hist[cur.first] = cur.second;

		int curIdx = cur.first;
		int curLen = 0;
		// 요기 고치기
		while (true)
		{
			if (curIdx >= M)
			{
				q.push(pair<int, int>{curIdx, cur.second});
				break;
			}
			curLen += v[curIdx]+1;
			if (curLen > N+1) break;
			curIdx++;
			q.push(pair<int, int>{curIdx, cur.second + (N - curLen + 1) * (N - curLen + 1)});
		}
	}

	int minVal = 1e9;
	for (int i = 0; i < results.size(); ++i)
		if (results[i] < minVal) minVal = results[i];

	cout << minVal << "\n";

	return 0;
}