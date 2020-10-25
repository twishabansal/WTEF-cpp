#include <bits/stdc++.h>

using namespace std;

int main(){
    int t,n;
    cin >> t;
    for (int i = 0; i < t; i++){
        cin >> n;
        int workers[n];
        int count = 0;
        int min_val = 0;
        for (int j = 0; j < n; j++){
            cin >> workers[j];
            count += workers[j];
        }
        min_val = *min_element(workers, workers + n);
        count -= min_val * n;
        cout << count<< "\n";
    }
    return 0;
}


