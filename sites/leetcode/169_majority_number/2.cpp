// time: O(N), space: O(1)
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int cnt = 0;
        int major = 0;
        for(int num: nums){
            if(cnt == 0) major = num;
            if(major == num) cnt++;
            else cnt--;
        }
        return major;
    }
};