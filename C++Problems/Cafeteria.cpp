// A cafeteria table consists of a row of NN seats, numbered from 11 to NN from left to right. Social distancing guidelines require that every diner be seated such that KK seats to their left and KK seats to their right (or all the remaining seats to that side if there are fewer than KK) remain empty.
// There are currently MM diners seated at the table, the iith of whom is in seat S_iS 
// i
// ​
//  . No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.
// Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
// Please take care to write a solution which runs within the time limit.
// Constraints
// 1 \le N \le 10^{15}1≤N≤10 
// 15
 
// 1 \le K \le N1≤K≤N
// 1 \le M \le 500{,}0001≤M≤500,000
// M \le NM≤N
// 1 \le S_i \le N1≤S 
// i
// ​
//  ≤N
// Sample test case #1
// N = 10
// K = 1
// M = 2
// S = [2, 6]
// Expected Return Value = 3
// Sample test case #2
// N = 15
// K = 2
// M = 3
// S = [11, 6, 14]
// Expected Return Value = 1
// Sample Explanation
// In the first case, the cafeteria table has N = 10N=10 seats, with two diners currently at seats 22 and 66 respectively. The table initially looks as follows, with brackets covering the K = 1K=1 seat to the left and right of each existing diner that may not be taken.
//   1 2 3 4 5 6 7 8 9 10
//   [   ]   [   ]
// Three additional diners may sit at seats 44, 88, and 1010 without violating the social distancing guidelines.
// In the second case, only 11 additional diner is able to join the table, by sitting in any of the first 33 seats.

// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
using namespace std;
// Write any include statements here

long long getMaxAdditionalDinersCount(long long N, long long K, int M, vector<long long> S) {
  // Write your code here
  long long additionalDiners=0;
  vector<long long> vals;
  for(int i=0; i<N; i++){ // 0(N)
    vals[i] = i+1;
  }
  
  for(int i=0; i<S.size(); i++){ // 0(S) S = size of S
    if(vals[S[i]-1] == S[i]){
      vals[S[i]-1] = 0;
      for(int j=1; j<=K; j++){ // 0(K) -> worst case 0(N)
          vals[S[i]-j] = -1;
          vals[S[i]+j] = -1;   
      }
    }
  }
  for (int i=0; i < vals.size(); i++){ // 0(N)
      if(i == 0){ // edge case
          if(vals[i] != 0 && vals[i] != -1){
              additionalDiners++;
              vals[i] = 0;
              for(int j=1; j<=K; j++){ // 0(K) -> worst case 0(N)
                  vals[i+j] = -1;   
              }
          }
      }else if(i == vals.size()-1){ // edge case
          if(vals[i] != 0 && vals[i] != -1){
              additionalDiners++;
              vals[i] = 0;
              for(int j=1; j<=K; j++){ // 0(K) -> worst case 0(N)
                  vals[i-j] = -1;
              }
          }
      }else{
          if(vals[i] != 0 && vals[i] != -1){
              additionalDiners++;
              vals[i] = 0;
              for(int j=1; j<=K; j++){ // 0(K) -> worst case 0(N)
                  vals[i-j] = -1;
                  vals[i+j] = -1;   
              }
          }
      }
  }
  return additionalDiners;
}
