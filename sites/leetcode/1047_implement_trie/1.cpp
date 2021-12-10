#include<cstring>
#include<iostream>

using namespace std;

class Node {
public:
    Node* _children[26];
    char val;

    Node(int _val): val(_val) {};
    Node(): val(0) {};
};

class Trie {
public:
    Node* root;
    Trie() {
        root = new Node();
    }
    
    void insert(string word) {
        Node* cur = root;
        for(int idx=0; idx<word.size(); ++idx)
        {
            int isFound=false;
            int i=0;
            for(; i<26; ++i)
            {
                if(cur->_children[i]==nullptr) break;
                if(cur->_children[i]->val==word[idx])
                {
                    isFound=true;
                    break;
                }
            }
            if(!isFound)
            {
                cur->_children[i] = new Node(word[idx]);
            }
        }
    }
    
    bool search(string word) {
        
    }
    
    bool startsWith(string prefix) {
        
    }
};

int main()
{
    Trie* trie = new Trie();
    trie->insert("apple");
    trie->search("apple");   // return True
    trie->search("app");     // return False
    trie->startsWith("app"); // return True
    trie->insert("app");
    trie->search("app");     // return True
    return 0;
}