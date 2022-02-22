#include <iostream>
#include <string>

using namespace std;

string GetRuler(const string& kingdom) {
  // TODO: implement this method to determine the ruler name, given the kingdom.
  char last = kingdom[kingdom.size()-1];
  char aliceList[] = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'};
  char yList[] = {'y', 'Y'};
  for(int i=0; i<sizeof(yList)/sizeof(yList[0]); ++i)
    if(last == yList[i]) return "nobody";
  for(int i=0; i<sizeof(aliceList)/sizeof(aliceList[0]); ++i)
    if(last == aliceList[i]) return "Alice";
  return "Bob";
}

int main() {
  int testcases;
  cin >> testcases;
  string kingdom;

  for (int t = 1; t <= testcases; ++t) {
    cin >> kingdom;
    cout << "Case #" << t << ": " << kingdom << " is ruled by "
         << GetRuler(kingdom) << ".\n";
  }
  return 0;
}
