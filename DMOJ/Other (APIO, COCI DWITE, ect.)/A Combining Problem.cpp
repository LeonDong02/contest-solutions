#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, a, b;
    scanf("%d", &n);
    scanf("%d", &a);
    long long c = 0;
    for(int i = 0; i < n - 1; i++){
        scanf("%d", &b);
        c += max(a, b);
        a = b;
    }
    printf("%lld\n", c);
}
