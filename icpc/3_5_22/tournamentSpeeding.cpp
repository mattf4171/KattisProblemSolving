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
    // cout << "halfway: " << halfway << "\n";
    // cout << "ratings[halfway]: " << ratings[halfway] << "\n";
    for (int i = 0; i < halfway; i++) {
      // cout << "ratings:[i]: " << ratings[i] << "\n";
      // cout << "close: " << close << "\n";
      if (ratings[i]+close >= ratings[halfway + buffer]) {
        count++;
        buffer++;
        // cout << "Count: " << count << "\n";
      }
    }
    ratings.erase(ratings.begin(), ratings.begin()+halfway);
  }
  cout << count;
}
