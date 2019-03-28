//
// Created by Leon on 2019-03-28.
//
#include <bits/stdc++.h>

using namespace std;

int x, y;
int main(){
    cin >> x >> y;
    if(x > 0){
        if(y > 0) {
            cout << 1;
        }else{
            cout << 4;
        }
    }else{
        if(y > 0) {
            cout << 2;
        }else{
            cout << 3;
        }
    }
}
