// Prompt is located at problem X of the pacnw_div2.pdf file

#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int main() {
  int rounds, close;
  vector<int> ratings;
  int temp;
  int count = 0;
  int halfway;

  cin >> rounds;
  cin >> close;

  for (int i = 0; i < pow(2, rounds); i++) {
    cin >> temp;
    ratings.push_back(temp);
  }

  sort(ratings.begin(), ratings.end());

  while (rounds--) {
    halfway = pow(2, rounds);
    int buffer = 0;

    for (int i = 0; i < halfway; i++) {

      if (ratings[i]+close >= ratings[halfway + buffer]) {
        count++;
        buffer++;
    
      }
    }
    ratings.erase(ratings.begin(), ratings.begin()+halfway);
  }
  cout << count;
}
