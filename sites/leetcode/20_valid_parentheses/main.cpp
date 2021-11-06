#include<string>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        if(s.size()%2 == 1)
        {
            return false;
        }
        
        char stack[10001] = {0,};
        int top = 0;
        int isVal=true;
        for(int i=0; i<s.size(); ++i)
        {
            if(s[i] == '(')
            {
                stack[top++] = 0;
            }else if(s[i] == ')')
            {
                if(top==0)
                {
                    isVal=false;
                    break;
                }else
                {
                    if(stack[top-1] == 0)
                    {
                        top--;
                    }else
                    {
                        isVal = false;
                        break;
                    }
                }
            }else if(s[i] == '{')
            {
                stack[top++] = 1;
            }else if(s[i] == '}')
            {
                if(top==0)
                {
                    isVal=false;
                    break;
                }else
                {
                    if(stack[top-1] == 1)
                    {
                        top--;
                    }else
                    {
                        isVal = false;
                        break;
                    }
                }
            }else if(s[i] == '[')
            {
                stack[top++] = 2;
            }else if(s[i] == ']')
            {
                if(top==0)
                {
                    isVal=false;
                    break;
                }else
                {
                    if(stack[top-1] == 2)
                    {
                        top--;
                    }else
                    {
                        isVal = false;
                        break;
                    }
                }
            }
        }
        if(isVal && top == 0) return true;
        else return false;
    }
};

int main()
{
    Solution *s = new Solution();
    printf("%d\n", s->isValid(string("(]")));
    return 0;
}