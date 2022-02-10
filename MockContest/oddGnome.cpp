#include <iostream>
#include <vector>
#include <bits/stdc++.h> 

using namespace std;

int main(){

    int rows, stop, nums, gnome;
    string str = "t";
    cin >> rows;
    vector<int> gnomes;
    while(true){
        if(stop>=rows){
            break;
        }
        cin >> nums;
        for (int i=0; i<nums; i++){
            cin >> gnome;
            gnomes.push_back(gnome);
        }
        stop++;
    }
    for(int i: gnomes){
        cout << i << " ";
    }
    // for(int i =0; i < gnomes; i++){
    //     for(int j=0; j<gnomes[0]){
    //         if(gnomes[j] > gnomes[j+1])){
    //             cout << gnomes[j+1] << endl;
    //         }
    //     }
    //     gnomes.clear(); // clean slate for the vector elements
    // }

    return 0;
}