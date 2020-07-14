#include <bits/stdc++.h>

using namespace std;

int main(){
    int t, C, D, L;
    cin >> t;
    for (int i = 0; i < t; i++){
    cin >> C >> D >> L;
    int max_val, min_val;
    max_val = 4 * (C + D);
    if (C > 2 * D){
        min_val = 4 * (C - D);
    }else{
        min_val = 4 * D;
    }
    if ((L <= max_val) && (L >= min_val) && (L % 4 == 0)){
        cout << "yes"<<"\n";
    }
    else{
        cout << "no" << "\n";
    }
    }
    return 0;
}




