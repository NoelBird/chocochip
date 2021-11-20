#include<algorithm>
// TLE
#include<vector>
#include<stdio.h>

using namespace std;

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> res;
        
        for(int i=0; i<nums.size(); ++i)
        {
            printf("%d ", nums[i]);
            if(nums[i] != i+1)
            {
                res.push_back(i+1);
            }
        }
        return res;
    }
};