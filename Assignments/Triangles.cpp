#include <iostream>

using namespace std;

int main(){
    int min, max;
    cin >> min >> max;
    int count = 0;
    for (int i = min, i <= max; i++){
        for (int j = i + 1, j <= max, j++){
            if (i + j < max + 1)
            {
                count += i - 1;
            }else{
                count += end - j;
            }
        }
    }
    cout << count << "\n";
    return 0;
}
