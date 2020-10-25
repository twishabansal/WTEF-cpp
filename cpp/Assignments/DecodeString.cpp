#include <bits/stdc++.h>

using namespace std;

vector<int> digits(string s){
    vector<int> ans = {1};
    int count = 0;
    for (char const &c : s){
        if (c == 'I'){
            count = 0;
            int k = ans.size();
            ans.push_back(k + 1);
        }
        else{
            count ++;
            int tmp = ans.back();
            for (int i = (int)ans.size() - 1; i > (int)ans.size() - 1 - count; i--){
                ans[i] += 1;
            }
            ans.push_back(tmp);
        }
    }
   return ans; 
}

int main(){
    string s;
    cin >> s;
    vector<int> ans = digits(s);
    for (int i = 0; i < ans.size(); i++){
        cout << ans[i];
    }
    return 0;
}
