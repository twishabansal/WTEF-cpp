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

set<string> words(string filename, int word_len){
    set<string> words;
    fstream file;
    file.open(filename);
    string word;
    while (file >> word){
        if (word.length() == word_len){
          dict_words.insert(word);
        }
    }
    return words;
}
    

int main(int argc, char* argv[]) {
    int word_len = stoi(argv[i]);
    set<string> words = words("sowpods.txt", word_len);
    int words_reqd = 10, count = 0, iter = 0;
    while (words_reqd < 10) {
        string gen_word = make_word(word_len);
        if (words.find(gen_word) != words.end()){
            count ++;
            cout << iter << " " << gen;
        }
        iter ++;
    }
    cout << endl;
    return 0;
}

