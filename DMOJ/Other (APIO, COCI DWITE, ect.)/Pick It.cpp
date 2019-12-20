#include <bits/stdc++.h>

using namespace std;
int n; int a[300]; int dp[300][300];

int main() {
  scanf("%d", &n);
  while(n){
    for(int i = 0; i < n; i++){
      scanf("%d", &a[i]);
    }
    for(int i = 1; i < n - 1; i++){
      dp[i][i] = a[i - 1] + a[i] + a[i + 1];
    }
    for(int i = n - 2; i > 0; i--){
      for(int j = i + 1; j < n - 1; j++){
        for(int k = 0; k < j - i + 1; k++){
          dp[i][j] = max(dp[i][j], dp[i][i + k - 1] + dp[i + k + 1][j] + a[i + k] + a[i - 1] + a[j + 1]);
        }
      }
    }
    printf("%d\n", dp[1][n - 2]);
    for(int i = 1; i < n - 1; i++){
        for(int j = i; j < n - 1; j++){
            dp[i][j] = 0;
        }
    }
    scanf("%d", &n);
  }
}
