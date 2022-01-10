class Solution {
public:
    bool isPalindrome(string s) {
        string a = "";
        for(int i=0; i<s.size(); i++)
        {
            if(s[i]>='A' && s[i] <='Z')
            {
                a += s[i] - 'A' + 'a';
            }else if(s[i]>='a' && s[i]<='z')
            {
                a += s[i];
            }else if(s[i]>='0' && s[i]<='9')
            {
                a+= s[i];
            }
        }
        
        int isPal = true;
        for(int i=0; i<a.size()/2; i++)
        {
            if(a[i] != a[a.size()-i-1])
            {
                isPal = false;
                break;
            }
        }
        return isPal;
    }
};