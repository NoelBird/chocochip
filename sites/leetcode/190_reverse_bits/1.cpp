#include <iostream>
#include<stdio.h>

using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t a=0;
        for(int i=0; i<32; ++i)
        {
            a |= n&1;
            if(i==31)break;
            n >>= 1;
            a <<= 1;
            printf("%x\n", a);
        }
        return a;
    }
};

int main()
{
    Solution *s = new Solution;
    s->reverseBits(0b00000010100101000001111010011100);
    return 0;
}