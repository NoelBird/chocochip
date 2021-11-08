// 
#include<vector>

using namespace std;

class Solution {
public:
    int binarySearch(vector<int>& nums, int key, int lo, int hi)
    {
        while(true)
        {
            int mid = (hi+lo)/2;

            // terminal condition - fail
            // to find this conditions is too hard...
            if(lo + 1 >= hi)
            {
                return mid+1;
            }
            
            if(nums[mid] == key)
            {
                return mid;
            }else if(nums[mid] > key)
            {
                hi = mid;
            }else if(nums[mid] < key)
            {
                lo = mid;
            }
        }
        return lo;
    }
    
    int searchInsert(vector<int>& nums, int target) {
        if(target > nums[nums.size()-1])
        {
            return nums.size();
        }
        if(target <= nums[0])
        {
            return 0;
        }
        return binarySearch(nums, target, 0, nums.size()-1);
    }
};