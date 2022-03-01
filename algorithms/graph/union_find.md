# Union FInd

> feature

1. path compression
2. union by rank

```C++

class Solution {
    // init
    Solution(){
        for (int i = 0; i < 201; i++) {
            root[i] = i;
            rank[i] = 1;
        }
    }

    // find
    int find(int x) {
        if (x == root[x]) return x;
        return root[x] = find(root[x]);
    }

    // union
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

    // check if connected
    bool isConnected(int x, int, y)
    {
        return find(x) == find(y);
    }
};
```