#include <bits/stdc++.h>
#define mil 1000000
using namespace std;
int h, k, curin, minlo, lo, hi, mi, val;
deque <int> n;


bool check(int d){
  int ind, c, curp;
  ind = 0; c = 0;
  while(ind < h && c < k){
    curp = n[ind] + d;
    ind += 1;
    while(ind < h && abs(n[ind] - curp) <= d){
      ind += 1;
    }
    c += 1;
  }
  return ind == h;
}


int main() {
  scanf("%d", &h);
  for(int i = 0; i < h; i++){
    scanf("%d", &curin);
    n.push_back(curin);
  }
  scanf("%d", &k);
  sort(n.begin(), n.end());
  minlo = mil + 1;
  for(int i = 0; i < h; i++){
    lo = 0; hi = mil;
    mi = (lo + hi) >> 1;
    while(lo < hi){
      if(!check(mi)){
        lo = mi + 1;
      }else{
        hi = mi;
      }
      mi = (lo + hi) >> 1;
    }
    minlo = min(minlo, lo);
    val = n.front(); n.pop_front();
    n.push_back(val + mil);
  }
  printf("%d", minlo);
}
