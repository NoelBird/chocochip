// 2
// 3
// 5 1 2
// 6
// 1 3 3 2 2 15

// segment tree
#include<bits/stdc++.h>
using namespace std;

// long long init(vector<long long> &a, vector<long long> &tree, int node, int start, int end) {
//     if (start == end) {
//         return tree[node] = a[start];
//     } else {
//         return tree[node] = init(a, tree, node*2, start, (start+end)/2) + init(a, tree, node*2+1, (start+end)/2+1, end);
//     }
// }

void update(int tree[], int node, int start, int end, int index, long long diff) {
    if (index < start || index > end) return;
    tree[node] = tree[node] + diff;
    if (start != end) {
        update(tree, node * 2, start, (start + end) / 2, index, diff);
        update(tree, node * 2 + 1, (start + end) / 2 + 1, end, index, diff);
    }
}
long long sum(int tree[], int node, int start, int end, int left, int right) {
    if (left > end || right < start) {
        return 0;
    }
    if (left <= start && end <= right) {
        return tree[node];
    }
    return sum(tree, node * 2, start, (start + end) / 2, left, right) + sum(tree, node * 2 + 1, (start + end) / 2 + 1, end, left, right);
}
int main() {
    int T;
    cin >> T;
    for (int i = 1; i < T + 1; ++i)
    {
        int N;
        int h;
        cin >> N;
        //1. init segment tree
        int tree[100000 * 4] = { 0, };
        int hIndex = 1;
        string result = "";
        for (int j = 0; j < N; ++j)
        {
            cin >> h;
            update(tree, 1, 1, 100000, h, 1);
            int q = sum(tree, 1, 1, 100000, hIndex + 1, 100000);
            if (q >= hIndex + 1)
            {
                hIndex++;
            }
            result += to_string(hIndex) +" ";
        }
        //2. update segment tree
        //3. query
        cout << "Case #" << i << ": ";
        cout << result << "\n";
    }
    return 0;
}