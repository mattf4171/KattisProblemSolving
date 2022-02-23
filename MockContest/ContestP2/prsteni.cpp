// g++ -o prsteni prsteni.cpp
// ./prsteni 

#include <iostream>
#include <vector>
using namespace std;

int gcd(long x, long y){
    vector<int> vals;
    if(y==0) {
        // vals.push_back(x);
        // vals.push_back(counter);
        return x;
    }
    // counter +=1;
    // if(gcd(y,x%y) == 1) return y;
    return gcd(y, x%y);
}
// int count(int x){
    
// }

int main(){
    int rings, x, counter;
    cin >> rings;
    vector<int> values, returnVals;
    while(rings!=0){
        cin >> x;
        values.push_back(x);
        rings--;
    }

    for(int i= values.size()-1; i>0; i--){
        // cout << gcd(values[i], values[i+1]) << endl;
        // counter = 0;
        // returnVals = gcd(values[i-1], values[i]);
        cout << gcd(values[0], values[i]) << endl;
        // cout << (gcd(values[i-1], values[i], counter)) << endl;
    }
    // use euclidean algorthm 
}