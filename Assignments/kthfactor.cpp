#include <iostream>

using namespace std;

int kth_factor(int n, int k){
    int c = 1;
    int i = 2;
    while (c < k){
        if (n % i == 0){
        c += 1;
        }
        i += 1;
    }
    return i - 1;
}

int main(){
    int n, k;
    cin >> n >> k;
    int ans = kth_factor(n, k);
    cout << ans;
    return 0;
}
