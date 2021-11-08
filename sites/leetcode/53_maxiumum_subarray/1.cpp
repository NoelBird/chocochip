// brute force: worst Big-O(n^3) case
#include<vector>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxVal = -99999;
        for(int i=0; i<nums.size(); ++i)
        {
            for(int j=0; j<nums.size(); ++j)
            {
                int sum=0;
                
                for(int k=j; k<nums.size(); ++k)
                {
                    sum += nums[k];
                    if(sum > maxVal)
                    {
                        maxVal = sum;
                    }
                }
            }
        }
        return maxVal;
    }
};