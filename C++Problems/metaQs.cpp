#include <iostream>
#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include <bits/stdc++.h>
using namespace std;

// To execute C++, please define "int main()"

int fastestPower(int a, int b){ // 0(logn) MOST EFF ALG
    if(b ==0){
        return 1;
    }
    int x = fastestPower(a, b/2);
    x = x * x;
    if(n%2 ==1){
        x = x *a;
    }
    return x;
}


int power(int a, int b){ // a = 2 | b = 5
    int val=1; // 1     
    for( int i=1; i <= b; i++){ // i=1 | i=2 | i=3 | i=4
      
      val = a * val;     // 2*1=2 | 2*2 =4 | 3* 9 =27 | 27*3
    }


    return val;
}

int power2(int a, int b){
  int val =1;
  if(b%2==0){
    for(int i=1; i <= b/2; i++){
        val = a* val;
    } 
    val = val * val; 
  }else{
    int remaining = a;
    for(int i=1; i<= floor(b/2); i++){
      val = a * val; 
    }
    val = (val * val) * remaining;
  }
  return val;
}

int powerResursive(int a, int b){ // 3 , 4
  int val = a * a; // 9  | 
  if(b==1){ // b == 1
    return val;
  }else{
      powerResursive(a, b-1); // 3, 3
  }
}

int main() {
  int a = 3, b=4; 
  power(a, b);
  
  return 0;
}



// # Implement the power function that computes a to the power of b using basic arithmetic operations (+, -, *, /, %), b is a non-negative integer
// def power(a, b)

// (3, 4)   =>  81
// (5, 1)   =>  5
// (2, 10)  =>  1024



vector<vector<int>> findPair(vector<int> arr, int x){ // [1 10 8 -15 3 5] , 13
  vector<vector<int>> TdVec; 
  for(int i=0; i<arr.size(), i++){ // 0(n) i=2
    vector<int> tempVec; 
    for(int j=arr.size()-1; j>i; j--){ // 0(nlogn) j index start at back of arr
      if(arr[i] + arr[j] == x){
        tempVec.push_back(arr[i]);
        tempVec.push_back(arr[j]);
        TdVec.push_back(tempVec);
      }
    }
  }
  return TdVec;
}

// Alternatively the fastest algorithm would be hash map



// # Find pairs of numbers that sums to x
// def findPair(arr, x)

// [1 10 8 -15   3 5], 13  => [5 8]  [10 3]
// [1 10 8 -15   3 5], 5  =>  NULL