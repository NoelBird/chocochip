// better version n^3 => n^2. but TLE
#include<vector>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxVal = -99999;
        for(int i=0; i<nums.size(); ++i)
        {
            int sum=0;
            for(int j=i; j<nums.size(); ++j)
            {
                sum += nums[j];
                if(sum>maxVal)
                {
                    maxVal = sum;
                }
            }
            
        }
        return maxVal;
    }
};