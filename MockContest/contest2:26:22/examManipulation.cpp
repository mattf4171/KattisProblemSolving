#include <iostream>
using namespace std;
int main() {
  int s, q;
  int i, j;
  char questions[1000][10];
  int count[1000];
  string quest;
  int tCount, fCount;
  cin >> s;
  cin >> q;
  for (i = 0; i < s; i++) {
    cin >> quest;
    for (j = 0; j < q; j++) {
      questions[i][j] = quest[j];
    }
    count[i] = 0;
  }
  for (j = 0; j < q; j++) {
    tCount = 0;
    fCount = 0;
    for (i = 0; i < s; i++) {
      if (questions[i][j] == 'T') {
        tCount++;
      } else {
        fCount++;
      }
    }
    if (tCount >= fCount) {
      for (i = 0; i < s; i++) {
        if (questions[i][j] == 'T') {
          count[i]++;
        }
      }
    } else {
      for (i = 0; i < s; i++) {
        if (questions[i][j] == 'F') {
          count[i]++;
        }
      }
    }
  }
  int tempCount = q;
  for (i = 0; i < s; i++) {
    if (tempCount > count[i]) {
      tempCount = count[i];
    }
  }
  cout << tempCount << endl;
}