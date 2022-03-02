// 다익스트라 알고리즘
// double이 부정확해서 문제가 되는 것 같음
#include<bits/stdc++.h>
#include <limits>

using namespace std;

constexpr int MAX_SIZE = 5010;
constexpr long long MAX_VAL = numeric_limits<long long>::max();

// 7 6 5 13
// 1 2 8 1 0
// 3 2 4 0 1
// 1 5 5 0 0
// 1 4 10 0 0
// 1 6 10 0 0
// 6 7 5 0 0
int main()
{
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int N, M; // N: the number of points, M: intersection of points, tS: start point, tE: end point
    double tS, tE;
    cin >> N >> M >> tS >> tE;
    bool delayedMap[MAX_SIZE][MAX_SIZE] = { 0, };
    double lengthMap[MAX_SIZE][MAX_SIZE] = { 0, };
    double minTime[MAX_SIZE] = { 0, };

    for (int i = 1; i < N+1; ++i)
    {
        for (int j = 1; j < N + 1; ++j)
        {
            lengthMap[i][j] = MAX_VAL;
        }
        minTime[i] = MAX_VAL;
    }
    for (int i = 0; i < M; ++i)
    {
        // A, B, L, t1, t2. A, B: points, L: length of the intersection, t1: delayed A=>B, t2: delayed B=>A
        long long a, b;
        double l;
        bool t1, t2;
        cin >> a >> b >> l >> t1 >> t2;
        delayedMap[a][b] = t1;
        delayedMap[b][a] = t2;

        lengthMap[a][b] = l;
        lengthMap[b][a] = l;
    }

    queue<int> q;
    q.push(1); // company

    minTime[1] = 0.0;
    while (!q.empty())
    {
        int qLen = q.size();
        for (int i = 0; i < qLen; ++i)
        {
            int src = q.front();
            q.pop();
            for (int dst = 1; dst < N+1; ++dst)
            {
                if (src == dst) continue;
                bool isDelayed = delayedMap[src][dst];
                double dist = lengthMap[src][dst];
                double totalTime = 0.0;
                if (isDelayed)
                {
                    double time1, time2, time3;
                    double s, e;
                    // section 1
                    s = min(minTime[src], tS);
                    e = min(minTime[src] + dist / 1.0, tS);  // velocity: 1.0
                    
                    time1 = e - s;
                    dist -= time1;
                    totalTime += time1;
                    // section 2
                    s = max(tS, min(tE, minTime[src] + totalTime));
                    e = max(tS, min(tE, minTime[src] + totalTime + dist * 2.0));
                    
                    time2 = e - s;
                    dist -= time2*0.5;
                    totalTime += time2;
                    // section 3
                    s = max(minTime[src] + totalTime, tE);
                    e = max(minTime[src] + totalTime + dist, tE);
                    time3 = e - s;
                    totalTime += time3;
                }
                else
                {
                    totalTime = lengthMap[src][dst];
                }

                if (minTime[src] + totalTime < minTime[dst])
                {
                    minTime[dst] = minTime[src] + totalTime;
                    q.push(dst);
                }
            }
        }
    }

    double maxVal = minTime[1];
    for (int i = 1; i < N + 1; ++i)
    {
        if (minTime[i] > maxVal && minTime[i] != MAX_VAL)
        {
            maxVal = minTime[i];
        }
    }

    cout << maxVal << "\n";
    
    return 0;
}