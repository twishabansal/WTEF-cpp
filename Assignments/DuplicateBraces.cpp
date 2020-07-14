#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool duplicate(string &s){
    vector<char> expression;
    for (char const &c : s){
        if (c == ')'){
            bool possible = true;
            char last = expression.back();
            expression.pop_back();
            while (last != '('){
                if (last == '+'||last == '-'|| last == '*'||last == '/'){
                    possible = false;
                }
                last = expression.back();
                expression.pop_back();
            }
            if (possible == true){
                return true;
            }   
        }
        else{
            expression.push_back(c);
        }
    }
    return false;
}

int main(){
    string s;
    cin >> s;
    cout << duplicate(s)<< endl;
    return 0;
}
