//
// Created by Leon on 2019-02-12.
//
#include <bits/stdc++.h>

using namespace std;

int n, m;
char nl;
char grid[2001][2001];
bool visited[2001][2001];
void dfs(int x, int y){
  int cur[2];
  int move[2];
  if(grid[x][y] == 'N'){
    move[0] = -1;
    move[1] = 0;
  }
  else if(grid[x][y] == 'E'){
    move[0] = 0;
    move[1] = 1;
  }
  else if(grid[x][y] == 'S'){
    move[0] = 1;
    move[1] = 0;
  }
  else if(grid[x][y] == 'W'){
    move[0] = 0;
    move[1] = -1;
  }
  cur[0] = x + move[0];
  cur[1] = y + move[1];
  while(((0 <= cur[0]) and (cur[0] < n)) and ((0 <= cur[1]) and (cur[1] < m))){
    if (grid[cur[0]][cur[1]] != '.'){
      if(!visited[cur[0]][cur[1]]){
        dfs(cur[0], cur[1]);
        visited[cur[0]][cur[1]] = true;
      }
    }
    cur[0] += move[0];
    cur[1] += move[1];
  }
  cout << "(" << x << "," << y << ")" << "\n";
  visited[x][y] = true;
}

int main() {
  cin.sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      cin >> grid[i][j];
      visited[i][j] = false;
    }
  }
  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      if(grid[i][j] != '.'){
        if(!visited[i][j]){
          dfs(i, j);
        }
      }
    }
  }
}
