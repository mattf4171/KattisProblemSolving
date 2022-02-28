#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
  int cases;
  int guests;
  int temp;
  int odd;
  int count = 1;
  vector<int> code;
  int i, j;
  cin >> cases;
  for (i = 0; i < cases; i++) {
    cin >> guests;
    for (j = 0; j < guests; j++) {
      cin >> temp;
      code.push_back(temp);
    }
    sort(code.begin(), code.end());
    for (j = 0; j < guests; j++) {
      if (j == guests-1) {
        odd = code[j];
        break;
      }
      if (code[j] != code[j+1]) {
        odd = code[j];
        break;
      }
    }
    cout << "Case #" << count << ": " << odd << "\n";
    count++;
    code.clear();
  }
}









