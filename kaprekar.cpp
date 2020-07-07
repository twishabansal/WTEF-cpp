#include <bits/stdc++.h>

using namespace std;

string sorted_str(int n){
    string s = to_string(n);
    sort(s.begin(), s.end());
    return s;
}

int min_no(int n){
    string s = sorted_str(n);
    return stoi(s);
}

int max_no(int n){
    string s = sorted_str(n);
    reverse(s.begin(), s.end());
    return stoi(s);
}

int next(int n){
    return max_no(n) - min_no(n);
}

vector<int> kaprekar(int n){
    vector<int> v = {n};
    int next_no = next(n);
    if (next_no != n ){
        vector<int> v2 = kaprekar(next_no);
        v.insert(v.end(), v2.begin(), v2.end());
    }
    return v;
}

int main(int argc, char *argv[]){
    int n = stoi(argv[1]);
    vector<int> v = kaprekar(n);
    for (int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    }return 0;
}
