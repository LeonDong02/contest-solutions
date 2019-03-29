//
// Created by Leon on 2019-03-29.
//
#include <bits//stdc++.h>

using namespace std;

int m, n;
int main(){
    cin >> m >> n;
    int c = 0;
    for(int i = 1; i <= m; i ++){
        for(int j = 1; j <= n; j ++){
            if(i + j == 10){
                c++;
                break;
            }
        }
    }
    if(c != 1){
        cout << "There are " << c << " ways to get the sum 10.";
    }else{
        cout << "There is 1 way to get the sum 10.";
    }
}
