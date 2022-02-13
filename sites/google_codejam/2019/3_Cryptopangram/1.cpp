#include<bits/stdc++.h>
#define rep(i, a, b) for(int i=a; i<b; i++)
using namespace std;

int main()
{
    int T;
    cin >> T;
    rep(i, 1, T+1)
    {
        int N, L;
        cin >> N >> L;
        vector<int> nums(L);
        vector<int> middle(L);
        vector<int> result(L+1);
        rep(j, 0, L)
        {
            int num;
            cin >> num;
            nums[j] = num;
        }

        int pA = 0, pB = 0;
        rep(j, 2, nums[0])
        {
            if(nums[0]%j==0)
            {
                pA = j;
                pB = nums[0]/j;
                break;
            }
        }
        if(nums[1]%pA==0)
        {
            pA = pB;
        }
        middle[0] = pA;
        rep(j, 0, nums.size())
        {
            middle[j+1] = nums[j]/middle[j];
        }
        auto last = unique(middle.begin(), middle.end());
        middle.resize(distance(middle.begin(), last));
        sort(middle.begin(), middle.end());
        
    }
    return 0;
}
    // for j in range(len(values)):
    //     val_dict[values[j]] = chr(j+ord('A'))
    // print(f"Case #{i}: ", end="")
    // for j in range(len(ll)):
    //     print(val_dict[ll[j]], end="")
    // print()