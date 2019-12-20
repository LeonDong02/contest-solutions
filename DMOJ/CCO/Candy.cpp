#include <bits/stdc++.h>
#define ll long long
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;
int n, ki, vi, m, sumcandy;
bool dp[10000007];
int k[101]; int v[101];

int main() {
  cin.sync_with_stdio(0); cin.tie(0);
  sumcandy = 0;
  scan(n);
  for(int i = 0; i < n; i++){
    scan(ki); scan(vi);
    sumcandy += ki * vi;
    k[i] = ki; v[i] = vi;
  }
  m = sumcandy / 2;
  dp[0] = 1;
  for(int i = 0; i < n; i++){
    for(int j = m - v[i]; j > -1; j--){
      if(dp[j]){
        for(int a = j + v[i]; a < min(sumcandy + 1, j + (k[i] * v[i]) + 1); a += v[i]){
          if(dp[a]){
              break;
          }
          dp[a] = 1;
        }
      }
    }
  }
  for(int i = m; i > -1; i--){
    if(dp[i]){
      cout << sumcandy - (i << 1);
      return 0;
    }
  }
}
