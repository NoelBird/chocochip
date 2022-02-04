// quick and dirty solution
// 1. insert '0' into the begin of the string and the end of the string
// 2. if next item is greater than current item, then add '(' to the result string
// 3. else if next item is less than current item, then add ')' to the result string

// trial1 failed: because I printed '(result)' instead of 'Case #1: (result)'

#define _CRT_SECURE_NO_WARNINGS
#include<bits/stdc++.h>
#define all(x) (x).begin(), (x).end()
using namespace std;

//4
//0000
//101
//111000
//1

int main()
{
	cin.tie(nullptr); cout.tie(nullptr);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 1; t <=T; t++)
	{
		string s, dst;
		cin >> s;

		// insert 0 into begin, end
		s.insert(s.begin(), '0');
		s += '0';
		for (int i = 0; i < s.size() - 1; i++)
		{
			int diff = s[i + 1] - s[i];
			dst += s[i];
			if (diff > 0)
			{
				for (int j = 0; j < diff; j++)
				{
					dst += '(';
				}
			}
			else if (diff == 0)
			{

			}
			else if (diff < 0)
			{
				diff = -diff;
				for (int j = 0; j < diff; j++)
				{
					dst += ')';
				}
			}
		}
		dst.erase(dst.begin());

		cout << "Case #" << t << ": " << dst << endl;
	}
	
	
	return 0;
}