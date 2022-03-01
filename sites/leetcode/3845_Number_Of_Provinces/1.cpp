// union find
// path compression

class Solution {
private:
    int root[201];
    int rank[201];
public:
    Solution(){
        for (int i = 0; i < 201; i++) {
            root[i] = i;
            rank[i] = 1;
        }
    }

    int find(int x) {
        if (x == root[x]) return x;
        return root[x] = find(root[x]);
    }

    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                root[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                root[rootX] = rootY;
            } else {
                root[rootY] = rootX;
                rank[rootX] += 1;
            }
        }
    }

    int findCircleNum(vector<vector<int>>& isConnected) {
        for(int i=0; i<isConnected.size(); ++i)
            for(int j=0; j<isConnected[i].size(); ++j)
                if(isConnected[i][j]) unionSet(i, j);
        int cntArr[201] = {0,};
        for(int i=0; i<isConnected.size(); ++i)
        {
            cntArr[find(i)]++;
        }
        int cnt=0;
        for(int i=0; i<201; ++i)
        {
            if(cntArr[i]) cnt++;
        }
        return cnt;
        
    }
};