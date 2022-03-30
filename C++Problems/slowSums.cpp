// Suppose we have a list of N numbers, and repeat the following operation until we're left with only a single number: Choose any two numbers and replace them with their sum. Moreover, we associate a penalty with each operation equal to the value of the new number, and call the penalty for the entire list as the sum of the penalties of each operation.
// For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first operation, which would transform the list into [1, 5, 4, 5] and incur a penalty of 5. The goal in this problem is to find the highest possible penalty for a given input.
// Signature:
// int getTotalTime(int[] arr)
// Input:
// An array arr containing N integers, denoting the numbers in the list.
// Output format:
// An int representing the highest possible total penalty.
// Constraints:
// 1 ≤ N ≤ 10^6
// 1 ≤ Ai ≤ 10^7, where *Ai denotes the ith initial element of an array.
// The sum of values of N over all test cases will not exceed 5 * 10^6.
// Example
// arr = [4, 2, 1, 3]
// output = 26
// First, add 4 + 3 for a penalty of 7. Now the array is [7, 2, 1]
// Add 7 + 2 for a penalty of 9. Now the array is [9, 1]
// Add 9 + 1 for a penalty of 10. The penalties sum to 26.
#include <bits/stdc++.h>
// Add any extra import statements you may need here

using namespace std;

// Add any helper functions you may need here


int getTotalTime(vector <int> arr) {
  // Write your code here
  vector<int> penaltyArr;
  int maxPenalty = 0;
  int lim = arr.size()-1;
  for (int i =0; i < lim; i++){ // need to pass predefined condition to perform loop as expected
      int maxSum =0;
      int maxEle = *max_element(arr.begin(), arr.end()); // find max element in arr
      arr.erase(max_element(arr.begin(), arr.end()));
      int nextMaxEle = *max_element(arr.begin(), arr.end()); // find next max element in arr
      arr.erase(max_element(arr.begin(), arr.end()));
      maxSum = maxEle + nextMaxEle;
      arr.push_back(maxSum); // add sumMax elements back into arr
      penaltyArr.push_back(maxSum); // add maxSum penalty to seperate array, will use to find max penalty sum
  }
  for(int i=0; i < penaltyArr.size(); i++){ // find the maxPenalty
    maxPenalty += penaltyArr[i];
  }
  return maxPenalty;
}












// These are the tests we use to determine if the solution is correct.
// You can add your own at the bottom.
void printInteger(int n) {
  cout << "[" << n << "]";
}

int test_case_number = 1;

void check(int expected, int output) {
  bool result = (expected == output);
  const char* rightTick = u8"\u2713";
  const char* wrongTick = u8"\u2717";
  if (result) {
    cout << rightTick << "Test #" << test_case_number << "\n";
  }
  else {
    cout << wrongTick << "Test #" << test_case_number << ": Expected ";
    printInteger(expected); 
    cout << " Your output: ";
    printInteger(output);
    cout << endl; 
  }
  test_case_number++;
}

int main() {

  vector <int> arr_1{4, 2, 1, 3};
  int expected_1 = 26;
  int output_1 = getTotalTime(arr_1);
  check(expected_1, output_1);

  vector <int> arr_2{2, 3, 9, 8, 4};
  int expected_2 = 88;
  int output_2 = getTotalTime(arr_2);
  check(expected_2, output_2);

  // Add your own test cases here
  vector <int> arr_3{12, 15, 4, 9, 20};
  int expected_3 = 198;
  int output_3 = getTotalTime(arr_3);
  check(expected_3, output_3);

  vector <int> arr_4{9, 7, 18, 16, 22, 3};
  int expected_4 = 362;
  int output_4 = getTotalTime(arr_4);
  check(expected_4, output_4);
}