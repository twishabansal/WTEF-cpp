#include <iostream>

using namespace std;

int trailing_zeroes(int n){
    int no = 0;
    for (int i = 5; n / i >= 1; i *= 5){
        no += n / i;
    }
    return no;
}

int main(){
    int n;
    cin >> n;
    int zeroes = trailing_zeroes(n);
    cout << zeroes;
    return 0;
}
