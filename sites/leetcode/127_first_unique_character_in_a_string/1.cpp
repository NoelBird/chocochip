// runtime: 56ms
// slow

class Solution {
public:
    int firstUniqChar(string s) {
        int idx;
        bool impossibleArr[100001] = {0,};
        bool isFound;
        for(int i=0; i<s.size(); ++i)
        {
            if(impossibleArr[i]==true) continue;
            idx=i;
            isFound=true;
            for(int j=i+1; j<s.size(); ++j)
            {
                if(s[i]==s[j])
                {
                    isFound=false;
                    impossibleArr[i] = true;
                    impossibleArr[j] = true;
                }
            }
            if(isFound)
            {
                break;
            }
        }
        if(!isFound) return -1;
        return idx;
    }
};