//
// Created by Leon on 2019-02-12.
//
#include <bits/stdc++.h>

using namespace std;

int n;
double sheep [100][2];
bool eat [100];
int main() {
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> sheep[i][0] >> sheep[i][1];
    }
    for(float i = 0.00; i < 1000.01; i += 0.01){
        int ind = 0;
        double s = pow((sheep[0][0] - i), 2) + pow(sheep[0][1], 2);
        for(int j = 1; j < n; j++){
            double x = pow((sheep[j][0] - i), 2) + pow(sheep[j][1], 2);
            if(x < s){
                ind = j;
                s = x;
            }
        }
        eat[ind] = true;
    }
    for(int i = 0; i < n; i++){
        if(eat[i]){
            printf("The sheep at (");
            printf("%.2f", sheep[i][0]);
            printf(", ");
            printf("%.2f", sheep[i][1]);
            printf(") might be eaten. \n");
        }
    }
    return 0;
}
