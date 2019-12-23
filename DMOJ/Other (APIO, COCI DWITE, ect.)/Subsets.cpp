#include <bits/stdc++.h>
#define mod 1000000001
#define ll long long
using namespace std;
int n; ll c;
bool needsolve[100005];


int solve(int x){
  float cur = n / x;
  int length = floor((log(cur) / log(2))) + 1;
  int h = floor((log(cur) / log(3))) + 1;
  int compmask[h];
  int curn = x;
  for(int i = 0; i < h; i++){
    int ind = 0; int curv = curn;
    while(curv < n + 1){
      curv <<= 1;
      ind += 1;
    }
    compmask[i] = (1 << (length - ind)) - 1;
    curn *= 3;
  }
  vector <int> masks;
  for(int i = 0; i < (1 << length); i++){
    if(!(i & (i << 1))){
      masks.push_back(i);
    }
  }
  int sz = masks.size();
  bool canmask[h][sz]; bool graph[sz][sz];
  for(int i = 0; i < h; i++){
    for(int j = 0; j < sz; j++){
      canmask[i][j] = !(masks[j] & compmask[i]);
    }
  }
  for(int i = 0; i < sz; i++){
    for(int j = 0; j < sz; j++){
      graph[i][j] = !(masks[i] & masks[j]);
    }
  }
  int dp[h + 1][sz];
  for(int i = 0; i < h + 1; i++){
    for(int j = 0; j < sz; j++){
      dp[i][j] = 0;
    }
  }
  dp[h][0] = 1;
  for(int i = h - 1; i > -1; i--){
    for(int j = 0; j < sz; j++){
      if(canmask[i][j]){
        for(int k = 0; k < sz; k++){
          if(graph[j][k]){
            dp[i][j] = (dp[i][j] + dp[i + 1][k]) % mod;
          }
        }
      }
    }
  }
  int s = 0;
  for(int i = 0; i < sz; i++){
    s = (s + dp[0][i]) % mod;
  }
  return s;
}


int main() {
  scanf("%d", &n);
  for(int i = 0; i < n + 1; i++){
    needsolve[i] = true;
  }
  for(int i = 2; i < n + 1; i += 2){
    needsolve[i] = false;
  }
  for(int i = 3; i < n + 1; i += 3){
    needsolve[i] = false;
  }
  c = 1;
  for(int i = 1; i < n + 1; i++){
    if(needsolve[i]){
      c = (c * solve(i)) % mod;
    }
  }
  printf("%lld\n", c);
}
