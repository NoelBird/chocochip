class Solution {
public:
    bool isPerfectSquare(int num) {
        unsigned int left = 1;
        unsigned int right = (1<<16);
        unsigned int mid;
        unsigned int squared;
        while(left<=right)
        {
            mid = left + (right-left)/2;
            squared = mid*mid;

            if(squared == num)
            {
                return true;
            }else if(squared > num)
            {
                right = mid-1;
            }else
            {
                left = mid+1;
            }
        }
        return false;
    }
};