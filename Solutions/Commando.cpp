//
// Created by Leon on 2019-02-12.
//
#include <iostream>
#include <limits>
using namespace std;

long long n, a, b, c;
long long effect[1000001];
long long dp[1000001];

long long func(long long x) {
    return a*x*x + b*x + c;
}

int main () {
    cin >> n >> a >> b >> c;
    for (int i = 0; i <= n; i++) {
        dp[i] = -numeric_limits<long long>::max();
    }
    dp[0] = 0;
    effect[0] = 0;
    for (int i = 1; i <= n; i++) {
        cin >> effect[i];
        effect[i] += effect[i-1];
        for (int j = max(0, i - 200); j < i; j++) {
            dp[i] = max(dp[i], dp[j] + func(effect[i] - effect[j]));
        }
    }
    cout << dp[n];
}
