#include <bits/stdc++.h>

using namespace std;
int r, c;
vector <long long> masks;
long long dp[100][3000];
vector <int> graph[3000];

int main() {
  long long mod = 1000000007;
  cin >> r >> c;
  for(int i = 0; i < (1 << (c - 2)); i++){
    if(!(i & (i << 1)) && !(i & (i << 2))){
      masks.push_back(i);
    }
  }
  int n = masks.size();
  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      if(!(masks[i] & masks[j]) && !(masks[i] & (masks[j] << 1)) && !(masks[j] & (masks[i] << 1))){
        graph[i].push_back(j);
      }
    }
  }
  for(int i = 0; i < n; i++){
    dp[r - 1][i] = 0;
  }
  dp[r - 1][0] = 1;
  for(int i = r - 2; i > -1; i--){
    for(int j = 0; j < n; j++){
      for(int k: graph[j]){
        dp[i][j] = (dp[i][j] + dp[i + 1][k]) % mod;
      }
    }
  }
  long long s = 0;
  for(int i = 0; i < n; i++){
    s = (s + dp[0][i]) % mod;
  }
  cout << s - 1 << "\n";
}
