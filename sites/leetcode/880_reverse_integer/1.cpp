class Solution {
public:
    int reverse(int x) {
        bool isPlus = false;
        if(x>=0) isPlus=true;
        
        long long val = x;
        if(!isPlus) val*=-1;
        
        int arr[33] = {0,};
        int len = 0;
        long long y=0;
        
        while(val)
        {
            arr[len] = val % 10;
            
            val /= 10;
            len++;
        }
        
        for(int i=0; i<len; i++)
        {
            y += arr[i];
            y *= 10;
        }
        y/=10;
        
        if(y >= INT_MAX) return 0;
        if(!isPlus) y*=-1;
        return y;
        
        
    }
};