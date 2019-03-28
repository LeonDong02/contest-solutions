//
// Created by Leon on 2019-03-28.
//
#include <bits/stdc++.h>

using namespace std;

int a, b, c, d, t;
int main(){
    cin >> a >> b >> c >> d >> t;
    int dis = abs(a - c) + abs(b - d);
    if(dis <= t and !(t - dis) % 2){
        cout << 'Y';
    }else{
        cout << 'N';
    }
}
