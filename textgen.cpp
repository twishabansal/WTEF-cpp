#include <bits/stdc++.h>
using namespace std;

const string ALPHABETS("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
default_random_engine rand_engine;
uniform_int_distribution<size_t> dist(0, ALPHABETS.length() - 1);

string make_word(int how_long) {
    string word;
    for (int i = 0; i < how_long; ++i) {
        word += ALPHABETS[dist(rand_engine)];
    }            
    return word;
}

unordered_set<string> words(string filename, int word_len){
    unordered_set<string> words;
    ifstream sowpods(filename);
    string word;
    while (sowpods >> word){
        if (word.length() == word_len){
        words.insert(word);
        }
    }
    return words;
}
    

int main(int argc, char* argv[]) {
    const int word_len = stoi(argv[1]);
    unordered_set <string> all_words = words("sowpods.txt", word_len);
    int words_reqd = 10, count = 0, iter = 0;
    string word;
    while (count < words_reqd) {
        string gen_word = make_word(word_len);
        if (all_words.find(gen_word) != all_words.end()){
            count ++;
            cout << iter << " " << gen_word << endl;
        }
        iter ++;
    }
    return 0;
}
