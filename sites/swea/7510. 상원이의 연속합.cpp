#include<iostream>

using namespace std;

void main() {
	int T, N, minv, ans;
	cin>>T;
	for (int j = 1;j < T + 1;j++) {
		cin>>N;
		ans = 0;
		minv = N;
		for (int i = 1;i < N+1;i++) {
			if (i % 2) {		//홀수인 경우, N을 i로 나눈 나머지가 0이어야 함.
				if((N % i) != 0)
					continue;
			}else {				//짝수인 경우, N을 i로 나눈 나머지가 i*k+(i/2) == N을 만족하는 k가 있어야함.
				if ((N - i / 2) % i != 0)
					continue;
			}
			minv = N / i - (i - 1) / 2;		// 최소 숫자 구하기
			if (minv >= 1)	// 가장 작은 수가 1이하가 되면 종료.
				ans += 1;
			else
				break;
		}
		cout <<"#"<< j << " " << ans << endl;
	}
}