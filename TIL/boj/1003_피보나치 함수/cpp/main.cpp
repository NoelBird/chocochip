#include<iostream>
// #include<map>
#include<vector>

using namespace std;

vector<int> visited_ur;
vector<int> visited_dr;

int nq(vector<int> l, int x, int y, int n);

int main(){
    int n;
    cin>>n;
    vector<int> l;
    for(int i=0;i<n;i++){
        l.push_back(i);
    }

    cout<<nq(l, 0, 0, n)<<endl;

    return 0;
}

int nq(vector<int> l, int x, int y, int n){
    if(l.size() == n){
        return 1;
    }
    if(l.size() > n){
        return 0;
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            
        }
    }


}