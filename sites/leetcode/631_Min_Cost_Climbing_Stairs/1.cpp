class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int arr[1000] = {0,};
        arr[0] = cost[0];
        arr[1] = cost[1];
        for(int i=2; i<cost.size(); ++i)
        {
            arr[i] = arr[i-1] < arr[i-2] ? arr[i-1] : arr[i-2];
            arr[i] += cost[i];
        }
        int min = arr[cost.size()-1];
        if(arr[cost.size()-2] < min)
            min = arr[cost.size()-2];
        return min;
    }
};
