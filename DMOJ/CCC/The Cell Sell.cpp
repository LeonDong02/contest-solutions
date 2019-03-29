//
// Created by Leon on 2019-03-29.
//
#include <bits//stdc++.h>

using namespace std;

int a, b, c;

double plana(int a, int b, int c){
    return ((max(a - 100, 0)*0.25) + (0.15*b) + (0.2*c));
}

double planb(int a, int b, int c){
    return ((max(a - 250, 0)*0.45) + (0.35*b) + (0.25*c));
}

int main(){
    cin >> a >> b >> c;
    double x = plana(a, b, c);
    double y = planb(a, b, c);
    cout << "Plan A costs " << x << "\n";
    cout << "Plan B costs " << y << "\n";
    if(x > y){
        cout << "Plan B is cheapest.";
    }else if(y > x){
        cout << "Plan A is cheapest.";
    }else{
        cout << "Plan A and B are the same price.";
    }
}