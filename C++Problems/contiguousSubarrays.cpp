// You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
// The value at index i must be the maximum element in the contiguous subarrays, and
// These contiguous subarrays must either start from or end on index i.
// Signature
// int[] countSubarrays(int[] arr)
// Input
// Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
// Size N is between 1 and 1,000,000
// Output
// An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]
// Example:
// arr = [3, 4, 1, 6, 2]
// output = [1, 3, 1, 5, 1]
// Explanation:
// For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
// For index 1 - [4], [3, 4], [4, 1]
// For index 2 - [1]
// For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
// For index 4 - [2]
// So, the answer for the above input is [1, 3, 1, 5, 1]
#include <bits/stdc++.h>
// Add any extra import statements you may need here

using namespace std;

// Add any helper functions you may need here


vector <int> CountSubarrays(vector <int> arr) {
  // Write your code here -> permutations
  vector<int> contiguousSubarrays;
  for (int i=0; i < arr.size(); i++){
    int counts =0;
    if(i==0){
        counts+=1;
        for (int j=1; j<arr.size(); j++){ // start at second from front element in array
            if(arr[i] > arr[j]){
                counts +=1;
            }else{
                break;
            }
        }
        contiguousSubarrays.push_back(counts);
    }else if(i == arr.size()-1){
        counts+=1;
        for (int j=arr.size()-2; j>-1; j--){ // start at second to last element in array
            if(arr[i] > arr[j]){
                counts +=1;
            }else{
                break;
            }
        }
        contiguousSubarrays.push_back(counts);
    }
    else{
      // check forward && back
      counts+=1;
      for (int j=i-1; j>-1; j--){ // right to left
          if(arr[i] > arr[j]){
              counts +=1;
          }else{
              break;
          }
      }
      for (int j=i+1; j<arr.size(); j++){ // left to right
            if(arr[i] > arr[j]){
                counts +=1;
            }else{
                break;
            }
        }
      contiguousSubarrays.push_back(counts);
    }
    
  }
  return contiguousSubarrays;
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

  vector <int> test_1{3, 4, 1, 6, 2};
  vector <int> expected_1{1, 3, 1, 5, 1};
  vector <int> output_1 = CountSubarrays(test_1);
  check(expected_1, output_1);

  vector <int> test_2{2, 4, 7, 1, 5, 3};
  vector <int> expected_2{1, 2, 6, 1, 3, 1};
  vector <int> output_2 = CountSubarrays(test_2);
  check(expected_2, output_2);

  // Add your own test cases here
  
}