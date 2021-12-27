// Kruscal's Algorithm
// 처음에는 모든 간선을 포함하지 않고, 노드만 있음
// 간선을 추가했을 때 사이클이 발생하지 않으면 신장 트리에 추가하는 과정 반복

// 1. 간선의 가중치를 오름차순으로 정렬
// 2. 사이클이 만들어지지 않도록 간선 선택

// 3 3
// 1 2 1
// 2 3 2
// 1 3 3

// decisions
// 1. data structure(list vs matrix) => list. sparse form
// 2. algorithm(kruskal vs prim) => kruskal
// 3. two items in same group ? (complete search vs union find) => union find

#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

constexpr int MAX_EDGES = 100000;
constexpr int MAX_NODES = 10000;

int link[MAX_NODES] = { 0, };
int linkLen[MAX_NODES] = { 1, };

bool comp(vector<int> a, vector<int> b)
{
    if (a[2] < b[2])
        return true;
    else
        return false;
}

// union-find 경로 압축 x
// int find(int x)
// {
//     while(x != link[x]) x=link[x];
//     return x;
// }

// union-find 경로압축
int find(int x)
{
    if (x == link[x]) return x;
    link[x] = find(link[x]);
    return link[x];
}

// O(logN)
bool isSameGroup(int node1, int node2)
{
    return find(node1) == find(node2);
}

// O(logN)
void unite(int node1, int node2)
{
    if (linkLen[node1] > linkLen[node2])
    {
        int node2Parent = find(node2);
        link[node2Parent] = node1;
        linkLen[node1] += linkLen[node2Parent];
        linkLen[node2Parent] = 0;
    }
    else
    {
        int node1Parent = find(node1);
        link[node1Parent] = node2;
        linkLen[node2] += linkLen[node1Parent];
        linkLen[node1Parent] = 0;
    }
}

int main()
{
    int V, E;
    vector<vector<int>> edges;
    vector<int> selectedEdgeIndices;
    scanf("%d %d", &V, &E);

    for (int i = 0; i < E; i++)
    {
        int e1, e2, val;
        scanf("%d %d %d", &e1, &e2, &val);
        edges.push_back(vector<int>{ e1, e2, val });
    }

    sort(edges.begin(), edges.end(), comp);
    fill(linkLen, linkLen + V+1, 1);

    // initialize union-find-array
    for (int i = 0; i < V+1; i++)
    {
        link[i] = i;
    }

    selectedEdgeIndices.push_back(0);

    unite(edges[0][0], edges[0][1]);

    for (int i = 1; i < edges.size(); i++)
    {
        if (!isSameGroup(edges[i][0], edges[i][1]))
        {
            selectedEdgeIndices.push_back(i);
            unite(edges[i][0], edges[i][1]);
        }
    }

    int _sum = 0;
    for (int i = 0; i < selectedEdgeIndices.size(); i++)
    {
        _sum += edges[selectedEdgeIndices[i]][2];
    }

    printf("%d\n", _sum);

    return 0;
}