# include <iostream>
# include <vector>

using namespace std;

int next_no(int n){
    return n % 2 == 0 ? n /= 2 : 3 * n + 1;
}
    

vector<int> seq(int n){
    vector<int> v;
    v.push_back(n);
    while (n != 1) {
        v.push_back(next_no(n));
        n = next_no(n);
    }
    return v;
}

int main(){
    int n;
    cin >> n;
    vector<int> v;
    v = seq(n);
    for (int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    }return 0;
}



