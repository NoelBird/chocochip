class Solution {
public:
    int firstUniqChar(string s) {
        int idx;
        for(int i=0; i<s.size(); ++i)
        {
            int idx=i;
            bool flag=false;
            for(int j=i+1; j<s.size(); ++j)
            {
                if(i==j)
                {
                    flag=true;
                    break;
                }
            }
            if(!flag)
            {
                cout << idx << endl;
            }
        }
    }
    return idx;
};