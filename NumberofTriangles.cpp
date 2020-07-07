#include <iostream>
#include <vector>

using namespace std;

vector<int> range(int min, int max){
    vector<int> ans(max - min + 1);
    for (int i = min; i <= max; i++){
        ans.push_back(i);
    }
    return ans;
}

int triangles(vector<int> range){
    int n = range.size();
    long long count = 0;
    for (int i = n - 1; i >= 1; i--){
        int l = 0;
        int r = i - 1;
        while (l < r){
            if ( range[l] + range[r] > range[i]){
                count += r - l;
                r --;
            }
            else{
                l++;
            }
        }
    }return count;
}

int main(){
    int min, max;
    cin >> min >> max;
    vector<int> range_vector = range(min, max);
    cout << triangles(range_vector);
    return 0;
}
