// jinhan814 - 8ms

// [좋은 점]
// 직접 syscall을 사용하는게 인상적이었음
// loop 최적화를 위해서 while(m--)로 사용한 것이 인상적
// main 대신에 __libc_start_main()을 사용했음
// early return을 사용해서 분기를 없앤 것도 좋았음

// [나쁜 점]
// 속도를 위해서 함수를 전부 전처리로 돌려서 디버깅은 거의 불가능에 가까울 듯
// 문자 ascii code '0'을 표현하려고 48을 썼는데 그건 0x30이나 '0'을 그대로 쓰는게 더 좋았을 듯(가독성)

#include <unistd.h>

#define SZ (1 << 15)

#define ReadChar(ch) { \
    if (p == r + SZ) syscall(0, 0, p = r, SZ); \
    ch = *p++; }

#define ReadInt(n) { \
    char ch; ReadChar(ch) \
    for (; ~ch & 16;) ReadChar(ch) \
    for (; ch & 16;) { n = 10 * n + (ch & 15); ReadChar(ch) } }

#define WriteInt(n) { \
    if (idx + 10 >= SZ) syscall(1, 1, w, idx), idx = 0; \
    int m = n, sz = GetSize(m); \
    for (int j = sz; j --> 0; m /= 10) w[idx + j] = m % 10 | 48; \
    idx += sz; }

inline int GetSize(int n) {
    int ret = 1;
    for (n = n >= 0 ? n : -n; n >= 10; n /= 10) ret++;
    return ret; }

__libc_start_main() {
    char r[SZ], w[SZ], *p = r; syscall(0, 0, r, SZ);
    int n = 0, m = 0, idx = 0; ReadInt(n); ReadInt(m);
    short adj[201][201], dp[201][201];
    for (int i = 1; i <= n; i++) for (int j = 1; j <= n; j++) {
        adj[i][j] = 1e4;
    }
    while (m--) {
        int a = 0, b = 0, c = 0; ReadInt(a); ReadInt(b); ReadInt(c);
        adj[a][b] = adj[b][a] = c;
    }
    for (int i = 1; i <= n; i++) for (int j = 1; j <= n; j++) {
        if (i == j) adj[i][i] = 0;
        else dp[i][j] = j;
    }
    for (int k = 1; k <= n; k++) for (int i = 1; i <= n; i++) for (int j = 1; j <= n; j++) {
        if (adj[i][j] <= adj[i][k] + adj[k][j]) continue;
        adj[i][j] = adj[i][k] + adj[k][j], dp[i][j] = dp[i][k];
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == j) w[idx++] = '-';
            else WriteInt(dp[i][j]);
            if (j < n) w[idx++] = ' ';
        }
        w[idx++] = '\n';
    }
    syscall(1, 1, w, idx); _exit(0);
} main;