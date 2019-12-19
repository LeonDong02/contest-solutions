#include <bits/stdc++.h>

using namespace std;
#define ll long long

ll mod = 1000000007;
ll ans, n, a, b, ind;
string leaf;
int rb[300005];
vector <ll> graph[300005];
ll c[300005];


void dfs(ll u, ll p, ll col){
  ll tot = 0; ll comb = 0;
  for(ll i: graph[u]){
    if(i != p){
      dfs(i, u, col);
      comb = (comb + ((tot + comb) * c[i])) % mod;
      tot = (tot + c[i]) % mod;
    }
  }
  if(rb[u - 1] == col){
    c[u] = (1 + tot + comb) % mod;
    ans = (ans + c[u]) % mod;
  }else{
    c[u] = (tot + comb) % mod;
    ans = (ans + comb) % mod;
  }
}


int main(){
  scanf("%lld", &n);
  cin >> leaf;
  ind = 0;
  for (auto it = leaf.begin() ; it != leaf.end(); ++it) {
    if(*it == 'R'){
      rb[ind] = 0;
    }else{
      rb[ind] = 1;
    }
    ind += 1;
	}
  for(int i = 0; i < n - 1; i++){
    scanf("%lld %lld", &a, &b);
    graph[a].push_back(b); graph[b].push_back(a);
    c[i] = 0;
  }
  c[n - 1] = 0; c[n] = 0;
  dfs(1, -1, 1); dfs(1, -1, 0);
  printf("%llu\n", ans);
}
