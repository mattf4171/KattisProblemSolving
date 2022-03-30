// You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the product of the three largest elements out of arr[0..i] (or equal to -1 if i < 2, as arr[0..i] then includes fewer than three elements).
// Note that the three largest elements used to form any product may have the same values as one another, but they must be at different indices in arr.
// Signature
// int[] findMaxProduct(int[] arr)
// Input
// n is in the range [1, 100,000].
// Each value arr[i] is in the range [1, 1,000].
// Output
// Return a list of n integers output[0..(n-1)], as described above.
// Example 1
// n = 5
// arr = [1, 2, 3, 4, 5]
// output = [-1, -1, 6, 24, 60]
// The 3rd element of output is 3*2*1 = 6, the 4th is 4*3*2 = 24, and the 5th is 5*4*3 = 60.
// Example 2
// n = 5
// arr = [2, 1, 2, 1, 2]
// output = [-1, -1, 4, 4, 8]
// The 3rd element of output is 2*2*1 = 4, the 4th is 2*2*1 = 4, and the 5th is 2*2*2 = 8.
#include <bits/stdc++.h>
// Add any extra import statements you may need here

using namespace std;

// Add any helper functions you may need here


vector <int> findMaxProduct(vector <int> arr) {
  // Write your code here
  vector<int> largestTriple;
  vector<int> max3Elements; // order by ascending order
  for (int i =0; i < arr.size(); i++){
      int prodEle =1;
      if(i ==0 || i == 1){
          largestTriple.push_back(-1);
          max3Elements.push_back(arr[i]);
      }else{
          if(i==2){ // simply find product of all element in arr
              max3Elements.push_back(arr[2]);
              prodEle = max3Elements[0] * max3Elements[1] * max3Elements[2]; // find prod of 3 largest elements from [0..i]
              largestTriple.push_back(prodEle); // append prod to output vector
          }else{
              // append new element from arr, and also append to max3Elements
              max3Elements.push_back(arr[i]);
              sort(max3Elements.begin(), max3Elements.end()); // sort for removal of smallest
              max3Elements.erase(max3Elements.begin()); // remove the smallest element
              prodEle = max3Elements[0] * max3Elements[1] * max3Elements[2];
              largestTriple.push_back(prodEle);
          }
      }
  }
  return largestTriple;
}












// These are the tests we use to determine if the solution is correct.
// You can add your own at the bottom.
void printIntegerVector(vector <int> array) {
  int size = array.size();
  cout << "[";
  for (int i = 0; i < size; i++) {
    if (i != 0) {
      cout << ", ";
    }
   cout << array[i];
  }
  cout << "]";
}

int test_case_number = 1;

void check(vector <int>& expected, vector <int>& output) {
  int expected_size = expected.size(); 
  int output_size = output.size(); 
  bool result = true;
  if (expected_size != output_size) {
    result = false;
  }
  for (int i = 0; i < min(expected_size, output_size); i++) {
    result &= (output[i] == expected[i]);
  }
  const char* rightTick = u8"\u2713";
  const char* wrongTick = u8"\u2717";
  if (result) {
    cout << rightTick << "Test #" << test_case_number << "\n";
  }
  else {
    cout << wrongTick << "Test #" << test_case_number << ": Expected ";
    printIntegerVector(expected); 
    cout << " Your output: ";
    printIntegerVector(output);
    cout << endl; 
  }
  test_case_number++;
}

int main() {
  vector <int> arr_1{1, 2, 3, 4, 5};
  vector <int> expected_1{-1, -1, 6, 24, 60};
  vector <int> output_1 = findMaxProduct(arr_1);
  check(expected_1, output_1);

  vector <int> arr_2{2, 4, 7, 1, 5, 3};
  vector <int> expected_2{-1, -1, 56, 56, 140, 140};
  vector <int> output_2 = findMaxProduct(arr_2);
  check(expected_2, output_2);

  // Add your own test cases here
  vector <int> arr_3{0, 0, 0, 0, 0};
  vector <int> expected_3{-1, -1, 0, 0, 0};
  vector <int> output_3 = findMaxProduct(arr_3);
  check(expected_3, output_3);

  vector <int> arr_4{100, 200, 300, 400, 500};
  vector <int> expected_4{-1, -1, 6000000, 24000000, 60000000};
  vector <int> output_4 = findMaxProduct(arr_4);
  check(expected_4, output_4);
}