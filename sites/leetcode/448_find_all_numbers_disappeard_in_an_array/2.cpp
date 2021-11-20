#include<algorithm>
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
            int lo=0;
            int hi=nums.size()-1;
            bool isFound = false;
            while(lo<=hi)
            {
                int mid = (lo+hi)/2;
                if(nums[mid] == i+1)
                {
                    isFound = true;
                    break;
                }else if(nums[mid] > i+1)
                {
                    hi = mid-1;
                }else if(nums[mid] < i+1)
                {
                    lo = mid+1;
                }
            }
            if(!isFound)
            {
                res.push_back(i+1);
            }
        }
        return res;
    }
};