#include <bits/stdc++.h>

using namespace std;

int factorial(int n){
    if (n == 0){
        return 1;
    }
    return n * factorial(n-1);
}

int single_term(int n, int r){
    return factorial(n) / (factorial(r) * factorial(n - r));
}

vector<int> nth_row(int n){
    vector<int> v;
    for (int i = 0; i <= n; i++){
       v.push_back(single_term(n, i));
    }
   return v;
}

int main(int argc, char *argv[]){
    int n = stoi(argv[1]);
    char c = ' ';
    for (int i = 0; i < n; i++){
        vector<int> v = nth_row(i);
        cout << string(n - i - 1, c);
        for(int j = 0; j < v.size(); j++){
           cout << v[j] << " ";
        }
       cout << "\n";
    }
}

