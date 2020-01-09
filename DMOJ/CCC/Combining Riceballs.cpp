#include <bits/stdc++.h>

using namespace std;
int n, ans;
int a[405], p[405];
int dp[405][405];

int main() {
  ans = 0;
  scanf("%d", &n);
  for(int i = 0; i < n; i++){
    scanf("%d", &a[i]);
    ans = max(ans, a[i]);
  }
  p[0] = 0;
  for(int i = 0; i < n; i++){
    p[i + 1] = p[i] + a[i];
  }
  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      if(j <= i){
        dp[i][j] = 1;
      }else{
        dp[i][j] = 0;
      }
    }
  }
  for(int i = n - 2; i > -1; i--){
    for(int j = i + 1; j < n; j++){
      for(int a = i; a < j; a++){
        for(int b = a + 1; b < j + 1; b++){
          if(p[a + 1] - p[i] == p[j + 1] - p[b]){
            dp[i][j] = max(dp[i][j], dp[i][a] & dp[b][j] & dp[a + 1][b - 1]);
            if(dp[i][j]){
              ans = max(ans, p[j + 1] - p[i]);
            }
            break;
          }
        }
      }
    }
  }
  printf("%d", ans);
}
