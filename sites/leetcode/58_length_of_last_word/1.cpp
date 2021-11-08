#include<string>

using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = 0;
        int buf = 0;
        for(int i=0; i<s.size(); ++i)
        {
            if(s[i] != ' ')
            {
                len++;
            }else
            {
                len = 0;
            }
            if(len)
                buf = len;
        }
        return buf;
    }
};