class Solution {
public:
    int romanToInt(string s) {
        int res = 0;
        for(int i=0; i<s.size(); ++i)
        {
            char x=s[i];
            if(x=='I')
            {
                if(i!=s.size()-1 && (s[i+1] == 'V' || s[i+1] == 'X'))
                {
                    res -= 1;
                }else
                {
                    res += 1;
                }
            }else if(x=='V')
            {
                res += 5;
            }else if(x=='X')
            {
                if(i!=s.size()-1 && (s[i+1] == 'L' || s[i+1] == 'C'))
                {
                    res -= 10;
                }else
                {
                    res += 10;
                }
            }else if(x=='L')
            {
                res += 50;
            }else if(x=='C')
            {
                if(i!=s.size()-1 && (s[i+1] == 'D' || s[i+1] == 'M'))
                {
                    res -= 100;
                }else
                {
                    res += 100;
                }
            }else if(x=='D')
            {
                res += 500;
            }else if(x=='M')
            {
                res += 1000;
            }
        }
        
        return res;
    }
};