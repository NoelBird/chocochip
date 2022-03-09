#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    scanf("%d", &N);
    int st = 0;
    char cmd[10] = { 0, };
    int val = 0;
    for (int i = 0; i < N; ++i)
    {
        scanf("%s", cmd);
        if (cmd[1] != 'l') scanf("%d", &val);
        if (cmd[1] == 'd') st |= 1 << val;
        else if (cmd[1] == 'e') st &= ~(1 << val);
        else if (cmd[1] == 'h') printf("%d\n", (st>>val) & 1);
        else if (cmd[1] == 'o') st ^= 1 << val;
        else if (cmd[1] == 'l') st = 0b111111111111111111111;
        else if (cmd[1] == 'm') st = 0;
    }
    return 0;
}