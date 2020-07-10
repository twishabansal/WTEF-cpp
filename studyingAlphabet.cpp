#include <iostream>
#include <string>
#include <set>

using namespace std;

bool possible(set<char> known, string read){
    for (char c: read){
        if (known.find(c) == known.end()){
            return false;
        }
    }
    return true;
}

int main(){
    string known_letters;
    cin >> known_letters;
    set<char> known (known_letters.begin(), known_letters.end());

    int n;
    cin >> n;
    string read;

    for (int i = 0; i < n; i++){
        cin >> read;
        cout << ( possible(known, read) ? "Yes" : "No");
    }
    return 0;
}

        
