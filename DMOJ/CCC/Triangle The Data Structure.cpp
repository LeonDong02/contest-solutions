#include <bits/stdc++.h>

using namespace std;
int n, k;
long long ans;
int grid[3005][3005];
int tree[3005][3005];

int query(int x, int y){
  int a = 0; int ty;
  x++; y++;
  while(x > 0){
    ty = y;
    while(ty > 0){
      a = max(a, tree[x][ty]);
      ty -= ty & (-ty);
    }
    x -= x & (-x);
  }
  return a;
}

void update(int x, int y, int v){
  int ty;
  x++; y++;
  while(x < n + 1){
    ty = y;
    while(ty < n + 1){
      tree[x][ty] = max(tree[x][ty], v);
      ty += ty & (-ty);
    }
    x += x & (-x);
  }
}

int main() {
  scanf("%d %d", &n, &k);
  for(int i = 0; i < n; i++){
    for(int j = 0; j < i + 1; j++){
      scanf("%d", &grid[i][j]);
    }
    for(int j = i + 1; j < n; j++){
      grid[i][j] = 0;
    }
  }
  for(int i = 0; i < n + 1; i++){
    for(int j = 0; j < n + 1; j++){
      tree[i][j] = 0;
    }
  }
  for(int i = 0; i < k; i++){
    for(int j = 0; j < n + 1; j++){
      update(n - i + j - 1, n - j - 1, grid[i][j]);
    }
  }
  ans = 0;
  for(int i = k; i < n; i++){
    for(int j = 0; j < i - k + 1; j++){
      ans += query(n - i + k + j - 1, n - j - 1);
    }
    for(int j = 0; j < i + 1; j++){
      update(n - i + j - 1, n - j - 1, grid[i][j]);
    }
  }
  for(int i = 0; i < n - k + 1; i++){
    ans += query(k + i - 1, n - i - 1);
  }
  printf("%lld", ans);
}
