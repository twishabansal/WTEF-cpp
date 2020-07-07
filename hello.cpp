#include <iostream>

using namespace std;

int main(int argc, char *argv[]){
    string name;
    cout << "What is your name?";
    getline(cin, name);
    cout << "Hello "<<name<<endl;
    cout << "Welcome to C++"<<endl;
    return 0;
}
