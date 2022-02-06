#include<bits/stdc++.h>
#define all(x) (x).begin(), (x).end()
#define rep(i, n) for(int i=0; i<n; i++)

using namespace std;

//4
//3
//360 480
//420 540
//600 660
//3
//0 1440
//1 3
//2 4
//5
//99 150
//1 100
//100 301
//2 5
//150 250
//2
//0 720
//720 1440

int arr[1001][2] = { 0, };

string solution(int N, int arr[1001][2])
{
	// 1. 원래의 인덱스를 저장하고 소팅(시작 값, idx)
	vector<tuple<int, int>> savedIdx;
	for (int i = 0; i < N; i++)
	{
		savedIdx.push_back(make_tuple(arr[i][0], i));
	}
	
	vector<vector<int>> mat;
	for (int i = 0; i < N; i++)
	{
		mat.push_back(vector<int>{arr[i][0], arr[i][1]});
	}
	sort(mat.begin(), mat.begin() + N);
	sort(savedIdx.begin(), savedIdx.begin() + N);
	// 2. J부터 시작하면서 일을 할당함
	// 3. 할당이 불가능하다면 IMPOSSIBLE
	// 4. 할당이 가능하다면 원본 인덱스를 복원하고 출력
	int endTimeJ=-1;
	int endTimeC=-1;

	string _result;
	for (int i = 0; i < N; i++)
	{
		if (endTimeJ <= mat[i][0])
		{
			endTimeJ = mat[i][1];
			_result += 'J';
		}
		else if (endTimeC <= mat[i][0])
		{
			endTimeC = mat[i][1];
			_result += 'C';
		}
		else
		{
			return "IMPOSSIBLE";
		}
	}
	
	// 원래 순서 복원
	string result(N, '0');
	for (int i = 0; i < N; i++)
	{
		result.at(get<1>(savedIdx[i])) = _result[i];
	}

	
	return result;
}

int main()
{
	cin.tie(nullptr); cout.tie(nullptr);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		int N;
		cin >> N;
		for (int j = 0; j < N; j++)
		{
			cin >> arr[j][0];
			cin >> arr[j][1];
		}

		string result;
		result = solution(N, arr);
		cout << "Case #" << t << ": " << result << endl;
	}

	return 0;
}