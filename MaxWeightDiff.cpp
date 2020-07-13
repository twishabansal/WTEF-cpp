#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        int n, k;
        cin >> n >> k;
        int weights[n];
        int s1 = 0, s2 = 0;
        for (int j = 0; j < n; j++){
            cin >> weights[j];
        }
        k = min(k, n - k);
        sort(weights, weights + n);
        for (int l = 0; l < n; l++){
            if (l < k){
                s1 += weights[l];
            }
            else{
                s2 += weights[l];
            }
        }
        cout << abs(s1 - s2) << "\n";
    }
    return 0;
}
