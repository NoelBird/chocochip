class Solution {
public:
    bool isPalindrome(string s) {
        string a = "";
        char tmp;
        for(int i=0; i<s.size(); i++)
        {
            tmp = s[i];
            if(tmp>='A' && tmp <='Z')
            {
                a += tmp - 'A' + 'a';
            }else if(tmp>='a' && tmp<='z')
            {
                a += tmp;
            }else if(tmp>='0' && tmp<='9')
            {
                a+= tmp;
            }
        }
        
        int isPal = true;
        int aSize = a.size();
        for(int i=0; i<aSize/2; i++)
        {
            if(a[i] != a[aSize-i-1])
            {
                isPal = false;
                break;
            }
        }
        return isPal;
    }
};