#include <iostream>
#include <string>
#include <array>

using namespace std;

bool possible(int known[], string read){
    for (char ch: read){
        if (known[int(ch)] != 1){
            return false;
        }
    }
    return true;
}

int main(){
    string known_str;
    cin >> known_str;
    int known[26] = {0};
    for (char ch: known_str){
        known[int(ch)] = 1;
    }
    int n;
    cin >> n;
    for (int i = 0; i < n; i++){
        string read;
        cin >> read;
        string ans;
        ans = possible(known, read) ? "Yes" : "No";
        cout << ans;
    }return 0;
}


    
