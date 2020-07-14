#include <bits/stdc++.h>

using namespace std;

vector<int> digits(string s){
    vector<int> ans = {1};
    int count = 0;
    for (char const &c : s){
        if (c == 'I'){
            ans.push_back(ans.size() + 1);
            count = 0;
        }
        else{
            count ++;
            int tmp = ans.back();
            for (int i = 0; i < ans.size() ; i++){
                cout << ans[i] << " ";
            }
            cout << endl;
            cout << count<< endl;
            for (int i = ans.size() - 1; i > ans.size() - 1 - count; i--){
                cout << ans[i]<<" ";
                ans[i] ++;
                cout << ans[i]<<endl;
            }
            for (int i = 0; i < ans.size() ; i++){
                cout << ans[i] << " ";
            }
            cout << endl;
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
