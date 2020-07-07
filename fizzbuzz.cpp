#include <bits/stdc++.h>

using namespace std;

string fizzbuzz(int n){
    pair <string, string> crypt ("fizz", "buzz");
    string s = "";
    if (n % 3 == 0){
        s += crypt.first;        
    }if (n % 5 == 0){
        s += crypt.second;
    }
    return s == "" ? to_string(n) : s;
}        

vector<string> seq(int n){
    vector<string> ans;
    for(int i = 0; i < n; i++){
        ans.push_back(fizzbuzz(i));
    }
    return ans;
}

int main(int argc, char *argv[1]){
    int n = stoi(argv[1]);
    vector<string> ans = seq(n);
    for (int i = 0; i < ans.size(); i++){
        cout << ans[i]<< " ";
    }
    return 0;
}



