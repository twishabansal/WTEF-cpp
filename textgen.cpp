#include <iostream>
#include <random>
#include <string>

using namespace std;

const string ALPHABETS("abcdefghijklmnopqrstuvwxyz");
default_random_engine rand_engine;
uniform_int_distribution<size_t> dist(0, ALPHABETS.length() - 1);

string make_word(int how_long) {
    string word;
    for (int i = 0; i < how_long; ++i) {
        word += ALPHABETS[dist(rand_engine)];
    }            
    return word;
}

bool read_compare(string filename, string gen_word){
    fstream file;
    string word, t, q;
    file.open(filename.c_str());
    while (file >> word){
        if (word == word_gen){
            return true;
        }
    }
    return false;
}

int main(int argc, char* argv[]) {
    string gen_word;
    int count = 0;
    while (count < 10) {
        gen_word = make_word(stoi(argv[i]));
        if (read_compare("sowpods.txt", gen_word){
            cout <<gen_word<<" " << i << endl;
            count ++;  
        }
    }
    return 0;
}

